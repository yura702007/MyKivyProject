from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MyLoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('login_screen.kv')

    def logger(self):
        name = self.root.ids.user.text
        self.root.ids.welcome_label.text = f'Sup {name}!'

    def clear(self):
        self.root.ids.welcome_label.text = 'Welcome'
        self.root.ids.user.text = ''
        self.root.ids.password.text = ''


if __name__ == '__main__':
    MyLoginApp().run()
