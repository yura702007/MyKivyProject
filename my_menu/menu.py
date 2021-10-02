from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown


class DropDownCustom(DropDown):
    pass


class MyWidget(BoxLayout):

    def spinner_clicked(self, value):
        self.ids.click_label.text = f'You selected: {value}'


class MyMenuApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyMenuApp().run()
