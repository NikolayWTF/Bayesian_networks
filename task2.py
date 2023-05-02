from tkinter import *
from tkinter import ttk
from visualization import SimpleRectangle, Edge

# Вероятность, что дом ограбит вор = 0.0002. Вероятность землетрясения = 0.01
# Тревога может сработать не только на вора, но и на землетрясение, со следующей вероятностью
#         |        Вор+        |        Вор-      |
#         | Земл.+  |  Земл.-  |  Земл.+ | Земл.- |
# Тревога+|    1    |    1     |   0.1   |    0   |
# Тревога-|    0    |    0     |   0.9   |    1   |

# 1. С какой вероятностью в дом пробрался вор, если тревога сработала?
# 2. По радио сообщили, что произошло землетрясение. Какова теперь вероятность, что в дом попал вор?
#   (Если землетрясения нет, то радио не сообщит о нём, а если оно случилось - то сообщат с вероятностью = 0.5)


thief = {"+": 0.0002,
         "-": 0.9998}

earthquake = {"+": 0.01,
              "-": 0.99}

radio = {"+": {"+": 1,
               "-": 0},
         "-": {"+": 0.5,
               "-": 0.5}}

# Тревога | Вор | Землетрясение
alarm = {"+": {"+": {"+": 1,
                     "-": 1},
               "-": {"+": 0.1,
                     "-": 0}},
         "-": {"+": {"+": 0,
                     "-": 0},
               "-": {"+": 0.9,
                     "-": 1}}}


def Bayes_formula(radio_exist):
    thief_rectangle.positive_probability = thief["+"]
    thief_rectangle.negative_probability = thief["-"]
    earthquake_rectangle.positive_probability = earthquake["+"]
    earthquake_rectangle.negative_probability = earthquake["-"]
    if radio_exist:

        if radio_rectangle.positive_probability == 1:
            true_or_false = "+"
        else:
            true_or_false = "-"
        earthquake_rectangle.positive_probability = round(radio[true_or_false]["+"]
                                                          * earthquake_rectangle.positive_probability / (
                                                                  radio[true_or_false]["+"]
                                                                  * earthquake_rectangle.positive_probability
                                                                  + radio[true_or_false]["-"]
                                                                  * earthquake_rectangle.negative_probability))
        earthquake_rectangle.negative_probability = round(1 - radio[true_or_false]["+"]
                                                          * earthquake_rectangle.positive_probability / (
                                                                  radio[true_or_false]["+"]
                                                                  * earthquake_rectangle.positive_probability
                                                                  + radio[true_or_false]["-"]
                                                                  * earthquake_rectangle.negative_probability))

    if alarm_rectangle.positive_probability == 1:
        true_or_false = "+"
    else:
        true_or_false = "-"
    probability_observable_event = alarm[true_or_false]["+"]["+"] * thief_rectangle.positive_probability \
                                   * earthquake_rectangle.positive_probability + alarm[true_or_false]['+']["-"] \
                                   * thief_rectangle.positive_probability * earthquake_rectangle.negative_probability \
                                   + alarm[true_or_false]["-"]["+"] * thief_rectangle.negative_probability \
                                   * earthquake_rectangle.positive_probability \
                                   + alarm[true_or_false]["-"]["-"] * thief_rectangle.negative_probability \
                                   * earthquake_rectangle.negative_probability
    probability_thief = alarm[true_or_false]["+"]["+"] * thief_rectangle.positive_probability \
                        * earthquake_rectangle.positive_probability \
                        + alarm[true_or_false]["+"]["-"] * thief_rectangle.positive_probability \
                        * earthquake_rectangle.negative_probability \
                        / probability_observable_event
    probability_earthquake = alarm[true_or_false]["+"]["+"] * thief_rectangle.positive_probability \
                             * earthquake_rectangle.positive_probability + alarm[true_or_false]["-"]["+"] \
                             * thief_rectangle.negative_probability * earthquake_rectangle.positive_probability \
                             / probability_observable_event

    thief_rectangle.positive_probability = round(probability_thief, 2)
    thief_rectangle.negative_probability = round(1 - probability_thief, 2)
    earthquake_rectangle.positive_probability = round(probability_earthquake, 2)
    earthquake_rectangle.negative_probability = round(1 - probability_earthquake, 2)
    thief_rectangle.draw_rectangle(canvas)
    earthquake_rectangle.draw_rectangle(canvas)


def click_button(obj: SimpleRectangle, on_or_off):
    if on_or_off:
        obj.positive_probability = 1
        obj.negative_probability = 0
    else:
        obj.positive_probability = 0
        obj.negative_probability = 1
    obj.draw_rectangle(canvas)
    Bayes_formula(check_radio_exist.is_radio_exist)


def draw_button(obj: SimpleRectangle, name_positive, name_negative):
    x, y, x_size, y_size = obj.x, obj.y, obj.x_size, obj.y_size
    btn_positive = ttk.Button(canvas, text=name_positive, command=lambda: click_button(obj, True))
    btn_negative = ttk.Button(canvas, text=name_negative, command=lambda: click_button(obj, False))
    btn_positive.place(x=x + 1, y=(y + y_size / 3) + 1, height=y_size / 3 - 1, width=2 * x_size / 3 - 1)
    btn_negative.place(x=x + 1, y=(y + 2 * y_size / 3) + 1, height=y_size / 3 - 1, width=2 * x_size / 3 - 1)


def add_radio():
    radio_rectangle.draw_rectangle(canvas)
    draw_button(radio_rectangle, "+", "-")
    Edge(earthquake_rectangle, radio_rectangle, canvas)
    btn_add_radio.destroy()
    check_radio_exist.turn_on_radio()


class Radio:
    def __init__(self):
        self.is_radio_exist = False

    def turn_on_radio(self):
        self.is_radio_exist = True


root = Tk()
canvas = Canvas(root, width="1024", height="512")  # Создаю окно
canvas.pack()

check_radio_exist = Radio()

btn_add_radio = ttk.Button(canvas, text="Добавить радио", command=add_radio)
btn_add_radio.place(x=860, y=20, height=50, width=120)

thief_rectangle = SimpleRectangle(14, 60, 180, 120, "Вор", "+", "-", "?", "?")
thief_rectangle.draw_rectangle(canvas)

earthquake_rectangle = SimpleRectangle(442, 60, 180, 120, "Землетрясение", "+", "-", "?", "?")
earthquake_rectangle.draw_rectangle(canvas)

alarm_rectangle = SimpleRectangle(227, 260, 180, 120, "Тревога", "+", "-", "0", "1")
alarm_rectangle.draw_rectangle(canvas)

radio_rectangle = SimpleRectangle(672, 260, 180, 120, "Радио", "+", "-", "0", "1")

draw_button(alarm_rectangle, "+", "-")

thief_edge_alarm = Edge(thief_rectangle, alarm_rectangle, canvas)
earthquake_edge_alarm = Edge(earthquake_rectangle, alarm_rectangle, canvas)

root.mainloop()
