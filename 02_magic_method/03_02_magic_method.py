# Chapter 03-02
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 클래스 예제 2
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50, 15)
# Max(5, 10) = 10

class Vector(object):
    def __init__(self, *args):
        '''
        Create a vector, example : v = Vector(5, 10)
        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''
        Return the vector information.
        '''
        return 'Vector(%r, %r)' % (self._x, self._y)
    
    def __add__(self, other):
        '''
        Return the vector addtion of self and other
        '''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        '''
        Return the vector multiply of self and y
        '''
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))

print(Vector.__init__.__doc__)
print(Vector)

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(bool(v1), bool(v2), bool(v3))