from PyQt6.QtWidgets import QWidget
import json
import os

class LanguageManager:
    instance = None
    translations : dict[str, dict[str, dict[str, dict[str, str]]]]
    
    def __new__(self, *args, **kwargs):
        if not self.instance:
            self.instance = super().__new__(self, *args, **kwargs)
        return self.instance

    def __init__(self, default_language="en"):
        self.current_language = default_language
        self.translations = self.load_languages()
        self.widgets = []

    def load_languages(self, directory="languages"):
        translations = {}
        
        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                language_code = os.path.splitext(filename)[0]  # Extract language code (e.g., 'en' from 'en.json')
                try:
                    with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
                        translations[language_code] = json.load(file)
                except FileNotFoundError:
                    print(f"Translation file {filename} not found. Skipping.")
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in {filename}. Skipping.")

        if not translations:
            print("No translation files found. Ensure there are JSON files in the directory.")
        
        return translations
    
    def update_language_files(self, directory="languages"):
        for language_code, content in self.translations.items():
            filename = f"{language_code}.json"
            try:
                with open(os.path.join(directory, filename), "w", encoding="utf-8") as file:
                    json.dump(content, file, ensure_ascii=False, indent=4)
                print(f"Updated {filename} successfully.")
            except IOError:
                print(f"Error writing to {filename}. Skipping.")

    def register_widget(self, widget, page_name):
        self.widgets.append((widget, page_name))
        self.apply_language_to_widget(widget, page_name)

    def change_language(self, language_code):
        self.current_language = language_code
        self.apply_language()

    def apply_language(self):
        for widget, page_name in self.widgets:
            self.apply_language_to_widget(widget, page_name)

    def apply_language_to_widget(self, widget, page_name):
        if widget.text_key in self.translations[self.current_language][page_name][widget.type]:
            getattr(widget, "setText")(self.translations[self.current_language][page_name][widget.type][widget.text_key])

    def reset_widgets(self):
        self.widgets = []

    def fill_language_files(self, pageManager):
        for language in self.translations.keys():
            for page_name in pageManager.pages:
                if page_name == "meta":
                    continue
                if page_name not in self.translations[language]:
                    self.translations[language][page_name] = {}
                for widget in pageManager.pages[page_name].findChildren(QWidget):
                    if widget.type not in self.translations[language][page_name]:
                        self.translations[language][page_name][widget.type] = {}
                    if widget.text_key not in self.translations[language][page_name][widget.type]:
                        self.translations[language][page_name][widget.type][widget.text_key] = ""
        self.update_language_files()