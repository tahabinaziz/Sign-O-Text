from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition,SlideTransition
from kivy.lang import Builder


from connected import Connected

class Signin(Screen):
  
      

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]username and/ or password required[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00FF00]Logged In successfully!!![/color]'
                app = App.get_running_app()
               # app.username = loginText
                #app.password = passwordText
                self.manager.transition = SlideTransition(direction="left")
                self.manager.current = 'connected'
               # app.config.read(app.get_application_config())
                app.config.write()

               
            else:
                info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'


    
        
            
            


class SigninApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(Signin(name='signin'))

        manager.add_widget(Connected(name='connected'))
      

        return manager


if __name__=="__main__":
     SigninApp().run()
    