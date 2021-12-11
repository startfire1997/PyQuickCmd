from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

import json
import subprocess

# print(QtCore.__version__)

class configMgr:
    configDict = {}
    def __init__(self):
        configFile = open('conf/setting.json', 'r')
        content = configFile.read()
        self.configDict = json.loads(content)
        configFile.close()
        # print(self.configDict)

class CMDButton(QPushButton):
    m_cmdValue = 'text'
    def __init__(self, cmdKey, cmdValue):
        super().__init__()
        # 创建界面
        self.setText(cmdKey)
        self.m_cmdValue = cmdValue
        self.clicked.connect(self.doCmd)
        # print(self.m_cmdValue)

    @QtCore.Slot()
    def doCmd(self):
        p = subprocess.Popen(self.m_cmdValue, stdout = subprocess.PIPE, shell = True)
        print(p.stdout.readlines())  
        out,err = p.communicate()
        print(out)
        print(err)

class QuickCmd(QWidget):
    m_layout = QVBoxLayout()
    def __init__(self):
        super().__init__()
        # 创建界面
        self.setWindowTitle('QuickCmd')
        self.setWindowFlag(QtCore.Qt.WindowType.WindowMinMaxButtonsHint, False)

    def InitWidget(self, cfgMgr):
        for k,v in cfgMgr.configDict.items():
            temp = CMDButton(k, v)
            temp.setFixedWidth(150)
            temp.setFixedHeight(30)
            self.m_layout.addWidget(temp)
        self.resize(160, len(cfgMgr.configDict) * 32)
        self.setLayout(self.m_layout)

app = QApplication([])
confMgr = configMgr()
gui = QuickCmd()
gui.InitWidget(confMgr)
gui.show()
app.exec_()
