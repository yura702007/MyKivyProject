from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('viewer.kv')


class MyWidget(Widget):
    def selected(self, file_name):
        try:
            self.ids.my_image.source = file_name[0]
        except:
            pass


class MyApp(App):
    widget = MyWidget()

    def build(self):
        return self.widget


if __name__ == '__main__':
    MyApp().run()
