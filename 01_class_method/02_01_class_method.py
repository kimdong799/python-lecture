# Chapter 02-01
# 객체지향 프로그래밍 (OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트 (프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩
# 변수가 너무 많아짐
# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

# 리스트 구조
# 관리가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'Silver', 'horsepower': 300, 'price': 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조
# 코드 반복, 중첩 문제(Key), 키 조회 예외 처리

car_dicts = [
    {'car_company': 'Ferari', 'car_datail': {'color': 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'Bmw', 'car_datail': {'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_datail': {'color': 'Silver', 'horsepower': 300, 'price': 6000}}
]

del car_dicts[1]
print(car_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

# 클래스는 명사로 생성
# Python에서 클래스는 Object 객체를 자동으로 상속받아 생성된다.
# 클래스에서 사용 가능한 매직메소드는 Object 객체의 기본 Method이다.
class Car():
    def __init__(self, company, details):
        self.company = company
        self.details = details

    # 매직메소드를 이용한 클래스 속성을 내가 원하는 방식으로 출력
    # 사용자 레벨에서 프린트문으로 어떤 정보를 확인할 때 사용
    def __str__(self):
        return f'str: {self.company} - {self.details}'

    # 엔지니어 레벨에서 텍스트뿐만 아니라 객체의 엄격한 타입 정보를 인식할 수 있는 공식적인 자료로 사용하고자 할 때 사용
    # __str__ 메소드가 구현되어 있으면 __str__이 실행됨
    def __repr__(self):
        return f'repr: {self.company} - {self.details}'
    
car1 = Car('Ferari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})
print(car1)
print(car2)
print(car3)

# 객체의 모든 속성정보(어트리뷰트)값 확인
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# dir 함수를 이용하면 모든 메타정보를 확인할 수 있음
print(dir(car1))

print()
print()

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# __str__, __repr__ 모두 구현 시 아래와 같이 List내의 객체 정보를 확인하는 경우 __repr__ 이 호출됨
print(car_list)

# 이 경우는 __str__로 객체 정보가 출력됨
for i in car_list:
    print(i)

# 명시적으로 지정하는 경우 __repr__로 출력할 수 있음
for i in car_list:
    print(repr(i))