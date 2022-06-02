import tkinter
from mass_flow_calc import MassFlowCalc
from tube_calc import TubeCalc


# Функция для расчета потребления сред и вывода результата на экран
def calculate():
    """Расчет массовых характеристик потребляемых сред"""
    mfc = MassFlowCalc(int(input_txt.get()), root)
    mfc.print_results()
    tc = TubeCalc(root)
    tc.input_mass()


# создание основного экрана
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
