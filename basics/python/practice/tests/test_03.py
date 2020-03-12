import unittest
import solution_03_process as rna

class TestProcess(unittest.TestCase):
 
    def test_transcribe(self):
        dna = 'GATGGTACTTGACTACGTAAATT'
        ans = 'GAUGGUACUUGACUACGUAAAUU'
        
        result = rna.transcribe(dna)
        self.assertEqual(result, ans)


    def test_count_nucleotides(self):
        dna = 'AGCTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
        ans = 20, 12, 17, 20
        
        result = rna.count_nucleotides(dna)
        self.assertEqual(result, ans)
 
 
if __name__ == '__main__':
    unittest.main()
