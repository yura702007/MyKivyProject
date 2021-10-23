from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MySwiperTricksApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        file = Builder.load_file('swiper_tricks.kv')
        obj = file.ids.swiper.get_items()
        print(obj)
        return file


if __name__ == '__main__':
    MySwiperTricksApp().run()
