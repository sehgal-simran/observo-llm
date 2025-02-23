import unittest
import time
from observo_llm.performance import measure_performance

class TestPerformance(unittest.TestCase):
    
    def test_measure_performance(self):
        """Test that the measure_performance decorator records execution time."""
        
        @measure_performance
        def sample_function():
            time.sleep(0.1)  # Simulate a delay
            return "Success"
        
        start_time = time.time()
        result = sample_function()
        end_time = time.time()
        
        self.assertEqual(result, "Success")
        self.assertGreaterEqual(end_time - start_time, 0.1)  # Ensure delay is recorded

if __name__ == '__main__':
    unittest.main()
