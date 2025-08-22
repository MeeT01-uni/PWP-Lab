from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class TextInputApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.text_input = TextInput(
            hint_text='Type something here...', 
            multiline=False,
            font_size=24
        )
        self.layout.add_widget(self.text_input)

        self.button = Button(
            text='Display Text',
            size_hint=(1, 0.2),
            font_size=32
        )
        self.button.bind(on_press=self.display_text)
        self.layout.add_widget(self.button)
        
        self.display_label = Label(
            text='',
            font_size=30
        )
        self.layout.add_widget(self.display_label)

        return self.layout

    def display_text(self, instance):
        self.display_label.text = self.text_input.text

if __name__ == '__main__':
    TextInputApp().run()
