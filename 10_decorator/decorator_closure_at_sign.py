# decorator_closure.py 에서 만든 데코레이터를 '@' 을 이용해 간편하게 사용할 수 있다.

def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
  
@trace
def hello():
  print("hello")

@trace
def world():
  print("world")