# -*- coding:utf-8 _*-
from PyQt5.QtCore import Qt, QTimer, QSize, QRect, QPoint, QPropertyAnimation
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from 健康手册app.常量 import *

# 创建窗口
class Text(QWidget):
    def __init__(self, txt, imagepath, imagepath1):
        super().__init__()
        self.setWindowTitle("文章界面")
        self.resize(window_width, window_height)
        self.interest_num = 1
        self.fr1 = QFrame(self)  # 创建图片和简介部分框架
        self.fr2 = QFrame(self)  # 评论区框架
        self.first_image_x = vm_w  # 第一张图片的x坐标
        self.comment_num = 1
        self.url = imagepath
        self.url1 = imagepath1
        self.txt = txt
        self.setui()
        # 创建轮播图
        self.turn_image(self.url, self.url1)

        # 创建下拉列表
        self.create_qscrollbar()

        # 创建评论区
        self.setui_2()
        self.first_comment_y = self.label_title.pos().y() + self.label_title.height() + self.disscuss_line.height() + 5
    # 创建组件
    def setui(self):
        self.resize(window_width, window_height)
        # 创建顶部按钮组件框架
        frtop = QFrame(self)
        self.fr1.resize(vm_w*2, vm_h)
        frtop.resize(vmfr_top_w, vmfr_top_h)
        frtop.move(0, 0)
        frtop.setStyleSheet("background-color:#a9ffa7;")

        # 返回按钮
        self.btn_back = QPushButton(frtop)
        self.btn_back.resize(frtop.width() / 10, vmfr_top_h)
        self.btn_back.setIcon(QIcon("图片/方向-向左.png"))
        self.btn_back.setIconSize(QSize(frtop.width() / 10, vmfr_top_h))
        self.btn_back.setStyleSheet("background-color:transparent;")

        # 转发按钮
        self.btn_transmit = QPushButton(frtop)
        self.btn_transmit.resize(frtop.width() / 10, vmfr_top_h)
        self.btn_transmit.move(frtop.width() - frtop.width() / 10, 0)
        self.btn_transmit.setIconSize(QSize(frtop.width() / 10, vmfr_top_h))
        self.btn_transmit.setStyleSheet("background-color:transparent;")
        self.btn_transmit.setIcon(QIcon("图片/转发.png"))

        # 博主头像按钮
        self.btn_mhead = QPushButton(frtop)
        self.btn_mhead.resize(vmfr_down_h, vmfr_down_h)
        self.btn_mhead.move(frtop.width() / 10, 0)
        self.btn_mhead.setStyleSheet("border-radius:{}px;border-image:url(图片/头像 男孩.png);".format(vmfr_down_h / 2))
        # 博主名称
        self.label_bzname = QLabel(frtop)
        self.label_bzname.setText("小明")
        self.label_bzname.resize(2 * vmfr_down_h, vmfr_down_h / 2)
        self.label_bzname.move(frtop.width() / 10 + vmfr_down_h + 8, 0)
        self.label_bzname.setStyleSheet("font-size:20px;color:red;")
        # 博主粉丝
        self.label_bzname = QLabel(frtop)
        self.label_bzname.setText("500粉丝")
        self.label_bzname.resize(2 * vmfr_down_h, vmfr_down_h / 2)
        self.label_bzname.move(frtop.width() / 10 + vmfr_down_h + 8, vmfr_down_h / 2)
        # 关注按钮
        self.btn_interest = QPushButton("关注", frtop)
        self.btn_interest.resize(vmfr_down_w / 6, vmfr_down_h * 4 / 5)
        self.btn_interest.move(vm_w - frtop.width() / 10 - vmfr_down_w / 6, 3)
        self.btn_interest.setStyleSheet("border-radius:15px;background-color:#ff4a6b;")
        self.btn_interest.clicked.connect(self.intereset)

    # 创建轮播图
    def turn_image(self, url, url1):
        self.label_image = QLabel(self.fr1)
        self.label_image.resize(self.first_image_x, window_height * 4 / 5)
        self.label_image.move(0, vmfr_top_h)
        self.label_image.setStyleSheet("border-image:url({});".format(url))


        self.label_image1 = QLabel(self.fr1)
        self.label_image1.resize(self.first_image_x, window_height * 4 / 5)
        self.label_image1.move(self.first_image_x, 0)
        self. label_image1.setStyleSheet("border-image:url({});".format(url1))
        self.first_image_x += vm_w
        # ******************结束*******************
        # 创建计时器
        # 计时器运行函数--使图片轮转
        def imagemove():
            # self.animations(label_image.)
            x1 = self.label_image.pos().x()
            # x2 = self.label_image1.pos().x()
            if x1 == 0:
                self.animations(self.label_image, 0, vmfr_top_h, -vm_w, vmfr_top_h, 2000)
                self.animations(self.label_image1, self.first_image_x, vmfr_top_h, 0, vmfr_top_h, 2000)
            else:
                self.animations(self.label_image, -vm_w, vmfr_top_h, 0, vmfr_top_h, 2000)
                self.animations(self.label_image1, 0, vmfr_top_h, self.first_image_x, vmfr_top_h, 2000)
        timer = QTimer(self.fr1)
        # print(label_image.pos().x())
        timer.timeout.connect(imagemove)
        timer.start(4000)

        # 创建图片区域
        self.fr_btn = QFrame(self)
        self.fr_btn.resize(vm_w, 20)
        # self.fr_btn.setStyleSheet("background-color:red;")
        self.fr_btn.move(0, window_height * 4 / 5 + vmfr_top_h-20)

        # 创建图片按钮
        btn1 = QPushButton()
        btn1.setStyleSheet("background-color:white; border-radius:5px")
        btn1.setMaximumSize(QSize(10, 10))
        btn1.setMinimumSize(QSize(10, 10))
        btn2 = QPushButton()
        btn2.setStyleSheet("background-color:white;border-radius:5px")
        btn2.setMaximumSize(QSize(10, 10))
        btn2.setMinimumSize(QSize(10, 10))

        layout_btn = QHBoxLayout()
        layout_btn.addWidget(btn1)
        layout_btn.addWidget(btn2)
        self.fr_btn.setLayout(layout_btn)

        def btn1_func():
            timer.stop()
            self.label_image.move(0, vmfr_top_h)
            self.label_image1.move(-vm_w, vmfr_top_h)

        def btn2_func():
            timer.stop()
            self.label_image.move(-vm_w, vmfr_top_h)
            self.label_image1.move(0, vmfr_top_h)

        btn1.clicked.connect(btn1_func)
        btn2.clicked.connect(btn2_func)

    # 创建评论部分UI
    def setui_2(self):
        # 创建评论区框架
        self.fr2.resize(window_width, window_height)
        self.fr2.move(0, window_height*4/5+vmfr_top_h)
        # self.fr2.setStyleSheet("background-color:yellow")
        # 创建文章区
        self.label_title = QLabel(self.fr2)
        self.label_title.setWordWrap(True)  # 自动换行
        # self.label_title.setMaximumWidth(vm_w-5)
        self.label_title.setText("{}".format(self.txt))
        self.label_title.move(10, 10)
        self.label_title.setMaximumWidth(vm_w-7)
        # self.label_title.setMinimumHeight(600)
        self.label_title.adjustSize()
        self.label_title.setStyleSheet("font-size:15px;background-color:transparent;")
        self.label_title.setAlignment(Qt.AlignTop)  # 文字置顶
        # 创建发布时间
        self.label_showtime = QLabel("05-13", self.fr2)
        self.label_showtime.move(10, self.label_title.pos().y()+self.label_title.height()+3)
        self.label_showtime.setStyleSheet("background:transparent;")
        # 创建水平线
        self.label_line = QLabel(self.fr2)
        self.label_line.resize(vm_w-10, 1)
        self.label_line.move(10, self.label_title.pos().y()+self.label_title.height()+15)
        self.label_line.setStyleSheet("background-color:#e3e1db")
        # 创建写评论文本框
        self.disscuss_line = QTextEdit(self.fr2)
        self.disscuss_line.setAlignment(Qt.AlignLeading)
        self.disscuss_line.resize(vm_w*3/4, window_height / 15)
        self.disscuss_line.move(10, self.label_title.pos().y()+self.label_title.height()+30)
        # print(self.label_title.height())
        # 创建发表评论按钮
        self.btn_send = QPushButton("发表\n评论", self.fr2)
        self.btn_send.resize(vm_w/6, window_height/15)
        self.btn_send.move(20+vm_w*3/4, self.label_title.pos().y()+self.label_title.height()+30)
        self.btn_send.clicked.connect(self.discuss)

    # 创建下拉条
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
        self.fr_btn.move(0, window_height * 4 / 5 + vmfr_top_h-20-h*2)
        self.fr2.move(0, window_height*4/5+vmfr_top_h-2*h)

    # 创建动画
    def animations(self, widget, starx, stary, endx, endy, time):
        # 创建动画对象，并且设置目标、属性
        animation = QPropertyAnimation(self)
        animation.setTargetObject(widget)
        animation.setPropertyName(b"pos")

        # 设置属性值：开始 插值 结束
        animation.setStartValue(QPoint(starx, stary))
        animation.setEndValue(QPoint(endx, endy))

        # 动画时长
        animation.setDuration(time)

        # 启动动画
        animation.start()

    # 关注按钮槽函数
    def intereset(self):
        if self.interest_num:
            self.btn_interest.setStyleSheet("border-radius:5px;background-color:#ff4a6b;")
            self.interest_num = False
        else:
            self.btn_interest.setStyleSheet("border-radius:5px;background-color:#c8c3c2;")
            self.interest_num = True
    # 打开评论区按钮槽函数
    def comment(self):
        self.fr1.move(0, -window_height)
        self.qs.setValue((vm_h + progressbar_h)/2)

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

    # 创建评论
    def commentions(self):
        # 头像
        btn_comment_head = QPushButton(self.fr2)
        btn_comment_head.setVisible(True)
        btn_comment_head.resize(vmfr_down_h*2/3, vmfr_down_h*2/3)
        btn_comment_head.move(10, self.first_comment_y)
        btn_comment_head.setStyleSheet("border-radius:{};border-image:url(图片/头像 男孩.png)".format(vmfr_down_h/4*3))
        # 用户名
        label_name = QLabel("小明", self.fr2)
        label_name.setVisible(True)
        label_name.resize(2 * vmfr_down_h, vmfr_down_h / 2)
        label_name.move(vmfr_down_h*2/3+20, self.first_comment_y)
        label_name.setStyleSheet("color:red")
        # 评论
        label_comment = QLabel(self.fr2)
        label_comment.setVisible(True)
        label_comment.setText(self.commention)
        label_comment.move(vmfr_down_h*2/3+20, self.first_comment_y+vmfr_down_h/2+10)
        label_comment.adjustSize()
        label_comment.setWordWrap(True)  # 自动换行
        label_comment.setAlignment(Qt.AlignTop)  # 文字置顶
        # 创建水平线
        label_line = QLabel(self.fr2)
        label_line.setVisible(True)
        label_line.resize(vm_w - 20, 1)
        label_line.move(10, self.first_comment_y+vmfr_down_h/2+ vmfr_down_h / 2+20)
        label_line.setStyleSheet("background-color:#e3e1db")

        self.comment_num += 1
        self.first_comment_y += 40 + label_comment.height() + vmfr_down_h / 2

if __name__ == "__main__":
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    txt = "         标题:111\n据新华社讯近日，\n世界卫生组织在其官网上发布了5条新年健康饮食小贴士，"\
                                  "提醒人们如何吃得更健康均衡，增强身体抵抗力。\n一、吃多种食物。均衡饮食有助增强身体抵抗力，使人更加健康"\
                                  "长寿。世卫建议，日常饮食应尽量包括小麦、大米、玉米、土豆等多种主食，外加各种豆类、新鲜果蔬以及鱼肉蛋奶"\
                                  "等动物来源食品；尽可能多吃燕麦、糙米等富含膳食纤维的全谷物食品；零食最好选择新鲜果蔬和无盐坚果，而非高"\
                                  "糖、高脂和高盐食品。二、少吃盐。吃盐过多会导致血压升高增加心脏病和中风风险。世卫建议成人每天食盐摄入量"\
                                  "不超过5克（约一茶匙）。人们在烹饪时应少放盐，减少使用酱油等咸味调味品；在购买罐头、蔬菜干、坚果等食物时"\
                                  "，尽量挑选不添加盐和糖的品种；餐桌上不摆放盐瓶和含盐调味品；检查食品标签，选择低钠产品。\n三、低脂少"\
                                  "油。人们在饮食中如果摄入过多脂肪会增加肥胖、心脏病、中风风险，人造反式脂肪对健康危害尤其大。世卫建议，"\
                                  "用大豆油、菜籽油、玉米油等更健康的油替代黄油和猪油；选择鸡鸭鱼肉等脂肪含量较低的“白肉”，而不是猪牛羊肉"\
                                  "等“红肉”；烹饪时尽量用蒸或煮替代油炸；购买食品时应检查标签，避免购买含人造反式脂肪的各种加工食品、快餐"\
                                  "和煎炸食品。\n"
    window = Text(txt, "./文章图片/花生.png", "./文章图片/坚果.png")
    window.show()
    # 应用程序执行，进入消息循环

    sys.exit(app.exec_())
