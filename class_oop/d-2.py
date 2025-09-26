# 課題D-2: 長方形オブジェクト
# 次のコードが正しく動作するような Rectangle クラスを実装してください
# diagonal は 対角線(の長さ) という意味です。

import math

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return format(self.height * self.width, ".2f")

    def diagonal(self):
        return format(math.sqrt(self.width**2 + self.height**2), ".2f")


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
