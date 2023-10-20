import console_views.views as view
import csv


def read_file(path):
    with open(path, 'r', encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            list_convert_in_dict = {key: value for key, value in iterable}

            data.append(list_convert_in_dict)
        return data


def search_country(check_country="pais", data=None):
    if data is None:
        data = []

    for i in data:
        if i.get("Country/Territory").lower() == check_country:
            dic = {
                "2022": int(i["2022 Population"]),
                "2020": int(i["2020 Population"]),
                "2015": int(i["2015 Population"]),
                "2010": int(i["2010 Population"]),
                "2000": int(i["2000 Population"]),
                "1990": int(i["1990 Population"]),
                "1980": int(i["1980 Population"]),
                "1970": int(i["1970 Population"]),
            }
            return dic


if __name__ == '__main__':
    view.show_title("this file is just the support for others files")
