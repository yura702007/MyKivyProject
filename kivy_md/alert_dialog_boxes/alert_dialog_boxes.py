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
                title='Pretty Neat, Right',
                text='This is some text...',
                buttons=[
                    MDFlatButton(
                        text='CANCEL',
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text="Yes, It'S Neat!", text_color=self.theme_cls.primary_color
                    )
                ]
            )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


if __name__ == '__main__':
    MyDialogBoxesApp().run()
