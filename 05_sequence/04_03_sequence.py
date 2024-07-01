# Chapter 04-03
# 시퀀스형
# 컨테이너 (Container : 서로 다른 자료형[List, tuple, collections.deque])
# 플랫 (Flat : 한개의 자료형[str, bytes, bytearray, array.array, memooryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(str, bytes, tuple)
# 해시테이블
# Key에 Value를 저장하는 구조
# 파이썬 dict 해시테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해시 주소 -> key에 대한 value 참조

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50]) # list는 가변형 데이터 타입으로 hash값 참조 불가

print(hash(t1))
# print(hash(t2)) # 예외 발생

print()
print()

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v) # k를 Key값으로 v를 리스트로 추가

print(new_dict2)

# 주의사항
new_dict3 = {k: v for k, v in source}
print(new_dict3) # value가 업데이트됨