import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')

from kivy_garden.mapview import MapView

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        return mapview

MapViewApp().run()



class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return label

if __name__ == '__main__':
#    app = MainApp()
    app = MapViewApp()
    app.run()



