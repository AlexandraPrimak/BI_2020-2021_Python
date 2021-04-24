import unittest

from filter_fastq import count_GC
from filter_fastq import validate_read

class TestFunctions(unittest.TestCase):
    def test_count_GC(self):
        
        read = 'GCAT'
        result = count_GC(read)
        self.assertEqual(result, 50)

        read = 'GCATA'
        result = count_GC(read)
        self.assertEqual(result, 40)

        read = 'GCGC'
        result = count_GC(read)
        self.assertEqual(result, 100)

        read = 'ATATAT'
        result = count_GC(read)
        self.assertEqual(result, 0)

        read = 'GATATATATA'
        result = count_GC(read)
        self.assertEqual(result, 10)

        read = 'GATATGTGTATATAGTGATGACTTCCGCATATAG'
        result = count_GC(read)
        self.assertEqual(result, 35)

    def test_validate_read(self):
        read = 'GATATGTGTATATAGTGATGACTTCCGCATATAG'
        gc_count = count_GC(read)
        
        # testing min_length param
        gc_bounds = []
        min_len = 100
        result = validate_read(read, min_len, gc_bounds)
        self.assertEqual(result, False)
        min_len = 10
        result = validate_read(read, min_len, gc_bounds)
        self.assertEqual(result, True)
        
        min_len = 10
        #testing gc_bounds
        gc_bounds = [gc_count + 1]
        result = validate_read(read, min_len, gc_bounds)
        self.assertEqual(result, False)

        gc_bounds = [gc_count - 1]
        result = validate_read(read, min_len, gc_bounds)
        self.assertEqual(result, True)

        gc_bounds = [gc_count - 1, gc_count + 1]
        result = validate_read(read, min_len, gc_bounds)
        self.assertEqual(result, True)
        
        gc_bounds = [gc_count - 10, gc_count -1]
        result = validate_read(read, min_len, gc_bounds)
        self.assertEqual(result, False)
        
        gc_bounds = [gc_count + 1, gc_count + 10]
        result = validate_read(read, min_len, gc_bounds)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()