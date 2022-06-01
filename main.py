import tkinter
from energy import Fermentor
from tubes import Tubes


def calculate():
    fermenter = Fermentor(int(input_txt.get()))
    calc_g_steam_fsip_ps['text'] = f"1. Технический пар на полную стерилизацию {fermenter.g_steam_fsip_ps()} кг/ч"



# create main screen
root = tkinter.Tk()
root.title("Расчет характеристик оборудования Biotechno")
root.geometry("600x600")

# Наименование ввода значения
input_title = tkinter.Label(root, text="Введите объем сосуда в литрах")
input_title.grid(column=0, row=0, columnspan=2)

# Ввод объема сосуда
input_txt = tkinter.Entry(root)
input_txt.grid(column=0, row=1)

# Кнопка запуска расчета
btn_input = tkinter.Button(root, text="Расчет", command=calculate)  # функция указывается без вызова
btn_input.grid(column=1, row=1)

calc_mass_info = tkinter.Label(root, text="Расчетные массовые расходы сред :", anchor='nw')
calc_mass_info.grid(column=0, row=2, columnspan=2)

calc_g_steam_fsip_ps = tkinter.Label(root, text="1. Технический пар на полную стерилизацию", anchor='nw')
calc_g_steam_fsip_ps.grid(column=0, row=3, columnspan=2)

calc_g_steam_esip_cs = tkinter.Label(root, text="2. Чистый пар на пустую стерилизацию", anchor='nw')
calc_g_steam_esip_cs.grid(column=0, row=4, columnspan=2)

calc_g_steam_tcm_ps = tkinter.Label(root, text="3. Технический пар на подогрев продукта", anchor='nw')
calc_g_steam_tcm_ps.grid(column=0, row=5, columnspan=2)

calc_g_water_fcip = tkinter.Label(root, text="4. Вода на захолаживание после полной стерилизации", anchor='nw')
calc_g_water_fcip.grid(column=0, row=6, columnspan=2)

calc_g_water_tcm = tkinter.Label(root, text="5. Вода на захолаживание после пустой стерилизации", anchor='nw')
calc_g_water_tcm.grid(column=0, row=7, columnspan=2)

calc_g_prod = tkinter.Label(root, text="6. Выход продукта", anchor='nw')
calc_g_prod.grid(column=0, row=8, columnspan=2)

calc_g_air = tkinter.Label(root, text="7. Воздух", anchor='nw')
calc_g_air.grid(column=0, row=9, columnspan=2)

'''
user_input = float(input("Введите полный объем ферментера в литрах: \n"))

# define fermenter
fermenter = Fermentor(user_input)

++
++
++
++
++
++
++
++

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
