import unittest

class MiPrueba(unittest.TestCase): 
	def test_algo(self): 
	    self.assertEqual(1 + 1, 2) 

if __name__ == '__main__': 
	unittest.main() 