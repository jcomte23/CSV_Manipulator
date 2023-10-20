import Console_views.views as view

view.show_title("Welcome to the CSV manipulator")

try:
    number = int(input("Enter"))
except ValueError as error:
    view.show_error(error.args[0])
