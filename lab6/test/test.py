from src.main import Knutt_Morris_Pratt
import unittest


class Testing(unittest.TestCase):
    def test1(self):
        self.assertEqual(Knutt_Morris_Pratt("message", "age"), 4)

    def test2(self):
        self.assertEqual(Knutt_Morris_Pratt("haystack", "stack"), 3)
