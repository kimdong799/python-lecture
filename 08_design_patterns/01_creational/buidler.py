"""
생성형 - 빌더(Builder) 패턴
- 객체를 생성하는 과정을 단순화하여 가독성과 유연성을 높임
- 객체를 생성하는 과정을 단계별로 처리
- 객체 생성 과정을 조합하여 객체 생성
- 생성자의 매개변수가 많아지거나 객체 생성 과정이 복잡해지는 경우에 유용함
"""

# Abstract Building
class Building:
  def __init__(self) -> None:
    self.build_floor()
    self.build_size()
    
  def build_floor(self):
    raise NotImplementedError
  
  def build_size(self):
    raise NotImplementedError
  
  def __repr__(self) -> str:
    return "Floor: {0.floor} | Size: {0.size}".format(self)
  
  
# Concrete Buildings
class House(Building):
  def build_floor(self) -> None:
    self.floor = "One"
    
  def build_size(self) -> None:
    self.size = "Big"
    
    
class Flat(Building):
  def build_floor(self) -> None:
    self.floor = "More than One"
    
  def build_size(self) -> None:
    self.size = "Small"
    
    
class ComplexBuilding:
  def __repr__(self) -> str:
    return "Floor: {0.floor} | Size: {0.size}".format(self)
  
class ComplexHouse(ComplexBuilding):
  def build_floor(self) -> None:
    self.floor = "One"
    
  def build_size(self) -> None:
    self.size = "Big and fancy"
    
# 인스턴스 생성 함수
def construct_buildings(cls) -> Building:
  # class를 받아 Building 인스턴스 생성
  building = cls()
  building.build_floor()
  building.build_size()
  return building

def main():
    """
    >>> house = House()
    >>> house
    Floor: One | Size: Big

    >>> flat = Flat()
    >>> flat
    Floor: More than One | Size: Small

    # Using an external constructor function:
    >>> complex_house = construct_building(ComplexHouse)
    >>> complex_house
    Floor: One | Size: Big and fancy
    """

if __name__ == "__main__":
    import doctest

    doctest.testmod()