# -*- coding:utf-8 _*-
from PyQt5.Qt import *
from 健康手册app.常量 import *
from PIL import Image
import sys
from 健康手册app.我的 import Mine
from 健康手册app.bottom_btn import Bottom_btn
from 健康手册app.发表 import PublishWindow

class MainWindow(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.resize(window_width, window_height)
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
        self.setWindowTitle("“健”你所见")
        self.setWindowIcon(QIcon("../健康手册app/图片/窗口图标-树叶.jpg"))


if __name__ == "__main__":
    # 创建一个应用程序对象
    app = QApplication(sys.argv)

    # 展示个人主页
    def show_mine():
        window.fr1.raise_()
        publish.move(window_width, 0)
        mine.move(0, 0)

    # 展示发表页面
    def show_publish():
        window.fr1.raise_()
        mine.move(window_width, 0)
        publish.move(0, 0)

    window = MainWindow()
    #创建个人主页
    mine = Mine(window)
    window.btn5.clicked.connect(lambda: mine.mine_sign.emit())
    mine.mine_sign.connect(show_mine)
    mine.move(window_width, 0)
    mine.show()

    #创建发表页面
    publish = PublishWindow(window)
    publish.move(window_width, 0)
    window.btn3.clicked.connect(lambda: publish.publish_sign.emit())
    publish.publish_sign.connect(show_publish)
    publish.move(window_width, 0)
    window.show()
    # 应用程序执行，进入消息循环

    sys.exit(app.exec_())
