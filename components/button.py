from PyQt6.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self, text_key: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text_key = text_key
