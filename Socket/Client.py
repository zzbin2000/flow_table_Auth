#!/usr/bin/python
#coding=utf-8
import socket
from Server import get_ip_address
HOST=get_ip_address('eth0')
PORT=11111
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect((HOST,PORT))       #要连接的IP与端口
print '连接到：',HOST,'：',PORT
while 1:
    cmd=raw_input("Please input cmd:")       #与人交互，输入命令
    s.sendall(cmd)      #把命令发送给对端
    data=s.recv(1024)     #把接收的数据定义为变量
    print data         #输出变量
s.close()   #关闭连接