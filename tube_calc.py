from tubes import Tubes
import tkinter

answers = {}


class TubeCalc:
    def __init__(self, root):
        self.root = root

    def input_mass(self):
        questions = [
            "Введите принятое значение расхода воды (кг/час): ",
            "Введите принятое значение расхода тех. пара (кг/час): ",
            'Введите принятое значение расхода чистого пара (кг/час): ',
            "Введите принятное значение расхода продукта (кг/час): ",
            "Введите принятное значение расхода воздуха (м3/час): "
        ]
        line = tkinter.Label(self.root, text='-----')
        line.grid(column=0, row=10, columnspan=2, padx=5, pady=5)

        for i, quest in enumerate(questions):
            question = tkinter.Label(self.root, text=quest)
            question.grid(column=0, row=i + 11, columnspan=2, padx=5, pady=5, sticky='w')

            input_char = tkinter.Entry(self.root)
            input_char.grid(column=2, row=i + 11, padx=15, pady=5, sticky="e")

            answers[i] = input_char

        btn_tube = tkinter.Button(self.root, text="Расчет", command=self.tubes)  # функция указывается без вызова
        btn_tube.grid(column=1, row=17, padx=5, pady=5)

    def tubes(self):

        tube = Tubes(g_water=float(answers[0].get()),
                     g_p_steam=float(answers[1].get()),
                     g_c_steam=float(answers[2].get()),
                     g_prod=float(answers[3].get()),
                     g_air=float(answers[4].get()))

        tubes_diams = [
            f"Вода: [{tube.d_water()}] мм ",
            f"Технический пар: [{tube.d_p_steam()}] мм ",
            f"Чистый пар: [{tube.d_c_steam()}] мм ",
            f"Продукт: [{tube.d_prod()}] мм ",
            f"Воздух: [{tube.d_air()}] мм "
        ]

        d_up = tkinter.Label(self.root, text="-----")
        d_up.grid(column=0, row=17, columnspan=2, padx=5, pady=5, sticky='w')

        d_down = tkinter.Label(self.root, text="Расчетные диаметры трубопроводов:")
        d_down.grid(column=0, row=18, columnspan=2, padx=5, pady=5, sticky='w')

        for i, diam in enumerate(tubes_diams):
            d_a = tkinter.Label(self.root, text=diam)
            d_a.grid(column=0, row=i + 19, columnspan=2, padx=5, pady=5, sticky='w')
