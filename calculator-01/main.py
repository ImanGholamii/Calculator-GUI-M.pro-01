from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        root_widget = BoxLayout(orientation='vertical')
        output_lable = Label(size_hint_y=0.5, font_size=50)
        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')
        button_grid = GridLayout(cols=4, size_hint_y=1.5)
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))
        clear_button = Button(text = 'Clear', size_hint_y=None, height=85)
        
        def print_button_text(instance):
            """ takes an instance (a button instance) as an argument.
            It appends the text of the pressed button (instance.text) to the output_label text,
            when a button is pressed. """    
            output_lable.text += instance.text
        
            