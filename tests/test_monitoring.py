import unittest
from observo_llm.monitoring import Monitoring

class TestMonitoring(unittest.TestCase):
    
    def setUp(self):
        self.monitor = Monitoring()
    
    def test_log_metric(self):
        """Test logging a metric value."""
        self.monitor.log_metric("accuracy", 0.95)
        self.assertIn("accuracy", self.monitor.metrics)
        self.assertEqual(self.monitor.metrics["accuracy"], [0.95])
    
    def test_log_multiple_metrics(self):
        """Test logging multiple values for the same metric."""
        self.monitor.log_metric("loss", 0.2)
        self.monitor.log_metric("loss", 0.15)
        self.assertEqual(self.monitor.metrics["loss"], [0.2, 0.15])
    
    def test_get_metric_average(self):
        """Test retrieving the average of logged metric values."""
        self.monitor.log_metric("latency", 100)
        self.monitor.log_metric("latency", 200)
        avg = self.monitor.get_metric_average("latency")
        self.assertEqual(avg, 150)
    
    def test_get_metric_average_no_data(self):
        """Test retrieving an average when no data exists."""
        avg = self.monitor.get_metric_average("nonexistent")
        self.assertIsNone(avg)

if __name__ == '__main__':
    unittest.main()
