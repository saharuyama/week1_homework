"""
課題B-6: N面サイコロの反復試行
N面サイコロをM回振ったときの結果を表示してください
N, M は正の整数とします
N, M はユーザーからの入力を利用すること

実行例
サイコロの面の数は?: 8
何回振りますか?: 20
[6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]
"""

import random

dice_faces = int(input("サイコロの面の数は？： "))
dice_rolls = int(input("何回振りますか？： "))

def dice_results(faces,rolls):
    results = []
    for i in range(rolls):
        roll = random.randint(1, faces)
        results.append(roll)
    return results
    
print(dice_results(dice_faces, dice_rolls))