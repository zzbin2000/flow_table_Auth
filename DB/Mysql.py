#!/usr/bin/python
#coding=utf-8
import MySQLdb
# 创建连接
config = {
          'user':'ovs',
          'password':'bupt777',
          'host':'127.0.0.1',
          'port':3306,
          'database':'ovs'}
def executeSql(sqlIn):
    # 连接
    try:
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='ovs',
            passwd='bupt777',
            db='ovs',
        )
        # 创建游标
        cur = conn.cursor()
        cur.execute(sqlIn)
        # 关闭游标和连接
        cur.close()
        conn.commit()
        conn.close()
        print 'execute sql ok...'
    except Exception, e:
      print str(e)

def test():
    print 'as'
    # sql1 = "insert into flow_tables (flow_tables,ip,conn_port,thread_id) values ("sss","127.0.0.1",77775,17);"
    sql1 = "insert into flow_tables (flow_tables,ip,conn_port,thread_id) VALUES ('test','127.0.0.1',77775,17)"
    executeSql(sql1)
# test()

# print "hello world!"