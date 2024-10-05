from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):

    def test_add_number(self):
        res = calc.add(1, 2)
        self.assertEqual(res, 3)

    def test_substruct_number(self):
        re = calc.substruct(9, 5)
        self.assertEqual(re, 4)
