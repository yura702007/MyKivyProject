from kivy.lang.builder import Builder
from kivymd.app import MDApp
import os


class MyImageSwiper(MDApp):
    img_dir = 'images/'
    img_paths = []
    count_img = 0

    def build(self):
        self.paths_constructor()
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_file('image_swiper.kv')

    def paths_constructor(self):
        paths = next(os.walk('images'))[-1]
        for path in paths:
            self.img_paths.append(self.img_dir + path)

    def listing_image(self):
        if self.count_img < len(self.img_paths) - 1:
            self.count_img += 1
        else:
            self.count_img = 0
        self.root.ids.my_image.source = self.img_paths[self.count_img]


if __name__ == '__main__':
    MyImageSwiper().run()
