from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
import json , glob , random
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self , uname , pword):
        with open("E:/Visual Studio Code/Python/Mobile App/users.json") as file:
            users = json.load(file)
        
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Incorrect username or password! Try again!"    



class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self,uname,pword):
        with open("E:/Visual Studio Code/Python/Mobile App/users.json") as file:
            users = json.load(file)
    
        users[uname] = {'username': uname , 'password': pword ,
            'created': datetime.now().strftime("%Y-%m-%d  %H-%M-%S")}
        
        self.manager.current = 'sign_up_screen_success'
        print (users) 

        with open("E:/Visual Studio Code/Python/Mobile App/users.json" , 'w') as file:
            json.dump(users , file) 


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        #self.manager.transition.duration = 0.6
        self.manager.current = 'login_screen'

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'     

    def get_quote(self , feel):
        feel = feel.lower()
        print(feel)      
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
        
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt" , encoding ="utf8" ) as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)    
        #print(available_feelings)
        else:
            self.ids.quote.text = "Super sorry! We don't have the answers for that feeling yet! Go type what I told you to type dumby :)"

class ImageButton(ButtonBehavior , HoverBehavior , Image ):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run() 