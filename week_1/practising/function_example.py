# 位置を更新する関数と位置履歴を保存するプログラム

# 位置を更新する関数を作成
# TODO: position, velocity, time_stepを引数に取り、位置を更新する関数 "update_position" を作成してください

# 初期設定
position = 0  # 初期位置
velocity = 0.5
time_step = 1  # 時間間隔
total_time = 10  # シミュレーションの合計時間

# 位置を保存するリスト
positions = [position]  # 初期位置をリストに保存

# シミュレーション開始
for t in range(0, total_time, time_step):
    # ロボットの位置を更新し、リストに保存
    # TODO: update_position関数を呼び出して、位置を更新し、positionsリストに新しい位置を追加してください
    
    # TODO: positionsリストに新しい位置を追加するには、positions.append()を使用してください
    
# すべての位置を表示