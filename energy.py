# Плотности компонентов оборудования
RO_PROD = 1000  # kg/m3 - плотность продукта
RO_WATER = 1000  # kg/m3 - плотность продукта
RO_STEAM = 2.7  # kg/m3 - плотность продукта
RO_SS = 7800  # kg/m3 - плотность продукта
RO_AIR = 1.29 * 7  # kg/m3 - плотность воздуха

# Линейные скороскти в м/с
SP_WATER = 3
SP_STEAM = 25
SP_PROD = 2
SP_AIR = 40

# Удельные теплоемкости Dj/kg*oC
C_WATER = 4200
C_SS = 462
C_PROD = 4200
R_STEAM = 2100000

# Температуры на входе

T_WATER = 9
T_STEAM = 143
T_PROD = 15
T_STER = 121

# Давление воздуха
P_AIR = 4


class Fermentor:
    def __init__(self, v_poln):
        self.v_poln = v_poln
        self.v_rab = 0.75 * (v_poln / 1000)
        self.m_nerj = 2 * v_poln
        self.m_prod = self.v_rab * RO_PROD
        self.m_jack = 0.25 * v_poln

    def q_nagrev_fcip_ps(self):
        """teplota na nagrev full vessel with empty jacket by PS 15->121*C"""
        return C_PROD * self.m_prod * (T_STER - T_PROD) + C_SS * self.m_nerj * (T_STER - T_PROD)

