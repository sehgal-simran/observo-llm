import unittest
import logging
from observo_llm.logging_module import setup_logging  # Adjust based on actual module structure

class TestLogging(unittest.TestCase):
    
    def setUp(self):
        self.logger = setup_logging()
    
    def test_logging_info(self):
        with self.assertLogs(self.logger, level='INFO') as log:
            self.logger.info("Test info message")
            self.assertIn("Test info message", log.output[0])
    
    def test_logging_error(self):
        with self.assertLogs(self.logger, level='ERROR') as log:
            self.logger.error("Test error message")
            self.assertIn("Test error message", log.output[0])

if __name__ == '__main__':
    unittest.main()
