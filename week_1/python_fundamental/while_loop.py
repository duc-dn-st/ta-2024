# while loop : while 文を使った繰り返し
# while文の処理の流れ
"""
while 条件式:
    実行する文
"""
number = [2, 3, 6, 1, 9]
count = 0

while count < len(number):
    print(number[count])
    count += 1

# 条件式がTrueの間、実行する文を繰り返す
# count < len(number)はTrueなので、number[count]を表示する
# ...
# count += 1でcountに1を足している
# count < len(number)はFalseなので、while文を抜ける
