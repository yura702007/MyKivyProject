from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
# from kivy.properties import ObjectProperty

Builder.load_file('slider.kv')


class MyWidget(Widget):
    # slider_text = ObjectProperty()

    def slider_it(self, *args):
        self.slider_text.font_size = 5 * args[1]
        self.slider_text.text = str(args[1])


class SliderApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    SliderApp().run()
