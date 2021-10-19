from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MyNavBarApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_file('navbar.kv')


if __name__ == '__main__':
    MyNavBarApp().run()
