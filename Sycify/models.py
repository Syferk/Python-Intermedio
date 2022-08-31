"""
models.py: 
    Modelo Sycify App.
"""

import os
from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from validations_regex import Validations


#Find path to DB
BASE_DIR = os.path.join(os.path.dirname((os.path.abspath(__file__))), "music.db") 

#ORM using Sqlite DB
db = SqliteDatabase(BASE_DIR) 

#Class Model
class BaseModel(Model):
    class Meta:
        """
        Creación Base de Datos.
        
        :param db: database.
        """
        database = db

#Class Music - Inheritance of the BaseModel
class Music(BaseModel):
    """
    Creación de tabla: Music.
    Tipos de datos para cada campo en la tabla.
    """
    link = CharField(unique=True)
    artista = CharField()
    cancion = CharField()
    duracion = CharField()
    tipo = CharField()
    visualizaciones = CharField()
    likes = CharField()

#Establish connection
try:
    db.connect()
    db.create_tables([Music])
    print("The connection was established successfully.")
except:
    print("Connection error.")

class Abmc():
    #Method init
    def __init__(self, ):
        pass
    #Method loading and creating records   
    def load(self, links, artist, songs, duration, visualization, like, types, tree):
        """
        Método de carga de información.
        """
        song=Music()
        validates = Validations()
        acum_validate = 0
        try:
            acum_validate += validates.links(links)
            acum_validate += validates.name_artist(artist)
            acum_validate += validates.name_song(songs)
            acum_validate += validates.durations(duration)

            if acum_validate == 0:
                song.link=links.get()
                song.artista=artist.get()
                song.cancion=songs.get()
                song.duracion=duration.get()
                song.tipo=types.get()
                song.visualizaciones=visualization.get()
                song.likes=like.get()
                song.save()
                showinfo("OK", "Successfully loaded.")
                links.set("")
                artist.set("")
                songs.set("")
                duration.set("")
                types.set("")
                visualization.set("")
                like.set("")
            else:
                raise AttributeError ("Error in validations.")
        except AttributeError:
            showerror("ERROR", "Invalid characters.")
        else:
            self.update_treeview(tree)
    
    #Method Log Deletion
    def delete(self, tree):
        """
        Método de eliminación de registros.

        :param item: Item.
        """
        valor = tree.selection()
        item = tree.item(valor)
        borrar = Music.get(Music.id==item["text"])
        borrar.delete_instance()
        self.update_treeview(tree)
        showinfo("OK", "Record deleted successfully")
    
    #Method to query    
    def query(self, tree):
        """
        Método de consulta de registros cargados manualmente en la BD.
        """
        self.update_treeview(tree)
    
    #Method for records modifications 
    def modify(self, links, tree):
        """
        Método de modificación de datos en el registro seleccionado.

        :param links: Link.
        """
        valor = tree.selection()
        item = tree.item(valor)
        actualization=Music.update(link=links.get()).where(Music.id==item["text"])
        actualization.execute()
        self.update_treeview(tree)
        links.set("")
        showinfo("OK", "Record modified successfully")
    
    #Method to update the treeview
    def update_treeview(self, mitreview):
        """
        Actualización de TreeView
        """
        records = mitreview.get_children()

        for element in records:
            mitreview.delete(element)

        for fila in Music.select():
            mitreview.insert(
                "",
                0,
                text=fila.id,
                values=(
                    fila.link,
                    fila.artista,
                    fila.cancion,
                    fila.duracion,
                    fila.tipo,
                    fila.visualizaciones,
                    fila.likes,
                ),
            )
