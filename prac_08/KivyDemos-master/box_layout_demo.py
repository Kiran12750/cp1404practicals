from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

def handle_clear(self):
    self.root.ids.input_name.text = ''  # Clear input text
    self.root.ids.output_label.text = ''  # Clear output label


BoxLayoutDemo().run()
