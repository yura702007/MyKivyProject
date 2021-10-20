from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton


class MyDialogBoxesApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        return Builder.load_file('alert_dialog_boxes.kv')

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text='Pretty Neat, Right',
                buttons=[
                    MDFlatButton(
                        text='CANCEL', text_color=self.theme_cls.primary_color
                    ),
                    MDRectangleFlatButton(
                        text="Yes, It'S Neat!", text_color=self.theme_cls.primary_color
                    )
                ]
            )
        self.dialog.open()


if __name__ == '__main__':
    MyDialogBoxesApp().run()
