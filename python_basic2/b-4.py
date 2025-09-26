"""
課題B-4: 天気情報の分析
要件
3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています
このデータを使って3つの問を満たす実装をしてください
"""

def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    total = 0
    for temps in weather_information: 
        total += temps["temperature"]
    print(total / len(weather_information))

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    osaka_stations = [] #空のリストを用意
    for stat in weather_information: #辞書からデータをひとつづつ取り出す
        if stat["prefecture"] == "大阪府": #もし大阪府だったら
            osaka_stations.append(stat["station"]) # 辞書から駅名を取り出して、osaka_stations というリストに追加する

    print(",".join(osaka_stations)) # ,で結合して出力

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    fukuoka_temps_total = 0
    fukuoka_count = 0 #変数を0にしておく

    for fukuoka_temps in weather_information:
        if fukuoka_temps["prefecture"] == "福岡県":
            fukuoka_temps_total += fukuoka_temps["temperature"]
            fukuoka_count += 1

    print(fukuoka_temps_total / fukuoka_count)


if __name__ == '__main__':
    main()
