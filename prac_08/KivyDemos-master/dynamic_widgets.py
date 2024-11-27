from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class DynamicLabelsApp(App):
    def build(self):
        # Create a BoxLayout with a vertical orientation
        box = BoxLayout(orientation='vertical')

        # List of names to dynamically create labels for
        names = ["Alice", "Bob", "Charlie", "David"]

        # Loop through the list of names and create a Label for each name
        for name in names:
            label = Label(text=name)
            box.add_widget(label)  # Add the label to the layout

        return box

# Run the app
if __name__ == "__main__":
    DynamicLabelsApp().run()
