# Sender-mail-api
邮件接口
使用方式
curl http://$ip:2345/sender/mail  -d "tos=a@.com,b@.com&subject=xx&content=yy"



example:
       curl http://192.168.249.130:2345/sender/mail -d  "tos=he@ee.com&subject=hello&content=我还好！"
