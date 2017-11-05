import sys
from PyQt5.QtWidgets import QApplication
from dumbDialog import DumbDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dia = DumbDialog()
    dia.show()
    app.exec_()
