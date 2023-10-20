import console_views.views as view
import moduls.chart_generator as graphics
import moduls.manager_csv as manager_csv


def graphic_population_country(data):
    try:
        country = input("Enter the country name to search for its population=> ").lower().strip()
        dictionary = manager_csv.search_country(country, data)
        if dictionary:
            labels = list(dictionary.keys())
            values = list(dictionary.values())
            graphics.bar_chart_generator(labels, values)
        else:
            view.show_title("The requested country was not found")
    except ValueError as error:
        view.show_error(error.args[0])


view.show_title("Welcome to the CSV manipulator")

while True:
    view.show_menu()
    option = input("Enter the option ->").upper().strip()
    if option == "A":
        data_csv = manager_csv.read_file('./archive/data.csv')
        graphic_population_country(data_csv)
    elif option == "B":
        view.show_title("Good bye")
        exit()
    else:
        view.show_error("Option Invalid")
