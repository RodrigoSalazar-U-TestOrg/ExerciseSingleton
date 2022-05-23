class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class WindowRenderer(metaclass=SingletonMeta):
    def __init__(self):
        self.pixels = []

    def resize_window(self, size_x, size_y):
        self.pixels = [["*" for x in range(size_x)] for y in range(size_y)]

    def display(self):
        for row in self.pixels:
            for p in row:
                print(p, end=" ")
            print()


class TextBox():
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def render(self):
        WindowRenderer().pixels[self.y][self.x] = "T"

    def __str__(self):
        return "TextBox at ({x},{y}): {text}".format(x=self.x, y=self.y, text=self.text)


class InputBox():
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def render(self):
        WindowRenderer().pixels[self.y][self.x] = "I"

    def __str__(self):
        return "InputBox at ({x},{y}): {text}".format(x=self.x, y=self.y, text=self.text)


if __name__ == '__main__':
    WindowRenderer().resize_window(10,10)
    tb = TextBox(1, 5, "Sample text")
    ib = InputBox(8, 8, "Sample input")
    tb.render()
    ib.render()
    WindowRenderer().display()
