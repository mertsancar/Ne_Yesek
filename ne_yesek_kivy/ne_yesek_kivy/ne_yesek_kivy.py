#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,  Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.graphics import *
from kivy.graphics.instructions  import CanvasBase
from kivy.event import ObjectWithUid

#yemeksepeti sayfasına gitmek için
import webbrowser

#yemek veritabanı
import pyodbc
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\User\source\repos\ne_yesek_kivy\ne_yesek_kivy\neyesek.accdb;")
ne_yesek = conn.cursor()
ne_yesek.execute("select * from yemekler")
yemek_liste = ne_yesek.fetchall() 
yemek_liste = list(yemek_liste)


#rastgele yemek için
import random



# yemeksepeti kırmızısı: rgb(171, 0, 18)
# yemeksepeti turuncusu: rgb(253, 165, 48)
Window.clearcolor = (171/255, 0, 18/255,1)


class MainWindow(Screen):
    pass



class SecondWindow(Screen):
        
    def rastgele(self,hungry_level):

        temp_list=[]
        temp_list.extend(yemek_liste)
        i = 0
        while i != 5:
            for x in temp_list:
                if ( hungry_level  in x) == False:
                    temp_list.remove(x)
            i += 1
        random_mama =  random.choice(temp_list)
        mama_name = random_mama[0]


        show = Label(text=mama_name)
        popupWindow = Popup(title="İşte Yemeğin", content=show, size_hint=(None,None),size=(400,400))
        popupWindow.open()

        webbrowser.open(random_mama[random.randint(2,6)])

       

        

class WindowManager(ScreenManager):
    pass


class P(FloatLayout):
    pass
    

kv = Builder.load_file("my.kv")
class NeYesek(App):

    def build(self):
        def sound(self):
            sound = SoundLoader.load('TrueArtRealAffectionPart4 - Noir Et Blanc Vie.mp3')
            if sound:
                sound.play()
        sound(self)


        return kv

    
        
    





if __name__ == "__main__":
    NeYesek().run()
