from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MyDatePickerApp(MDApp):
    def build(self):
        return Builder.load_file('date_picker.kv')


if __name__ == '__main__':
    MyDatePickerApp().run()
