import os
import sys
from . import proxy

from requests import get as compat_get
from time import strftime as compat_strftime
from time import sleep as compat_sleep


class Tor:

    @property
    def compat_proxy_connect(self):
        url      = "http://my-ip.herokuapp.com"
        Proxy    = proxy.Proxy()
        Proxy.SetDefaultProxy
        response = compat_get(url).json()
        sys.stdout.write(proxy.fg + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: configuring tor proxy .. \r\r")
        Proxy.ConfigureProxy
        try:
            response_tor = compat_get(url).json()
        except:
            compat_sleep(2)
            sys.stdout.write(proxy.fg + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: configuring tor proxy .. (" + proxy.fr + proxy.sb  + "failed" + proxy.fg + proxy.sd  + ")\t\t\r\r\n")
            sys.stdout.write(proxy.fg + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: make sure tor services are running. \t\t\t\r\r\n")
            Proxy.SetDefaultProxy
            proxy_ip = response.get('ip') or None
        else:
            proxy_ip = response_tor.get('ip') or None
            default_ip = response.get('ip') or None
            if default_ip != proxy_ip:
                compat_sleep(2)
                sys.stdout.write(proxy.fg + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: configuring tor proxy .. (" + proxy.fg + proxy.sb  + "done" + proxy.fg + proxy.sd  + ")\t\t\r\r\n")
            else:
                compat_sleep(2)
                sys.stdout.write(proxy.fg + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: configuring tor proxy .. (" + proxy.fr + proxy.sb  + "failed" + proxy.fg + proxy.sd  + ")\t\t\r\r\n")

    @property
    def compat_proxy_newid(self):
        url      = "http://my-ip.herokuapp.com"
        Proxy    = proxy.Proxy()
        Proxy.SetDefaultProxy
        response = compat_get(url).json()
        sys.stdout.write(proxy.fg + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: requesting new identity .. \r\r")
        compat_sleep(2)
        _resp = Proxy.NewIdentity
        if '250 OK' in _resp:
            compat_sleep(2)
            sys.stdout.write(proxy.fg + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: requesting new identity .. (" + proxy.fg + proxy.sb  + "done" + proxy.fg + proxy.sd  + ")\t\t\r\r\n")
            Proxy.ConfigureProxy
            try:
                response_tor = compat_get(url).json()
            except:
                Proxy.SetDefaultProxy
                proxy_ip = response.get('ip') or None
            else:
                proxy_ip = response_tor.get('ip') or None
                sys.stdout.write(proxy.fg + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: configuring tor proxy .. \r\r")
                default_ip = response.get('ip') or None
                if default_ip != proxy_ip:
                    compat_sleep(2)
                    sys.stdout.write(proxy.fg + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: configuring tor proxy .. (" + proxy.fg + proxy.sb  + "done" + proxy.fg + proxy.sd  + ")\t\t\r\r\n")
                else:
                    compat_sleep(2)
                    sys.stdout.write(proxy.fr + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: configuring tor proxy .. (" + proxy.fr + proxy.sb  + "failed" + proxy.fg + proxy.sd  + ")\t\t\r\r\n")
        else:
            sys.stdout.write(proxy.fg + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: requesting new identity .. (" + proxy.fr + proxy.sb  + "failed" + proxy.fg + proxy.sd  + ")\t\t\r\r\n")
            sys.stdout.write(proxy.fg + proxy.sd + "["+compat_strftime("%H:%M:%S")+"] [INFO] TOR: make sure tor services are running .. \t\t\t\r\r\n")
            Proxy.SetDefaultProxy
