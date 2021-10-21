from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MyImageSwiper(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_file('image_swiper.kv')


if __name__ == '__main__':
    MyImageSwiper().run()
