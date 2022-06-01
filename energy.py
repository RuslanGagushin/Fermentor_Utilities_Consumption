# Плотности компонентов оборудования
RO_PROD = 1000  # kg/m3 - плотность продукта
RO_WATER = 1000  # kg/m3 - плотность продукта
RO_STEAM = 2.7  # kg/m3 - плотность продукта
RO_SS = 7800  # kg/m3 - плотность продукта
RO_AIR = 1.29 * 7  # kg/m3 - плотность воздуха

# Линейные скороскти в м/с
SP_WATER = 3 # Вода
SP_STEAM = 25 # Пар
SP_PROD = 2 # Продукт
SP_AIR = 40 # Воздух

# Удельные теплоемкости Dj/kg*oC
C_WATER = 4200 # Вода
C_SS = 462 # Нержавеющая сталь
C_PROD = 4200 # Продукт
R_STEAM = 2100000 # Пар

# Исходные температуры гр. Цельсия
T_WATER = 9 # Вода
T_STEAM = 143 # Пар
T_PROD = 15 # Продукт
T_STER = 121 # Температура стерилизации

# Давление воздуха
P_AIR = 4


class Fermentor:
    def __init__(self, v_poln):
        self.v_poln = v_poln
        self.v_rab = 0.75 * (v_poln / 1000)
        self.m_nerj = 2 * v_poln
        self.m_prod = self.v_rab * RO_PROD
        self.m_jack = 0.25 * v_poln

    # fsip - полная стерилизация / esip - пустая
    # ps - технический пар / cs - чистый пар

    def q_nagrev_fsip_ps(self):
        """теплота на нагрев полной емкости с пустой рубашкой, техническим паром 15->121*C"""
        return C_PROD * self.m_prod * (T_STER - T_PROD) + C_SS * self.m_nerj * (T_STER - T_PROD)

    def q_nagrev_esip_cs(self):
        """теплота на нагрев пустой емкости с пустой рубашкой, чистым паром 15->121*C"""
        return C_SS * self.m_nerj * (T_STER - T_PROD)

    def q_nagrev_tcm_ps(self):
        """теплота на нагрев полной емкости с полной рубашкой рубашкой, техническим паром 20->37*C"""
        return C_PROD * (self.m_jack + self.m_prod) * (37 - 20) + C_SS * self.m_nerj * (37 - 20)

    def q_hold_fsip_ps(self):
        """теплота на выдержку 45 минут, технический пар"""
        return 0.25 * self.q_nagrev_fsip_ps()

    def q_hold_esip_cs(self):
        """теплота на выдержка 45 минут, чистый пар"""
        return 0.5 * self.q_nagrev_esip_cs()

    def m_para_fsip_ps(self):
        """масса необходимого технического пара, кг"""
        return self.q_nagrev_fsip_ps() / R_STEAM

    def m_para_esip_cs(self):
        """масса необходимого чистого пара, кг"""
        return 2 * self.q_nagrev_esip_cs() / R_STEAM

    def m_para_tcm_ps(self):
        """масса необходимого технического пара на нагрев рубашки, кг"""
        return self.q_nagrev_tcm_ps() / R_STEAM

    def m_water_fsip(self):
        """масса воды на захолаживание пустой емкости с полной рубашкой 121->30*C, кг"""
        return (4 * self.q_nagrev_fsip_ps()) / (C_WATER * (T_STER - T_WATER))

    def m_water_tcm(self):
        """масса воды на захолаживание полной емкости с полной рубашкой 37->20*C, кг"""
        return (2 * self.q_nagrev_tcm_ps()) / (C_WATER * (37 - T_WATER))

