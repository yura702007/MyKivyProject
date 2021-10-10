from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.core.window import Window

# set app size
Window.size = (500, 700)

Builder.load_file('calculator.kv')


class MyWidget(Widget):

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if prior == '0':
            pass
        elif '-' in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def remove(self):
        prior = self.ids.calc_input.text
        if len(prior) > 1:
            self.ids.calc_input.text = prior[:-1]
        else:
            self.ids.calc_input.text = '0'

    def clear(self):
        self.ids.calc_input.text = '0'

    def press_num_btn(self, symbol):
        prior = self.ids.calc_input.text
        if prior == '0':
            self.ids.calc_input.text = f'{symbol}'
        else:
            self.ids.calc_input.text = f'{prior}{symbol}'

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split('+')
        if '.' in num_list[-1]:
            pass
        else:
            self.ids.calc_input.text = f'{prior}.'

    def equals(self):
        prior = self.ids.calc_input.text
        if '+' in prior:
            num_list = prior.split('+')
            answer = 0.0
            for num in num_list:
                answer += float(num)
            self.ids.calc_input.text = str(answer)


class MyCalculator(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyCalculator().run()
