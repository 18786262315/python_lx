import configparser

config = configparser.ConfigParser()
config.read('E:\\ycc\pythonlianxi\\配置文件模块\\conf.ini')
# print(config.sections()) #获取所有 sections
# config.items('topsecret.com') #获取分类下的所有keys和values
# print(config.options('topsecret.com')) #获取keys
# for option in config['bitbucket.org']: #循环打印bitbucket.org的内容
#     print (option)

# print(config['topsecret.com']['ForwardX11'])#获取指定 key 的 value
# print(config['DEFAULT']['ForwardX11']) #获取指定 key 的 value
# # print(config.has_section('bitbucket.org','User')) #判断内容是否存在
# print('Tom' in config['bitbucket.org']['User']) #检查内容

# print(config.get('bitbucket.org', 'User')) #获取值
# print(config.getint('topsecret.com', 'Port')) #以数字类型获取内容，如果内容不是数字类型则报错

# config.add_section('Section_1') #新增一个类别
# config.set('Section_1', 'key_1', 'value_1')    # 注意键值是用set()方法
# config.remove_option('Section_1', 'key_1') #删除键值
# config.remove_section('Section_1') #删除title
# config.clear() #清空所有内容
# config.set('DEFAULT', 'ForwardX11','yes') #给DEFAULT增加内容、修改内容
# config.write(open('E:\\ycc\pythonlianxi\\配置文件模块\\conf.ini', 'w'))    # 一定要写入才生效