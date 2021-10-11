from kivy.app import App
from kivy.core.spelling import Spelling
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('main.kv')


class MyWidget(Widget):
    def press(self):
        s = Spelling()
        s.select_language('en-US')
        word = self.ids.word_input.text
        option = s.suggest(word)
        self.ids.word_label.text = f'{option}'


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
