import tkinter
from energy import Fermentor
from tubes import Tubes

def input_mass():
    titles = [
        "Введите принятное значение рахода воды (кг/час): ",
        "Введите принятное значение рахода тех. пара (кг/час): ",
        "Введите принятное значение рахода чистого пара (кг/час): ",
        "Введите принятное значение рахода продукта (кг/час): ",
        "Введите принятное значение воздуха (м3/час): "
    ]

    line = tkinter.Label(root, text='-----')
    line.grid(column=0, row=10, columnspan=2, padx=5, pady=5)

    for i in range(5):
        question = tkinter.Label(root, text=titles[i])
        question.grid(column=0, row=i + 11, columnspan=2, padx=5, pady=5, sticky='w')

        input_char = tkinter.Entry(root)
        input_char.grid(column=2, row=i + 11, padx=15, pady=5, sticky="e")

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
root.geometry("700x600")

# Наименование ввода значения
input_title = tkinter.Label(root, text="Введите объем сосуда в литрах")
input_title.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

# Ввод объема сосуда
input_txt = tkinter.Entry(root)
input_txt.grid(column=0, row=1, padx=5, pady=5)

# Кнопка запуска расчета
btn_input = tkinter.Button(root, text="Расчет", command=calculate)  # функция указывается без вызова
btn_input.grid(column=1, row=1, padx=5, pady=5)

'''
g_water = int(input("Введите принятное значение рахода воды (кг/час): "))
g_p_steam = int(input("Введите принятное значение рахода тех. пара (кг/час): "))
g_c_steam = int(input("Введите принятное значение рахода чистого пара (кг/час): "))
g_prod = int(input("Введите принятное значение рахода продукта (кг/час): "))
g_air = int(input("Введите принятное значение воздуха (м3/час): "))

tube = Tubes(g_water, g_p_steam, g_c_steam, g_prod, g_air)

print("Диаметры труб, мм:")
print(f"Вода: {tube.d_water()} мм:")
print(f"Технический пар: {tube.d_p_steam()} мм:")
print(f"Чистый пар: {tube.d_c_steam()} мм:")
print(f"Продукт: {tube.d_prod()} мм:")
print(f"Воздух: {tube.d_air()} мм:")
'''

root.mainloop()
