import unittest
import main

class SystemMonitorTests(unittest.TestCase):
    def test_snapshot_has_core_metrics(self):
        data = main.snapshot()
        for key in ("platform", "cpu_percent", "memory_percent", "disk_percent", "uptime"):
            self.assertIn(key, data)
        self.assertGreaterEqual(data["cpu_percent"], 0)
        self.assertGreaterEqual(data["memory_percent"], 0)
        self.assertGreaterEqual(data["disk_percent"], 0)

if __name__ == "__main__":
    unittest.main()
