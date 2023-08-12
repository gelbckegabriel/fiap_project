def say_my_name(name, lastname="Gelbcke"):
    print(f"Your name is {lastname}... {name} {lastname}!", end="\n\n")


def options_question():
    return input(
            "Which action you wish to perform ?\n" +
            "<I> - Insert an User. \n" +
            "<S> - Search an User. \n" +
            "<D> - Delete an User. \n" +
            "<L> - List all Users. \n" +
            "Answer: "
            ).upper()


