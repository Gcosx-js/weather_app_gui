
from PyQt5 import QtCore, QtGui, QtWidgets


class About_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1242, 822)
        Form.setStyleSheet("#Form{\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, 10, 1271, 641))
        self.label.setStyleSheet("image: url(:/newPrefix/Blue Modern Who Is He Youtube Thumbnail.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.instagram_button = QtWidgets.QPushButton(Form)
        self.instagram_button.setGeometry(QtCore.QRect(300, 700, 91, 71))
        self.instagram_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.instagram_button.setStyleSheet("image: url(:/newPrefix/instagram.JPG);")
        self.instagram_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/instagram.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.instagram_button.setIcon(icon)
        self.instagram_button.setIconSize(QtCore.QSize(95, 300))
        self.instagram_button.setObjectName("instagram_button")
        self.github_butotn = QtWidgets.QPushButton(Form)
        self.github_butotn.setGeometry(QtCore.QRect(590, 690, 91, 81))
        self.github_butotn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.github_butotn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/github.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.github_butotn.setIcon(icon1)
        self.github_butotn.setIconSize(QtCore.QSize(100, 300))
        self.github_butotn.setObjectName("github_butotn")
        self.twitter_button = QtWidgets.QPushButton(Form)
        self.twitter_button.setGeometry(QtCore.QRect(870, 700, 101, 71))
        self.twitter_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.twitter_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/twitter.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twitter_button.setIcon(icon2)
        self.twitter_button.setIconSize(QtCore.QSize(100, 300))
        self.twitter_button.setObjectName("twitter_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import a_img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = About_ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
