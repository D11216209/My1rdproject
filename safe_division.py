"""
防呆計算機 - Safe Division Function
此模組提供安全的除法運算，防止除以零的錯誤
"""


def safe_division(a, b):
    """
    安全除法函式，防止除以零
    
    參數:
        a: 被除數 (分子)
        b: 除數 (分母)
    
    回傳:
        如果除數不為零，回傳 a / b 的結果
        如果除數為零，回傳錯誤訊息字串
    
    範例:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        '錯誤：除數不能為零'
    """
    if b == 0:
        return "錯誤：除數不能為零"
    return a / b


if __name__ == "__main__":
    # 測試範例
    print("=== 安全除法測試 ===")
    print(f"10 ÷ 2 = {safe_division(10, 2)}")
    print(f"15 ÷ 3 = {safe_division(15, 3)}")
    print(f"7 ÷ 2 = {safe_division(7, 2)}")
    print(f"10 ÷ 0 = {safe_division(10, 0)}")
    print(f"0 ÷ 5 = {safe_division(0, 5)}")
    print(f"-10 ÷ 2 = {safe_division(-10, 2)}")
