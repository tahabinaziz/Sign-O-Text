
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition


class nscreen(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")

        self.manager.current = 'user'
      #  self.manager.get_screen('login').resetForm()
