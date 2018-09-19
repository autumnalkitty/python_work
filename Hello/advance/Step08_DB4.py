#-*- coding:utf-8 -*-

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
        
        #삭제할 회원의 번호 입력 받기
        inputNum=input(u'삭제할 회원의 번호: ')
        
        #실행할 sql 문
        sql='''
            DELETE FROM member 
            WHERE num=%s
        '''
        
        #sql 문 수행하기
        cursor.execute(sql, (inputNum,))
        
        #sql 문 수행의 영향을 받은 row 의 개수
        updateCount=cursor.rowcount
        if updateCount > 0:
            print u'{}번 회원 정보를 삭제했습니다.'.format(inputNum)
        else:
            print u'{}번 회원은 존재하지 않습니다.'.format(inputNum)
        
        #DB 에 실제 반영하기
        conn.commit()

    except Exception, e:
        print e
    
    finally:
        try:
            conn.close()
        
        except NameError, ne:
            print ne
    
    print u"Step08_DB2.py 가 종료됩니다."