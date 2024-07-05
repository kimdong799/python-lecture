# 가변 인수 함수 데코레이터

def trace(func):
  def wrapper(*args, **kwargs):
    r = func(*args, **kwargs)
    print(f"{func.__name__}(args={args}, kwargs={kwargs}) -> {r}")
    
    return r
  return wrapper

@trace
def get_max(*args):
  return max(args)

@trace
def get_min(**kwargs):
  return min(kwargs.values())

print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))