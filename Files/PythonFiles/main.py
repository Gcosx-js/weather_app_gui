from interface import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import Qt,QDate
import requests,threading,ctypes
from datetime import datetime,timedelta
from about import About_screen
try:
    print('Getting Geolocation...')
    def geo_api_req():
        
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data['city']

    geo_api = threading.Thread(target=geo_api_req)
    geo_api.start()


    print('Starting API for Geolocation...')
    print('Starting Threads. Please wait a moment...')
    def weather_api_req(seher = geo_api_req()):
        
        response = requests.get(f'https://api.weatherapi.com/v1/current.json?key=ef5940247d54433992b133742230705&q={seher}&aqi=yes')
        return response.json()

    def history_data(history_date=str(datetime.today() + timedelta(days=1))[:10],seher=geo_api_req()):
                
                response = requests.get(f'https://api.weatherapi.com/v1/history.json?key=ef5940247d54433992b133742230705&q={seher}&dt={history_date}')
                return response.json() 

    history_d = threading.Thread(target=history_data)
    history_d.start()
    today_main_data = weather_api_req()

    tomorrow_main_data = history_data()

    
    class WeatherApp(QWidget):
            def __init__(self,today_main_data) -> None:
                super().__init__()
                self.app = Ui_Form()
                print('All data successfully received!')
                self.app.setupUi(self)
                alert = QMessageBox()
                alert.setIcon(QMessageBox.Warning)
                alert.setWindowTitle("Attention")
                alert.setText("NOT : There are some limits to going back in time.\nYou can only go back 7 days.\nPlease confirm message to enter the app!")
                alert.setStandardButtons(QMessageBox.Ok)
                alert.exec_()
                
                
            
            #Today area --------------------------------------------------
            
                self.tarix = datetime.strptime(f'{datetime.today()}', "%Y-%m-%d %H:%M:%S.%f")
                self.today_date = self.tarix.strftime("%d %B")
                self.app.today_day.setText(self.today_date)
                self.app.dateEdit.setMinimumDate(QDate.currentDate().addDays(-7))
                self.app.dateEdit.setMaximumDate(QDate.currentDate().addDays(+1))# Minimum date is set 7 days before today
                self.app.dateEdit.setDisplayFormat("yyyy-MM-dd")
                self.app.dateEdit.setDate(QDate.currentDate())
                temperature_celsius = today_main_data['current']['temp_c']
                formatted_temperature = f'{str(temperature_celsius)[:2]}° C'
                self.app.today_degree.setText(formatted_temperature)
                
                
                
            
                
                if int(str(temperature_celsius)[:2]) == 25 or int(str(temperature_celsius)[:2])>25:
                    
                    self.app.today_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/hot.png'))
                
                
                elif int(str(temperature_celsius)[:2]) >=16 and int(str(temperature_celsius)[:2])<=24:
                    
                    self.app.today_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/warm.png'))
                
                
                
                elif int(str(temperature_celsius)[:2]) >=0 and int(str(temperature_celsius)[:2])<=15:
                    self.app.today_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/cold.png'))
                
                
                elif int(str(temperature_celsius)[:2]) < 0:
                    self.app.today_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/frosty.png'))
                
                
                
                
                tz_id = today_main_data['location']['tz_id']
                self.app.location_label.setText(tz_id)
                
                
                wind_km = today_main_data['current']['wind_mph']
                self.app.today_wind_km.setText(str(wind_km))
                
                
                current_date = today_main_data['location']['localtime']
                self.app.today_date.setText(current_date)
                
                
                today_weather_status = today_main_data['current']['condition']['text']
                self.app.today_weather_status.setText(today_weather_status)
                
                self.app.today_date.setText(str(datetime.today())[:16])
                
                
                
            #Tomorrow area ----------------------------------------------
            
                tomorrow_day_date = datetime.today() + timedelta(days=1)
                self.app.tomorrow_day.setText(tomorrow_day_date.strftime("%d %B"))
                
                
                tomorrow_degree = tomorrow_main_data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
                self.app.hide_label.setText(f'{str(tomorrow_degree)[:2]}° C')
                #print(str(tomorrow_degre)[:2])
                
                if int(str(tomorrow_degree)[:2]) == 25 or int(str(tomorrow_degree)[:2])>25:
                    
                    self.app.tomorrow_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/hot.png'))
                
                
                elif int(str(tomorrow_degree)[:2]) >=16 and int(str(tomorrow_degree)[:2])<=24:
                    
                    self.app.tomorrow_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/warm.png'))
                
                
                
                elif int(str(tomorrow_degree)[:2]) >=0 and int(str(tomorrow_degree)[:2])<=15:
                    self.app.tomorrow_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/cold.png'))
                
                
                elif int(str(tomorrow_degree)[:2]) < 0:
                    self.app.tomorrow_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/frosty.png'))
                
                
                tomorrow_wind  = tomorrow_main_data['forecast']['forecastday'][0]['hour'][0]['wind_mph']
                self.app.tomorrow_wind_km.setText(f'{tomorrow_wind} km/h')
                
                
                sun_rise = tomorrow_main_data['forecast']['forecastday'][0]['astro']['sunrise']
                self.app.sun_rise_label.setText(sun_rise)
                
                
                sun_set = tomorrow_main_data['forecast']['forecastday'][0]['astro']['sunset']
                self.app.sunset_label.setText(sun_set)
                
                tomorrow_w_status = tomorrow_main_data['forecast']['forecastday'][0]['day']['condition']['text']
                self.app.tomorrow_weather_status.setText(tomorrow_w_status)
                self.app.goto_button.clicked.connect(self.goto_func)
                self.app.about_button.clicked.connect(self.about_s)
                self.about_sc = About_screen()
            
            def goto_func(self):
                goto_date = self.app.dateEdit.text().replace('/','-')
                self.tarix = datetime.strptime(f'{goto_date}', "%Y-%m-%d")
                self.goto_date_for_day_d = self.tarix.strftime("%d %B")
                self.app.tomorrow_day.setText(self.goto_date_for_day_d)
                selected_date = self.app.dateEdit.date()
                tomorrow = QDate.currentDate().addDays(1)
                if selected_date != tomorrow:
                    self.app.gizli_label.setText(goto_date)
                    self.app.gizli_label.setStyleSheet('background-color:#67A5BB;\ncolor:white;')
                else:
                    self.app.gizli_label.setText('')
                    self.app.gizli_label.setStyleSheet('background-color:transparent;')
                

                goto_main_data = history_data(history_date=goto_date)
                tomorrow_day_date = datetime.today() + timedelta(days=1)
                
                
                tomorrow_degree = goto_main_data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
                self.app.hide_label.setText(f'{str(tomorrow_degree)[:2]}° C')
                
                if int(str(tomorrow_degree)[:2]) == 25 or int(str(tomorrow_degree)[:2])>25:
                    
                    self.app.tomorrow_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/hot.png'))
                
                
                elif int(str(tomorrow_degree)[:2]) >=16 and int(str(tomorrow_degree)[:2])<=24:
                    
                    self.app.tomorrow_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/warm.png'))
                
                
                
                elif int(str(tomorrow_degree)[:2]) >=0 and int(str(tomorrow_degree)[:2])<=15:
                    self.app.tomorrow_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/cold.png'))
                
                
                elif int(str(tomorrow_degree)[:2]) < 0:
                    self.app.tomorrow_png.setPixmap(QtGui.QPixmap(':/newPrefix/weather_pngs/frosty.png'))
                
                
                tomorrow_wind  = goto_main_data['forecast']['forecastday'][0]['hour'][0]['wind_mph']
                self.app.tomorrow_wind_km.setText(f'{tomorrow_wind} km/h')
                
                
                sun_rise = goto_main_data['forecast']['forecastday'][0]['astro']['sunrise']
                self.app.sun_rise_label.setText(sun_rise)
                
                
                sun_set = goto_main_data['forecast']['forecastday'][0]['astro']['sunset']
                self.app.sunset_label.setText(sun_set)
                
                tomorrow_w_status = goto_main_data['forecast']['forecastday'][0]['day']['condition']['text']
                self.app.tomorrow_weather_status.setText(tomorrow_w_status)
                self.app.goto_button.clicked.connect(self.goto_func)
                
                
                
            def about_s(self):
                self.about_sc.show()
                
            
                
                
        
    app = QApplication([])
    ekran = WeatherApp(today_main_data)
    ekran.show()
    app.exec_()

except Exception as a:
    ctypes.windll.user32.MessageBoxW(0,f'Program has stopped. Please try again.\n\nError message : {a}', "Error", 0)