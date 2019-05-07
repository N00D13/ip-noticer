import os.path

class config:
    configFile = os.path.expanduser('~/.ip-noticer/config.yml')
    statusFile = os.path.expanduser('~/.ip-noticer/status.yml')
    configFolder = os.path.expanduser('~/.ip-noticer')

    @staticmethod
    def checkServiceExisting():
        print("test")

    @staticmethod
    def checkConfigFileExisting():
        config.checkFileExisting(config.configFolder, config.configFile, True)
        config.checkFileExisting(config.configFolder, config.statusFile, True)

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