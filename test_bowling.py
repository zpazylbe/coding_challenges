# unit test for ten_pin_bowling.py challenge

import ten_pin_bowling as tpb

import unittest


class TestCalc(unittest.TestCase):

    def test(self):
        self.assertEqual(tpb.bowlingScore('X X X X X X X X X XXX'), 300)
        self.assertEqual(tpb.bowlingScore('90 90 90 90 90 90 90 90 90 90'), 90)
        self.assertEqual(tpb.bowlingScore('5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5'), 150)
        self.assertEqual(tpb.bowlingScore('00 00 00 00 00 00 00 00 00 00 00'), 0)
        self.assertEqual(tpb.bowlingScore('X 0/ X 50 8/ 90 X 81 10 4/X'), 137)
        self.assertEqual(tpb.bowlingScore('62 71  X 90 8/  X  X 35 72 5/8'), 140)
        self.assertEqual(tpb.bowlingScore('X X 9/ 80 X X 90 8/ 7/ 44'), 171)


if __name__ == '__main__':
    unittest.main()