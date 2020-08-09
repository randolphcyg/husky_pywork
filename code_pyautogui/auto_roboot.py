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
    pyautogui.typewrite(message=['english', 'input', 'test'], interval=.5)
    # input_str = "多喝热水"
    # for j in range(2):
    #     for con in input_str:
    #         pyperclip.copy(con)
    #         time.sleep(0.09)
    #         pyautogui.hotkey('ctrl', 'v')
    #         time.sleep(0.09)
        # pyautogui.press('enter')
        # pyautogui.hotkey('ctrl', 'enter')


if __name__ == "__main__":
    # send_zhihu_comment()
    auto_send_msg()
