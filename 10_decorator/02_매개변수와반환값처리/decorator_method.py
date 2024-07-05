# 메소드에 데코레이터를 사용할 땐 self를 인자로 전달해야함!
# 클래스 메소드는 cls를 전달!

def trace(func):
  def wrapper(self, a, b):
    r = func(self, a, b)
    print(f'{func.__name__}(a={a}, b={b}) -> {r}')
    return r
  return wrapper

class Calc:
  def __init__(self) -> None:
    print(f"instance of {self.__class__.__name__} initialized")
  
  @trace
  def add(self, a, b):
    return a + b

c = Calc()
print(c.add(10, 20))