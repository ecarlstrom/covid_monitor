# GUI class requirements and widgets
import kivy.utils
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition,CardTransition
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from bar import Bar

# backend/data modules
from datetime import date, time
from covid import Covid

#initialize screen settings (change this later if desired)
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '900')
Config.set('graphics', 'borderless', '1')
Config.write()

#############################################################

class ImageButton(ButtonBehavior, Image):
    pass

class LabelButton(ButtonBehavior, Label):
    pass

class Spacer(Label):
    pass

class Dashboard(Screen):
    pass

class BoxButton(ButtonBehavior, BoxLayout):
    pass


class LocationBarItem(BoxLayout):
    def __init__(self,**kwargs):
        self.orientation = "horizontal"
        self.size_hint = (0.74, 1)
        super().__init__()

        bar_item = BoxButton(orientation = "vertical", size_hint = (0.01, 0.9))
        _bar = Bar(size_hint = (1.2, 0.9), value = kwargs['cases'])
        _loc = Label(size_hint = (1, 0.1), text = kwargs['loc'], font_size = "10sp", color = kivy.utils.get_color_from_hex("#47546e"))
        bar_item.add_widget(_bar)
        bar_item.add_widget(_loc)
        self.add_widget(bar_item)

GUI = Builder.load_file("main.kv")

class Main(App):
        
        def build(self):
            self.today = date.today()
            self.date = self.today.strftime("%B %d, %Y")
            return GUI
        
        def on_start(self):
            LabelBase.register(name = "myriad_pro_reg", fn_regular = "MYRIADPRO-REGULAR.OTF")
            LabelBase.register(name = "d_din_reg", fn_regular = "d-din.regular.ttf")
            LabelBase.register(name = "roboto-medium", fn_regular = "Roboto-Medium.ttf")
            LabelBase.register(name = "roboto-thin", fn_regular = "Roboto-Thin.ttf")
            LabelBase.register(name = "bistecca", fn_regular = "Bistecca.ttf")
            LabelBase.register(name = "teko-reg", fn_regular = "Teko-Regular.ttf")
            LabelBase.register(name = "barlow-reg", fn_regular = "BarlowSemiCondensed-Regular.ttf")
            LabelBase.register(name = "barlow-bold", fn_regular = "BarlowSemiCondensed-SemiBold.ttf")

            self.root.ids['dashboard'].ids['date_label_id'].text = self.date
            ## maybe add the current time under the date field?
            case_plot = self.root.ids['dashboard'].ids['case_plot']


            self.covid = Covid(source = "worldometers")

            ## manual dictionary of countries on graph plot for now
            ## will work on pulling a dictionary from API and also searching for abbreviations
            chart_countries = {
                "CO": "Colombia",
                "MX": "Mexico",
                "ES": "Spain",
                "CL": "Chile",
                "AR": "Argentina",
                "BO": "Bolivia",
                "PA": "Panama",
                "CR": "Costa Rica",
                "HT": "Haiti",
                "UK": "UK",
                "FR": "France",
                "IT": "Italy",
                "PT": "Portugal",
                "NO": "Norway",
                "GR": "Greece",
                "RS": "Serbia",
                "SA": "Saudi Arabia",
                "IN": "India",
                "BD": "Bangladesh",
                "SG": "Singapore",
                "PK": "Pakistan",
                "TR": "Turkey",
                "IQ": "Iraq",
                "IL": "Israel",
                "US": "USA",
                "CA": "Canada",
                "CN": "China",
                "JP": "Japan",
                "NE": "Nigeria",
                "GH": "Ghana",
                "ZM": "Zambia",
                "KE": "Kenya",
                "EG": "Egypt",
                "AU": "Australia",
                "GN": "Guinea",
            }
            # print(self.covid.list_countries())
            temp_json = self.covid.get_status_by_country_name("USA")
            CO_cases = temp_json['confirmed']

            for key, value in chart_countries.items():
                locations_case = self.covid.get_status_by_country_name(value)
                normalized_value = int((locations_case['confirmed'] / CO_cases) * 100)
                location_bar_item = LocationBarItem(loc = str(key), cases = normalized_value)
                case_plot.add_widget(location_bar_item)

        def close(self):
            quit()
        
        def minimize(self):
            Window.minimize()
        
        def process_data_search(self):
            _location = (self.root.ids['dashboard'].ids['search_location'].text).strip()
            err = "This location cannot be found!"
            try:
                _data = self.covid.get_status_by_country_name(_location)
                # this variable will be the percentage of total confirmed cases that have recovered
                recovery_rate = (_data['recovered'] / _data['confirmed']) * 100
                # print(_data)

                self.root.ids['dashboard'].ids['confirmed_cases'].text = (f"{(_data['confirmed']):,d}")
                self.root.ids['dashboard'].ids['confirmed_cases_delta'].text = (f"{(_data['new_cases']):,d}")
                self.root.ids['dashboard'].ids['confirmed_deaths'].text = (f"{(_data['deaths']):,d}")
                self.root.ids['dashboard'].ids['confirmed_deaths_delta'].text = (f"{(_data['new_deaths']):,d}")
                self.root.ids['dashboard'].ids['recovered_cases'].text = (f"{(_data['recovered']):,d}")
                self.root.ids['dashboard'].ids['active_cases'].text = (f"{(_data['active']):,d}")
                self.root.ids['dashboard'].ids['recovery_rate_id'].text = str(int(recovery_rate)) + "% cases\nrecovered"
                self.root.ids['dashboard'].ids['critical_cases'].text = str((f"{(_data['critical']):,d}")) + " cases in \ncritical condition"
                self.root.ids['dashboard'].ids['error_msg'].text = ""
            except:
                self.root.ids['dashboard'].ids['error_msg'].text = err
                print("Location does not exist!")


Main().run()
