# Chapter 04-02
# 시퀀스형
# 컨테이너 (Container : 서로 다른 자료형[List, tuple, collections.deque])
# 플랫 (Flat : 한개의 자료형[str, bytes, bytearray, array.array, memooryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(str, bytes, tuple)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpaking

# 교차할당
# b, a = a, b

print(divmod(100, 9))
print(divmod(*(100, 9))) # 튜플을 Unpacking하여 인자 2개 전달 "*"
print(*(divmod(100, 9))) # return된 tuple도 Unpacking하여 print

print()

# return될 값의 갯수보다 할당할 변수가 적은 경우 아래와 같이 사용도 가능
x, y, *rest = range(10)
print(x, y, rest)

# return될 값의 갯보다 할당할 변수가 많은 경우 빈 리스트로 반환
x, y, *rest = range(2)
print(x, y, rest)

# 나머지 값들은 rest 변수에 리스트로 할당됨
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()

# Mutable(가변), Immutable(불변)
l = (15, 20, 25) # 불변
m = [15, 20, 25] # 가변

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

# 곱해서 새로운 변수에 할당하여 id가 달라짐
print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

# 불변형은 id값이 계속 바뀜, 내부적으로 id가 재할당됨
# 가변형은 id값이 동일함
# 변경이 심한 데이터는 list를 활용하자
print(l, id(l))
print(m, id(m))

# sort vs sorted
# reverse, key=len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print(f'sorted - {sorted(f_list)}')

# 역순 정렬(내림차)
print(f'sorted - {sorted(f_list, reverse=True)}')

# 길이순
print(f'sorted - {sorted(f_list, key=len)}')

# 함수
# 마지막 글자 기준 정렬
print(f'sorted - {sorted(f_list, key=lambda x: x[-1])}')

# 함수 + 역순
# 마지막 글자 기준 정렬
print(f'sorted - {sorted(f_list, key=lambda x: x[-1], reverse = True)}')

# sort : 정렬 후 객체 직접 변경 (원본 수정)

# 반환 값 확인(None)
print(f'sort - {f_list.sort()}', f_list)
print(f'sort - {f_list.sort(reverse=True)}', f_list)
print(f'sort - {f_list.sort(key=len)}', f_list)
print(f'sort - {f_list.sort(key=lambda x: x[-1])}', f_list)
print(f'sort - {f_list.sort(key=lambda x: x[-1], reverse=True)}', f_list)

# list vs array 적합한 사용법
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열, 리스트와 거의 호환