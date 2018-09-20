#-*- coding:utf-8 -*-

'''
[sqllite3 database]
python 에 내장
'''
import sqlite3


if __name__ == '__main__':
    print sqlite3.sqlite_version
    
    try:
        conn=sqlite3.connect('test.db')
        
        #cursor 객체 얻어오기
        cursor=conn.cursor()
        
        #table 없으면 만들기
        cursor.execute('''
            CREATE TABLE 
            IF NOT EXISTS member
            (num INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, addr TEXT)
        ''')
        
        #데이터 입력 받기
        inputName=raw_input(u"이름: ").decode('utf-8')
        inputAddr=raw_input(u"주소: ").decode('utf-8')
        
        #sqlite 의 바인딩 인자는 ? 로 표기된다.
        sql='''
            INSERT INTO member 
            (name, addr) 
            VALUES(?, ?)
        '''
        #sql 문 수행
        cursor.execute(sql, (inputName, inputAddr))
        conn.commit()
        
        print u"회원정보를 저장했습니다."
    
    except Exception, e:
        print e
    
    finally:
        try:
            conn.close()
        
        except NameError, ne:
            print ne 
    print u"Step09_sqlite.py 가 종료 됩니다."