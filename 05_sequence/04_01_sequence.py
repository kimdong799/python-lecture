# Chapter 04-01
# 시퀀스형
# 컨테이너 (Container : 서로 다른 자료형[List, tuple, collections.deque])
# 플랫 (Flat : 한개의 자료형[str, bytes, bytearray, array.array, memooryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(str, bytes, tuple)
# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending List)
chars = '+_)(*&^%$#@!)'
code_list1 = []

# 유니코드 리스트
for s in chars:
    code_list1.append(ord(s))

# List Comprehension
code_list2 = [ord(s) for s in chars]
print(code_list1, code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x: x>40, map(ord, chars)))
print(code_list4)

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()

# Generator 생성
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X)
# ( ) 로 Comprehension 사용 시 Generator로 생성됨
tuple_g = (ord(s) for s in chars)
print(tuple_g, type(tuple_g))

array_g = array.array('I', (ord(s) for s in chars))
print(array_g, type(array_g))
print(array_g.tolist())

print()
print()

# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21))) # generator object 출력됨, next 사용 필요
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s, end=" ")

print()
print()

# 리스트 주의
marks1 = [['~'] * 3 for _ in range(4)] # 리스트 생성을 반복한 것, 모두 다른 주소값을 가짐
print(marks1)

marks2 = [['~'] * 3] * 4 # 동일한 리스트가 4번 복사된 것, 모두 같은 주소값을 가짐
print(marks2)

# 수정
marks1[0][1] = 'X'
print(marks1)
# [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]

marks2[0][1] = 'X'
print(marks2)
# [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2]) # 모두 동일한 주소를 가짐

