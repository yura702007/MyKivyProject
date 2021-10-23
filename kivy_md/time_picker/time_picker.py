from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker


class MyTimePickerApp(MDApp):
    def build(self):
        return Builder.load_file('time_picker.kv')

    def get_time(self, instance, time):
        self.root.ids.my_label.text = f'{time}'

    def on_cancel(self, instance, time):
        self.root.ids.my_label.text = 'You clicked Cancel'

    def open_time_picker(self):
        from datetime import datetime
        default_time = datetime.strptime('4:20:15', '%H:%M:%S').time()
        time_dialog = MDTimePicker()
        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time)
        time_dialog.open()


if __name__ == '__main__':
    MyTimePickerApp().run()
