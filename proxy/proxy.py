#!/usr/bin/python
import os
import re
import sys
import time
import socket
import subprocess

from . import socks
from .Color import *
from .tor_paths import check_path
if os.name == "nt":
    from . import inet_pton
else:
    pass

def clean(value):
    if sys.version_info[:2] >= (3, 0):
        return value.decode('utf-8')
    else:
        return value
    
class Proxy:

    def __init__(self):
        self._proxy_type = socks.SOCKS5
        self._addr = '127.0.0.1'
        self._connection_port = 9050
        self._control_port = 9051

    @property
    def ConfigureTor(self):

        search_torrc = os.getcwd()+'\\proxy\\tor_configs\\win\\*torrc'
        search_torexe = os.getcwd()+'\\proxy\\tor_configs\\win\\*tor.exe'
        search_geoip = os.getcwd()+'\\proxy\\tor_configs\\win\\*geoip'
        search_geoip6 = os.getcwd()+'\\proxy\\tor_configs\\win\\*geoip6'

        torexe = check_path(search_torexe)
        torrc = check_path(search_torrc)
        geoip = check_path(search_geoip)
        geoip6 = check_path(search_geoip6)
        write_dd = 'DataDirectory %s\n' % (geoip.replace('\geoip',''))
        write_geoip = 'GeoIPFile %s\n' % (geoip)
        write_geoip6 = 'GeoIPv6File %s\n' % (geoip6)
        
        fd = open(torrc)
        torrc_read = fd.readlines()
        fd.close()
        
        torrc_file = open(torrc, 'w')
        torrc_read[4] = write_geoip
        torrc_read[5] = write_geoip6
        torrc_read[6] = write_dd
        torrc_file.writelines(torrc_read)
        torrc_file.close()
        
        cmd = subprocess.Popen([torexe, '-f', torrc], stdout=subprocess.PIPE)
        req, umsg = 1, "User requested new identity.."
        while True:
            try:
                line = cmd.stdout.readline()
                if line != '':
                    line = clean(line)
                    if '0.3.2.10' in line:
                        t, v = (line.strip().split('running')[0].split('[notice]')[1]).split()
                        print ('{}{}[{}{}*{}{}] {:<4} :  {}'.format(fg, sd, fm, sb, fg, sd, t, v))
                    if 'Bootstrapped' in line:
                        per, msg = ((line.strip())[42:]).split(":")
                        print ('{}{}[{}{}*{}{}] {:<4} : {}'.format(fg, sd, fm, sb, fg, sd, per, msg))
                        if 'Done' in msg:
                            print (fg + sb + '\n----------------------------------------------------------------------------\n')
                    if 'opened from 127.0.0.1' in line:
                        print ('{}{}[{}{}*{}{}] {req:02d}   :  {umsg!s}'.format(fg, sd, fm, sb, fg, sd, req=req, umsg=umsg))
                        req += 1
            except KeyboardInterrupt:
                print ('\n{}{}[{}{}-{}{}] -- User interrupted closing the services..'.format(fg, sd, fr, sb, fg, sd))
                time.sleep(1)
                break
                
        
        
    @property
    def ConfigureProxy(self):
        try:
            socks.set_default_proxy(self._proxy_type, self._addr, self._connection_port)
        except:
            pass
        else:
            socket.socket = socks.socksocket
            
    @property
    def SetDefaultProxy(self):
        socks.setdefaultproxy()

    @property
    def NewIdentity(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self._addr, self._control_port))
        except:
            return 'failed'
            s.close()
        else:
            passwd = 'r0oth3x49'
            s.send("AUTHENTICATE \"%s\"\r\n" % (passwd))
            resp = s.recv(128)
            if resp.startswith('250 OK'):
                s.send('SIGNAL NEWNYM\r\n')
                return resp
            else:
                return resp
        s.close()
