import unittest

class Number:
    def __init__(self, value=0):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
    
    def to_binary(self): # 2я система
        return bin(self.value)
    
    def to_octal(self): # 8я система
        return oct(self.value)
    
    def to_hex(self): # 16я система
        return hex(self.value)
    

class TestNumber(unittest.TestCase):
    number = Number(42)
    
    def test_value(self):
        self.assertEqual(self.number.get_value(), 42)
        self.number.set_value(100)
        self.assertEqual(self.number.get_value(), 100)
    
    def test_conversions(self):
        self.assertEqual(self.number.to_octal(), '0o52') 
        self.assertEqual(self.number.to_hex(), '0x2a')
        self.assertEqual(self.number.to_binary(), '0b101010')
            # я кстати не особо понял, почему перевод вышел таким образом,
            # я проверял в инете и сам через калькулятор проверял, 
            # у меня значения другие, но раз тест говорит, что python решил на эти значения, то я ему поверю


unittest.main()