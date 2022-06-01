import math

# Линейные скороскти в м/с
SP_WATER = 3  # Вода
SP_STEAM = 25  # Пар
SP_PROD = 2  # Продукт
SP_AIR = 40  # Воздух

# Плотности компонентов оборудования
RO_PROD = 1000  # kg/m3 - плотность продукта
RO_WATER = 1000  # kg/m3 - плотность продукта
RO_STEAM = 2.7  # kg/m3 - плотность продукта
RO_SS = 7800  # kg/m3 - плотность продукта
RO_AIR = 1.29 * 7  # kg/m3 - плотность воздуха


class Tubes:
    def __init__(self, g_water, g_p_steam, g_c_steam, g_prod, g_air):
        self.g_water = g_water
        self.g_p_steam = g_p_steam
        self.g_c_steam = g_c_steam
        self.g_prod = g_prod
        self.g_air = g_air

    def d_water(self):
        return round(math.sqrt(
            (4 * (self.g_water / 3600)) / (math.pi * SP_WATER * RO_WATER)
        ) * 1000, 2)

    def d_p_steam(self):
        return round(math.sqrt(
            (4 * (self.g_p_steam / 3600)) / (math.pi * SP_STEAM * RO_STEAM)
        ) * 1000, 2)

    def d_c_steam(self):
        return round(math.sqrt(
            (4 * (self.g_c_steam / 3600)) / (math.pi * SP_STEAM * RO_STEAM)
        ) * 1000, 2)

    def d_prod(self):
        return round(math.sqrt(
            (4 * (self.g_prod / 3600)) / (math.pi * SP_PROD * RO_PROD)
        ) * 1000, 2)

    def d_air(self):
        return round(math.sqrt(
            (4 * (self.g_air / 3600)) / (math.pi * SP_AIR * RO_AIR)
        ) * 1000, 2)
