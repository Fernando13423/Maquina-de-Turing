import tkinter as tk
from tkinter import messagebox

from maquina_turing import MaquinaDeTuring

FONDO   = "#d2eaf3"   # azul cielo (fondo ventana)
PANEL   = "#ffffff"   # blanco (campos de texto)
TEXTO   = "#2c3e50"
ACENTO  = "#3a7ca5"
VERDE   = "#2e8b57"
ROJO    = "#c0392b"

ventana = tk.Tk()
ventana.title("Simulador MT")
ventana.configure(bg=FONDO)
tk.Label(ventana, text="Estado inicial:", bg=FONDO, fg=TEXTO).pack(pady=(10, 2))

# campos para ingresar el estado inicial y el estado final, y las transiciones
campo_q0 = tk.Entry(ventana, bg=PANEL, fg=TEXTO)
campo_q0.pack(pady=(0, 10))

tk.Label(ventana, text="Estado final:", bg=FONDO, fg=TEXTO).pack(pady=(10, 2))
campo_final = tk.Entry(ventana, bg=PANEL, fg=TEXTO)
campo_final.pack(pady=(0, 10))

tk.Label(ventana, text="Transiciones (una por línea: q0,a,q1,X,D):", bg=FONDO, fg=TEXTO).pack(pady=(10, 2))
area_transiciones = tk.Text(ventana, height=10, width=60, bg=PANEL, fg=TEXTO)
area_transiciones.pack(pady=(0, 15))

# ingresar la palabra a simular en la MT
etiqueta = tk.Label(ventana, text="Palabra:", bg=FONDO, fg=TEXTO)
etiqueta.pack(pady=(10, 2))

# campo para ingresar la palabra a simular en la MT
campo = tk.Entry(ventana, bg=PANEL, fg=TEXTO)
campo.pack(pady=(0, 10))

# etiqueta para mostrar el resultado de la simulacio, si la palabra es aceptada o rechazada
resultado_label = tk.Label(ventana, text="", bg=FONDO, fg=TEXTO)
resultado_label.pack(pady=(10, 2))

# Area de texto para mostrar las descripciones instantaneas de cada paso de la simulacion 
area_pasos = tk.Text(ventana, height=20, width=60, bg=PANEL, fg=TEXTO)
area_pasos.pack(pady=(0, 15))


#funcion que se ejecuta al presionar el boton, lee los datos de la interfaz, crea la MT y simula la palabra ingresada, mostrando el resultado.
def presionar_boton():

    # Leer estado inicial
    q0 = campo_q0.get().strip()
    if not q0:
        messagebox.showerror("Error", "Debes ingresar el estado inicial.")
        return

    # Leer estado final
    texto_finales = campo_final.get().strip()
    if not texto_finales:
        messagebox.showerror("Error", "Debes ingresar al menos un estado final.")
        return

    estados_finales = {e.strip() for e in texto_finales.split(",")}# Crea un conjunto de estados finales a partir del texto ingresado,
    
    # Leer transciones 
    transiciones = {}
    texto = area_transiciones.get("1.0", tk.END).strip()

    if not texto:
        messagebox.showerror("Error", "Debes ingresar al menos una transición.")
        return
        
    for linea in texto.splitlines():
        partes = linea.split(",")


        if len(partes) != 5:
            messagebox.showerror("Error", "Transición con formato incorrecto:\n" + linea)
            return

        estado_actual, simbolo, nuevo_estado, nuevo_simbolo, direccion = partes
        direccion = direccion.strip()

        if direccion not in ("D", "I"):
            messagebox.showerror("Error", "La dirección debe ser D o I:\n" + linea)
            return
        
        
        transiciones[(estado_actual.strip(), simbolo.strip())] = (
            nuevo_estado.strip(), nuevo_simbolo.strip(), direccion
        )


    # Crear la MT con lo que escribió el usuario
    mt = MaquinaDeTuring(q0, estados_finales, transiciones)

    #simular la MT con la palabra del usuario y mostrar el resultado en la interfaz y los pasos en el area de texto
    palabra = campo.get()
    aceptada, pasos = mt.simular(palabra)
    if aceptada:
        resultado_label.config(text="✔ ACEPTADA", fg=VERDE)
    else:
        resultado_label.config(text="✘ RECHAZADA", fg=ROJO)
    area_pasos.delete("1.0", tk.END)
    for paso in pasos:
        area_pasos.insert(tk.END, paso + "\n")



boton = tk.Button(ventana, text="Mostrar", command=presionar_boton, bg=ACENTO, fg="white" )
boton.pack(pady=(5, 15))

ventana.mainloop()