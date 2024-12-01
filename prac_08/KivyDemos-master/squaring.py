from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class SquareApp(App):
    def build(self):
        # Load the kv file to build the GUI
        return BoxLayout()

    def calculate_square(self):
        # Get the value entered in the TextInput widget
        input_text = self.root.ids.input_number.text

        try:
            # Convert the input text to a number
            number = float(input_text)

            # Calculate the square of the number
            squared_value = number ** 2

            # Update the result label with the squared value
            self.root.ids.result_label.text = f"Squared Value: {squared_value}"
        except ValueError:
            # If the input is not a valid number, show an error message
            self.root.ids.result_label.text = "Invalid input. Please enter a valid number."

# Run the app
if __name__ == "__main__":
    SquareApp().run()
