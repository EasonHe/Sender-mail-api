#!/bin/sh
start() {
port=`grep listenport   ./mail.conf  | cut -d'=' -f 2` 
if [ -n $port ];then
nohup python ./httpmail.py $port& 
fi
}

stop() {
ps -ef |grep  httpmail.py | grep -v grep |awk -F' ' '{print $2}' | xargs -r   kill -9

}


case $1 in 
start)
start
echo "启动"
;;

stop)
stop
echo "停止";;
restart)
stop
start
echo "重启"
;;
esac 


 
