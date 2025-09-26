"""
課題B-5:基本統計量の計算
スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
合計値
最大値
最小値
平均値
ただし、計算用の組み込み関数やライブラリは使わないこと(sum()やnp.mean()などはNG print()はOK)
1つの統計量につき、それ専用の関数を実装すること

実行例
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
"""


value = input("データを入力してください（スペース区切り） >")
value = [int(i) for i in value.split()]

# 合計値
def total_value(value):
    total = 0
    for i in value:
        total += i
    return total

# 最大値
def max_value(value):
    max_value = value[0] #いまの最大値0
    for i in value:
        if i > max_value: #もし今の最大値よりiが大きかったら
            max_value = i #iが最大値
    return max_value

# 最小値
def min_value(value):
    min_value = value[0]
    for i in value:
        if i < min_value:
            min_value = i
    return min_value

# 平均値
def ave_value(value):
    count_value = len(value)
    ave_value = total_value(value) // count_value
    return ave_value


print(
    f"合計値：{total_value(value)}\n"
    f"最大値：{max_value(value)}\n"
    f"最小値：{min_value(value)}\n"
    f"平均値：{ave_value(value)}")
