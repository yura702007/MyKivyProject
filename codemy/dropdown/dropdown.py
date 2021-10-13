from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('main.kv')


class MyWidget(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f'You selected: {value}'


class DropDownApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    DropDownApp().run()
