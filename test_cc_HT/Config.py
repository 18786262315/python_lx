import os,sys
# 加入模块环境变量配置
proDir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(proDir)
import codecs
import configparser
from Common import Log


configPath = os.path.join(proDir, R"Flie\config\configs.ini")

class ReadConfig:
    def __init__(self):
        fd = open(configPath,encoding='utf-8')
        data = fd.read()
        #  remove BOM         
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,encoding='utf-8-sig')
    def sets(self,configPath):
        self.cf.write(open(configPath, "w",encoding='utf-8'))

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value
    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value
    def get_user(self,name):
        value = self.cf.get('USER',name)
        return value
    def set_user(self,keys,value):
        value = self.cf.set('USER',keys,value)
        self.sets(configPath)
        return value


if __name__ == "__main__":
    red = ReadConfig()
    red.set_user('id','111')
    print(red.get_user('id'))