import os.path
from twisted.internet import task, reactor
from json import load
from urllib2 import urlopen
from .mail import mail

class noticer:
    ipadress = '1.1.1.1'

    @staticmethod
    def checkIP():
        my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
        print(my_ip)

        if noticer.ipadress == '':
            noticer.ipadress = my_ip
            return

        if noticer.ipadress == my_ip:
            return

        if noticer.ipadress != my_ip:
            print('IP has changed!')
            noticer.ipadress = my_ip
            mail.send_mail(my_ip)

        pass

    @staticmethod
    def startService():
        timeout = 60.0 # Sixty seconds
        l = task.LoopingCall(noticer.checkIP)
        l.start(timeout) # call every sixty seconds

        reactor.run()

        

