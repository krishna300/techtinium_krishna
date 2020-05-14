

import unittest
import techtinium

# techtinium.py
class TestTechtinium(unittest.TestCase):

    
    def test_techtinium(self):
        r1={'output': [{'region': 'newyork', 'total_cost': 10150, 'machines': [('8XL', 7), ('XL', 1), ('L', 1)]}, {'region': 'india', 'total_cost': 9520, 'machines': [('8XL', 7), ('L', 3)]}, {'region': 'china', 'total_cost': 8570, 'machines': [('8XL', 7), ('XL', 1), ('L', 1)]}]}
        r2={'output': [{'region': 'newyork', 'total_cost': 774, 'machines': [('4XL', 1)]}, {'region': 'india', 'total_cost': 826, 'machines': [('2XL', 2)]}, {'region': 'china', 'total_cost': 670, 'machines': [('4XL', 1)]}]}
        r3={'output': [{'region': 'newyork', 'total_cost': 2200, 'machines': [('8XL', 1), ('2XL', 1), ('XL', 1), ('L', 1)]}, {'region': 'india', 'total_cost': 2133, 'machines': [('8XL', 1), ('2XL', 1), ('L', 3)]}, {'region': 'china', 'total_cost': 1890, 'machines': [('8XL', 1), ('XL', 3), ('L', 1)]}]}
        r4={'output': [{'region': 'newyork', 'total_cost': 1004, 'machines': [('4XL', 1), ('XL', 1)]}, {'region': 'india', 'total_cost': 1106, 'machines': [('2XL', 
2), ('L', 2)]}, {'region': 'china', 'total_cost': 870, 'machines': [('4XL', 1), ('XL', 1)]}]}
        r5={'output': [{'region': 'newyork', 'total_cost': 9854, 'machines': [('8XL', 6), ('4XL', 1), ('2XL', 1), ('XL', 1)]}, {'region': 'india', 'total_cost': 9319, 'machines': [('8XL', 6), ('2XL', 3), ('L', 2)]}, {'region': 'china', 'total_cost': 8350, 'machines': [('8XL', 6), ('4XL', 1), ('XL', 3)]}]}


        
        self.assertEqual(techtinium.get_run(1150),r1)
        self.assertEqual(techtinium.get_run(80), r2)
        self.assertEqual(techtinium.get_run(230), r3)
        self.assertEqual(techtinium.get_run(100), r4)
        self.assertEqual(techtinium.get_run(1100), r5)
    

       


if __name__ == '__main__':
    unittest.main()