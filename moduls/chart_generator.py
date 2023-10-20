import matplotlib.pyplot as plt


def bar_chart_generator(labels, values):
    figure, coordinates = plt.subplots()
    coordinates.bar(labels, values)
    plt.show()


def pie_chart_generator(labels, values):
    figure, coordinates = plt.subplots()
    coordinates.pie(values, labels=labels)
    coordinates.axis('equal')
    plt.show()


if __name__ == '__main__':
    sections = ['Section A', 'Section B', 'Section C']
    values_section = [200, 600, 450]
    bar_chart_generator(sections, values_section)
    pie_chart_generator(sections, values_section)
