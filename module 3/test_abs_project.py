import unittest

class TestAbs(unittest.TestCase):

    # функция проверки абсолютного значения
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    # функция проверки абсолютного значения
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()