from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MyButtonBarApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_file('bbutton.kv')

    def pressed(self):
        self.root.ids.my_label.text = 'You pressed button'


if __name__ == '__main__':
    MyButtonBarApp().run()
