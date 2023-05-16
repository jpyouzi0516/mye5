import time
import winsound

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"专注计时器已启动，将持续{minutes}分钟。")

    # 等待指定时间
    time.sleep(seconds)

    # 提醒用户结束专注时间
    frequency = 2500  # 声音频率（Hz）
    duration = 1000  # 声音持续时间（毫秒）
    winsound.Beep(frequency, duration)

    print("专注时间已结束！")

# 设置专注时间为25分钟
focus_timer(25)
