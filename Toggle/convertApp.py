from kivy.uix.filechooser import Screen
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

class Screen2(Screen):
    def convert(self, *args):
        num= int(self.ids.txt_number.text)
        #lbl_output.text = bin (ค่าตัวแปรที่ต้องการแปลงเป็นเลขฐาน 2)
        if args[0].text=="base2":
            self.ids.lbl_output.text= bin(num)[2:]
        if args[0].text=="base8":
            self.ids.lbl_output.text= oct(num)[2:]
        if args[0].text=="base10":
            self.ids.lbl_output.text= hex(num)[2:]
class Screen1(Screen): 
    pass

class UI(ScreenManager):
    pass


class convertApp(App):
    def build(self):
        return UI()
    
if __name__=='__main__':
    convertApp().run()