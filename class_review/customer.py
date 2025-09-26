# 基本課題
# 下記の雛形を利用して、各問のコードが期待通り動作するようなCustomerクラスを実装してください


# 雛形
from math import degrees
import re


class Customer:
    # 各問のコードが期待通り動作するように実装

    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # C-1. フルネームを取得できる
    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    # C-2. 年齢という概念の追加
    def age(self):
        return f"{self.age}"

    # C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
    # 料金の計算ルール
    # こども料金(20歳未満): 1000円
    # おとな料金(20歳以上65歳未満): 1500円
    # シニア料金(65歳以上): 1200円
    def entry_fee(self):
        if self.age < 20:
            return f"1000"
        elif self.age < 65:
            return f"1500"
        else:
            return f"1200"

    # C-4. 単一の顧客情報をCSV形式で取得できる
    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    # C-5. 3歳以下の入場料金の無料化
    # 以下のコードを追加して、期待どおりの出力が得られる用に実装してください。
    # C-6. 75歳以上の料金区分の追加
    # 75歳以上の入場料金は500円にしてください
    def entry_fee(self):
        if self.age <= 3:
            return f"0"
        elif self.age < 20:
            return f"1000"
        elif self.age < 65:
            return f"1500"
        elif self.age >= 75:
            return f"500"
        else:
            return f"1200"

    # C-7. 単一顧客の情報取得形式の追加その1
    # 単一顧客の情報取得をタブ区切りにも対応させてください
    # 下記は出力の例
    # Ken Tanaka      15      1000
    # Tom Ford        57      1500
    # Ieyasu Tokugawa 75      500
    # Michelle Tanner 3       0
    def info_tab(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    # C-8. 単一顧客の情報取得形式の追加その2
    # 単一顧客の情報取得を「|」(パイプ)区切りにも対応させてください
    # 下記は出力の例
    def info_pipe(self):
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"

    pass
