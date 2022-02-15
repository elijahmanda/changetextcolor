import random
import re
from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.toast import toast
kv  = '''
MDBoxLayout :
    orientation:"vertical"
    padding : '20dp'
    MDTextField:
        id : field
        hint_text:"Enter your name"
        helper_text_mode: "on_focus"
        helper_text: "some text"
        line_color_focus: 1, 0, 1, 1
        mode: "rectangle"
        on_text : app.set_color()
    Label :
        id : label
        text : field.text
        halign : 'center'
        font_size : 150
        
    


        
    Widget :
'''
class Mywidget(BoxLayout):
       pass
class Myapp(MDApp):
    
    def build(self):
            return Builder.load_string(kv)

    def set_color(self, *args):
        list_ = [random.random() for i in range(3)]
        list_.append(1)
        toast(str(list_))
        self.root.ids.label.color = list_
        list_.clear()



    
        

    

Myapp().run()