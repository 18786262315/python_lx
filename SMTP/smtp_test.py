
 
import yagmail
 
#链接邮箱服务器
 
#此处的password是授权码
 
yag= yagmail.SMTP( user="ycc843092012@gmail.com", password="xumeagqowzcgbfji", host='smtp.qq.com')
 
# 邮箱正文
 
contents = [
    '''
    ——————标题——————
    文本内容1文本内容1文本内容1
    文本内容1
    文本内容1
    文本内容1
    ''']

# 发送邮件
 
# yag.send('843092012@qq.com','subject', contents)
 
# 四行代码完工，简单吧
 
# 给多个用户发送邮件
 
# yag.send(['aa@126.com','bb@qq.com','cc@gmail.com'],'subject', contents)
 
# # 发送邮件带附件
 
yag.send('843092012@qq.com','发送附件', contents, ["C:\\Users\\Administrator\\Desktop\\bq包\\211347811066.jpg"])

