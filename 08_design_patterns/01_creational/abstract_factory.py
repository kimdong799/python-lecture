"""
추상 팩토리 패턴은 연관성이 있는 객체 군이 여러개 있을 경우 이들을 묶어 추상화하고, 
어떤 구체적인 상황이 주어지면 팩토리 객체에서 집합으로 묶은 객체 군을 구현화 하는 생성 패턴이다. 
클라이언트에서 특정 객체을 사용할때 팩토리 클래스만을 참조하여 특정 객체에 대한 구현부를 감추어 역할과 구현을 분리시킬 수 있다.
즉, 추상 팩토리의 핵심은 제품 '군' 집합을 타입 별로 찍어낼수 있다는 점이 포인트 이다. 
예를들어 모니터, 마우스, 키보드를 묶은 전자 제품군이 있는데 
이들을 또 삼성 제품군이냐 애플 제품군이냐 로지텍 제품군이냐에 따라 집합이 브랜드 명으로 여러갈래로 나뉘게 될때, 
복잡하게 묶이는 이러한 제품군들을 관리와 확장하기 용이하게 패턴화 한것이 추상 팩토리 이다.

출처: https://inpa.tistory.com/entry/GOF-💠-추상-팩토리Abstract-Factory-패턴-제대로-배워보자 [Inpa Dev 👨‍💻:티스토리]

ex) 선택한 팩토리(개, 고양이 또는 Random_animal)에 따라 애완동물 생성을 추상화

"""

import random
from typing import Type

class Pet:
  def __init__(self, name: str) -> None:
    self.name = name
    
  def speak(self) -> None:
    raise NotImplementedError
  
  def __str__(self) -> str:
    raise NotImplementedError
  
  
class Dog(Pet):
  def speak(self) -> None:
    print("woof")
    
  def __str__(self) -> str:
    return f"Dog<{self.name}>"
  
  
class Cat(Pet):
  def speak(self) -> None:
    print("meow")
    
  def __str__(self) -> str:
    return f"Cat<{self.name}>"
  
  
class PetShop:
  """A pet shot"""
  
  def __init__(self, animal_factory: Type[Pet]) -> None:
    """pet_factory is out abstract factory. We can set it at will."""
    
    self.pet_factory = animal_factory
    
  def buy_pet(self, name: str) -> Pet:
    """Creates and shows a pet using the abstract factory"""
    
    pet = self.pet_factory(name)
    print(f"Here is your lovely {pet}")
    return pet
  
# Show pets with various factories
def main() -> None:
  """
  # A Shop that sells only cats
  >>> cat_shop = PetShop(Cat)
  >>> pet = cat_shot.buy_pet("Lucy")
  Here is your lovely Cat<Lucy>
  >>> pet.speak()
  meow
  """
  
  if __name__ == "__main__":
    shop = PetShop(random_animal)
    import doctest
    
    doctest.testmod()