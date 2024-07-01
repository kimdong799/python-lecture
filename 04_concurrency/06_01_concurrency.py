# Chapter 06_01
# 병행성(Concurrency)
# Iterator, Generator

# Iterator
# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args... : iterable

# 반복 가능한 이유 -> 내부적으로 iter(x) 함수 호출
t = 'ABCDEEFGHIJKLMNOPQRSTUVWXYZ'
print('__iter__' in dir(t))

for c in t:
    print(c, end=' ')

w = iter(t)
print('__iter__' in dir(w))
print('__next__' in dir(w))

# 위치 정보를 기억하고 있음
print(next(w)) # A
print(next(w)) # B
print(next(w)) # C

# 반복문이 내부적으로 동작하는 로직
# while
w = iter(t)

while True:
    try:
        print(next(w), end=' ')
    except StopIteration:
        print('-StopIteration-')
        break

print()

# 반복형 확인 1
# hasattr()
print(hasattr(t, '__iter__'))

# 반복형 확인 2
# 상속받았는지 확인
from collections import abc
print(isinstance(t, abc.Iterable))

print()
print()

# next 패턴
class WordSpliter():
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)
    
wi = WordSpliter('DO today what you could do tommorow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리 조각 사용

# __iter__ 함수를 yield 키워드로 구현하면 제네레이터 생성 가능
class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')
    
    # 리턴, 예외처리 생략 가능
    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wg = WordSplitGenerator('DO today what you could do tommorow')

wt = iter(wg)

print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))