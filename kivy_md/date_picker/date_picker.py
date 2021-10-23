from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker


class MyDatePickerApp(MDApp):
    def build(self):
        return Builder.load_file('date_picker.kv')

    def open_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.open()


if __name__ == '__main__':
    MyDatePickerApp().run()
