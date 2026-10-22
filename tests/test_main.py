import unittest
import main as m

class Behavior(unittest.TestCase):
    def test_behavior(self):
        self.assertEqual(m.earliest_finish({'A':(2,[]),'B':(3,['A'])})['B'],5)
        with self.assertRaises(ValueError): m.earliest_finish({'A':(1,['A'])})
        with self.assertRaises(ValueError): m.earliest_finish({'A':(1,['missing'])})
