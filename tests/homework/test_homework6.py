import unittest

#write import statement for homework 6 functions

from src.homework.homework6 import get_point_mutations
from src.homework.homework6 import get_dna_complement
from src.homework.homework6 import transcribe_dna_into_rna
from src.homework.homework6 import get_gc_content

#from homework6 import get_point_mutations
#from homework6 import get_dna_complement
#from homework6 import transcribe_dna_into_rna
#from homework6 import get_gc_content

class TestHomework6(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1,1)

    
    #create a test case for function get_point_mutations with arguments GAGCCTACTAACGGGAT and CATCGTAATGACGGCCT
    #the result should be 7
        
    def test_get_point_mutations_w_2strings_GAGCCTACTAACGGGAT_and_CATCGTAATGACGGCCT(self):
        self.assertEqual(7,get_point_mutations('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT'))

    #create a test case for function get_dna_complement with argument AAAACCCGGT the result should be ACCGGGTTTT

    def test_get_dna_complement_AAAACCCGGT(self):
        self.assertEqual('ACCGGGTTTT',get_dna_complement('AAAACCCGGT'))

    #create a test case for function transcribe_dna_into_rna with argument GATGGAACTTGACTACGTAAATT
    #the result should be GAUGGAACUUGACUACGUAAAUU

    def test_transcribe_dna_to_rna_w_string_GATGGAACTTGACTACGTAAATT(self):
        self.assertEqual('GAUGGAACUUGACUACGUAAAUU',transcribe_dna_into_rna('GATGGAACTTGACTACGTAAATT'))


    #create a test case for function get_gc_content with arguments
    #CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT
    #the result should be 60.919540

    def test_get_gc_content(self):
        self.assertEqual(60.919540,get_gc_content('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'))


    #create a test case for function find_motif_in_dna with arguments GATATATGCATATACTT and ATAT
    #the result should be 2 4 10 (three different integers)


#if __name__=='__main__':
    #unittest.main(verbosity=2)
