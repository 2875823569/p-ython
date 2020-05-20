# -*- coding:utf-8 _*-
from PyQt5.Qt import *
from 健康手册app.常量 import *
import sys
import pymysql
from 健康手册app.注册界面 import Sign_up
from 健康手册app.登陆界面 import Login
from 健康手册app.Main import MainWindow
from 健康手册app.我的 import Mine
if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("QObject.qss", "r") as f:
        qApp.setStyleSheet(f.read())

    # 登陆界面注册按钮槽函数
    def show_sign_up():
        sign_up.move(0, 0)

    # 注册界面的退出按钮
    def signup_back():
        sign_up.move(window_width, 0)

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
                mainWindow.show()
                window.close()
            else:
                QMessageBox.information(window, "提示", "密码错误")
            db.close()  # 关闭连接

    #展示个人主页的槽函数
    def show_mine():
        mine.move(0, 0)

    window = Login()
    window.login_sign.connect(show_sign_up)

    # ******************创建注册界面*******************
    sign_up = Sign_up(window)
    sign_up.move(window_width, 0)
    sign_up.show()
    # ******************结束*******************

    # ******************创建主界面*******************
    mainWindow = MainWindow()
    mine = Mine(mainWindow)
    mainWindow.btn5.clicked.connect(lambda: mine.mine_sign.emit())
    mine.mine_sign.connect(show_mine)
    mine.move(window_width, 0)
    # mainWindow.show()
    # ******************结束*******************
    window.show()

    # ******************连接信号槽*******************
    sign_up.btn_back.clicked.connect(signup_back) #连接注册的退出槽
    window.btn_login.clicked.connect(login)  # 登陆按钮连接登陆函数
    # ******************结束*******************
    sys.exit(app.exec_())
