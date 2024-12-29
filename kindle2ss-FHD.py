import pyautogui
import win32gui
import win32ui
import win32con
import win32api
import time
import os
import datetime
import random
from PIL import Image

# ページ数
page = 5
# 取得範囲：左上座標
x1, y1 = 270, 160
# 取得範囲：右下座様
x2, y2 = 3230, 2010
# スクリーンショットを取得したい範囲の座標
left, top, width, height = 340, 120, 1240, 880
# スクショ間隔(秒)
#span = 1
span = [1.5, 2, 2.5]
# 出力フォルダ頭文字
h_foldername = "output"
# 出力ファイル頭文字
h_filename = "picture"


#########################
# スクリーンショット取得処理
#########################

# 待機時間５秒
# (この間にスクショを取得するウィンドウをアクティブにする)
time.sleep(5)

# 出力フォルダ作成(フォルダ名：頭文字_年月日時分秒)
folder_name = h_foldername + "_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
os.mkdir(folder_name)



# スクショ処理
prev_img = None
same_cnt = 0
p = 0
while True:
    # ページ数分スクリーンショットをとる
    #for p in range(page):
    # 出力ファイル名(頭文字_連番.png)
        out_filename = h_filename + "_" + str(p+1).zfill(4) + '.png'
    # スクリーンショット取得・保存処理
    # キャプチャ範囲： 左上のx座標, 左上のy座標, 幅, 高さ
        #s = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
        s = pyautogui.screenshot(region=(left, top, width, height))
        
        p = p + 1
    # 前回の画像と同じか判定
        if prev_img is None or not s.tobytes() == prev_img.tobytes():
        # 前回の画像と異なる場合はスクリーンショットを保存
            out_filename = h_filename + "_" + str(p).zfill(4) + '.png'
            s.save(folder_name + "/" + out_filename)
            prev_img = s
            same_cnt = 0
        # 次のページ
            pyautogui.press('left') #元はKeyDown, 右ならright
            #pyautogui.click(150, 800) #クリック座標指定
        # 画面の動作待ち
        #time.sleep(span)
            time.sleep(random.choice(span))
        else:
        # 前回の画像と同じ場合はカウンタを増やす
            same_cnt += 1

    # 3回同じ画像が出現した場合は終了
        if same_cnt >= 3:
            break

    # 処理中のページ番号を画面に出力
        print(f"Processing page {p}")

