class ProgrammingLanguage:

    def __init__(self):
        self.title = title
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.islower() == "dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First Appeared in {}".format(self.title, self.typing, self.reflection, self.year)