import unittest
from buidler import ComplexHouse, Flat, House, construct_buildings

class TestSimple(unittest.TestCase):
  # 메소드 이름은 test로 시작해야함
  def test_house(self):
    house = House()
    self.assertEqual(house.size, "Big")
    self.assertEqual(house.floor, "One")

  def test_flat(self):
    flat = Flat()
    self.assertEqual(flat.size, "Small")
    self.assertEqual(flat.floor, "More than One")
    
class TestComplex(unittest.TestCase):
  def test_house(self):
    house = construct_buildings(ComplexHouse)
    self.assertEqual(house.size, "Big and fancy")
    self.assertEqual(house.floor, "One")
    
# unittest를 실행
if __name__ == '__main__':
    unittest.main()