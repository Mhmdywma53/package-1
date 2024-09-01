from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton

KV = '''
ScreenManager:
    ScreenOne:
    ScreenTwo:

<ScreenOne>:
    name: 'screen_one'
    MDRaisedButton:
        text: 'Go to Screen Two'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: app.change_screen('screen_two')

<ScreenTwo>:
    name: 'screen_two'
    MDRaisedButton:
        text: 'Go to Screen One'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: app.change_screen('screen_one')
'''

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def change_screen(self, screen_name):
        screen_manager = self.root
        screen_manager.transition = SwapTransition(duration=0.5)
        screen_manager.current = screen_name

if __name__ == '__main__':
    TestApp().run()
