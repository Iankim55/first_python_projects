import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.initUI()

    def initUI(self):
        # Set up the label to display time
        self.time_label = QLabel("00:00:00.00", self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 32px;")

        # Set up buttons
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_timer)

        self.stop_button = QPushButton("Reset", self)
        self.stop_button.clicked.connect(self.reset_timer)

        # Set up layouts
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.time_label)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.setWindowTitle("Stopwatch")
        self.setGeometry(600, 400, 300, 200)

    def start_timer(self):
        if not self.timer.isActive():
            self.start_button.setText("Pause")
            self.timer.start(10)  # Updates every 10ms
        else:
            self.start_button.setText("Start")
            self.timer.stop()

    def reset_timer(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.update_time()
        self.start_button.setText("Start")

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.time.toString("hh:mm:ss.zzz")[:-1])  # Display up to centiseconds

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
