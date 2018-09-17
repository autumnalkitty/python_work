#-*- coding:utf-8 -*-

class AttackUnit:
    #모든 객체가 공유할 클래스 변수
    attackPower=10
    
    #인스턴스 메소드(참조값으로  호출하는 메소드)
    def attack(self):
        print u"{}의 파워로 공격합니다.".format(AttackUnit.attackPower)
        
    #클래스 메소드(클래스명으로 호출하는 메소드)
    @classmethod
    def setPower(cls, power): #인자로 전달되는 cls 에는 클래스의 참조값이 담겨있다.
        cls.attackPower=power #AttackUnit.attackPower=power 와 같은 코드
    
    @classmethod
    def showPower(cls):
        print u"현재의 공격력: {}".format(cls.attackPower)
    
if __name__ == '__main__':
    AttackUnit().attack()
    AttackUnit.setPower(20)
    AttackUnit.showPower()
    
    unit1=AttackUnit()
    unit1.attack()