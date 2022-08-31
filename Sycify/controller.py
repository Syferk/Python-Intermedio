"""
controller.py: 
    Controlador Sycify App.
"""

from tkinter import Tk
import viewer

__author__="Fernando E. Paz"
__email__="fernan16p@gmail.com"
__copyright__="Copyright 2022"
__versión__="0.1"

class Controller:
    def __init__(self, root):
        """
        Método init a ventana tkinter.

        :param root: App.
        """
        self.root_controler = root
        self.objeto_vista = viewer.Window(self.root_controler)

if __name__ == "__main__":
    app_main = Tk()
    Controller(app_main)
    app_main.mainloop()
