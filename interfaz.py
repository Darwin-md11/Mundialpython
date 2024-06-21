import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time

class Equipo:
    def __init__(self, nombre, entrenador):
        self.nombre = nombre
        self.entrenador = entrenador
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

class Jugador:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion

class Partido:
    def __init__(self, equipo_local, equipo_visitante, resultado):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.resultado = resultado

class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

class Estadio:
    def __init__(self, nombre, ciudad, capacidad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad

class Mundial:
    def __init__(self):
        self.grupos = []
        self.estadios = []
        self.partidos = []

    def registrar_grupo(self, grupo):
        self.grupos.append(grupo)

    def registrar_estadio(self, estadio):
        self.estadios.append(estadio)

    def registrar_partido(self, partido):
        self.partidos.append(partido)

class SplashScreen(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("300x300")
        self.overrideredirect(True)  # Remove window decorations

        # Load and display the image
        imagen = Image.open("C:/mundial/imagen.png")  # Ruta completa de la imagen
        imagen = imagen.resize((300, 300))
        self.imagen = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(self, image=self.imagen)
        label_imagen.pack()

        # Center the splash screen on the screen
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def show(self, duration=7000):
        self.after(duration, self.destroy)
        self.mainloop()

class MundialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion del mundial")
        self.root.geometry("800x600")

        self.mundial = Mundial()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tab_equipos = ttk.Frame(self.notebook)
        self.tab_partidos = ttk.Frame(self.notebook)
        self.tab_grupos = ttk.Frame(self.notebook)
        self.tab_estadios = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_equipos, text="Equipos")
        self.notebook.add(self.tab_partidos, text="Partidos")
        self.notebook.add(self.tab_grupos, text="Grupos")
        self.notebook.add(self.tab_estadios, text="Estadios")

        self.init_tab_equipos()
        self.init_tab_partidos()
        self.init_tab_grupos()
        self.init_tab_estadios()

    def init_tab_equipos(self):
        frame = ttk.LabelFrame(self.tab_equipos, text="Registrar Equipo")
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Nombre").pack(padx=5, pady=5)
        self.entry_nombre_equipo = ttk.Entry(frame)
        self.entry_nombre_equipo.pack(padx=5, pady=5)

        ttk.Label(frame, text="Entrenador").pack(padx=5, pady=5)
        self.entry_entrenador_equipo = ttk.Entry(frame)
        self.entry_entrenador_equipo.pack(padx=5, pady=5)

        ttk.Button(frame, text="Registrar Equipo", command=self.registrar_equipo).pack(padx=5, pady=5)

        self.lista_equipos = tk.Listbox(frame)
        self.lista_equipos.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    def init_tab_partidos(self):
        frame = ttk.LabelFrame(self.tab_partidos, text="Registrar Partido")
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Equipo Local").pack(padx=5, pady=5)
        self.combo_equipo_local = ttk.Combobox(frame, state="readonly")
        self.combo_equipo_local.pack(padx=5, pady=5)

        ttk.Label(frame, text="Equipo Visitante").pack(padx=5, pady=5)
        self.combo_equipo_visitante = ttk.Combobox(frame, state="readonly")
        self.combo_equipo_visitante.pack(padx=5, pady=5)

        ttk.Label(frame, text="Resultado").pack(padx=5, pady=5)
        self.entry_resultado_partido = ttk.Entry(frame)
        self.entry_resultado_partido.pack(padx=5, pady=5)

        ttk.Button(frame, text="Registrar Partido", command=self.registrar_partido).pack(padx=5, pady=5)

        self.lista_partidos = tk.Listbox(frame)
        self.lista_partidos.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    def init_tab_grupos(self):
        frame = ttk.LabelFrame(self.tab_grupos, text="Registrar Grupo")
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Nombre").pack(padx=5, pady=5)
        self.entry_nombre_grupo = ttk.Entry(frame)
        self.entry_nombre_grupo.pack(padx=5, pady=5)

        ttk.Button(frame, text="Registrar Grupo", command=self.registrar_grupo).pack(padx=5, pady=5)

        self.lista_grupos = tk.Listbox(frame)
        self.lista_grupos.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    def init_tab_estadios(self):
        frame = ttk.LabelFrame(self.tab_estadios, text="Registrar Estadio")
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Nombre").pack(padx=5, pady=5)
        self.entry_nombre_estadio = ttk.Entry(frame)
        self.entry_nombre_estadio.pack(padx=5, pady=5)

        ttk.Label(frame, text="Ciudad").pack(padx=5, pady=5)
        self.entry_ciudad_estadio = ttk.Entry(frame)
        self.entry_ciudad_estadio.pack(padx=5, pady=5)

        ttk.Label(frame, text="Capacidad").pack(padx=5, pady=5)
        self.entry_capacidad_estadio = ttk.Entry(frame)
        self.entry_capacidad_estadio.pack(padx=5, pady=5)

        ttk.Button(frame, text="Registrar Estadio", command=self.registrar_estadio).pack(padx=5, pady=5)

        self.lista_estadios = tk.Listbox(frame)
        self.lista_estadios.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    def registrar_equipo(self):
        nombre = self.entry_nombre_equipo.get()
        entrenador = self.entry_entrenador_equipo.get()
        if nombre and entrenador:
            equipo = Equipo(nombre, entrenador)
            if self.mundial.grupos:
                self.mundial.grupos[0].agregar_equipo(equipo)
                self.lista_equipos.insert(tk.END, equipo.nombre)
            self.entry_nombre_equipo.delete(0, tk.END)
            self.entry_entrenador_equipo.delete(0, tk.END)
            self.actualizar_combobox_equipos()

    def registrar_partido(self):
        equipo_local = self.combo_equipo_local.get()
        equipo_visitante = self.combo_equipo_visitante.get()
        resultado = self.entry_resultado_partido.get()
        if equipo_local and equipo_visitante and resultado:
            equipo_local = next(e for g in self.mundial.grupos for e in g.equipos if e.nombre == equipo_local)
            equipo_visitante = next(e for g in self.mundial.grupos for e in g.equipos if e.nombre == equipo_visitante)
            partido = Partido(equipo_local, equipo_visitante, resultado)
            self.mundial.registrar_partido(partido)
            self.lista_partidos.insert(tk.END, f"{equipo_local.nombre} vs {equipo_visitante.nombre} - {resultado}")
            self.entry_resultado_partido.delete(0, tk.END)

    def registrar_grupo(self):
        nombre = self.entry_nombre_grupo.get()
        if nombre:
            grupo = Grupo(nombre)
            self.mundial.registrar_grupo(grupo)
            self.lista_grupos.insert(tk.END, grupo.nombre)
            self.entry_nombre_grupo.delete(0, tk.END)

    def registrar_estadio(self):
        nombre = self.entry_nombre_estadio.get()
        ciudad = self.entry_ciudad_estadio.get()
        capacidad = self.entry_capacidad_estadio.get()
        if nombre and ciudad and capacidad:
            estadio = Estadio(nombre, ciudad, capacidad)
            self.mundial.registrar_estadio(estadio)
            self.lista_estadios.insert(tk.END, f"{estadio.nombre} - {ciudad} - {capacidad}")
            self.entry_nombre_estadio.delete(0, tk.END)
            self.entry_ciudad_estadio.delete(0, tk.END)
            self.entry_capacidad_estadio.delete(0, tk.END)

    def actualizar_combobox_equipos(self):
        equipos = [equipo.nombre for grupo in self.mundial.grupos for equipo in grupo.equipos]
        self.combo_equipo_local['values'] = equipos
        self.combo_equipo_visitante['values'] = equipos

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  

    splash = SplashScreen(root)
    root.deiconify()  
    app = MundialApp(root)
    root.mainloop()
