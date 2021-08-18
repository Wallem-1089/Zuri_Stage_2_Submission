from kivymd.app import MDApp
from kivy.lang import Builder

# task question No.2
print('Walter Ikhile')


screen_helper = '''
Screen:
    NavigationLayout:
        ScreenManager:
            id: screen_manager
            Screen:
                id: home
                name: 'home_page'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Print Input'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    Widget:
                    MDLabel:
                    MDTextField:
                        id: mode 
                        hint_text: 'enter data here'
                        helper_text: 'enter here'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Show'
                            on_release: app.show_data()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: mode_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 55
'''


class PhonicsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'
        self.title = 'Phonics'
        screen = Builder.load_string(screen_helper)
        return screen

    def show_data(self):
        text = self.root.ids.mode.text
        self.root.ids.mode_text_input.text = text

if __name__ == '__main__':
    app = PhonicsApp()
    app.run()
