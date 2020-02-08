import unittest

from pairwise_alignment import pairwise_alignment

class TestAlignment(unittest.TestCase):

    def test_pairwise_alignment(self):
        a = "GCATGCU"
        b = "GATTACA"
        data = '{}\n{}\n'.format(a, b)
        results, score = pairwise_alignment(data)
        ans = 0

        self.assertEqual(score, ans)
            

if __name__ == '__main__':
    unittest.main()
