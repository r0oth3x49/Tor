import os as _os
from colorama import init as _init
from colorama import Fore as _Fore
from colorama import Back as _Back
from colorama import Style as _Style

if _os.name == "posix":
    # colors foreground text:
    fc = "\033[0;96m"
    fg = "\033[0;92m"
    fw = "\033[0;97m"
    fr = "\033[0;91m"
    fb = "\033[0;94m"
    fy = "\033[0;33m"
    fm = "\033[0;35m"

    # colors background text:
    bc = "\033[46m"
    bg = "\033[42m"
    bw = "\033[47m"
    br = "\033[41m"
    bb = "\033[44m"
    by = "\033[43m"
    bm = "\033[45m"

    # colors style text:
    sd = _Style.DIM
    sn = _Style.NORMAL
    sb = _Style.BRIGHT
else:
    ## ----------------------------------------------------------------------------------------------------------------------  ##
    _init(autoreset=True)
    # colors foreground text:
    fc = _Fore.CYAN
    fg = _Fore.GREEN
    fw = _Fore.WHITE
    fr = _Fore.RED
    fb = _Fore.BLUE
    fy = _Fore.YELLOW
    fm = _Fore.MAGENTA
    

    # colors background text:
    bc = _Back.CYAN
    bg = _Back.GREEN
    bw = _Back.WHITE
    br = _Back.RED
    bb = _Back.BLUE
    by = _Back.YELLOW
    bm = _Back.MAGENTA

    # colors style text:
    sd = _Style.DIM
    sn = _Style.NORMAL
    sb = _Style.BRIGHT
    ## ----------------------------------------------------------------------------------------------------------------------  ##
