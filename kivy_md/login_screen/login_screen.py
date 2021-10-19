from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MyLoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('login_screen.kv')


if __name__ == '__main__':
    MyLoginApp().run()
