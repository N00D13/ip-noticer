import os.path
from json import load
from urllib2 import urlopen
from .mail import mail

class noticer:
    test = ""

    @staticmethod
    def checkIP():
        my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
        print(my_ip)

    @staticmethod
    def startService():
        noticer.checkIP()

        

