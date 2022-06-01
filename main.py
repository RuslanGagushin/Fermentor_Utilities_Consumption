from energy import Fermentor

print("Программа расчета характеристик ферментеров марки Biotechno")

user_input = float(input("Введите полный объем ферментера в литрах: \n"))

# define fermenter
fermenter = Fermentor(user_input)

print("Расчетные массовые расходы сред :")
print(f"Технический пар на полную стерилизацию: {round(fermenter.g_steam_fsip_ps(), 2)} кг/час")
print(f"Чистый пар на пустую стерилизацию: {round(fermenter.g_steam_esip_cs(), 2)} кг/час")
print(f"Технический пар на подогрев продукта: {round(fermenter.g_steam_tcm_ps(), 2)} кг/час")
print(f"Вода на захолаживание после полной стерилизации: {round(fermenter.g_water_fcip(), 2)} кг/час")
print(f"Вода на захолаживание после пустой стерилизации: {round(fermenter.g_water_tcm(), 2)} кг/час")
print(f"Выход продукта: {round(fermenter.g_prod(), 2)} кг/час")
print(f"Воздух: {round(fermenter.g_air(), 2)} м3/час")

g_water = int(input("Введите принятное значение рахода воды (кг/час): "))
g_p_steam = int(input("Введите принятное значение рахода тех. пара (кг/час): "))
g_c_steam = int(input("Введите принятное значение рахода чистого пара (кг/час): "))
g_prod = int(input("Введите принятное значение рахода продукта (кг/час): "))
g_air = int(input("Введите принятное значение воздуха (м3/час): "))