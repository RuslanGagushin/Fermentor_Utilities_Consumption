# Плотности компонентов оборудования
RO_PROD = 1000  # kg/m3 - плотность продукта
RO_WATER = 1000  # kg/m3 - плотность продукта
RO_STEAM = 2.7  # kg/m3 - плотность продукта
RO_SS = 7800  # kg/m3 - плотность продукта
RO_AIR = 1.29 * 7  # kg/m3 - плотность воздуха

# Линейные скороскти в м/с
SP_WATER = 3  # Вода
SP_STEAM = 25  # Пар
SP_PROD = 2  # Продукт
SP_AIR = 40  # Воздух

# Удельные теплоемкости Dj/kg*oC
C_WATER = 4200  # Вода
C_SS = 462  # Нержавеющая сталь
C_PROD = 4200  # Продукт
R_STEAM = 2100000  # Пар

# Исходные температуры гр. Цельсия
T_WATER = 9  # Вода
T_STEAM = 143  # Пар
T_PROD = 15  # Продукт
T_STER = 121  # Температура стерилизации

# Давление воздуха
P_AIR = 4


class Fermentor:
    def __init__(self, v_poln):
        """Для расчета требуется указать полный объем емкости"""
        self.v_poln = v_poln
        self.v_rab = 0.75 * (v_poln / 1000)
        self.m_nerj = 2 * v_poln
        self.m_prod = self.v_rab * RO_PROD
        self.m_jack = 0.25 * v_poln

    # fsip - полная стерилизация / esip - пустая
    # ps - технический пар / cs - чистый пар

    def q_nagrev_fsip_ps(self):
        """Теплота на нагрев полной емкости с пустой рубашкой, техническим паром 15->121*C"""
        return C_PROD * self.m_prod * (T_STER - T_PROD) + C_SS * self.m_nerj * (T_STER - T_PROD)

    def q_nagrev_esip_cs(self):
        """Теплота на нагрев пустой емкости с пустой рубашкой, чистым паром 15->121*C"""
        return C_SS * self.m_nerj * (T_STER - T_PROD)

    def q_nagrev_tcm_ps(self):
        """Теплота на нагрев полной емкости с полной рубашкой рубашкой, техническим паром 20->37*C"""
        return C_PROD * (self.m_jack + self.m_prod) * (37 - 20) + C_SS * self.m_nerj * (37 - 20)

    def q_hold_fsip_ps(self):
        """Теплота на выдержку 45 минут, технический пар"""
        return 0.25 * self.q_nagrev_fsip_ps()

    def q_hold_esip_cs(self):
        """Теплота на выдержку 45 минут, чистый пар"""
        return 0.5 * self.q_nagrev_esip_cs()

    def m_para_fsip_ps(self):
        """Масса необходимого технического пара, кг"""
        return self.q_nagrev_fsip_ps() / R_STEAM

    def m_para_esip_cs(self):
        """Масса необходимого чистого пара, кг"""
        return 2 * self.q_nagrev_esip_cs() / R_STEAM

    def m_para_tcm_ps(self):
        """Масса необходимого технического пара на нагрев рубашки, кг"""
        return self.q_nagrev_tcm_ps() / R_STEAM

    def m_water_fsip(self):
        """Масса воды на захолаживание пустой емкости с полной рубашкой 121->30*C, кг"""
        return (4 * self.q_nagrev_fsip_ps()) / (C_WATER * (T_STER - T_WATER))

    def m_water_tcm(self):
        """Масса воды на захолаживание полной емкости с полной рубашкой 37->20*C, кг"""
        return (2 * self.q_nagrev_tcm_ps()) / (C_WATER * (37 - T_WATER))

    # Массовый расход (минимальные расчетные значения)

    def g_steam_fsip_ps(self):
        """Массовый расход технического пара полная стерилизация, кг/час"""
        return round(1.2 * (self.m_para_fsip_ps() / 0.5), 2)

    def g_steam_esip_cs(self):
        """Массовый расход чистого пара пустая стерилизация, кг/час"""
        return round(1.2 * (self.m_para_esip_cs() / 0.5), 2)

    def g_steam_tcm_ps(self):
        """Массовый расход технического пара на нагрев рубашки и емкости, кг/час"""
        return round(1.2 * (self.m_para_esip_cs() / 0.5), 2)

    def g_water_fcip(self):
        """Массовый расход воды на захолаживание после полной стерилизации, кг/час"""
        return round(1.2 * (self.m_water_fsip() / 0.67), 2)

    def g_water_tcm(self):
        """Массовый расход воды на захолаживание, кг/час"""
        return round(1.2 * (self.m_water_tcm() / 0.25), 2)

    def g_prod(self):
        """Массовый расход продукта, кг/час"""
        return round(1.2 * (self.m_prod / 0.5), 2)

    def g_air(self):
        """Массовый расход воздуха, кг/час"""
        return round(2 * self.v_poln * 60 / 1000, 2)
