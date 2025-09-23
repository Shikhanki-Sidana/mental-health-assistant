import unittest
from src import screening

class TestScreening(unittest.TestCase):
    def test_phq9_none(self):
        score, cat = screening.score_phq9([0]*9)
        self.assertEqual(score, 0)
        self.assertEqual(cat, "None-minimal")

    def test_phq9_severe(self):
        score, cat = screening.score_phq9([3]*9)
        self.assertEqual(score, 27)
        self.assertEqual(cat, "Severe depression")

if __name__ == '__main__':
    unittest.main()
