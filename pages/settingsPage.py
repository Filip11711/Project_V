from PyQt6.QtWidgets import QWidget, QVBoxLayout
from components import Button
from components import Label
from languageManager import LanguageManager
from pageManager import PageManager

class SettingsPage(QWidget):
    def __init__(self, pageManager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language_manager = LanguageManager()
        self.page_manager = pageManager
        
        self.label = Label("settings_title_text")
        self.button = Button("save_button")

        self.button.clicked.connect(lambda: self.page_manager.navigate_to("home"))
    
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)