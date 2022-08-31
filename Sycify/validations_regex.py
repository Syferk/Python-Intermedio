"""
validations_regex.py: 
    Paquete de validaciones regex Sycify App.
"""
from tkinter.messagebox import showerror
import re


class Validations:
    def __init__(self, ):
        pass

    def name_artist(self, name):
        """
        Validación del campo nombre del artista.

        :param txt: cadena a obtener.
        
        :param reg: Expresión regular.

        :return: Retorno 0 -> válido.

        :return: Retorno 1 -> no válido.
        """
        txt = name.get()
        reg = re.compile("^[A-Za-z]*$")
        if re.match(reg, txt):
            print("Correct")
            return 0
        else:
            showerror("Error", "Incorrect name",)
            return 1

    def name_song(self, song):
        """
        Validación del campo nombre de la canción.

        :param txt: cadena a obtener.
        
        :param reg: Expresión regular.

        :return: Retorno 0 -> válido.

        :return: Retorno 1 -> no válido.
        """
        txt = song.get()
        reg = re.compile("^[A-Za-z]*$")
        if re.match(reg, txt):
            print("Correct")
            return 0
        else:
            showerror("Error","Incorrect name song",)
            return 1
    
    def style_type(self, style):
        """
        Validación del campo estilo de música.

        :param txt: cadena a obtener.
        
        :param reg: Expresión regular.

        :return: Retorno 0 -> válido.

        :return: Retorno 1 -> no válido.
        """
        txt = style.get()
        reg = re.compile("([A-Za-z]+)")
        if re.match(reg, txt):
            print("Correct")
            return 0
        else:
            showerror("Error","Incorrect name style",)
            return 1

    def visualization(self, visualizations):
        """
        Validación del campo visualizaciones.

        :param txt: cadena a obtener.
        
        :param reg: Expresión regular.

        :return: Retorno 0 -> válido.

        :return: Retorno 1 -> no válido.
        """
        txt = visualizations.get()
        reg = re.compile("([0-9]+)")
        if re.match(reg, txt):
            print("Correct")
            return 0
        else:
            showerror("Error","Incorrect number for visualizations",)
            return 1

    def likes(self, like):
        """
        Validación del campo likes.

        :param txt: cadena a obtener.
        
        :param reg: Expresión regular.

        :return: Retorno 0 -> válido.

        :return: Retorno 1 -> no válido.
        """
        txt = like.get()
        reg = re.compile("([0-9]+)")
        if re.match(reg, txt):
            print("Correct")
            return 0
        else:
            showerror("Error","Incorrect number for likes",)
            return 1

    def durations(self, duration):
        """
        Validación del campo duración.

        :param txt: cadena a obtener.
        
        :param reg: Expresión regular.

        :return: Retorno 0 -> válido.

        :return: Retorno 1 -> no válido.
        """
        txt = duration.get()
        reg = re.compile("^(?:([01]?\d|2[0-3]):([0-5]?\d):)?([0-5]?\d)$")
        if re.match(reg, txt):
            print("Correct")
            return 0
        else:
            showerror("Error","Incorrect number for duration",)
            return 1

    def links(self, link):
        """
        Validación del campo link.

        :param txt: cadena a obtener.
        
        :param reg: Expresión regular.

        :return: Retorno 0 -> válido.

        :return: Retorno 1 -> no válido.
        """
        txt = link.get()
        reg = re.compile("((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)")
        if re.match(reg, txt):
            print("Correct")
            return 0
        else:
            showerror("Error","Incorrect link",)
            return 1
