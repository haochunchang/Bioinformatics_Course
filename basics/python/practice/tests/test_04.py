import unittest
# change this script to test
import solution_04_data_structure as ds

class TestDS(unittest.TestCase):
 
    def test_find_ori(self):
        dna = 'GATGGTACTTGACTACGTAAATT'
        dna = [n for n in dna]
        ori = 'GGT'

        result = ds.find_ori(dna, ori)
        ans = 3
        self.assertEqual(result, ans)

    def test_is_on_the_sameline(self):
        
        points = [
                  [(0,1), (0,2), (0, 100), (0, 0.87)], 
                  [(2,5), (2,8), (6,9)], 
                  [(-43,87), (2,87), (-45,87)], 
                  [(-9.5,-5), (-7.5,-3), (0.5,5)]
                 ]
        results = []
        for point in points:
            results.append(ds.is_on_the_sameline(point))
        ans = [True, False, True, True]
        
        self.assertSequenceEqual(results, ans)

    def test_count_unique_genes(self):
        
        gene1 = []
        with open('geneset1.txt', 'r') as f:
            for line in f:
                gene1.append(line.rstrip())

        gene2 = []
        with open('geneset2.txt', 'r') as f:
            for line in f:
                gene2.append(line.rstrip())
    
        result = ds.count_unique_genes(gene1, gene2)
        ans = 20
        self.assertEqual(result, ans)

    def test_count_amino_acids(self):
        
        protein = ""
        with open('protein1.txt', 'r') as f:
            for line in f:
                if line.startswith('>'):
                    continue
                else:
                    protein += line.rstrip()

        ans = {'M': 14, 'S': 22, 'K': 37, 'I': 30, 
               'G': 33, 'V': 25, 'E': 29, 'Q': 18, 
               'D': 25, 'T': 24, 'R': 15, 'W': 7, 
               'L': 27, 'F': 17, 'P': 12, 'Y': 17, 
               'H': 9, 'N': 17, 'A': 31, 'C': 5
              }
        
        result = ds.count_amino_acids(protein)
        self.assertDictEqual(result, ans)

 
if __name__ == '__main__':
    unittest.main()
