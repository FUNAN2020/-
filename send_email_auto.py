import smtplib
from email.mime.text import MIMEText
from email.header import Header
from threading import Timer
import requests

#发送邮件的函数 参数的意思分别是 发件人邮箱、收件人邮箱、主题、附件、消息内容
def SendEmail(fromAdd, toAdd, subject, attachfile, htmlText):
  strFrom = fromAdd
  strTo = toAdd
  msg =MIMEText(htmlText)
  msg['Content-Type'] = 'Text/HTML'
  msg['Subject'] = Header(subject,'gb2312')
  msg['To'] = strTo
  msg['From'] = strFrom
  #链接QQ邮箱服务器
  smtp = smtplib.SMTP('smtp.qq.com')
  #登录邮箱
  smtp.login('the sender email','verfication code')
  try:
    #执行发送
    smtp.sendmail(strFrom,strTo,msg.as_string())
  finally:
    smtp.close


def get_news():
    
    """获取金山词霸每日一句，英文和翻译"""
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


content,note=get_news()
for i in range(5):
    contest=content+" "+note+str(i)
    SendEmail("the sender's email","the receiver's email","","hello",contest)
    print("发送邮件正确！")
