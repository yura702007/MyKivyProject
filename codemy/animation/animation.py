from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.animation import Animation

Builder.load_file('animation.kv')


class MyWidget(Widget):
    def animate_it(self, widget, *args):
        animate = Animation(
            background_color=(1, 0, 1, 1)  # смена цвета фона кнопки
        )
        animate += Animation(size_hint=(1, 1))  # смена размера кнопки
        animate += Animation(size_hint=(.5, 1))  # смена размера кнопки
        animate += Animation(pos_hint={'center_x': .25})  # смена позиции кнопки
        animate.start(widget)  # запуск анимации
        animate.bind(on_complete=self.my_callback)  # смена запуск обратного вызова

    def my_callback(self, *args):
        self.ids.my_label.text = 'Wow'


class MySomeApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MySomeApp().run()
