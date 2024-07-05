"""
데코레이터 패턴은 구현을 변경하지 않고 객체에 새로운 기능을 동적으로 추가하는 데 사용됨.
새 기능이 전체 하위 클래스가 아닌 특정 개체에만 추가되어 구현을 변경하지 않는다.
"""

class TextTag:
  """Reperesents a base text tag"""
  def __init__(self, text: str) -> None:
    self._text = text
    
    def render(self) -> str:
      return self._text
    
class BoldWrapper(TextTag):
  """Wraps a tag in <b>"""
  def __init__(self, wrapped: TextTag) -> None:
    self._wrapped = wrapped
    
  def render(self) -> str:
    return f"<b>{self._wrapped.render()}</b>"
  
class ItalicWrapper(TextTag):
  """Wraps a tag in <i>"""
  def __init__(self, wrapped: TextTag) -> None:
    self._wrapped = wrapped
    
  def render(self) -> str:
    return f"<i>{self._wrapped.render()}</i>"
  
def main():
    """
    >>> simple_hello = TextTag("hello, world!")
    >>> special_hello = ItalicWrapper(BoldWrapper(simple_hello))

    >>> print("before:", simple_hello.render())
    before: hello, world!

    >>> print("after:", special_hello.render())
    after: <i><b>hello, world!</b></i>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()