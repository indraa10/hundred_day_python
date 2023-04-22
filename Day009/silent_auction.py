import click


def clear_screen():
    click.clear()
    print("something")
    click.clear()


if __name__ == "__main__":
    clear_screen()
