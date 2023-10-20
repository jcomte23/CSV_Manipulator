INTERNAL_SPACING_TITLE = 18
INTERNAL_SPACING_ERROR = 5


def show_title(principal_title):
    title_size = len(principal_title)

    interface_size = title_size + (INTERNAL_SPACING_TITLE * 2)
    print(interface_size)

    print()
    print("=" * interface_size)
    print("|" + " " * (INTERNAL_SPACING_TITLE - 1) + principal_title + " " * (INTERNAL_SPACING_TITLE - 1) + "|")
    print("=" * interface_size)


def show_error(error):
    principal_title = f"ERROR => {error}"
    title_size = len(principal_title)

    interface_size = title_size + (INTERNAL_SPACING_ERROR * 2)
    print(interface_size)

    print()
    print("!" * interface_size)
    print("|" + " " * (INTERNAL_SPACING_ERROR - 1) + principal_title + " " * (INTERNAL_SPACING_ERROR - 1) + "|")
    print("!" * interface_size)
