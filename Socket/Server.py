#!/usr/bin/python
#coding=utf-8
import socket   #socket模块
import commands   #执行系统命令模块
import threading
from time import ctime
from DB.Mysql import *

global host_IP,port
host_IP = "127.0.0.1"
port = 11111

def serverCallone(host_ip = "127.0.0.1",port = 11111):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.bind((host_ip, port))  # 套接字绑定的IP与端口
    s.listen(1)  # 开始TCP监听
    while True :
        conn, addr = s.accept()  # 接受TCP连接，并返回新的套接字与IP地址
        print'Connected by', addr  # 输出客户端的IP地址
        # t = threading.Thread(target=oneThread())
        # t.daemon(True)
        # t.start()
        while 1:
            date = conn.recv(1024)  # 把接收的数据实例化
            print date,ctime()
            temp = date+ctime()
            conn.sendall(temp)
def serverCallMulti(host_ip = "127.0.0.1",port = 11111):
    count = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.bind((host_ip, port))  # 套接字绑定的IP与端口
    s.listen(1)  # 开始TCP监听
    while True :
        print "开始监听..."
        conn, addr = s.accept()  # 接受TCP连接，并返回新的套接字与IP地址
        print'Connected by', addr ,". Create a new thread :(",count,")" # 输出客户端的IP地址
        t = threading.Thread(target=oneThread, args=(addr,count,conn,),name=addr[0]+'|'+str(count))
        t.start()
        count+=1
def oneThread(addr,count,conn):

    print '开启新线程',threading.current_thread().getName()
    date = conn.recv(1024)  # 把接收的数据实例化 !!考虑存在阻塞
    print threading.current_thread().getName(),'send: ',date
    cmd_status, cmd_result = commands.getstatusoutput(
        date)  # commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
    print cmd_result,cmd_status
    conn.sendall(cmd_result)

    sql = "insert into flow_tables (flow_tables,ip,conn_port,thread_id) VALUES ('"+ str(cmd_result) +"','"+str(addr[0])+"',"+str(addr[1])+','+str(count)+');'
    print sql
    insertSql(sql)
    # temp = date + ctime()
    # conn.sendall(temp)
if __name__ =='__main__':
    host = socket.gethostname()
    serverCallMulti(host_ip=host)
    # serverCallMulti(host_ip='10.109.34.179')