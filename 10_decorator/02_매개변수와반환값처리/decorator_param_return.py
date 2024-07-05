# 매개변수와 반환값을 처리하는 데코레이터

def trace(func):
  def wrapper(a, b):
    r = func(a, b)
    print(f'{func.__name__}(a={a}, b={b}) -> {r}') # 매배견수와 반환값 출력
    return r
  return wrapper

@trace
def add(a, b):
  return a + b

print(add(10, 20))