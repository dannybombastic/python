import unittest
def doblar(a): return a*2
def sumar(a,b): return a+b
def is_par(x): return x % 2 == 0

class PruebasFunciones(unittest.TestCase):

    
    def test_doblar(self):
        self.assertEqual(doblar(10),20)
        self.assertEqual(doblar("ab"),"abab")
        
    def test_sumar(self):
        self.assertEqual(sumar(10, 10), 20)
        self.assertEqual(sumar("ab", "ab"), "abab")

    
    def test_par(self):
        self.assertEqual(is_par(13), True)
        self.assertEqual(is_par(11), False)

if __name__ == "__main__":
    unittest.main()