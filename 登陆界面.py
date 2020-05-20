# -*- coding:utf-8 _*-
from PyQt5.Qt import *
from 健康手册app.常量 import *
import sys
import pymysql
from PIL import Image

# 登陆
class Login(QWidget):
    login_sign = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowTitle("“健”你所见")
        self.resize(window_width, window_height)
        self.move(x, y)
        self.setWindowIcon(QIcon("../健康手册app/图片/窗口图标-树叶.jpg"))

        self.fram = QFrame(self)
        self.fram.resize(window_width, window_height)
        self.fram.setStyleSheet("background-image:url(../健康手册app/图片/登陆背景.jpg)")
        self.fram1 = QFrame(self)
        self.fram1.resize(fram1_w, fram1_h)
        self.fram1.move(fram1_x, fram1_y)
        # self.fram1.setStyleSheet("border: 1px solid gray;")
        # 账号组件
        self.label_zh = QLabel(self.fram1)
        self.label_zh.setObjectName("notice")
        self.label_zh.setText("账号：")
        self.label_zh.resize(label_zh_w, label_zh_h)
        self.label_zh.move(label_zh_x, label_zh_y)
        # label_zh.move(Lbel_zh_location_x, Lbel_zh_location_y)

        self.txt_zh = QLineEdit(self.fram1)
        self.txt_zh.setObjectName("notice")
        self.txt_zh.setPlaceholderText("请输入账号")
        self.txt_zh.resize(txt_w, txt_h)
        self.txt_zh.move(txt_zh_x, txt_zh_y)

        # 密码组件
        self.label_mm = QLabel(self.fram1)
        self.label_mm.setObjectName("notice")
        self.label_mm.setText("密码：")
        self.label_mm.setStyleSheet("font-size: {}".format(zt))
        self.label_mm.resize(label_zh_w, label_zh_h)
        self.label_mm.move(label_mm_x, label_mm_y)

        self.txt_mm = QLineEdit(self.fram1)
        self.txt_mm.setObjectName("notice")
        self.txt_mm.setPlaceholderText("请输入密码")
        self.txt_mm.resize(txt_w, txt_h)
        self.txt_mm.move(txt_mm_x, txt_mm_y)

        # 登陆按钮
        self.btn_login = QPushButton(self.fram1)
        self.btn_login.setObjectName("notice")
        self.btn_login.setText("登陆")
        self.btn_login.resize(btn_login_w, btn_login_h)
        self.btn_login.move(int(self.fram1.width() / 10), int(self.fram1.height() / 1.5))

        # 注册按钮
        self.btn_sign_up = QPushButton(self.fram1)
        self.btn_sign_up.setObjectName("notice")
        self.btn_sign_up.setText("注册")
        self.btn_sign_up.resize(btn_login_w, btn_login_h)
        self.btn_sign_up.move(int(self.fram1.width() / 2), int(self.fram1.height() / 1.5))
        self.btn_sign_up.clicked.connect(self.show_login_singnal)

    def show_login_singnal(self):
        self.login_sign.emit()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(window_width, window_height)
        # 底部按钮框架
        self.fr1 = QFrame(self)  # 底部框架
        self.fr1.resize(mine_fr1w, mine_fr1h)
        self.fr1.move(mine_fr1x, mine_fr1y)
        # self.fr1.setStyleSheet("background-color:yellow")
        # ******************创建五个底部按钮*******************
        # 设置按钮
        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(QRect(20, 590, 50, 50))
        self.btn1.setStyleSheet("QPushButton{border-image:url(./图片/首页.jpg)}"
                                "QPushButton:pressed{border-image:url(./图片/按下首页.jpg)}")
        self.btn1.setMaximumSize(mine_fr1w / 7, mine_fr1h)
        self.btn2 = QPushButton(self)
        self.btn2.setGeometry(QRect(117.5, 590, 50, 50))
        # self.btn2.setText("商城")
        self.btn2.setStyleSheet("QPushButton{border-image:url(./图片/商城.jpg)}"
                                "QPushButton:pressed{border-image:url(./图片/按下商城.jpg)}")
        self.btn2.setMaximumSize(mine_fr1w / 7, mine_fr1h)
        self.btn3 = QPushButton(self)
        self.btn3.setMaximumSize(mine_fr1w / 7, mine_fr1h / 1.5)
        self.btn3.setStyleSheet("border-radius:25px;background-image:url(图片/发表1.png);")

        self.btn4 = QPushButton(self)
        self.btn4.setGeometry(QRect(312.5, 590, 50, 50))
        # self.btn4.setText("咨询专家")
        self.btn4.setStyleSheet("QPushButton{border-image:url(./图片/咨询.jpg)}"
                                "QPushButton:pressed{border-image:url(./图片/按下咨询.jpg)}")
        self.btn4.setMaximumSize(mine_fr1w / 7, mine_fr1h)
        self.btn5 = QPushButton(self)
        self.btn5.setGeometry(QRect(410, 590, 50, 50))
        # self.btn5.setText("我的")
        self.btn5.setStyleSheet("QPushButton{border-image:url(./图片/我的.jpg)}"
                                "QPushButton:pressed{border-image:url(./图片/按下我的.jpg)}")
        self.btn5.setMaximumSize(mine_fr1w / 7, mine_fr1h)
        self.btn5.clicked.connect(self.mine)  # 连接个人主页
        self.btn1.clicked.connect(self.home)
        # ******************结束*******************

        # ******************底部按钮应用到窗口*******************
        self.layout_down = QHBoxLayout()
        self.layout_down.addWidget(self.btn1)
        self.layout_down.addWidget(self.btn2)
        self.layout_down.addWidget(self.btn3)
        self.layout_down.addWidget(self.btn4)
        self.layout_down.addWidget(self.btn5)
        self.fr1.setLayout(self.layout_down)
        # ******************结束*******************

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
        self.btn_quit.clicked.connect(loginback)
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

    def home(self):
        self.fr_mine.close()
        self.fr_home = QFrame(self)
        self.fr_home.setVisible(True)
        self.fr_home.resize(window_width, window_height / 8 * 7)

    def mine(self):
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
                                    "border-image: url(图片/头像22.png)".format(window_width / 6))
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
                                                      "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("QObject.qss", "r") as f:
        qApp.setStyleSheet(f.read())
    mainwindwo = MainWindow()
    window = Login()
    window.show()


    # 设置中退出登陆的槽函数
    def loginback():
        mainwindwo.close()
        window.show()


    # 登陆按钮的槽函数
    def login():
        db = pymysql.connect("localhost", "root", "root", "“健”你所见")
        cursor = db.cursor()
        sql = "select password from UserId where username={}".format(window.txt_zh.text())

        # 进行账号判断
        if window.txt_zh.text() == "":  # 如果账号未输入
            QMessageBox.information(window, "提示", "请输入账号")
        elif window.txt_mm.text() == "":  # 如果密码未输入
            QMessageBox.information(window, "提示", "请输入密码")
        elif not cursor.execute(sql):  # 如果查询的密码为空
            QMessageBox.information(window, "提示", "账号未注册")
        else:
            cursor.execute(sql)
            password = list(cursor.fetchone())[0]
            if password == window.txt_mm.text():
                QMessageBox.information(window, "提示", "登陆成功")

                mainwindwo.show()
                window.close()
            else:
                QMessageBox.information(window, "提示", "密码错误")
            db.close()  # 关闭连接


    window.btn_login.clicked.connect(login)  # 登陆按钮连接登陆函数

    sys.exit(app.exec_())
