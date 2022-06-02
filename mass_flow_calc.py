from energy import Fermentor
import tkinter



class MassFlowCalc(Fermentor):
    def __init__(self, v_poln, root):
        super().__init__(v_poln)
        self.root = root

    def results(self):
        '''Возвращает список расходов для каждой среды '''
        return [
            ":",
            self.g_steam_fsip_ps(),
            self.g_steam_esip_cs(),
            self.g_steam_tcm_ps(),
            self.g_water_fcip(),
            self.g_water_tcm(),
            self.g_prod(),
            self.g_air()
        ]

    def print_results(self):
        titles = [
            f"Расчетные массовые расходы сред {self.results()[0]} ",
            f"1. Технический пар на полную стерилизацию: [{self.results()[1]}] кг/час",
            f"2. Чистый пар на пустую стерилизацию: [{self.results()[2]}] кг/час",
            f"3. Технический пар на подогрев продукта [{self.results()[3]}] кг/час",
            f"4. Вода на захолаживание после полной стерилизации: [{self.results()[4]}] кг/час",
            f"5. Вода на захолаживание после пустой стерилизации [{self.results()[5]}] кг/час",
            f"6. Выход продукта: [{self.results()[6]}] кг/час",
            f"7. Воздух: [{self.results()[7]}] м3/час"
        ]

        for i, title in enumerate(titles):
            char = tkinter.Label(self.root, text=title, anchor='nw', justify="right")
            char.grid(column=0, row=i + 2, columnspan=2, sticky="w", padx=5, pady=5)