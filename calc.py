from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5), #width and height btw 0 and 1 
                      pos_hint={'center_x': .5, 'center_y': .5}) #centering on x and y axis

        return label

if __name__ == '__main__': 
    app = MainApp()
    app.run() ##this will run the app
