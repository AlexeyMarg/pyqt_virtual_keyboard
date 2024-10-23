from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton

class VirtualKeyboard(QWidget):
    def __init__(self, text_input=None, language='english'):
        super().__init__()
        self.caps_lock_on = True 
        self.text_input = text_input  # Текстовое поле, в которое будет производиться ввод
        self.buttons = {}  # Словарь для хранения кнопок
        self.language = language

        keyboard_layout = QGridLayout()
        self.create_virtual_keyboard(keyboard_layout)

        # Установка раскладки клавиатуры
        self.setLayout(keyboard_layout)

    def create_virtual_keyboard(self, layout):
        if self.language == 'russian':
            buttons = [
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', 'Ё',
                'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ',
                'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Ж', 'Ж', 'Э', 'Caps Lock',
                'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', ',', '.', ':', ';', '/', 
                '<', '>', '=', '+', '@', '#', '%', '^', '*', '/', '(', ')', '[', ']', 
                '{', '}', '\"', '\'', 'Space', 'Backspace'
            ]
            n_rows = 6
            n_columns = 12
        elif self.language == 'english':
            buttons = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', ':', ';', '/', '&',
            '<', '>', '=', '+', '@', '#', '%', '^', '*', '/', '(', ')', '[', ']', 
            '{', '}', '\"', '\'', 'Space', 'Backspace'
            ]
            n_rows = 6
            n_columns = 11
        else:
            raise ValueError('language parameter should be \'english\' or \'russian\'')
            
        positions = [(i, j) for i in range(n_rows) for j in range(n_columns)] 
        for position, button_label in zip(positions, buttons):
            if button_label == 'Space':
                button = QPushButton(' ')
                layout.addWidget(button, position[0], position[1], 1, 1)  
            elif button_label == 'Caps Lock':
                button = QPushButton(button_label)
                layout.addWidget(button, position[0], position[1], 1, 1)  
            else:
                button = QPushButton(button_label)
                layout.addWidget(button, position[0], position[1])

            # Сохранение кнопки в словарь для дальнейшего управления
            self.buttons[button_label] = button

            # Подключение события к соответствующим кнопкам
            if button_label == 'Caps Lock':
                button.clicked.connect(self.toggle_caps_lock)
            else:
                button.clicked.connect(lambda ch, text=button_label: self.handle_virtual_keypress(text))

    def toggle_caps_lock(self):
        self.caps_lock_on = not self.caps_lock_on
        for key, button in self.buttons.items():
            if key.isalpha(): 
                if self.caps_lock_on:
                    button.setText(key.upper())
                else:
                    button.setText(key.lower())

    def handle_virtual_keypress(self, key):
        if self.text_input is not None:
            current_text = self.text_input.text()

            if key == 'Backspace':
                self.text_input.setText(current_text[:-1])  
            elif key == 'Space':
                self.text_input.setText(current_text + ' ')  
            else:
                if self.caps_lock_on and key.isalpha():  
                    key = key.upper()
                elif not self.caps_lock_on and key.isalpha():
                    key = key.lower()
                self.text_input.setText(current_text + key)  