import kivy
from kivy.app import App
from kivy_garden.mapview import MapView

kivy.require('1.11.1')

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        return mapview

def main():
    mapview = MapViewApp()
    print(mapview.get_running_app())
    print(mapview.name)
    print(mapview.get_application_name())
    print(mapview.get_application_name())
    
    mapview.run()
   


main()






