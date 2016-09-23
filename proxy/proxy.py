#!/usr/bin/python
#######################################################
#       Author: Nasir khan (r0ot h3x49)               #
#######################################################

import os,sys,time
import socks
import socket
import subprocess
from tor_paths import check_path
if os.name == "nt":
    import inet_pton
else:
    pass

class Proxy:

    def __init__(self):
        self._proxy_type = socks.SOCKS5
        self._addr = '127.0.0.1'
        self._connection_port = 9050
        self._control_port = 9051

    @property
    def ConfigureTor(self):
        if sys.platform == 'win32':
            
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
            while True:
                try:
                    line = cmd.stdout.readline()
                    if line != '':
                        print line.strip()
                except KeyboardInterrupt:
                    print '[-] -- User interrupted closing the services..'
                    time.sleep(3)
                    break
                
        elif sys.platform == 'darwin':
            
            search_torexe = os.getcwd()+'/proxy/tor_configs/mac/*tor'
            search_torrc = os.getcwd()+'/proxy/tor_configs/mac/*torrc'
            search_geoip = os.getcwd()+'/proxy/tor_configs/mac/*geoip'
            search_geoip6 = os.getcwd()+'/proxy/tor_configs/mac/*geoip6'

            torexe = check_path(search_torexe)
            torrc = check_path(search_torrc)
            geoip = check_path(search_geoip)
            geoip6 = check_path(search_geoip6)
            
            write_dd = 'DataDirectory %s\n' % (geoip.replace('/geoip',''))
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
            while True:
                try:
                    line = cmd.stdout.readline()
                    if line != '':
                        print line.strip()
                except KeyboardInterrupt:
                    print '[-] -- User interrupted closing the services..'
                    time.sleep(3)
                    break
            
        else:
            
            search_torexe = os.getcwd()+'/proxy/tor_configs/linux/*tor'
            search_torrc = os.getcwd()+'/proxy/tor_configs/linux/*torrc'
            search_geoip = os.getcwd()+'/proxy/tor_configs/linux/*geoip'
            search_geoip6 = os.getcwd()+'/proxy/tor_configs/linux/*geoip6'

            torexe = check_path(search_torexe)
            torrc = check_path(search_torrc)
            geoip = check_path(search_geoip)
            geoip6 = check_path(search_geoip6)
            
            write_dd = 'DataDirectory %s\n' % (geoip.replace('/geoip',''))
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
            while True:
                try:
                    line = cmd.stdout.readline()
                    if line != '':
                        print line.strip()
                except KeyboardInterrupt:
                    print '[-] -- User interrupted closing the services..'
                    time.sleep(3)
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
