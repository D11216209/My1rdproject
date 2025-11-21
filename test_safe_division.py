"""
單元測試 - Safe Division Function
此模組包含 safe_division 函式的完整單元測試
"""

import unittest
from safe_division import safe_division


# 常數定義
ERROR_MESSAGE_DIVISION_BY_ZERO = "錯誤：除數不能為零"


class TestSafeDivision(unittest.TestCase):
    """測試 safe_division 函式的各種情況"""
    
    def test_normal_division_positive_numbers(self):
        """測試正常的正數除法"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(15, 3), 5.0)
        self.assertEqual(safe_division(100, 4), 25.0)
    
    def test_division_with_decimal_result(self):
        """測試產生小數結果的除法"""
        self.assertEqual(safe_division(7, 2), 3.5)
        self.assertEqual(safe_division(5, 4), 1.25)
        self.assertEqual(safe_division(1, 3), 1/3)
    
    def test_division_by_zero(self):
        """測試除以零的情況（應返回錯誤訊息）"""
        self.assertEqual(safe_division(10, 0), ERROR_MESSAGE_DIVISION_BY_ZERO)
        self.assertEqual(safe_division(0, 0), ERROR_MESSAGE_DIVISION_BY_ZERO)
        self.assertEqual(safe_division(-5, 0), ERROR_MESSAGE_DIVISION_BY_ZERO)
    
    def test_zero_as_numerator(self):
        """測試零作為被除數的情況"""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, 10), 0.0)
        self.assertEqual(safe_division(0, -3), 0.0)
    
    def test_negative_numbers(self):
        """測試負數的除法"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_division_by_one(self):
        """測試除以一的情況"""
        self.assertEqual(safe_division(5, 1), 5.0)
        self.assertEqual(safe_division(-5, 1), -5.0)
        self.assertEqual(safe_division(0, 1), 0.0)
    
    def test_division_of_one(self):
        """測試一除以其他數的情況"""
        self.assertEqual(safe_division(1, 2), 0.5)
        self.assertEqual(safe_division(1, 4), 0.25)
        self.assertEqual(safe_division(1, -2), -0.5)
    
    def test_large_numbers(self):
        """測試大數字的除法"""
        self.assertEqual(safe_division(1000000, 1000), 1000.0)
        self.assertEqual(safe_division(999999, 3), 333333.0)
    
    def test_small_numbers(self):
        """測試小數字的除法"""
        self.assertAlmostEqual(safe_division(0.1, 0.2), 0.5)
        self.assertAlmostEqual(safe_division(0.5, 0.25), 2.0)


if __name__ == "__main__":
    unittest.main()
