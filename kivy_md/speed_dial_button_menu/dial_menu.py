from pprint import pprint

from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MyDialMenuApp(MDApp):
    data = {
        'Python': 'language-python',
        'Ruby': 'language-ruby',
        'JS': 'language-javascript'
    }

    def callback(self, instance):
        text = instance.icon
        for key, value in self.data.items():
            if text == value:
                self.root.ids.my_label.text = f'You pressed {key}'
                break

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_file('dial_menu.kv')


if __name__ == '__main__':
    MyDialMenuApp().run()
