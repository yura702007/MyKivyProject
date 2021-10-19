from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MyDialMenuApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_file('dial_menu.kv')


if __name__ == '__main__':
    MyDialMenuApp().run()
