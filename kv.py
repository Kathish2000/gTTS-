
from kivy import Config
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '600')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

# Window.clearcolor = (237, 235, 235, 235)
# create a background class which inherits the boxlayout class 
class Background(BoxLayout): 
    def __init__(self, **kwargs): 
        super().__init__(**kwargs) 
    pass
  
# Create App class with name of your app 
class SampleApp(App): 
  
# return the Window having the background template. 
    def build(self): 
        return Background() 

  
# run app in the main function 
if __name__ == '__main__': 
    SampleApp().run() 
