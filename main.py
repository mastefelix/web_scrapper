from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QMessageBox, QScrollArea
from PyQt6.QtGui import QIcon
import parser


class ParserApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 500)
        self.setWindowTitle("Курсы Клуба программистов")
        self.setWindowIcon(QIcon("logo.jpg"))
        self.setStyleSheet("background-color: #83bca9; color: #282B28;"
                           "font-family: fantasy, Comic Sans MS; font-size: 18px;")
        self.courses = QTextEdit()
        self.courses.setReadOnly(True)
        self.courses.resize(450, 400)
        self.courses.setStyleSheet("background-color: #FFF; font-size: 16px;")

        self.button_get = QPushButton("Получить")
        self.button_get.setStyleSheet("background-color: #3E5641; color: #D36135; font-size: 24px; font-weight: bold")
        self.button_show = QPushButton("Посмотреть")
        self.button_show.setStyleSheet("background-color: #3E5641; color: #D36135; font-size: 24px; font-weight: bold")

        layout = QVBoxLayout()
        layout.addWidget(self.courses)
        layout.addWidget(self.button_get)
        layout.addWidget(self.button_show)

        self.setLayout(layout)

        self.button_get.clicked.connect(self.get_result)
        self.button_show.clicked.connect(self.show_result)

    def get_result(self):
        self.result = parser.parser()
        info = QMessageBox()
        info.setWindowTitle("Результат")
        info.setWindowIcon(QIcon("logo.jpg"))
        info.setStyleSheet("background-color: #83bca9; color: #282B28; font-family: fantasy, Comic Sans MS;"
                            "font-size: 18px;")
        info.setText("Данные получены!")
        info.exec()

    def show_result(self):
        add = ''
        for info in self.result:
            for key, value in info.items():
                add += value + '\n'
        self.courses.setText(add)


def main():
    app = QApplication([])
    window = ParserApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
