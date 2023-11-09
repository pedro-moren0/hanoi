import unittest

from hanoi import *


class TestSwitch(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(switch([], 'a', 'b'), [])

    def test_singleton_fst_pos(self):
        self.assertEqual(switch([('a', 'b')], 'a', 'c'), [('c', 'b')])

    def test_singleton_snd_pos(self):
        self.assertEqual(switch([('a', 'b')], 'b', 'c'), [('a', 'c')])

    def test_singleton_fst_and_snd_pos(self):
        self.assertEqual(switch([('b', 'c')], 'b', 'c'), [('c', 'b')])

    def test_general_case(self):
        tuple_list = [('a', 'b'), ('b', 'a'), ('b', 'c'),
                      ('c', 'b'), ('a', 'c'), ('c', 'a')]
        expected = [('c', 'b'), ('b', 'c'), ('b', 'a'),
                    ('a', 'b'), ('c', 'a'), ('a', 'c')]
        self.assertEqual(switch(tuple_list, 'a', 'c'), expected)


class TestHanoi(unittest.TestCase):
    def test_n_1(self):
        expected = [('A', 'C')]
        self.assertEqual(hanoi(1), expected)
        self.assertEqual(hanoi_len(1), len(expected))

    def test_n_2(self):
        expected = [('A', 'B'), ('A', 'C'), ('B', 'C')]
        self.assertEqual(hanoi(2), expected)
        self.assertEqual(hanoi_len(2), len(expected))

    def test_n_3(self):
        expected = [
            ('A', 'C'),
            ('A', 'B'),
            ('C', 'B'),
            ('A', 'C'),
            ('B', 'A'),
            ('B', 'C'),
            ('A', 'C')
        ]
        self.assertEqual(hanoi(3), expected)
        self.assertEqual(hanoi_len(3), len(expected))

    def test_n_4(self):
        expected = [
            ('A', 'B'),
            ('A', 'C'),
            ('B', 'C'),
            ('A', 'B'),
            ('C', 'A'),
            ('C', 'B'),
            ('A', 'B'),
            ('A', 'C'),
            ('B', 'C'),
            ('B', 'A'),
            ('C', 'A'),
            ('B', 'C'),
            ('A', 'B'),
            ('A', 'C'),
            ('B', 'C'),
        ]
        self.assertEqual(hanoi(4), expected)
        self.assertEqual(hanoi_len(4), len(expected))

    def test_n_5(self):
        expected = [
            ('A', 'C'),
            ('A', 'B'),
            ('C', 'B'),
            ('A', 'C'),
            ('B', 'A'),
            ('B', 'C'),
            ('A', 'C'),
            ('A', 'B'),
            ('C', 'B'),
            ('C', 'A'),
            ('B', 'A'),
            ('C', 'B'),
            ('A', 'C'),
            ('A', 'B'),
            ('C', 'B'),

            ('A', 'C'),

            ('B', 'A'),
            ('B', 'C'),
            ('A', 'C'),
            ('B', 'A'),
            ('C', 'B'),
            ('C', 'A'),
            ('B', 'A'),
            ('B', 'C'),
            ('A', 'C'),
            ('A', 'B'),
            ('C', 'B'),
            ('A', 'C'),
            ('B', 'A'),
            ('B', 'C'),
            ('A', 'C'),

        ]
        self.assertEqual(hanoi(5), expected)
        self.assertEqual(hanoi_len(5), len(expected))


if __name__ == '__main__':
    unittest.main()
