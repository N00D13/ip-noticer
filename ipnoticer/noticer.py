import os.path

class noticer:
    configFile = os.path.expanduser('~/.ip-noticer/config.yml')
    statusFile = os.path.expanduser('~/.ip-noticer/status.yml')
    configFolder = os.path.expanduser('~/.ip-noticer')

    @staticmethod
    def checkServiceExisting():
        print("test")

    @staticmethod
    def checkConfigFileExisting():
        if os.path.isfile(noticer.configFile):
            print("Yes!")
        else:
            if not os.path.isdir(noticer.configFolder):
                os.mkdir(noticer.configFolder)
            
            file = open(noticer.configFile, 'w+')

    @staticmethod
    def checkFileExisting(path, file, write):
        if os.path.isfile(file):
            return True
        if write:
            if not os.path.isdir(path):
                os.mkdir(file)
            
            file = open(file, 'w+')
        else:
            return False