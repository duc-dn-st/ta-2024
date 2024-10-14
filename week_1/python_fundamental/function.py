# 関数(function)とは、処理をまとめたもので、同じ処理を何度も使いたいときに使います。
# 関数の定義と関数の呼び出し
""" 1. 引数がない関数

def 関数名():
    関数内で実行する処理

    return 戻り値
"""
def function1():
    print("Hello, Pikachu!")

# 関数の呼び出し
function1()
# >> Hello, Pikachu!

#====================================
""" 2. 引数がある関数
def 関数名(引数1, 引数2, ...):
    関数内で実行する処理
"""

# 関数の定義
def say_hello(name):
    print("Hello, " + name + "!")

# 関数の呼び出し
say_hello("Jirachi")
# >> Hello, Jirachi!

#====================================
""" 3. 戻り値がある関数
def 関数名(引数1, 引数2, ...):
    関数内で実行する処理

    return 戻り値
"""
# 関数の定義 y = f(x1, x2)
def tashi_zan(x, y):
    return x + y

# 関数の呼び出し
result = tashi_zan(3, 5)
print(result)
# >> 8
