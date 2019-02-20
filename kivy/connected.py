
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition


class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")

        self.manager.current = 'signin'
      #  self.manager.get_screen('login').resetForm()
