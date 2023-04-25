from tkinter import *


class simple_rectangle:
    def __init__(self, x, y, x_size, y_size, name):
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.name = name
        self.center_y = y + y_size/2
        self.center_x = x + x_size/2
        self.down_y = (y + y_size)

        # self.name_positive = name_positive
        # self.name_negative = name_negative
        # self.positive_probability = positive_probability
        # self.negative_probability = negative_probability

    def draw_rectangle(self, name_positive, name_negative, positive_probability, negative_probability):
        x, y, x_size, y_size, name = self.x, self.y, self.x_size, self.y_size, self.name
        canvas.create_rectangle(x, y, x + x_size, y + y_size)
        canvas.create_line(x, y + y_size / 3, x + x_size, y + y_size / 3)
        canvas.create_line(x, y + 2 * y_size / 3, x + x_size, y + 2 * y_size / 3)
        canvas.create_line(x + 2 * x_size / 3, y + y_size / 3, x + 2 * x_size / 3, y + y_size)
        canvas.create_text(x + x_size / 2, y + y_size / 6, text=name)
        canvas.create_text(x + x_size / 3, y + y_size / 2, text=name_positive)
        canvas.create_text(x + x_size / 3, y + 5 * y_size / 6, text=name_negative)
        canvas.create_text(x + 5 * x_size / 6, y + y_size / 2, text=positive_probability)
        canvas.create_text(x + 5 * x_size / 6, y + 5 * y_size / 6, text=negative_probability)


class Edge:
    def __init__(self, first: simple_rectangle, second: simple_rectangle):
        self.first_rectangle = first
        self.second_rectangle = second
        self.draw_Edge()

    def draw_Edge(self):
        if self.first_rectangle.center_y <= self.second_rectangle.center_y:
            canvas.create_line(self.first_rectangle.center_x, self.first_rectangle.down_y,
                               self.second_rectangle.center_x, self.second_rectangle.y, arrow="last")
        else:
            canvas.create_line(self.second_rectangle.center_x, self.second_rectangle.down_y,
                               self.first_rectangle.center_x, self.first_rectangle.y, arrow="last")


root = Tk()
canvas = Canvas(root, width="1024", height="512")  # Создаю окно
canvas.pack()

disease_rectangle = simple_rectangle(437, 60, 150, 120, "Болезнь")
disease_rectangle.draw_rectangle("Болен", "Здоров", 0.001, 0.999)

test_rectangle = simple_rectangle(437, 220, 150, 120, "Тест")
test_rectangle.draw_rectangle("Положительный", "Отрицательный", 0.001, 0.999)

disease_edge_test = Edge(disease_rectangle, test_rectangle)

root.mainloop()
