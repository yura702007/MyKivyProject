from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.animation import Animation

Builder.load_file('animation.kv')


class MyWidget(Widget):
    def animate_it(self):
        pass


class MySomeApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MySomeApp().run()
