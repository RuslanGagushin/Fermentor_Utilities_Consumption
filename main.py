import tkinter
from energy import Fermentor
from tubes import Tubes


def input_mass():

    line = tkinter.Label(root, text='-----')
    line.grid(column=0, row=10, columnspan=2, padx=5, pady=5)
    # Вопрос 1
    question1 = tkinter.Label(root, text="Введите принятное значение расхода воды (кг/час): ")
    question1.grid(column=0, row=12, columnspan=2, padx=5, pady=5, sticky='w')

    input_char1 = tkinter.Entry(root)
    input_char1.grid(column=2, row=12, padx=15, pady=5, sticky="e")
    # Вопрос 2
    question2 = tkinter.Label(root, text="Введите принятное значение расхода тех. пара (кг/час): ")
    question2.grid(column=0, row=13, columnspan=2, padx=5, pady=5, sticky='w')

    input_char2 = tkinter.Entry(root)
    input_char2.grid(column=2, row=13, padx=15, pady=5, sticky="e")

    # Вопрос 3
    question3 = tkinter.Label(root, text="Введите принятное значение расхода чистого пара (кг/час): ")
    question3.grid(column=0, row=14, columnspan=2, padx=5, pady=5, sticky='w')

    input_char3 = tkinter.Entry(root)
    input_char3.grid(column=2, row=14, padx=15, pady=5, sticky="e")

    # Вопрос 4
    question4 = tkinter.Label(root, text="Введите принятное значение расхода продукта (кг/час): ")
    question4.grid(column=0, row=15, columnspan=2, padx=5, pady=5, sticky='w')

    input_char4 = tkinter.Entry(root)
    input_char4.grid(column=2, row=15, padx=15, pady=5, sticky="e")

    # Вопрос 5
    question5 = tkinter.Label(root, text="Введите принятное значение расхода воздуха (м3/час): ")
    question5.grid(column=0, row=16, columnspan=2, padx=5, pady=5, sticky='w')

    input_char5 = tkinter.Entry(root)
    input_char5.grid(column=2, row=16, padx=15, pady=5, sticky="e")

    def tubes():
        tube = Tubes(g_water=float(input_char1.get()),
                     g_p_steam=float(input_char2.get()),
                     g_c_steam=float(input_char3.get()),
                     g_prod=float(input_char4.get()),
                     g_air=float(input_char5.get()))

        d_up = tkinter.Label(root, text="-----")
        d_up.grid(column=0, row=17, columnspan=2, padx=5, pady=5, sticky='w')

        d_down = tkinter.Label(root, text="Расчетные диаметры трубопроводов:")
        d_down.grid(column=0, row=18, columnspan=2, padx=5, pady=5, sticky='w')

        d_1 = tkinter.Label(root, text=f"Вода: [{tube.d_water()}] мм ")
        d_1.grid(column=0, row=19, columnspan=2, padx=5, pady=5, sticky='w')

        d_2 = tkinter.Label(root, text=f"Технический пар: [{tube.d_p_steam()}] мм ")
        d_2.grid(column=0, row=20, columnspan=2, padx=5, pady=5, sticky='w')

        d_3 = tkinter.Label(root, text=f"Чистый пар: [{tube.d_c_steam()}] мм ")
        d_3.grid(column=0, row=21, columnspan=2, padx=5, pady=5, sticky='w')

        d_4 = tkinter.Label(root, text=f"Продукт: [{tube.d_prod()}] мм ")
        d_4.grid(column=0, row=22, columnspan=2, padx=5, pady=5, sticky='w')

        d_5 = tkinter.Label(root, text=f"Воздух: [{tube.d_air()}] мм ")
        d_5.grid(column=0, row=22, columnspan=2, padx=5, pady=5, sticky='w')



    #Создание кнопки
    # Кнопка запуска расчета
    btn_tube = tkinter.Button(root, text="Расчет", command=tubes)  # функция указывается без вызова
    btn_tube.grid(column=1, row=17, padx=5, pady=5)


def calculate():
    fermenter = Fermentor(int(input_txt.get()))

    chars = [":",
             fermenter.g_steam_fsip_ps(),
             fermenter.g_steam_esip_cs(),
             fermenter.g_steam_tcm_ps(),
             fermenter.g_water_fcip(),
             fermenter.g_water_tcm(),
             fermenter.g_prod(),
             fermenter.g_air()]

    titles = [
        f"Расчетные массовые расходы сред {chars[0]} ",
        f"1. Технический пар на полную стерилизацию: [{chars[1]}] кг/час",
        f"2. Чистый пар на пустую стерилизацию: [{chars[2]}] кг/час",
        f"3. Технический пар на подогрев продукта [{chars[3]}] кг/час",
        f"4. Вода на захолаживание после полной стерилизации: [{chars[4]}] кг/час",
        f"5. Вода на захолаживание после пустой стерилизации [{chars[5]}] кг/час",
        f"6. Выход продукта: [{chars[6]}] кг/час",
        f"7. Воздух: [{chars[7]}] м3/час"
    ]

    for i in range(8):
        char = tkinter.Label(root, text=titles[i], anchor='nw', justify="right")
        char.grid(column=0, row=i + 2, columnspan=2, sticky="w", padx=5, pady=5)

    input_mass()

# create main screen
root = tkinter.Tk()
root.title("Расчет характеристик оборудования Biotechno")
root.geometry("700x800")

# Наименование ввода значения
input_title = tkinter.Label(root, text="Введите объем сосуда в литрах")
input_title.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

# Ввод объема сосуда
input_txt = tkinter.Entry(root)
input_txt.grid(column=0, row=1, padx=5, pady=5)

# Кнопка запуска расчета
btn_input = tkinter.Button(root, text="Расчет", command=calculate)  # функция указывается без вызова
btn_input.grid(column=1, row=1, padx=5, pady=5)


root.mainloop()
