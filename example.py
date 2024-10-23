import sys
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QLineEdit, QApplication, QWidget
from vitual_keyboard import VirtualKeyboard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Example of virtual keyboard widget')
        self.grid_layout = QGridLayout()

        self.input_le = QLineEdit()
        self.grid_layout.addWidget(self.input_le, 0, 0)
        self.keyboard = VirtualKeyboard(text_input=self.input_le, language='english')
        self.grid_layout.addWidget(self.keyboard, 1, 0)        
        
        central_widget = QWidget()
        central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()





