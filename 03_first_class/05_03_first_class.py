# Chapter 05-03
# 일급 함수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능

# Closure 사용
def closure_ex1():
    # Free variable
    # 클로저 영역
    series = [] # series는 변수 값의 주소만을 가진 참조형 변수이기에 오류가 발생하지 않음
    def averager(v):
        series.append(v)
        print(f'inner >>> {series} / {len(series)}')
        return sum(series) / len(series)
    return averager # * averager 함수 결과를 closure_ex1 함수에서 반환 *

avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars) # 지유변수 출력
print(avg_closure1.__closure__[0].cell_contents) # 자유변수 값 출력

# 잘못된 클로져 사용
def closure_ex2():
    # Free varaible
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1
        total += v
        return total/cnt
    return averager


def closure_ex3():
    # Free varaible
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total # nonlocal 예약어 사용
        cnt += 1
        total += v
        return total/cnt
    return averager

print()
print()

avg_closure2 = closure_ex2()
# print(avg_closure2(10)) # 예외

avg_closure3 = closure_ex3()
print(avg_closure3(10))
print(avg_closure3(20))
print(avg_closure3(30))
