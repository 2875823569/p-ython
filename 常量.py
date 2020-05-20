from win32api import GetSystemMetrics
import sys

"""""""""""""""""""登陆界面"""""""""""""""""""""""""
# ******************屏幕大小*******************
window_width = int(GetSystemMetrics(0) / 3.79)
window_height = int(GetSystemMetrics(1) / 1.2)
# print(window_width, window_height)
# ******************结束*******************
# 屏幕位置
x = GetSystemMetrics(0) / 2.7
y = GetSystemMetrics(1) / 60
# ******************登陆界面控件大小*******************
fram1_w = int(window_width / 1.2)
fram1_h = int(window_height / 2)
label_zh_w = int(window_width / 5)
label_zh_h = int(fram1_h / 8)
txt_w = int(fram1_w / 1.5)
txt_h = int(fram1_h / 8)
label_mm_w = 0
label_mm_h = int(fram1_h / 8)
btn_login_w = int(fram1_w / 4)
btn_login_h = int(fram1_h / 8)

# ******************结束*******************

# ******************字体*******************
zt = 20
# ******************结束*******************

# ******************控件位置*******************
fram1_x = int(window_width / 10)
fram1_y = int(window_height / 4)
label_zh_x = 0
label_zh_y = int(fram1_h / 13)
label_mm_x = 0
label_mm_y = int(fram1_h / 2.5)
txt_zh_x = int(fram1_w / 3.5)
txt_zh_y = int(fram1_h / 13)
txt_mm_x = int(fram1_w / 3.5)
txt_mm_y = int(fram1_h / 2.5)

# ******************结束*******************

"""""""""""""""""""“我的”界面"""""""""""""""""""""""""
# ******************开始*******************
mine_image = "图片/个人主页背景.jpg"  # 个人主页图片
bq = "图片/窗口图标-树叶.jpg"  # 窗口标签
mine_head_image = "图片/头像.png"

# ******************结束*******************

# ******************大小*******************
mine_frw = window_width  # 个人主页图片部分的宽
mine_frh = window_height / 4  # 个人主页图片部分的宽
mine_fr2_w = window_width / 1.2  # 中间位置框架宽
mine_fr2_h = window_height / 8 * 5  # 中间位置框架高
btn_head_w = window_width / 3
btn_head_h = window_width / 3
btn_setting_w = int(mine_frw / 5)
btn_setting_h = int(mine_frh / 7)
btn_service_w = int(fram1_w / 5)
btn_service_h = int(mine_frh / 7)
mine_fr1w = window_width  # 底部框架宽
mine_fr1h = window_height / 8  # 底部框架高
# ******************结束*******************

# ******************位置*******************
mine_fr1x = 0  # 底部框架的x左边
mine_fr1y = window_height / 8 * 7  # 底部框架的y坐标
mine_fr2_x = int(window_height / 18)
mine_fr2_y = int(window_height / 4)
btn_setting_x = int(mine_frw / 1.3)
btn_setting_y = int(mine_frh / 15)
btn_service_x = int(mine_frw / 1.7)
btn_service_y = int(mine_frh / 15)
head_x = window_width / 15  # 头像的x坐标
head_y = window_height / 30  # 头像的y坐标
# ******************结束*******************

"""""""""""""""""""视频界面"""""""""""""""""""""""""
# ******************大小*******************
vm_w = int(window_width/1.07)    # 播放屏幕的宽
vm_h = int(window_height/1.07)    # 播放屏幕的高
progressbar_h = 4  # 进度条的宽度
vmfr_top_w = vm_w  # 顶部底部框架宽
vmfr_top_h = window_height-vm_h  #顶部底部框架高
vmfr_down_w = vm_w  #底部框架宽
vmfr_down_h = window_height-4-vm_h  #底部框架高
btn_play_w = window_width/4     #播放按钮宽
btn_play_h = window_width/4     #播放按钮高




# ******************结束*******************

# ******************位置*******************
btn_play_x = window_width/3
btn_play_y = window_height/3
# ******************结束*******************