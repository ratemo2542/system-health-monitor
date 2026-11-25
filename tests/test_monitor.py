import unittest
from monitor import snapshot

class MonitorTests(unittest.TestCase):
    def test_snapshot_has_expected_sections(self):
        data = snapshot()
        self.assertIn("cpu_percent", data)
        self.assertIn("memory", data)
        self.assertIn("disk", data)
        self.assertIn("top_processes", data)

if __name__ == "__main__":
    unittest.main()
