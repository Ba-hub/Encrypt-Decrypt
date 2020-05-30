#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os


class color:
    INFO = '\033[93m'
    ENDC = '\033[0m'
    GREEN = '\033[1;32m'


opt = raw_input("\n [?]" + color.INFO + "Install necessary libraries (y/n): " + color.ENDC)
if opt.lower() == "y":
    print("\n [+]" + color.INFO + " Installing libreries please wait... \n" + color.ENDC)
    os.system('sudo pip install urllib3 passlib argparse')
    os.system('sudo easy_install hashlib')
    print("\n [+]" + color.GREEN + " Libraries installed!!\n" + color.ENDC)
    raw_input("Press Enter to Continue..")
else:
    exit
