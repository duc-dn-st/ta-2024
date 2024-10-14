# for loop : for 文を使った繰り返し
# for文の処理の流れ
"""
for 変数 in イテラブルオブジェクト:
    実行する文
"""

# 例題1:
number = [2, 3, 6, 1, 9]

for i in range(len(number)):
    print(number[i])

# イテラブルオブジェクトから要素を取り出して、変数iに代入している
# len(number)はnumberリストの要素数を返す
# range(len(number))は0からlen(number) - 1までの範囲を返す
# つまり、0から4までの範囲を返す
# その範囲の数値を変数iに代入している
# number[i]はnumberリストのインデックスiの要素を取り出す
# つまり、number[0]からnumber[4]までの要素を取り出す
# それをprint()関数で表示している

