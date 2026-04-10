from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from foreman_engine import foreman_engine

class ForemanOverlay(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="FOREMAN v2.0", size_hint_y=0.2))
        
        # The input where you talk to the Foreman
        self.query_input = TextInput(hint_text="Ask the Vault...", multiline=False, size_hint_y=0.4)
        self.add_widget(self.query_input)
        
        # The button to trigger the Librarian/Bridge
        self.run_btn = Button(text="Run Logic", size_hint_y=0.4)
        self.run_btn.bind(on_press=self.execute_logic)
        self.add_widget(self.run_btn)
        
        # The output label
        self.output_label = Label(text="Standing by...", size_hint_y=0.2)
        self.add_widget(self.output_label)

    def execute_logic(self, instance):
        query = self.query_input.text
        if query:
            result = foreman_engine(query)
            self.output_label.text = "Result in Logs/Vault"
            print(result)

class ForemanApp(App):
    def build(self):
        return ForemanOverlay()

if __name__ == '__main__':
    ForemanApp().run()
