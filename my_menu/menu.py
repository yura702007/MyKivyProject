from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.base import runTouchApp


class UserSettings(DropDown):
    pass


class MyWidget(BoxLayout):
    my_settings = ObjectProperty()

    def show_user_settings(self):
        dp = UserSettings()
        btn = Button(text='HELLO')
        btn.bind(on_release=dp.open)
        dp.bind(on_select=lambda instance, x: setattr(btn, 'text', x))
        runTouchApp(btn)


class MyMenuApp(App):

    def build(self):
        widget = MyWidget()
        # widget.add_widget(self.settings)
        return widget


if __name__ == '__main__':
    MyMenuApp().run()
