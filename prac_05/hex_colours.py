"""
Hex Color Lookup
Estimate: 15 minutes
Actual:   10 minutes
"""

# Constant dictionary of color names and their corresponding hexadecimal codes
COLOR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7",
                "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
                "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4"}


def main():
    print("Welcome to the Hex Color Lookup!")

    color_name = input("Enter a color name (or press Enter to quit): ").lower()
    while color_name:  # Continue until the input is blank
        code = COLOR_CODES.get(color_name)  # Corrected from COLOR_CODE to COLOR_CODES
        if code:  # Check if the code was found
            print(code)
        else:
            print("Color not found.")
        color_name = input("Enter a color name (or press Enter to quit): ").lower()


main()
