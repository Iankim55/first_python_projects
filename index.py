import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer, QTime

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a QLabel to display the time
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 64px;
            font-family: 'Times New Roman';
            color: green;
        """)

        # Set the window background color to black
        self.setStyleSheet("background-color: black;")

        # Create a layout and add the QLabel
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # Set up the timer to update time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        # Set initial time
        self.update_time()

        # Set window properties
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

    def update_time(self):
        # Get the current time and update the label
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
