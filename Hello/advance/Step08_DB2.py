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
        
        #데이터 입력 받기
        inputName=raw_input(u'이름: ').decode('utf-8')
        inputAddr=raw_input(u'주소: ').decode('utf-8')
        
        #실행할 sql 문
        sql='''
            INSERT INTO member
            (name, addr) 
            VALUES(%s, %s)
        '''
        
        #sql 문 수행하기
        cursor.execute(sql, (inputName, inputAddr))
        
        #DB 에 실제 반영하기
        conn.commit()
        
        print u"회원 정보를 저장했습니다."
    
    except Exception, e:
        print e
    
    finally:
        try:
            conn.close()
        
        except NameError, ne:
            print ne
    
    print u"Step08_DB2.py 가 종료됩니다."