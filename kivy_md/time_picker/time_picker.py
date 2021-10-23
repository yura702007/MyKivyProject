from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker


class MyTimePickerApp(MDApp):
    def build(self):
        return Builder.load_file('time_picker.kv')


if __name__ == '__main__':
    MyTimePickerApp().run()
