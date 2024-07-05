# 호출할 함수를 매개로 받는 데코레이터 함수
def trace(func):
  def wrapper():
    print(func.__name__, "함수 시작")
    func()
    print(func.__name__, "함수 종료")
  return wrapper

def hello():
  print("hello")
  
def world():
  print("world")

# 데코레이터에 호출할 함수 전달
# trace 함수가 wrapper 함수를 반환하여 trace_hello 호출 = wrapper 함수 호출
trace_hello = trace(hello)
trace_hello()

trace_world = trace(world)
trace_world()