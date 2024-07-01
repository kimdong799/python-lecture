# Chapter 02-03
# 객체지향 프로그래밍 (OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트 (프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Kim
    Date : 2024.01.24
    Description : Class, Static, Instance Method
    """

    # 클래스 변수 선언 Scope
    # 클래스 변수는 모든 인스턴스가 공유한다!
    price_per_raise = 1.0

    # 인스턴스 메소드에 self가 첫번째 매개변수로 넘어오도록 정해짐
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 매직메소드를 이용한 클래스 속성을 내가 원하는 방식으로 출력
    # 사용자 레벨에서 프린트문으로 어떤 정보를 확인할 때 사용
    def __str__(self):
        return f'str: {self._company} - {self._details}'

    # 엔지니어 레벨에서 텍스트뿐만 아니라 객체의 엄격한 타입 정보를 인식할 수 있는 공식적인 자료로 사용하고자 할 때 사용
    # __str__ 메소드가 구현되어 있으면 __str__이 실행됨
    def __repr__(self):
        return f'repr: {self._company} - {self._details}'
    
    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print(f'Current ID : {id(self)}')
        print(f'Car Detail Info : {self._company} {self._details.get("price")}')

    # Instance Method
    # 인스턴스의 정보를 확인하기 위해 직접 Attibute에 접근하는 것은 좋지 못함.
    # 별도의 정보 출력을 위한 메소드 구현을 통해 데이터 은닉화가 중요
    def get_price(self):
        return f'Before Car Price -> company : {self._company}, price : {self._details.get("price")}'

    # Instance Method
    def get_price_culc(self):
        return f'After Car Price -> company : {self._company}, price : {self._details.get("price") * Car.price_per_raise}'

    # Class Method
    # 클래스 메소드는 @classmethod라는 데코레이터 사용
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return f'OK! This car is {inst._company}'
        else:
            return f'Sorry This car is not Bmw.'

# Self 의미
car1 = Car('Ferari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})

# 전체정보
car1.detail_info()
car2.detail_info()

# 가격정보(직접 접근)
print(car1._details.get('price'))
print(car1._details['price'])

# 가격정보(인상 전)
print(car1.get_price())
print(car1.get_price_culc())

# 가격 인상
# 가격정보(캐)
print(car1.get_price())
print(car1.get_price_culc())

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격정보(인상 후)
print(car1.get_price())
print(car1.get_price_culc())

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1)
Car.raise_price(1.5)

# 가격정보(인상 후)
print(car1.get_price())
print(car1.get_price_culc())

# 차종 확인 (인스턴스 메소드)
# 인스턴스 메소드는 Class, Instance 모두 호출 가능함
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))