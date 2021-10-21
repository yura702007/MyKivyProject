from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MySwiperTricksApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_file('swiper_tricks.kv')


if __name__ == '__main__':
    MySwiperTricksApp().run()
