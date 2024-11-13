from PyQt6.QtWidgets import QWidget, QVBoxLayout
from components import Button
from components import Label
from languageManager import LanguageManager
from pageManager import PageManager

class HomePage(QWidget):
    def __init__(self, pageManager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language_manager = LanguageManager()
        self.page_manager = pageManager
        
        self.label = Label("welcome")
        self.button = Button("click_me")

        self.button.clicked.connect(lambda: self.page_manager.navigate_to("settings"))
    
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)