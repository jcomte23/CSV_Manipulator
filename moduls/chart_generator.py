import matplotlib.pyplot as plt


def bar_chart_generator(path_image, labels, values):
    figure, coordinates = plt.subplots()
    coordinates.bar(labels, values)
    plt.savefig(path_image)
    plt.close()


def pie_chart_generator(path_image,labels, values):
    figure, coordinates = plt.subplots()
    coordinates.pie(values, labels=labels)
    coordinates.axis('equal')
    plt.savefig(path_image)
    plt.close()


if __name__ == '__main__':
    sections = ['Section A', 'Section B', 'Section C']
    values_section = [200, 600, 450]
    bar_chart_generator('../img/example_bar_chart.png', sections, values_section)
    pie_chart_generator('../img/example_pie_chart.png',sections, values_section)
