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
        
        #select 할 회원의 num 입력 받기
        inputNum=input(u'select 할 회원 번호: ')
        
        #실행할 sql 문
        sql='''
            SELECT num, name, addr 
            FROM member 
            WHERE num=%s
        '''
        
        #sql 문 수행하기
        cursor.execute(sql, (inputNum,))
        
        """
        cursor.fetchone() 을 호출하면 tuple type 이 리턴된다.
        tuple 에는 select 된 row 의 정보가 순서대로 들어있다.
        select 된 결과가 없을 때는 None 이 리턴된다.
        """
        result=cursor.fetchone()
        if result:
            print u'번호: {}, 이름: {}, 주소: {}'.format(result[0], result[1], result[2])
        else:
            print u'{}번 회원은 존재하지 않습니다.'.format(inputNum)
    
    except Exception, e:
        print e
    
    finally:
        try:
            conn.close()
        
        except NameError, ne:
            print ne
    
    print u"Step08_DB2.py 가 종료됩니다."