from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('checkbox.kv')


class MyWidget(Widget):
    toppings = []

    def checkbox_click(self, instance, value, topping):
        if value:
            self.toppings.append(topping)
        else:
            self.toppings.remove(topping)

        if self.toppings:
            self.ids.label_output.text = f'You selected {", ".join(self.toppings)}'
        else:
            self.ids.label_output.text = f'You selected nothing'


class CheckBoxApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    CheckBoxApp().run()
