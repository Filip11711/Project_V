class LanguageManager:
    instance = None
    
    def __new__(self, *args, **kwargs):
        if not self.instance:
            self.instance = super().__new__(self, *args, **kwargs)
        return self.instance

    def __init__(self, default_language="en"):
        self.current_language = default_language
        self.translations = self.load_language(self.current_language)
        self.widgets = []

    def load_language(self, language_code):
        import json
        import os
        try:
            with open(os.path.join("languages", f"{language_code}.json"), "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Translation file for {language_code} not found. Falling back to default (English).")
            with open(os.path.join("languages", "en.json"), "r", encoding="utf-8") as file:
                return json.load(file)

    def register_widget(self, widget, page_name):
        self.widgets.append((widget, page_name))
        self.apply_language_to_widget(widget, page_name)

    def change_language(self, language_code):
        self.current_language = language_code
        self.translations = self.load_language(language_code)
        self.apply_language()

    def apply_language(self):
        for widget, page_name in self.widgets:
            self.apply_language_to_widget(widget, page_name)

    def apply_language_to_widget(self, widget, page_name):
        getattr(widget, "setText")(self.translations[page_name][widget.type][widget.text_key])

    def reset_widgets(self):
        self.widgets = []
