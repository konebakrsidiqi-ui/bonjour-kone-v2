from kivy.app import App
from kivy.uix.label import Label

class BonjourApp(App):
    def build(self):
        return Label(text="Bonjour Aboubacar !")

BonjourApp().run()
