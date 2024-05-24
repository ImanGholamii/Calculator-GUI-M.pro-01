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
                          '7', '8', '9', '*',
                          '0', '.', '/', '=')
        button_grid = GridLayout(cols=4, size_hint_y=0.5)
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))
        clear_button = Button(text = 'Clear', size_hint_y=None, height=75)
        
        def print_button_text(instance):
            """ takes an instance (a button instance) as an argument.
            It appends the text of the pressed button (instance.text) to the output_label text,
            when a button is pressed. """    
            output_lable.text += instance.text
            
        for button in button_grid.children[1:]: #  iterate over all buttons in the button_grid except the first one (which is the clear button). 
            button.bind(on_press=print_button_text) # We bind the print_button_text function to the on_press event of each button. #  iterate over all buttons in the button_grid except the first one (which is the clear button). 
        
        def resize_lable_text(lable, new_height):
            lable.fontsize = 0.5*lable.height
            
        output_lable.bind(height=resize_lable_text)
        
        def evaluate_resulte(instance):
            try:
                output_lable.text = str(eval(output_lable.text))
            except SyntaxError:
                output_lable.text = 'Python Syntax Error!'
        button_grid.children[0].bind(on_press=evaluate_resulte)
        
        def clear_label(instance):
            output_lable.text = " "        
        
        clear_button.bind(on_press=clear_label)    
        
        root_widget.add_widget(output_lable)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_button)
        return root_widget
MyApp().run()