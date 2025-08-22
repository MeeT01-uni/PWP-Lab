from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CounterApp(App):
    def build(self):
        self.counter = 0
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.label = Label(text=str(self.counter), font_size=48)
        layout.add_widget(self.label)

        btn = Button(text='Increment', size_hint=(1, 0.2), font_size=32)
        btn.bind(on_press=self.increment_counter)
        layout.add_widget(btn)

        return layout

    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = str(self.counter)

if __name__ == '__main__':
    CounterApp().run()
