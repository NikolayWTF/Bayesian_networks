class SimpleRectangle:
    def __init__(self, x, y, x_size, y_size, name):
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.name = name
        self.center_y = y + y_size/2
        self.center_x = x + x_size/2
        self.down_y = (y + y_size)

    def draw_rectangle(self, name_positive, name_negative, positive_probability, negative_probability, canvas):
        x, y, x_size, y_size, name = self.x, self.y, self.x_size, self.y_size, self.name

        canvas.create_rectangle(x, y, x + x_size, y + y_size)
        canvas.create_line(x, y + y_size / 3, x + x_size, y + y_size / 3)
        canvas.create_line(x, y + 2 * y_size / 3, x + x_size, y + 2 * y_size / 3)
        canvas.create_line(x + 2 * x_size / 3, y + y_size / 3, x + 2 * x_size / 3, y + y_size)
        canvas.create_text(x + x_size / 2, y + y_size / 6, text=name)
        canvas.create_text(x + x_size / 3, y + y_size / 2, text=name_positive)
        canvas.create_text(x + x_size / 3, y + 5 * y_size / 6, text=name_negative)
        canvas.create_rectangle(x+2*x_size/3, y + y_size / 3, x+x_size, y+2*y_size/3, fill="white")
        canvas.create_rectangle(x + 2 * x_size / 3, y + 2*y_size/3, x + x_size, y + y_size, fill="white")
        canvas.create_text(x + 5 * x_size / 6, y + y_size / 2, text=positive_probability)
        canvas.create_text(x + 5 * x_size / 6, y + 5 * y_size / 6, text=negative_probability)


class Edge:
    def __init__(self, first: SimpleRectangle, second: SimpleRectangle, canvas):
        self.first_rectangle = first
        self.second_rectangle = second
        self.draw_Edge(canvas)

    def draw_Edge(self, canvas):
        if self.first_rectangle.center_y <= self.second_rectangle.center_y:
            canvas.create_line(self.first_rectangle.center_x, self.first_rectangle.down_y,
                               self.second_rectangle.center_x, self.second_rectangle.y, arrow="last")
        else:
            canvas.create_line(self.second_rectangle.center_x, self.second_rectangle.down_y,
                               self.first_rectangle.center_x, self.first_rectangle.y, arrow="last")
