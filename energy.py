
# Плотности компонентов оборудования
RO_PROD = 1000  # kg/m3 - плотность продукта
RO_WATER = 1000 # kg/m3 - плотность продукта
RO_STEAM = 2.7 # kg/m3 - плотность продукта
RO_SS = 7800 # kg/m3 - плотность продукта
RO_AIR = 1.29 * 7 # kg/m3 - плотность воздуха


class Fermentor:
    def __init__(self, v_poln):
        self.v_poln = v_poln
        self.v_rab = 0.75 * (v_poln / 1000)
        self.m_nerj = 2 * v_poln
        self.m_prod = self.v_rab * RO_PROD
        self.m_jack = 0.25 * v_poln
       
    # LOOOOOOOL
