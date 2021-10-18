from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_file('color_themes.kv')


if __name__ == '__main__':
    MainApp().run()
