from PyQt6.QtWidgets import QLabel

class Label(QLabel):
    def __init__(self, text_key: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = "label"
        self.text_key = text_key