# 这是一个发表页面类
import sys
from 健康手册app.常量 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# 这是发表页面下点击取消时的提示小窗口类
class PromptWindow(QWidget):
    prompt_sign = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi()

    def setupUi(self):
        self.resize(200, 80)

        self.label1 = QLabel(self)
        self.label1.setText("是否存入草稿箱?")
        self.label1.setGeometry(QRect(40, 10, 120, 20))

        self.nobutton = QPushButton(self)
        self.nobutton.setText("否")
        self.nobutton.setGeometry(QRect(40, 50, 50, 25))

        self.yesbutton = QPushButton(self)
        self.yesbutton.setText("是")
        self.yesbutton.setGeometry(QRect(100, 50, 50, 25))

        self.nobutton.clicked.connect(self.close)
        self.yesbutton.clicked.connect(self.close)


class PublishWindow(QWidget):
    publish_sign = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('发表')
        self.setupUi()

    # 显示对话框返回值
    def echo(self, value):
        QMessageBox.information(self, "返回值", "得到：{}\n\ntype: {}".format(value, type(value)),
                                QMessageBox.Yes | QMessageBox.No)
        return value

    def setupUi(self):
        self.resize(window_width, window_height)
        self.setStyleSheet("QWidget{background-color: #FFFFFF}")

        self.btn1 = QPushButton(self)
        # self.btn1_x = int(self.width/24)
        # self.btn1_y = int(self.width/24)
        self.btn1.setGeometry(QRect(20, 10, 50, 30))
        self.btn1.setText("取消")
        self.btn1.setStyleSheet("QPushButton{background-color:#FFFFFF}")

        self.btn2 = QPushButton(self)
        # self.btn2_x = int(self.width-self.width/24-50)
        # self.btn2_y = int(self.width/24)
        self.btn2.setGeometry(QRect(410, 10, 50, 30))
        self.btn2.setText("发表")
        self.btn2.setStyleSheet("QPushButton{background-color:#FFFFFF}")

        self.textedit1 = QTextEdit(self)
        self.textedit1.setGeometry(QRect(0, 50, 480, 180))
        self.textedit1.setPlaceholderText("分享你的新鲜事")
        self.textedit1.setStyleSheet("QTextEdit{border-image:url(./图片/分享你的新鲜事.png)}")

        self.upload_button = QPushButton(self)
        self.upload_button.setGeometry(QRect(20, 240, 100, 100))
        self.upload_button.setStyleSheet("QPushButton{border-image:url(./图片/上传.jpg)}")

        self.tilte_button = QPushButton(self)
        self.tilte_button.setGeometry(QRect(0, 360, 480, 50))
        self.tilte_button.setStyleSheet("QPushButton{border-image:url(./图片/选择标题.png)}")

        self.select_button = QPushButton(self)
        self.select_button.setGeometry(QRect(0, 410, 480, 50))
        self.select_button.setStyleSheet("QPushButton{border-image:url(./图片/设置权限.png)}")

        # 点击取消提示是否存入草稿箱
        if self.textedit1.toPlainText() != "":
            self.btn1.clicked.connect(self.hintmessage)

    def hintmessage(self, event):
        value = QMessageBox.information(self, "保存内容", "是否存入草稿箱", QMessageBox.Yes | QMessageBox.No)
        if value == 16384:
            print("保存成功")
        else:
            print("取消保存")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    minewindow = PublishWindow()
    minewindow.show()
    # 应用程序执行，进入消息循环

    sys.exit(app.exec_())
