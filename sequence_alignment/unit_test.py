import unittest

from global_alignment import global_alignment

class TestAlignment(unittest.TestCase):

    def test_global_alignment(self):
        a = "GCATGCU"
        b = "GATTACA"
        data = '{}\n{}\n'.format(a, b)
        results, score = global_alignment(data)
        ans = 0

        self.assertEqual(score, ans)
            

if __name__ == '__main__':
    unittest.main()
