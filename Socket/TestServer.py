#!/usr/bin/python
#coding=utf-8
import Server

def test():
    print "hello world"
server=Server.createServer()

Server.listenCall(server,test(),"hello1")