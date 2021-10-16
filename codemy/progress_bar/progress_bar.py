from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('progress_bar.kv')


class MyWidget(Widget):

    def press_it(self):
        v = self.ids.my_bar.value
        if v < 1:
            v += .25
        else:
            v = 0
        self.ids.my_bar.value = v
        self.ids.status.text = f'{v * 100}%'


class MySomeApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MySomeApp().run()
