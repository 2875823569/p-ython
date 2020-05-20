# -*- coding:utf-8 _*-
from PyQt5 import QtMultimedia
from PyQt5.QtCore import QUrl, Qt, QTimer, QSize, QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from 健康手册app.常量 import *
import sys


# 重写视频点击事件
class VM(QVideoWidget):
    pressnum = 1

    def mousePressEvent(self, evt):
        op = QGraphicsOpacityEffect()
        op.setOpacity(0)
        op1 = QGraphicsOpacityEffect()
        op1.setOpacity(1)
        if self.pressnum % 2 == 0:
            self.pressnum += 1
            window.frtop.move(0, -vmfr_top_h)
            window.player.play()
        else:
            self.pressnum += 1
            window.frtop.move(0, 0)
            window.frtop.raise_()
            window.player.pause()


# 创建窗口
class Vedio(QWidget):
    def __init__(self, path, txt):
        super().__init__()
        self.fr1 = QFrame(self)  # 视频区总框架
        self.frtop = QFrame(self.fr1)  # 视频区顶部框架
        self.frdown = QFrame(self)  # 视频区底部框架
        self.fr2 = QFrame(self)  # 评论区框架
        self.fr2.lower()
        self.setWindowTitle("视频")
        self.love_num = False
        self.collect_num = False
        self.interest_num = False
        self.commention = ""  # 评论的内容
        self.comment_num = 1
        self.path = path
        self.txt = txt

        # 初始化视频区UI
        self.setui_1(self.path)
        # 初始化评论区UI
        self.setui_2(self.txt)
        # 初始化进度条
        self.create_progressbar()
        # 初始化下拉列表
        self.create_qscrollbar()
        # 链接槽函数
        self.player.durationChanged.connect(self.time_change)
        self.player.positionChanged.connect(lambda val: self.pb.setValue(int(val / 1000)))

    # 创建视频部分UI
    def setui_1(self, path):
        self.resize(window_width, window_height)
        self.fr1.resize(window_width, window_height)
        self.vm = VM(self.fr1)
        self.vm.resize(vm_w, vm_h)
        self.vm.show()
        self.player = QMediaPlayer()  # 创建播放对象
        self.player.setVideoOutput(self.vm)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("{}".format(path))))  # 选取视频文件
        self.player.play()
        # 创建顶部按钮组件框架
        self.frtop.resize(vmfr_top_w, vmfr_top_h)
        self.frtop.move(0, -vmfr_top_h)
        self.frtop.setStyleSheet("background-color:#a9ffa7;")

        # 返回按钮
        self.btn_back = QPushButton(self.frtop)
        self.btn_back.resize(self.frtop.width() / 10, vmfr_top_h)
        self.btn_back.setIcon(QIcon("图片/方向-向左.png"))
        self.btn_back.setIconSize(QSize(self.frtop.width() / 10, vmfr_top_h))
        self.btn_back.setStyleSheet("background-color:transparent;")

        # 转发按钮
        self.btn_transmit = QPushButton(self.frtop)
        self.btn_transmit.resize(self.frtop.width() / 10, vmfr_top_h)
        self.btn_transmit.move(self.frtop.width() - self.frtop.width() / 10, 0)
        self.btn_transmit.setIconSize(QSize(self.frtop.width() / 10, vmfr_top_h))
        self.btn_transmit.setStyleSheet("background-color:transparent;")
        self.btn_transmit.setIcon(QIcon("图片/转发.png"))

        # 博主头像按钮
        self.btn_mhead = QPushButton(self.frtop)
        self.btn_mhead.resize(vmfr_down_h, vmfr_down_h)
        self.btn_mhead.move(self.frtop.width() / 10, 0)
        self.btn_mhead.setStyleSheet("border-radius:{}px;border-image:url(图片/头像 男孩.png);".format(vmfr_down_h / 2))
        # 博主名称
        self.label_bzname = QLabel(self.frtop)
        self.label_bzname.setText("小明")
        self.label_bzname.resize(2 * vmfr_down_h, vmfr_down_h / 2)
        self.label_bzname.move(self.frtop.width() / 10 + vmfr_down_h + 8, 0)
        self.label_bzname.setStyleSheet("font-size:20px;color:red;")
        # 博主粉丝
        self.label_bzname = QLabel(self.frtop)
        self.label_bzname.setText("500粉丝")
        self.label_bzname.resize(2 * vmfr_down_h, vmfr_down_h / 2)
        self.label_bzname.move(self.frtop.width() / 10 + vmfr_down_h + 8, vmfr_down_h / 2)
        # 关注按钮
        self.btn_interest = QPushButton("关注", self.frtop)
        self.btn_interest.resize(vmfr_down_w / 6, vmfr_down_h * 4 / 5)
        self.btn_interest.move(vm_w - self.frtop.width() / 10 - vmfr_down_w / 6, 3)
        self.btn_interest.setStyleSheet("border-radius:15px;background-color:#ff4a6b;")
        self.btn_interest.clicked.connect(self.intereset)

        # ******************创建底部框架*******************
        self.frdown.resize(vmfr_down_w, vmfr_down_h)
        self.frdown.move(0, vm_h + progressbar_h)
        self.frdown.setStyleSheet("background-color:#a8e8ca;")
        # 创建写评论按钮
        self.btn_discuss = QPushButton("说点什么。。")
        self.btn_discuss.setVisible(True)
        self.btn_discuss.setMaximumSize(QSize(vm_w * 2 / 5, vmfr_down_w * 2 / 3))
        self.btn_discuss.setStyleSheet("background-color:transparent;font-size:10px;text-align:left;")
        self.btn_discuss.setIcon(QIcon("图片/写评论.png"))
        self.btn_discuss.clicked.connect(self.comment)
        # 创建喜欢按钮
        self.btn_love = QPushButton()
        self.btn_love.setMaximumSize(QSize(vm_w / 10, vmfr_down_w * 2 / 3))
        self.btn_love.setIcon(QIcon("图片/喜欢.png"))
        self.btn_love.clicked.connect(self.love)
        self.btn_love.setStyleSheet("background-color:transparent;")
        # 创建收藏按钮
        self.btn_collect = QPushButton()
        self.btn_collect.setMaximumSize(QSize(vm_w / 10, vmfr_down_w * 2 / 3))
        self.btn_collect.setIcon(QIcon("图片/收藏.png"))
        self.btn_collect.setStyleSheet("background-color:transparent;")
        self.btn_collect.clicked.connect(self.collecte)
        # 创建评论按钮
        self.btn_comment = QPushButton()
        self.btn_comment.setMaximumSize(QSize(vm_w / 10, vmfr_down_w * 2 / 3))
        self.btn_comment.setIcon(QIcon("图片/评论.png"))
        self.btn_comment.setStyleSheet("background-color:transparent;")
        self.btn_comment.clicked.connect(self.comment)

        layout_down = QHBoxLayout()
        layout_down.setContentsMargins(0, vm_h + progressbar_h, 10, 5)
        layout_down.addWidget(self.btn_discuss)
        layout_down.addWidget(self.btn_love)
        layout_down.addWidget(self.btn_collect)
        layout_down.addWidget(self.btn_comment)
        self.setLayout(layout_down)
        # ******************结束*******************

    # 创建评论部分UI
    def setui_2(self, txt):
        # 创建评论区框架
        self.fr2.resize(window_width, window_height)
        self.fr2.move(0, vm_h + progressbar_h)
        # self.fr2.setStyleSheet("background-color:yellow")
        # 创建视频简介
        self.label_introduction = QLabel("", self.fr2)
        self.label_introduction.setText(txt)
        self.label_introduction.setWordWrap(True)  # 自动换行
        self.label_introduction.move(10, 10)
        self.label_introduction.setStyleSheet("font-size:15px;background-color:transparent;")
        self.label_introduction.adjustSize()

        self.label_introduction.setAlignment(Qt.AlignTop)  # 文字置顶
        # 创建发布时间
        self.label_showtime = QLabel("05-13", self.fr2)
        self.label_showtime.move(10, self.label_introduction.pos().y() + self.label_introduction.height() + 5)
        self.label_showtime.setStyleSheet("background:transparent;")
        # 创建水平线
        self.label_line = QLabel(self.fr2)
        self.label_line.resize(vm_w - 10, 1)
        self.label_line.move(10, self.label_showtime.pos().y() + self.label_showtime.height() + 3)
        self.label_line.setStyleSheet("background-color:#e3e1db")
        # 创建写评论文本框
        self.disscuss_line = QTextEdit(self.fr2)
        self.disscuss_line.setAlignment(Qt.AlignLeading)
        self.disscuss_line.resize(vm_w * 3 / 4, window_height / 15)
        self.disscuss_line.move(10, self.label_line.pos().y() + self.label_line.height() + 6)
        # 创建发表评论按钮
        self.btn_send = QPushButton("发表\n评论", self.fr2)
        self.btn_send.resize(vm_w / 6, window_height / 15)
        self.btn_send.move(20 + vm_w * 3 / 4, self.label_line.pos().y() + self.label_line.height() + 6)
        self.btn_send.clicked.connect(self.discuss)

        self.first_comment_y = self.disscuss_line.pos().y() + self.disscuss_line.height() + 6  # 第一条评论的y坐标

    # 创建评论
    def commentions(self):
        # 头像
        btn_comment_head = QPushButton(self.fr2)
        btn_comment_head.setVisible(True)
        btn_comment_head.resize(vmfr_down_h * 2 / 3, vmfr_down_h * 2 / 3)
        btn_comment_head.move(10, self.first_comment_y)
        btn_comment_head.setStyleSheet("border-radius:{};border-image:url(图片/头像 男孩.png)".format(vmfr_down_h / 4 * 3))
        # 用户名
        label_name = QLabel("小明", self.fr2)
        label_name.setVisible(True)
        label_name.resize(2 * vmfr_down_h, vmfr_down_h / 2)
        label_name.move(vmfr_down_h * 2 / 3 + 20, self.first_comment_y)
        label_name.setStyleSheet("color:red")
        # 评论
        label_comment = QLabel(self.fr2)
        label_comment.setVisible(True)
        label_comment.setText(self.commention)
        label_comment.move(vmfr_down_h * 2 / 3 + 20, self.first_comment_y + vmfr_down_h / 2 + 10)
        label_comment.setWordWrap(True)  # 自动换行
        label_comment.adjustSize()
        label_comment.setAlignment(Qt.AlignTop)  # 文字置顶
        # 创建水平线
        label_line = QLabel(self.fr2)
        label_line.setVisible(True)
        label_line.resize(vm_w - 20, 1)
        label_line.move(10, self.first_comment_y + vmfr_down_h / 2 + vmfr_down_h / 2 + 20)
        label_line.setStyleSheet("background-color:#e3e1db")

        self.comment_num += 1
        self.first_comment_y += 40 + label_comment.height() + vmfr_down_h / 2

    # 创建下拉列表
    def create_qscrollbar(self):
        self.qs = QScrollBar(self)
        self.qs.raise_()
        self.qs.setMaximum(self.height())
        self.qs.resize(window_width - vm_w, window_height)
        self.qs.move(vm_w, 0)
        self.qs.valueChanged.connect(self.valuechanged)

    # 下拉滑块时将控件上移
    def valuechanged(self):
        h = self.qs.value()
        self.fr1.move(0, -h * 2)
        self.fr2.move(0, vm_h + progressbar_h - h * 2)

    # 创建进度条
    def create_progressbar(self):
        self.pb = QProgressBar(self.fr1)
        self.pb.resize(vm_w, progressbar_h)
        self.pb.move(0, vm_h)
        self.pb.setFormat("")
        self.pb.setAlignment(Qt.AlignCenter)

    # 获取视频时间以及设置进度条区间
    def time_change(self):
        self.time = int(self.player.duration() / 1000)
        self.pb.setRange(0, self.time)
        self.pb.setValue(0)

    # 关注按钮槽函数
    def intereset(self):
        if self.interest_num:
            self.btn_interest.setStyleSheet("border-radius:5px;background-color:#ff4a6b;")
            self.interest_num = False
        else:
            self.btn_interest.setStyleSheet("border-radius:5px;background-color:#c8c3c2;")
            self.interest_num = True

    # 喜欢按钮槽函数
    def love(self):
        if self.love_num:
            self.btn_love.setIcon(QIcon("图片/喜欢.png"))
            self.love_num = False
        else:
            self.btn_love.setIcon(QIcon("图片/已喜欢.png"))
            self.love_num = True

    # 收藏按钮槽函数
    def collecte(self):
        if self.collect_num:
            self.btn_collect.setIcon(QIcon("图片/收藏.png"))
            self.collect_num = False
        else:
            self.btn_collect.setIcon(QIcon("图片/已收藏.png"))
            self.collect_num = True

    # 打开评论区按钮槽函数
    def comment(self):
        self.fr1.move(0, -window_height)
        self.qs.setValue((vm_h + progressbar_h) / 2)

    # 发评论按钮槽函数
    def discuss(self):
        if self.disscuss_line.toPlainText() == "":
            QMessageBox.information(self,
                                    "提示",
                                    "发表内容不能为空",
                                    QMessageBox.Yes)
        else:
            self.commention = self.disscuss_line.toPlainText()
            self.disscuss_line.setText("")
            self.commentions()
        # def remove():
        #     disscuss_line


if __name__ == "__main__":
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    window = Vedio("F:/python/寒假做的代码/健康手册app/视频/视频1.mp4", "视频简介\nsdfds\nsdf")
    window.show()
    # 应用程序执行，进入消息循环

    sys.exit(app.exec_())
