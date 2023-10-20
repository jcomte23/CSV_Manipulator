INTERNAL_SPACING = 10


def show_title(principal_title):
    # principal_title = "Welcome to the CSV manipulator"
    title_size = len(principal_title)

    interface_size = title_size + (INTERNAL_SPACING * 2)
    print(interface_size)

    print()
    print("=" * interface_size)
    print("|" + " " * (INTERNAL_SPACING - 1) + principal_title + " " * (INTERNAL_SPACING - 1) + "|")
    print("=" * interface_size)
