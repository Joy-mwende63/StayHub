# helpers.py
def validate_input(prompt, expected_type=int):
    """Helper function to validate user input."""
    while True:
        try:
            value = expected_type(input(prompt))
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {expected_type.__name__}.")
