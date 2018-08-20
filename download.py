import requests
import re
import urllib.request
import json
import time
import pymysql
import os
class dbase():
    def Insert(weather,mood,content,data):
           conn=pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='root',
                             database='linshun',
                             charset='utf8'
        )
           cur=conn.cursor()
           cur.execute('insert into diary(weather,mood,content,data)values(%s,%s,%s,%s)',(weather,mood,content,data))
           cur.execute('select * from diary')
           conn.commit()
           cur.close()
           conn.close()
           for i in cur.fetchall():
               for a in i:
                   print(a)
class lin(object):
    def __init__(self,url,dir_path):
         mysql=Mysql()
         header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
         html=requests.get(url,headers=header)
         for i in range(len(html.json()['data']['tracksAudioPlay'])):
             #time.sleep(1)
             m4a=html.json()['data']['tracksAudioPlay'][i]['src']
             writer=html.json()['data']['tracksAudioPlay'][i]['trackName']
             urllib.request.urlretrieve(m4a,dir_path+writer+'.mp3')
             mysql.creat_table( "CREATE TABLE school(ID INT PRIMARY KEY,FIRST_NAME  VARCHAR(50) NOT NULL,LAST_NAME  VARCHAR(100), AGE INT,SEX CHAR(1),INCOME FLOAT )")
             mysql.add_data("INSERT INTO school(FIRST_NAME,LAST_NAME)VALUES ('%s','%s')"%(writer,m4a))
             content=mysql.fet_data("SELECT * FROM school")
         for item in content:
             print(item[2])
    def mkdir(path):
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print(path+' 创建成功')
            return True
        else:
            print(path+' 目录已存在')
            return False
class Mysql(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(
               host='localhost',
               port=3306,
               user='root',
               password='root',
               database='linshun',
               charset='utf8'
            )
        except Exception as e:
            print(e)
        else:
            print('连接成功')
            self.cur = self.conn.cursor()
    def creat_table(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
    def add_data(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
    def fet_data(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()
    def up_data(self):
        sql="UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
    def del_data(self):
        sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
        try:
          self.cur.execute(sql)
          self.conn.commit()
        except:
            self.conn.rollback()
    def close_data(self):
        self.conn.close()



