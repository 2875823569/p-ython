# -*- coding:utf-8 _*-
from PyQt5.Qt import *
from PIL import Image
from 健康手册app.常量 import *
from 健康手册app.bottom_btn import Bottom_btn
import sys


# 创建窗口
class Mine(QWidget):
    mine_sign = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mine()

    # 客服按钮的槽函数
    def service(self):
        self.fr_mine.close()
        self.fr_service = QFrame(self)
        self.fr_service.setVisible(True)
        self.fr_service.resize(window_width, window_height / 8 * 5)
        self.label1 = QLabel("作者：寇靖，代澳林，包琴")
        self.label1.setStyleSheet("font-size:20px;")
        self.label2 = QLabel("客服人员：xxx")
        self.label2.setStyleSheet("font-size:20px;")
        self.label3 = QLabel("联系电话:xxx-xxxxxxxxx")
        self.label3.setStyleSheet("font-size:20px;")
        self.layout_service = QVBoxLayout()
        self.layout_service.addWidget(self.label1)
        self.layout_service.addWidget(self.label2)
        self.layout_service.addWidget(self.label3)
        self.fr_service.setLayout(self.layout_service)
        self.btn_sback = QPushButton(self.fr_service)
        self.btn_sback.setVisible(True)
        self.btn_sback.setText("返回")
        self.btn_sback.clicked.connect(self.sback)

    # 客服中的返回按钮
    def sback(self):
        self.fr_service.close()
        self.mine()

    # 设置中的退出登陆按钮槽函数
    def loginback(self):
        self.close()

    # 设置按钮的槽函数
    def set(self):
        self.fr_mine.close()
        self.fr_set = QFrame(self)
        self.fr_set.setVisible(True)
        self.fr_set.resize(window_width, window_height / 8 * 7)
        # 创建设置中的按钮
        self.btn_setback = QPushButton(self.fr_set)
        self.btn_setback.setVisible(True)
        self.btn_setback.setText("返回")
        self.btn_setback.resize(self.fr_set.width() / 4, self.fr_set.height() / 12)
        self.btn_setback.clicked.connect(self.setback)
        self.btn_quit = QPushButton("退出登陆")
        self.btn_quit.setMaximumSize(self.fr_set.width(), self.fr_set.height() / 12)
        self.btn_quit.setVisible(True)
        self.btn_quit.clicked.connect(self.loginback)
        self.btn_privacy = QPushButton("隐私设置")
        self.btn_privacy.setMaximumSize(self.fr_set.width(), self.fr_set.height() / 12)
        self.btn_privacy.setVisible(True)
        self.btn_notice = QPushButton("通知设置")
        self.btn_notice.setMaximumSize(self.fr_set.width(), self.fr_set.height() / 12)
        self.btn_notice.setVisible(True)
        self.btn_ty = QPushButton("通用设置")
        self.btn_ty.setMaximumSize(self.fr_set.width(), self.fr_set.height() / 12)
        self.btn_ty.setVisible(True)
        self.btn_about = QPushButton("关于")
        self.btn_about.setMaximumSize(self.fr_set.width(), self.fr_set.height() / 12)
        self.btn_about.setVisible(True)

        self.layout_set = QVBoxLayout()
        self.layout_set.addWidget(self.btn_quit)
        self.layout_set.addWidget(self.btn_privacy)
        self.layout_set.addWidget(self.btn_notice)
        self.layout_set.addWidget(self.btn_ty)
        self.layout_set.addWidget(self.btn_about)
        self.fr_set.setLayout(self.layout_set)

    # 设置中的返回按钮
    def setback(self):
        self.fr_set.close()
        self.mine()

    # def home(self):
    #     self.fr_mine.close()
    #     self.fr_home = QFrame(self)
    #     self.fr_home.setVisible(True)
    #     self.fr_home.resize(window_width, window_height / 8 * 7)

    def mine(self):
        self.resize(window_width, window_height)
        self.setWindowTitle("个人主页")
        self.fr_mine = QFrame(self)  # 除底部外的框架
        self.fr_mine.setVisible(True)
        self.fr_mine.resize(window_width, window_height / 8 * 7)
        # self.move(window_width/3, window_height/10)
        self.setWindowIcon(QIcon(bq))
        self.fr = QFrame(self.fr_mine)  # 顶部框架
        self.fr.setVisible(True)
        self.fr.resize(mine_frw, mine_frh)
        self.fr.setStyleSheet("background-image:url({})".format(mine_image))
        self.btn_head = QPushButton(self.fr_mine)
        self.btn_head.setVisible(True)
        self.btn_head.resize(btn_head_w, btn_head_h)
        self.btn_head.setStyleSheet("border-radius:{}px;"
                                    "border-image: url(更换的头像/头像1.png)".format(window_width / 6))
        self.btn_head.move(head_x, head_y)
        self.btn_head.clicked.connect(self.btn_head_choose)  # 连接选择文件的槽函数

        self.btn_setting = QPushButton(self.fr)  # 创建设置按钮
        self.btn_setting.setVisible(True)
        self.btn_setting.resize(btn_setting_w, btn_setting_h)
        self.btn_setting.move(btn_setting_x, btn_setting_y)
        self.btn_setting.setText("设置")
        self.btn_setting.clicked.connect(self.set)

        self.btn_service = QPushButton(self.fr)  # 创建客服按钮
        self.btn_service.setVisible(True)
        self.btn_service.setText("客服")
        self.btn_service.resize(btn_service_w, btn_service_h)
        self.btn_service.move(btn_service_x, btn_service_y)
        self.btn_service.clicked.connect(self.service)
        self.fr2 = QFrame(self.fr_mine)  # 创建中间框架
        self.fr2.setVisible(True)
        self.fr2.resize(mine_fr2_w, mine_fr2_h)
        self.fr2.move(mine_fr2_x, mine_fr2_y)
        # self.fr2.setStyleSheet("background-color: black")
        self.btn_sc = QPushButton("收藏")  # 创建收藏按钮
        self.btn_sc.setVisible(True)
        self.btn_sc.setMaximumSize(QSize(window_width, window_height / 15))
        self.btn_buycar = QPushButton("购物车")  # 创建购物车按钮
        self.btn_buycar.setVisible(True)
        self.btn_buycar.setMaximumSize(QSize(window_width, window_height / 15))
        self.btn_hestory = QPushButton("历史记录")  # 创建历史记录按钮
        self.btn_hestory.setVisible(True)
        self.btn_hestory.setMaximumSize(QSize(window_width, window_height / 15))
        self.btn_recive = QPushButton("待收货")  # 创建待收货按钮
        self.btn_recive.setVisible(True)
        self.btn_recive.setMaximumSize(QSize(window_width, window_height / 15))
        self.btn_appraise = QPushButton("评价")  # 创建评价按钮
        self.btn_appraise.setVisible(True)
        self.btn_appraise.setMaximumSize(QSize(window_width, window_height / 15))
        self.btn_aftermarket = QPushButton("退款售后")  # 创建退款售后按钮
        self.btn_aftermarket.setVisible(True)
        self.btn_aftermarket.setMaximumSize(QSize(window_width, window_height / 15))
        self.layout_fr2 = QVBoxLayout()
        self.layout_fr2.addWidget(self.btn_sc)
        self.layout_fr2.addWidget(self.btn_buycar)
        self.layout_fr2.addWidget(self.btn_hestory)
        self.layout_fr2.addWidget(self.btn_recive)
        self.layout_fr2.addWidget(self.btn_appraise)
        self.layout_fr2.addWidget(self.btn_aftermarket)
        self.layout_fr2.setSpacing(0)

        self.fr2.setLayout(self.layout_fr2)

    # 创建选择文件的槽函数
    def btn_head_choose(self, event):  # 从本地选取文件
        file_, filetype = QFileDialog.getOpenFileName(self, "选取文件", "C:/",
                                                      "All Files (*);png Files (*.png)")  # 设置文件扩展名过滤,注意用双分号间隔
        if file_ != "":
            self.echo(file_)

    def echo(self, value):
        # 将得到的图片切成圆形
        ima = Image.open(value).convert("RGBA")
        # ima = ima.resize((600, 600), Image.ANTIALIAS)
        size = ima.size

        # 因为是要圆形，所以需要正方形的图片
        r2 = min(size[0], size[1])
        if size[0] != size[1]:
            ima = ima.resize((r2, r2), Image.ANTIALIAS)

            # 最后生成圆的半径
        r3 = int(window_width / 12)
        imb = Image.new('RGBA', (r3 * 2, r3 * 2), (255, 255, 255, 0))
        pima = ima.load()  # 像素的访问对象
        pimb = imb.load()
        r = float(r2 / 2)  # 圆心横坐标

        for i in range(r2):
            for j in range(r2):
                lx = abs(i - r)  # 到圆心距离的横坐标
                ly = abs(j - r)  # 到圆心距离的纵坐标
                l = (pow(lx, 2) + pow(ly, 2)) ** 0.5  # 三角函数 半径

                if l < r3:
                    pimb[i - (r - r3), j - (r - r3)] = pima[i, j]
        imb.save("更换的头像/头像1.png")
        # 换上切成圆形以后的图片
        self.btn_head.setStyleSheet("border-radius:{}px;"
                                    "border-image: url(更换的头像/头像1.png)".format(window_width / 6))


if __name__ == "__main__":
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    minewindow = Mine()
    minewindow.show()
    # 应用程序执行，进入消息循环

    sys.exit(app.exec_())
