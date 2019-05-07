import os.path
from twisted.internet import task, reactor
from json import load
from urllib2 import urlopen
from .mail import mail

class noticer:

    @staticmethod
    def checkIP():
        my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
        print(my_ip)
        pass

    @staticmethod
    def startService():
        timeout = 60.0 # Sixty seconds
        l = task.LoopingCall(noticer.checkIP)
        l.start(timeout) # call every sixty seconds

        reactor.run()

        

