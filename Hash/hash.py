#!/usr/bin/python
#coding=utf-8
import hashlib

def getmd5(c):
    m = hashlib.md5()
    m.update(c)
    return m.hexdigest()
def getsha1(c):
    m = hashlib.sha1()
    m.update(c)
    return m.hexdigest()