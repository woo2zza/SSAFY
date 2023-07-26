# 클래스 정의  (속성 + 메서드)
'''
class Person:
    # 클래스 속성(변수)
    blood_color = 'red'

    # 메서드
    def __init__(self, name):   # __ >> 개발자가 직접호출하지 않고 자연스럽게 호출(매직 메서드, 생성자 메서드)
                                # name이라는 생성자를 작성 안할수있음.                     
        self.name = name
    # 인스턴스 메서드
    def singing(self):                             
        return f'{self.name}가 노래합니다.'         
    


# 인스턴스 생성
singer1 = Person('iu')   # 인자가 반드시 필요
singer2 = Person('bts')  # 같은 클래스를 가진 다른 인스턴스
                         # init가 들어가는 이유
 



# 메서드 호출
print(singer1.singing())
print(singer2.singing())


# 속성(변수) 사용
print(singer1.blood_color)
print(singer2.blood_color)
'''
print('▶ 보강')

#객체지향 프로그래밍(OOP)

'''
객체?

lol 게임 하나를 개발한다고 가정
게임 - 케릭터 아리 올라프 빅토르..
       각 게릭터 별 hp mp 스킬 기술 ...

이름 : 올라프
hp : 100
mp : 50
스킬  q = 도끼던지기()
      w = 공격력강화()
      e = 도끼로 머리 찍기()

이름 : 아리
hp : 50
mp : 100
스킬  q = 구슬던지기()
      w = 이동속도()
      e = 유혹하기()

      
이름 :
hp :                <<< 클래스
mp :
스킬 :

클래스를 통해서 만든 게임 케릭터 >> 객체 or 클래스의 인스턴스


절차지향             
직접 타먹는 방식                  
한명이 뜨거운묵을 붓고 있으면 다른일을을 한다
변수가 데이터를 접근할 때 기다리지 않고 메모리에 접근

객체지향
커피 자판기
실행속도가 느리다

'''
# 속성 = numberOfCalcul (클래스 변수) / result (인스턴스 변수)
# 메소드 = init , getsum
# 인스턴스 = cal1

# init(생성자함수) 인스턴스를 지정하면 반드시 실행
# self = 함수를 사용하는 인스턴스를 의미
class calculator():
    numberOfCalcul = 0              
    def __init__(self):
        self.result = 0
        calculator.numberOfCalcul += 1      # 인스턴스가 생성될때마다 반드시 실행되기 때문에 인스턴스의갯수 판단

    def getsum(self, value):
        self.result += value
        return self.result

# 인스턴스 변수
cal1 = calculator()

print(cal1.getsum(3))  # 3
print(cal1.getsum(4))  # 7
print(cal1.getsum(5))  # 12
# 인스턴스변수 - 인스턴스 개인이 개별적으로 가지고 있는 속성

cal2 = calculator()

print(cal2.getsum(6))  # 6
print(cal2.getsum(7))  # 13
print(cal2.getsum(8))  # 21

# 클래스 변수 - 한 클래스안의 모든 인스턴스가 공유하는 속성(변수)
print(calculator.numberOfCalcul)

# 클래스 변수 사용시 주의점!
# 클래스 변수값을 변경할 때에는 반드시 항상!!! 클래스명, 클래스변수 형식으로 접근해야 한다.

calculator.numberOfCalcul = 6
print(cal1.numberOfCalcul)
print(cal2.numberOfCalcul)

# 결론 : 클래스 변수 : 모든 인스턴스가 공유 / 인스턴스 전체가 사용해야 하는 값을 저장할때 사용 / 인스턴스로 접근 금지
# 인스턴스 변수 : 각 인스턴스별로 독립되어 있음/ 각 인스턴스가 따로값을 저장해야 할 때 사용

# 메서드
# 인스턴스 메소드 : 우리가 평소에 많이 쓰던 메소드
# 정적 메소드 : 클래스 변수나 인스턴스 변수를 사용하지 않을 때 사용
# 클래스 메소드 : 데코레이터를 사용하여 정의, 호출시 첫번째 인자로 사용

# 1) . 인스턴스 메소드 
'''
class plus_minus:
    # def data(self, first, second):
    #     self.first = first
    #     self.secnd = second
    def __init__(self,first,second):
        self.first = first
        self.seont = second


    def plus(self):
        result = self.first + self.second
        return result
    
    def minus(self):
        result = self.first - self.second
        return result
    

a = plus_minus()
a.data(3)
b = plus_minus()
b.data(2,7)
print(a.first, b.second)
'''

class car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __add__(self, another):
        return self.price + another.price
    
kia = car('k8', 500)
bmw = car('m5', 100)

print(kia.price + bmw.price)
print(kia + bmw)                # 커스터 마이징 (인스턴스의 합으로 두 차량가격의 합 출력)

# 인스턴스 삭제!
del bmw






print(' 클래스 관련 용어, 속성 - 클래스 변수 인스턴스 변수 . 메소드 - 인스턴스메소드 -------------------------------------------')
'''
def deco(fnc):
    def wrapper(value):
        print('뉴진스' * 3 )
        fnc(value)
        print('하입보이' * 3)
    return wrapper

@deco
def call_name(name):
    print(name)

def call_age(age):
    print(age)

call_name('심우석')
''' 
print('데코레이터---------------------------')
'''
# 정적메소드

class car:

    @staticmethod
    def add_price(one, another):
        print(one + another)

car.add_price(400, 800)

# 정적 메소드에는 @staticmethod 가 붙습니다.
# 그리고 인스턴스 메소드와 달리 self가 없다. 

# 정적 메소드 호출할 때는 클래스에서 바로 메소드를 호출하면 됨
# 인스턴스 없어도 문제 될 것이 없음

# self를 사용하지 않는다 !!! >> self와 같은 속성을 다루지 않고 함수의 행동(기능)만 단순하게 정의해서 사용하고 싶을 때 이용하는 메소드
'''
print('스태틱 메소드------------------------------------')

# 클래스 메소드
class make_pie:
    cnt = 0
    def __init__(self, name):
        self.name = name
        make_pie.cnt += 1

    
    @classmethod
    def number_of_pies(cls):                            # cls = make_pie
        print(f'파이를{cls.cnt}명이 만들고 있습니다.')


a = make_pie('kevin')
b = make_pie('bob')
c = make_pie('kate')
make_pie.number_of_pies()

# 클래스 메소드는 클래스메소드를 이용을 해서 인스턴스 없이 클래스 변수의 값을 바꾸고 싶을때 사용
print('클래스 메소드 -------------------------------------------')

print('정리')
'''
속성: 클래스 속성 / 인스턴스 속성
메소드 : 인스턴스 메소드 / 정적 메소드 / 클래스 메소드


클래스 속성(변수)
모든 인스턴스가 공유하는 변수로써 인스턴스 모두가 사용해야 하는 값을 저장할때 사용하는 변수
접근시 반드시 클래스를 통해서 접근을 해야 한다.(인스턴스를 이용해서 접근하는것은 금지!)
                            

인스턴스 속성
클래스 인스턴스가 각각 값을 따로 저장할때 사용

인스턴스 메소드: self를 첫번째 매개변수로 사용( self >> 해당 클래스의 인스턴스를 의미 )
정적 메소드 : 매개변수에 self 없음 / 인스턴스 없이 메소드의 순수한 기능 또는 동작만 사용하고 싶을때 사용하는 메소드
클래스 메소드 : 매개변수 self 없고 cls 사용 / cls를 통해서 클래스 변수의 값을 바꾸고 싶을때 사용하는 메소드
'''