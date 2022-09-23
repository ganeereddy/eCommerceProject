import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        url=config.get('common info','username')
        return url

    @staticmethod
    def getPassword():
        url=config.get('common info','password')
        return url
    