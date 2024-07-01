# Chapter 02-02
# 객체지향 프로그래밍 (OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트 (프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Kim
    Date : 2024.01.08
    """

    # 클래스 변수 선언 Scope
    # 클래스 변수는 모든 인스턴스가 공유한다!
    car_count = 0


    # 인스턴스 메소드에 self가 첫번째 매개변수로 넘어오도록 정해짐
    def __init__(self, company, details):
        self.company = company
        self.details = details
        Car.car_count += 1

    # 매직메소드를 이용한 클래스 속성을 내가 원하는 방식으로 출력
    # 사용자 레벨에서 프린트문으로 어떤 정보를 확인할 때 사용
    def __str__(self):
        return f'str: {self.company} - {self.details}'

    # 엔지니어 레벨에서 텍스트뿐만 아니라 객체의 엄격한 타입 정보를 인식할 수 있는 공식적인 자료로 사용하고자 할 때 사용
    # __str__ 메소드가 구현되어 있으면 __str__이 실행됨
    def __repr__(self):
        return f'repr: {self.company} - {self.details}'
    
    def detail_info(self):
        print(f'Current ID : {id(self)}')
        print(f'Car Detail Info : {self.company} {self.details.get("price")}')

    def __del__(self):
        Car.car_count -= 1

# Self 의미
car1 = Car('Ferari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# 인스턴스 고유 ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1.company == car2.company)
print(car1 is car2)

# dir & __dict__ 확인
# dir은 상위 클래스로부터 상속받는 모든 것들을 표시하지만 값은 보여주지 않음
print(dir(car1))
print(dir(car2))

print()
print()

# __dict__는 딕셔너리 형태로 모든 속성정보를 상세하게 보여줌
print(car1.__dict__)
print(car2.__dict__)

# Docstring 출력
print(Car.__doc__)

car1.detail_info()
car2.detail_info()
car3.detail_info()

# 클래스 ID 확인
# 인스턴스의 부모인 Class를 확인하기 때문에 모두 동일한 ID가 출력됨
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))

# 에러가 발생하는 상황
# TypeError: detail_info() missing 1 required positional argument: 'self'
# Car.detail_info()
# 아래의 방법으로는 메소드 호출 가능
# car1이 self로 전달되기 때문
Car.detail_info(car1)

# Namespace에는 없는데 car_count가 출력되는 이유
print(car1.__dict__)

# __init__ 메소드에 car_count 증가 로직을 추가한 후 3개의 인스턴스가 생성된 3이 출력된다.
# 클래스 변수까지 확인하기 위해선 __dict__가 아닌 dir로 확인
print(car1.car_count)

# 클래스변수 접근
# 인스턴스와 클래스가 모두 공유하는 변수이기 때문에 다음과 같이 접근 가능하다.
print(car1.car_count)
print(Car.car_count)

del car2
# 삭제확인
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))


