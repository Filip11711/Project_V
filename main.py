from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QVBoxLayout
from pageManager import PageManager
from languageManager import LanguageManager
from pages import HomePage, SettingsPage
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.language_manager = LanguageManager()
        self.page_manager = PageManager()

        self.page_manager.add_page("home", HomePage(self.page_manager))
        self.page_manager.add_page("settings", SettingsPage(self.page_manager))

        self.page_manager.navigate_to("home")

        self.language_selector = QComboBox()
        self.language_selector.addItem("English", "en")
        self.language_selector.addItem("Hrvatski", "hr")
        self.language_selector.currentIndexChanged.connect(self.change_language)

        central_widget = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(self.language_selector)
        layout.addWidget(self.page_manager)
        
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def change_language(self, index):
        language_code = self.language_selector.currentData()
        self.language_manager.change_language(language_code)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
