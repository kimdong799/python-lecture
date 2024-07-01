# Chapter 03-03
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

# 두 점 사이의 거리 구하기
l_leng1 = sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# named tuple
# 데이터 구조 측면에서 보다 효율적으로 관리 가능
from collections import namedtuple

# named tuple 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print('<named tuple info>')
print(pt3, pt4)
l_leng2 = sqrt((pt3[0] - pt4[0])**2 + (pt3[1] - pt4[1]) ** 2)
print(l_leng2)

# named tuple 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default = False, 중복, 예약어

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict) # ** = unpacking / Dict -> 튜플

print(p1)
print(p2)
print(p3)
# rename 테스트
print(p4)
print(p5)

# 사용
print(p1.x + p2.y)

x, y = p3
print(x, y)

# 네임드 튜플 메소드
temp = [52, 38]

# 리스트 -> 튜플
p4 = Point._make(temp)
print(p4)

# _fields : 필드 네임 확인 (Key 조회)
print(p1._fields, p2._fields, p3._fields)

# _asdict() : Ordered Dict 반환
print(p4._asdict())

# 실사용 실습
# 반 20명, 4개의 반 (A, B, C, D)
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = list('ABCD')

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

# 추천
students2 = [Classes(rank, number)
             for rank in list('ABCD')
             for number in [str(n) 
                for n in range(1, 21)]]
print(len(students2))
print(students2)