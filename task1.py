from tkinter import *
from tkinter import ttk
from visualization import SimpleRectangle, Edge

# Шанс заразиться редкой болезнью = 0.001. Тест на выявление болезни
# ошибается в 1 случае из 100. Результаты теста - наблюдаемое событие.
# С какой вероятностью человек болен, если тест положительный / отрицательный?

disease = {"Болен": 0.001,
           "Здоров": 0.999}

test = {"Положительный": {"Болен": 0.99,
                          "Здоров": 0.01},
        "Отрицательный": {"Болен": 0.01,
                          "Здоров": 0.99}
        }


def Bayes_formula(true_or_false):
    probability_observable_event = test[true_or_false]["Болен"] * disease["Болен"] + test[true_or_false]["Здоров"] * \
                                   disease["Здоров"]
    probability = test[true_or_false]["Болен"] * disease["Болен"] / probability_observable_event
    if true_or_false == "Положительный":
        test_rectangle.draw_rectangle("Положительный", "Отрицательный", "1", "0", canvas)

    else:
        test_rectangle.draw_rectangle("Положительный", "Отрицательный", "0", "1", canvas)

    disease_rectangle.draw_rectangle("Болен", "Здоров", round(probability, 2), 1 - round(probability, 2), canvas)


def draw_button(x, y, x_size, y_size, name_positive, name_negative):
    btn_positive = ttk.Button(canvas, text=name_positive, command=lambda: Bayes_formula(name_positive))
    btn_negative = ttk.Button(canvas, text=name_negative, command=lambda: Bayes_formula(name_negative))
    btn_positive.place(x=x + 1, y=(y + y_size / 3) + 1, height=y_size / 3 - 1, width=2 * x_size / 3 - 1)
    btn_negative.place(x=x + 1, y=(y + 2 * y_size / 3) + 1, height=y_size / 3 - 1, width=2 * x_size / 3 - 1)


root = Tk()
canvas = Canvas(root, width="1024", height="512")  # Создаю окно
canvas.pack()

disease_rectangle = SimpleRectangle(427, 60, 180, 120, "Болезнь")
disease_rectangle.draw_rectangle("Болен", "Здоров", "?", "?", canvas)

test_rectangle = SimpleRectangle(427, 220, 180, 120, "Тест")
test_rectangle.draw_rectangle("Положительный", "Отрицательный", "?", "?", canvas)
draw_button(test_rectangle.x, test_rectangle.y, test_rectangle.x_size, test_rectangle.y_size, "Положительный",
            "Отрицательный")

disease_edge_test = Edge(disease_rectangle, test_rectangle, canvas)

root.mainloop()
