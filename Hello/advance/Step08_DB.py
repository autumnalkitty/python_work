#-*- coding:utf-8 -*-

def test(num, name, addr):
    print num, name, addr

tuple1=(1, u'김구라', u'노량진')
dict1={'num':2, 'name':u'해골', 'addr':u'행신동'}

#test 함수 call 하는 방법
""" 
test(3, u'원숭이', u'동물원')
test(*tuple1) #test(1, u'김구라', u'노량진')
test(**dict1) #test(num=2, name=u'해골', addr=u'행신동')
"""

import mysql.connector

#DB 접속 정보를 dict type 에 담는다.
config={
        'user':'root', 
        'password':'maria', 
        'host':'127.0.0.1', 
        'database':'acorn', 
        'port':3306 #default
    }

if __name__ == '__main__':
    try:
        #MariaDB 연결 객체
        conn=mysql.connector.connect(**config) #dict type 매치
        
        #cursor: PreparedStatement in JAVA
        cursor=conn.cursor()
        
        #실행할 sql 문
        sql='''
            SELECT num, name, addr 
            FROM member 
            ORDER BY num DESC
        '''
        #sql 문 실행
        cursor.execute(sql)
        
        """
        result: ResultSet in JAVA
        tuple 이 저장된 list type: [(), (), (), …]
        tuple 에는 select 된 row 의 정보가 순서대로 들어있다.
        """
        result=cursor.fetchall()
        
        for tmp in result:
            num=tmp[0]
            name=tmp[1]
            addr=tmp[2]
            print u'번호: {}, 이름: {}, 주소: {}'.format(num, name, addr)
    
    except Exception, e:
        print e
    
    finally:
        try:
            conn.close()
        
        except NameError, ne:
            print ne
    
    print u"Step08_DB.py 가 종료됩니다."