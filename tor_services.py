from proxy import Proxy
from proxy.Color import *
torBanner = '''
%s%s----------------------------------------------------------------------------
%s%s _____          ___                    ___              _           
|_   _|__ _ _  | _ \_ _ _____ ___  _  / __| ___ _ ___ _(_)__ ___ ___
  | |/ _ \ '_| |  _/ '_/ _ \ \ / || | \__ \/ -_) '_\ V / / _/ -_|_-<
%s%s  |_|\___/_|   |_| |_| \___/_\_\\_,  | |___/\___|_|  \_/|_\__\___/__/
                                |__/                               
                                       %s%s:-%s%s  by Nasir Khan (r0ot h3x49)
%s%s----------------------------------------------------------------------------
''' % (fg, sb, fc, sb, fg, sb, fw, sb, fg, sb, fg, sb)
class TorServiceSetup(object):
	"""class to setup and start tor sevices"""

	def StartService(self):
		TorProxy = Proxy()
		print(torBanner)
		TorProxy.ConfigureTor
		
def main():
	Service = TorServiceSetup()
	Service.StartService()
	
if __name__ == '__main__':
	main()
