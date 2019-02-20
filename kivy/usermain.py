from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition,SlideTransition
from kivy.lang import Builder


# from connected import Connected
from nxtSceen import nscreen

class users(Screen):
  
      

    def validate_user(self):
       
                app = App.get_running_app()
               # app.username = loginText
                #app.password = passwordText
                self.manager.transition = SlideTransition(direction="left")
                self.manager.current = 'connected'
               # app.config.read(app.get_application_config())
                app.config.write()

       

    
        
            
            


class userApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(users(name='user'))

        manager.add_widget(nscreen(name='connected'))
      

        return manager


if __name__=="__main__":
     userApp().run()
    