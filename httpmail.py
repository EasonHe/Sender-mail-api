# -*- coding: utf-8 -*-
import  web
import re
import ConfigParser
def mailconf(tos,subject,content):
    try:
        config = ConfigParser.ConfigParser()
        config.read('mail.conf')
        web.config.smtp_server = config.get('section1', 'smtp_server')
        web.config.smtp_port = config.get('section1', 'smtp_port')
        web.config.smtp_username = config.get('section1', 'smtp_username')
        web.config.smtp_password = str(config.get('section1', 'smtp_password'))
        web.config.smtp_starttls = config.get('section1', 'smtp_starttls')
        fromuser=config.get('section1', 'fromuser')
        web.sendmail(fromuser,tos,subject,content)
        return True
    except  ValueError as e:
        print e
        return  False
    raise Exception('send fail')

urls = ('/sender/mail',
        'geturl')
app = web.application(urls, globals())
class geturl:
    def GET(self):
        pass
    def POST(self):
        data=web.data()
        prog = re.compile('tos=(.*)&subject=(.*)&content=(.*)')
        result = prog.match(data)
        mems = result.groups()
        tos = mems[0].split()
        subject = mems[1]
        content = mems[-1]
        print(tos,subject,content)
        if  True == mailconf(tos, subject, content):
            return   'success' + '\n'
        else:
            return  'false'

if __name__=='__main__':
     app.run()
