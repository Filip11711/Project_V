from PyQt6.QtWidgets import QStackedWidget, QWidget
from languageManager import LanguageManager

class PageManager(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.pages = {}
        self.language_manager = LanguageManager()

    def add_page(self, page_name, page_widget):
        self.pages[page_name] = page_widget
        self.addWidget(page_widget)

    def navigate_to(self, page_name):
        if page_name in self.pages:
            self.setCurrentWidget(self.pages[page_name])
            self.register_widgets_on_page(self.pages[page_name], page_name)
        else:
            raise ValueError(f"Page '{page_name}' not found.")

    def register_widgets_on_page(self, page, page_name):
        self.language_manager.reset_widgets()
        for widget in page.findChildren(QWidget):
            if hasattr(widget, 'text_key'):
                self.language_manager.register_widget(widget, page_name)
