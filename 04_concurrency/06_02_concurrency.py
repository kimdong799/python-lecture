# Chapter 06_02
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터(Worker)가 여러 작업을 동시에 수행 -> 속도

# Generator Ex 1
# 중단점 설정 및 기억
def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Countinue')
    yield 'B point'
    print('End')

# iter 함수에 들어간 함수는 Generator로 인식됨
temp = iter(generator_ex1())

print(next(temp)) # A Point 까지 수행
print(next(temp)) # B Point 부터 수행

# 반복문에서도 가능함 (Iterable)
for v in generator_ex1():
    print(v)

# Generator Ex 2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2) # yield 키워드는 return의 역할을 함
print(temp3) # 

for i in temp3:
    print(i)

print()
print()

# Generator Ex3 (중요 함수)
# filterfalse, takewhile, accumulate, chain, product, groupby

import itertools

# 무한대까지 증가, while 문 사용  X
gen1 = itertools.count(1, 2.5)
print(next(gen1))
print(next(gen1))
print(next(gen1))

# 조건
# itertools.takewhile()
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))
for v in gen2:
    print(v)

print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1, 2, 3, 4, 5])
for v in gen3:
    print(v)

print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print(v)

print()

# 연결1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5))

# 연결2
gen6 = itertools.chain(enumerate('ABC'))
print(list(gen6))

# 개별
gen7 = itertools.product('ABCDE')
print(list(gen7))

# 경우의 수
gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8))

# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')

for chr, group in gen9:
    print(chr, ' : ', list(group))

