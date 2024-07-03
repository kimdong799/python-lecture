import unittest
from unittest.mock import patch

from abstract_factory import Dog, Cat, PetShop

class TestPetShop(unittest.TestCase):
  def test_dog_pet_shop_shall_show_dog_instance(self):
    dog_pet_shop = PetShop(Dog)
    cat_pet_shop = PetShop(Cat)
    
    with patch.object(Dog, "speak") as mock_Dog_speak:
      pet = dog_pet_shop.buy_pet("")
      pet.speak()
      self.assertEqual(mock_Dog_speak.call_count, 1)
      
    with patch.object(Cat, "speak") as mock_Cat_speak:
      cat = cat_pet_shop.buy_pet("")
      cat.speak()
      self.assertEqual(mock_Cat_speak.call_count, 1)
      
# unittest를 실행
if __name__ == '__main__':
    unittest.main()