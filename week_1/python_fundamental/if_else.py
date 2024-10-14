# if文を使った条件分岐の例
"""
if 条件式1:
    条件式1がTrueの場合に実行される処理
elif 条件式2:
    条件式2がTrueの場合に実行される処理
else:
    条件式がFalseの場合に実行される処理
"""

# 例題1:
robot_velocity = 0.5

if robot_velocity > 0:
    print("Robot is moving forward")
elif robot_velocity < 0:
    print("Robot is moving backward")
else:
    print("Robot is stopped")