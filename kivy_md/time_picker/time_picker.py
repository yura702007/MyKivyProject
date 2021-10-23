from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker


class MyTimePickerApp(MDApp):
    def build(self):
        return Builder.load_file('time_picker.kv')

    def open_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.open()


if __name__ == '__main__':
    MyTimePickerApp().run()
