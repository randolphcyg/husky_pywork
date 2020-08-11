import time
import pyautogui
import pyperclip


def send_zhihu_comment():
    print("屏幕像素为", pyautogui.size())
    print("鼠标位置为", pyautogui.position())
    time.sleep(1)
    pyautogui.moveTo(x=1100, y=400, duration=0.7)                 # 坐标移动
    pyautogui.click(clicks=1, button='left', interval=0.05)       # 点击
    pyautogui.moveRel(xOffset=-10, yOffset=-40)                   # 偏移移动
    pyautogui.click(clicks=1, button='left', interval=0.05)       # 点击
    pyautogui.middleClick()                                       # 单击中键
    pyautogui.moveRel(xOffset=10, yOffset=20)
    # 滚动测试
    time.sleep(.5)
    pyautogui.moveTo(x=1100, y=400, duration=0.7)
    pyautogui.click(clicks=1, button='left', interval=0.05)         # 点击
    time.sleep(.5)
    pyautogui.scroll(-100)
    time.sleep(.5)
    pyautogui.scroll(-100)
    time.sleep(.5)
    pyautogui.scroll(-100)
    # 左右键和拖动测试
    time.sleep(2)
    pyautogui.doubleClick()                                       # 双击左键
    time.sleep(1)
    pyautogui.rightClick()                                        # 单击右键
    pyautogui.dragTo(x=500, y=700, duration=1)
    # 输入评论，中文输入测试
    pyautogui.click(clicks=1, button='left', interval=0.05)         # 点击
    input_str = "up主真棒，加油！"
    for j in range(1):
        for con in input_str:
            pyperclip.copy(con)
            time.sleep(0.09)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.09)
    pyautogui.dragRel(xOffset=500, yOffset=-20, button='left', duration=1)      # 按住左键相对拖动
    pyautogui.click(clicks=1, button='left', interval=0.05)         # 点击
    pyautogui.moveRel(xOffset=-100, yOffset=-100)


def auto_send_msg():
    '''将qq/WX聊天框置顶放在屏幕右侧，程序界面缩小到可以触发为止，保证鼠标移动位置在输入框中即可
    '''
    pyautogui.moveTo(x=1100, y=400, duration=0.7)
    pyautogui.click(clicks=1, button='left', interval=0.05)         # 点击
    time.sleep(1)
    pyautogui.press('shift')    # shift 键切换英文
    pyautogui.typewrite(['t', 'e', 's', 't', 'left', 'left', 'left', 'left', 'M', 'S', 'G'], interval=.2)       # 英文输入
    pyautogui.press('end')      # end键
    pyautogui.press('enter')    # enter键
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.keyDown('w')
    pyautogui.press('shift')    # shift 键切换中文
    time.sleep(2)
    pyautogui.keyUp('w')
    pyautogui.hotkey('ctrl', 'enter')
    input_str = "/doge多喝热水(＾Ｕ＾)ノ~ＹＯ"
    for j in range(2):
        for con in input_str:
            pyperclip.copy(con)
            time.sleep(0.09)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.09)
        # pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'enter')


def auto_run():
    '''TODO:根据图像进行定位完成和优化速度
    '''
    time.sleep(2)
    record_img = pyautogui.locateOnScreen("C:\\Users\\randolph\\Desktop\\record.png")
    pyautogui.moveTo(record_img, duration=.5)
    pyautogui.click(clicks=1, button='left', interval=0.05)
    time.sleep(2)
    # # 自动运行
    # run_img = pyautogui.locateOnScreen("C:\\Users\\randolph\\Desktop\\run.png")
    # print(run_img)
    # pyautogui.moveTo(run_img, duration=.5)
    # pyautogui.click(clicks=1, button='left', interval=0.05)
    # time.sleep(1)
    # 保存位置
    save_img = pyautogui.locateOnScreen("C:\\Users\\randolph\\Desktop\\save.png")
    print(save_img)
    pyautogui.moveTo(save_img, duration=.5)
    pyautogui.click(clicks=1, button='left', interval=0.05)
    time.sleep(3)
    # 是
    # yes_img = pyautogui.locateOnScreen("C:\\Users\\randolph\\Desktop\\yes.png")
    # print(yes_img)
    # pyautogui.moveTo(yes_img, duration=.5)
    # pyautogui.click(clicks=1, button='left', interval=0.05)
    # 测试案例
    auto_send_msg()
    time.sleep(2)
    # 停止记录
    stop_record_img = pyautogui.locateOnScreen("C:\\Users\\randolph\\Desktop\\stop_record.png")
    print(stop_record_img)
    pyautogui.moveTo(stop_record_img, duration=.5)
    pyautogui.click(clicks=1, button='left', interval=0.05)
    # 自动关闭
    stop_img = pyautogui.locateOnScreen("C:\\Users\\randolph\\Desktop\\stop.png")
    print(stop_img)
    pyautogui.moveTo(stop_img, duration=.5)
    pyautogui.click(clicks=1, button='left', interval=0.05)


if __name__ == "__main__":
    # send_zhihu_comment()
    auto_send_msg()
    # print(pyautogui.mouseInfo())
    # pyautogui.moveTo(x=1227, y=329, duration=.5)
    # all_wins = pyautogui.getActiveWindowTitle()
    # print(all_wins)
    # auto_run()
