# -*- coding:utf-8 _*-
from PyQt5.Qt import *
from 健康手册app.常量 import *
import sys
import pymysql


# 注册
class Sign_up(QWidget):
    signup_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("注册")
        self.resize(window_width, window_height)
        self.setWindowIcon(QIcon("图片/注册图标.png"))

        self.fram_sign_up = QFrame(self)
        self.fram_sign_up.resize(window_width, window_height)
        self.fram_sign_up.setStyleSheet("background-image:url(图片/注册背景.jpg)")
        self.fram_sign_up1 = QFrame(self)
        self.fram_sign_up1.resize(int(window_width / 1.2), int(window_height / 1.3))
        self.fram_sign_up1.move(int(window_width / 10), int(window_height / 5))
        # self.fram_sign_up1.setStyleSheet("background: white")

        # 放文字
        self.label_title = QLabel(self.fram_sign_up)
        self.label_title.resize(window_width / 1.4, window_height / 8.5)
        self.label_title.move(window_width / 7, window_height / 20)
        print(self.label_title.width(), self.label_title.height())
        self.label_title.setStyleSheet("background-image:url(图片/“健”你所见.png);")
        self.label_title.setScaledContents(True)

        # 注册账号
        self.label_zczh = QLabel(self.fram_sign_up1)
        self.label_zczh.setObjectName("register")
        self.label_zczh.setStyleSheet("font-size: {}px".format(zt))
        self.label_zczh.resize(label_zh_w * 1.2, label_zh_h)
        self.label_zczh.setText(" 账 号 ")
        self.label_zczh.move(int(self.fram_sign_up1.width() / 30), int(self.fram_sign_up1.height() / 11))
        self.txt_zczh = QLineEdit(self.fram_sign_up1)
        self.txt_zczh.setObjectName("register")
        self.txt_zczh.resize(int(self.fram_sign_up1.width() / 1.5), label_zh_h)
        self.txt_zczh.move(int(self.fram_sign_up1.width() / 3), int(self.fram_sign_up1.height() / 11))
        # self.txt_zczh.setPlaceholderText("账号只能是纯数字组合")
        # 注册密码
        self.label_zcmm = QLabel(self.fram_sign_up1)
        self.label_zcmm.setObjectName("register")
        self.label_zcmm.resize(label_zh_w * 1.2, label_zh_h)
        self.label_zcmm.setText(" 密 码 ")
        self.label_zcmm.setStyleSheet("font-size: {}px".format(zt))
        self.label_zcmm.move(int(self.fram_sign_up1.width() / 30), int(self.fram_sign_up1.height() / 4))
        self.txt_zcmm = QLineEdit(self.fram_sign_up1)
        self.txt_zcmm.setObjectName("register")
        self.txt_zcmm.resize(int(self.fram_sign_up1.width() / 1.5), label_zh_h)
        self.txt_zcmm.move(int(self.fram_sign_up1.width() / 3), int(self.fram_sign_up1.height() / 4))
        # self.txt_zcmm.setPlaceholderText("请输入密码")
        # 确认密码
        self.label_sure = QLabel(self.fram_sign_up1)
        self.label_sure.setObjectName("register")
        self.label_sure.resize(label_zh_w * 1.2, label_zh_h)
        self.label_sure.move(int(self.fram_sign_up1.width() / 30), int(self.fram_sign_up1.height() / 2.5))
        self.label_sure.setText("确认密码")
        self.label_sure.setStyleSheet("font-size: {}px".format(zt))
        self.txt_zcmm_sure = QLineEdit(self.fram_sign_up1)
        self.txt_zcmm_sure.setObjectName("register")
        self.txt_zcmm_sure.resize(int(self.fram_sign_up1.width() / 1.5), label_zh_h)
        self.txt_zcmm_sure.move(int(self.fram_sign_up1.width() / 3), int(self.fram_sign_up1.height() / 2.5))
        # self.txt_zcmm_sure.setPlaceholderText("请再次输入密码")
        # 注册按钮
        self.btn_signup = QPushButton(self.fram_sign_up1)
        self.btn_signup.setText("立即注册")
        self.btn_signup.setObjectName("register")
        self.btn_signup.resize(int(self.fram_sign_up1.width() / 3), int(self.fram_sign_up1.height() / 10))
        self.btn_signup.move(int(self.fram_sign_up1.width() / 9), int(self.fram_sign_up1.height() / 1.5))
        self.btn_signup.clicked.connect(self.zc)

        # 返回按钮
        self.btn_back = QPushButton(self.fram_sign_up1)
        self.btn_back.setText("返回")
        self.btn_back.setObjectName("register")
        self.btn_back.resize(int(self.fram_sign_up1.width() / 3), int(self.fram_sign_up1.height() / 10))
        self.btn_back.move(int(self.fram_sign_up1.width() / 1.8), int(self.fram_sign_up1.height() / 1.5))
        self.btn_back.clicked.connect(self.show_signup_signer)

    def show_signup_signer(self):
        self.signup_signal.emit()

    def zc(self):  # 注册按钮事件
        if self.txt_zczh.text() == "":  # 如果账号为空，发出提示
            QMessageBox.warning(self,
                                "提示",
                                "账号不能为空！",
                                QMessageBox.Yes | QMessageBox.No)
        elif self.txt_zcmm.text() != self.txt_zcmm_sure.text():  # 前后两次密码不一致提示
            QMessageBox.warning(self, '提示', '两次密码不一致')
            self.txt_zcmm.setText("")
            self.txt_zcmm_sure.setText("")
        elif self.txt_zcmm.text() == "":  # 密码为空提示
            QMessageBox.warning(self, "提示", "密码不能为空")
        else:  # 如果密码和确认密码相等，注册成功
            db = pymysql.connect("localhost", "root", "root", "“健”你所见")
            cursor = db.cursor()
            sql = """insert into UserId(username,password) values({}, {})""".format(str(self.txt_zczh.text()),
                                                                                    str(self.txt_zcmm.text()))
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                db.rollback()
            # 关闭数据库连接
            db.close()
            QMessageBox.information(self, '提示', '注册成功')


if __name__ == "__main__":
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    with open("QObject.qss", "r") as f:
        qApp.setStyleSheet(f.read())
    window = Sign_up()
    window.show()
    # 应用程序执行，进入消息循环
    print(window.x(), window.y())
    sys.exit(app.exec_())
