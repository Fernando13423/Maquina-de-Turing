import tkinter as tk

from maquina_turing import MaquinaDeTuring

ventana = tk.Tk()
ventana.title("Simulador MT")


tk.Label(ventana, text="Estado inicial:").pack()
campo_q0 = tk.Entry(ventana)
campo_q0.pack()

tk.Label(ventana, text="Estado final:").pack()
campo_final = tk.Entry(ventana)
campo_final.pack()

tk.Label(ventana, text="Transiciones (una por línea: q0,a,q1,X,D):").pack()
area_transiciones = tk.Text(ventana, height=10, width=60)
area_transiciones.pack()


etiqueta = tk.Label(ventana, text="Palabra:")
etiqueta.pack()

campo = tk.Entry(ventana)
campo.pack()


resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

area_pasos = tk.Text(ventana, height=20, width=60)
area_pasos.pack()

def presionar_boton():
    # Leer estado inicial
    q0 = campo_q0.get().strip()

    # Leer estado final
    final = campo_final.get().strip()
    estados_finales = {final}

    # Leer transciones 
    transiciones = {}
    texto = area_transiciones.get("1.0", tk.END).strip()
    
    for linea in texto.splitlines():
        partes = linea.split(",")
        estado_actual, simbolo, nuevo_estado, nuevo_simbolo, direccion = partes
        transiciones[(estado_actual.strip(), simbolo.strip())] = (
            nuevo_estado.strip(), nuevo_simbolo.strip(), direccion.strip()
        )

    # Crear la MT con lo que escribió el usuario
    mt = MaquinaDeTuring(q0, estados_finales, transiciones)


    #simular la MT con la palabra del usuario y mostrar el resultado en la interfaz y los pasos en el area de texto
    palabra = campo.get()
    aceptada, pasos = mt.simular(palabra)
    if aceptada:
        resultado_label.config(text="✔ ACEPTADA")
    else:
        resultado_label.config(text="✘ RECHAZADA")
    area_pasos.delete("1.0", tk.END)
    for paso in pasos:
        area_pasos.insert(tk.END, paso + "\n")

boton = tk.Button(ventana, text="Mostrar", command=presionar_boton)
boton.pack()

ventana.mainloop()