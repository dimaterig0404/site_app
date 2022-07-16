import os
from pickle import FALSE
import random
#pip install kivy-garden.zbarcam

from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.clock import Clock
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import Label
from kivymd.app import MDApp
import cv2
import sqlite3
import face_recognition







def read_sqlite_table_for_user(table):
    try:
        sqlite_connection = sqlite3.connect('E:/django/mysite/db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = f"""SELECT * from {table}"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        info = []
        for row in records:
            if row[2]:
                info.append(row[1])
        
        cursor.close()
        return info 

        

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def read_sqlite_table_for_user_code(table):
    try:
        sqlite_connection = sqlite3.connect('E:/django/mysite/db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = f"""SELECT * from {table}"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        info = []
        for row in records:
            if row[3].isdigit():
                info.append(row[3]+'|'+str(row[0]))
        
        cursor.close()
        return info 

        

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def make_po_foto_code(path,name):
    image = cv2.imread(path)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)
    knownEncodings = []
    knownNames = []
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)
    
    print(knownEncodings)
    return knownEncodings   

ii_code =  read_sqlite_table_for_user_code('myapp_ii')
       
user_isGreen =  read_sqlite_table_for_user('myapp_user')         


def write_sqlite_table_for_user_code(table,id_user,name_foto):
    try:
        sqlite_connection = sqlite3.connect('E:/django/mysite/db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = f"""
        UPDATE {table}
        SET info_vac='{name_foto}'
        WHERE id='{id_user}';"""
        cursor.execute(sqlite_select_query)
        
        
        cursor.close()
        

        

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")





try:
    os.mkdir('sdcard/scaner_temp')
except:
    pass


stri ='''
#:import get_color_from_hex kivy.utils.get_color_from_hex

#:import ZBarCam kivy_garden.zbarcam.ZBarCam
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol


MDScreen:

    

        
    name: 'screen 1'
    text: 'registration face'
    icon: 'qrcode-scan'
    badge_icon: "numeric-10"
    BoxLayout:
        orientation: 'horizontal'
        ZBarCam:
            id: zbarcam
            canvas.before:
                PushMatrix
                Rotate:
                    angle: -90
                    origin: self.center
            canvas.after:
                PopMatrix
        Label:
            size_hint: None, None
            size: 0, 0
            text: app.maini(', '.join([str(symbol.data) for symbol in zbarcam.symbols]),zbarcam)


# MDBottomNavigation:
    #     panel_color: get_color_from_hex("#eeeaea")
    #     selected_color_background: get_color_from_hex("#97ecf8")
    #     text_color_active: 0, 0, 0, 1

        # MDBottomNavigationItem:

        #     name: 'screen 2'
        #     text: 'qr/face scaner'
        #     icon: 'face-recognition'
        #     badge_icon: "numeric-5"
        #     # Camera:
        #     #     id: camera
        #     #     resolution: (1280, 1280)
        #     #     canvas.before:
        #     #         PushMatrix
        #     #         Rotate:
        #     #             angle: -270
        #     #             origin: self.center
        #     #     canvas.after:
        #     #         PopMatrix
        #     # 


'''




class YourApp(MDApp):




    def build(self):
        global mesg_1st
        mesg_1st = True

        self.theme_cls.material_style = "M3"
        return Builder.load_string(stri)




    def callpopup(self):
        
        dlg = MessageBox(titleheader="Finish", message="Это финальный этап регистрации пользователя.\nУбедитьесь что он смотрет в камеру и находиться\nпо центру кадра. Потому после нажатия кнопки\nок программа сделает снимок с камеры.", options={"Ок": "printyes()"})
        print("Messagebox shows as kivy popup and we wait for the \nuser action and callback to go to either routine")


    def printyes(self):
        # screenshot

        camera = zbarcamera_g
        idi = name_g
        os.mkdir(f"sdcard/scaner_temp/{idi}")

        camera.export_to_png(f"sdcard/scaner_temp/{idi}/0.png")


               
        info_face = make_po_foto_code(f"sdcard/scaner_temp/{idi}/0.png",name_g)
        write_sqlite_table_for_user_code('myapp_user',int(id_g),info_face)

        print("Captured")

    def maini(self,text,zbarcamera):

        
        global mesg_1st
           


        if str(text).replace("'",'').replace('b','') in ii_code  and mesg_1st == True:
            
            
            print(user_isGreen)
            global name_g
            global id_g
            name_g,id_g = user_isGreen[ii_code.index(str(text).replace("'",'').replace('b',''))].split('|')
            global zbarcamera_g
            zbarcamera_g = zbarcamera
            
            self.callpopup()
            mesg_1st = False
            
        
        
        print(ii_code)
        
        
        return text

class MessageBox(YourApp):
    def __init__(self, titleheader="Title", message="Message", options={"OK": "self.ok()", "NO": "self.no()"}):

        def popup_callback(instance):
            "callback for button press"
            # print('Popup returns:', instance.text)
            self.retvalue = instance.text
            self.popup.dismiss()

        self.retvalue = None
        self.options = options
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=message, font_size=15, pos_hint={'center_x':0.51,
                                            'center_y':-1}))
        b_list =  []
        buttonbox = BoxLayout(orientation='horizontal')
        for b in options:
            b_list.append(Button(text=b, size_hint=(1,.35), font_size=20))
            b_list[-1].bind(on_press=popup_callback)
            buttonbox.add_widget(b_list[-1])
        box.add_widget(buttonbox)
        self.popup = Popup(title=titleheader, content=box, size_hint=(None, None), size=(400, 400))
        self.popup.open()
        self.popup.bind(on_dismiss=self.OnClose)

    def OnClose(self, event):
        self.popup.unbind(on_dismiss=self.OnClose)
        self.popup.dismiss()
        if self.retvalue != None:
            command = "super(MessageBox, self)."+self.options[self.retvalue]
            # print "command", command
            exec(command)
            global mesg_1st
            mesg_1st = True



def update(dt):
    ii_code =  read_sqlite_table_for_user_code('myapp_ii')   
    user_isGreen =  read_sqlite_table_for_user('myapp_user')
    print(ii_code)
    print(user_isGreen) 
    




if __name__ == '__main__':
    
    Clock.schedule_interval(update, 60)
    YourApp().run()