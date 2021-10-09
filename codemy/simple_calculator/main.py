from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.core.window import Window

# set app size
Window.size = (500, 700)

Builder.load_file('calculator.kv')


class MyWidget(Widget):

    def clear(self):
        self.ids.calc_input.text = '0'

    def press_num_btn(self, symbol):
        prior = self.ids.calc_input.text
        if prior == '0':
            self.ids.calc_input.text = f'{symbol}'
        else:
            self.ids.calc_input.text += f'{symbol}'

    def equals(self):
        expression = self.ids.calc_input.text
        operands = ['+', '-', '*', '/']
        operand, exp = '', None
        result = 0
        for o in operands:
            if o in expression:
                exp = expression.split(o)
                operand = o
        if operand == '+':
            result += int(exp[0]) + int(exp[1])
        elif operand == '-':
            result += int(exp[0]) - int(exp[1])
        elif operand == '*':
            result += int(exp[0]) * int(exp[1])
        elif operand == '/':
            result += int(exp[0]) / int(exp[1])
        if result == int(result):
            self.ids.calc_input.text = str(int(result))
        else:
            self.ids.calc_input.text = str(result)



class MyCalculator(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyCalculator().run()
