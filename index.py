import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first Cool Gui")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("pythonProject1/tacos_tray_400x267.png"))
        label=QLabel("Hello User",self)
        label.setFont(QFont("Arial",40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color:red;"
                            "background-color:black;")
        pixmap=QPixmap("pythonProject1/tacos_tray_400x267.png")
        label.setPixmap(pixmap)
        
        label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # Use `app.exec_()` to start the event loop

if __name__ == '__main__':
    main()
