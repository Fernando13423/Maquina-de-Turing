BLANCO = "B"

class MaquinaDeTuring:


    def __init__(self,estado_inicial:str,estados_finales:set[str],trancisiones:dict):
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales
        self.tranciciones = trancisiones

    def simular(self,entrada):
        cinta = list(entrada) if entrada else [BLANCO] #pasa la palabra a una lista de caracteres, si en la entrada no hay nada, se inicializa en B
        cabezal = 0
        estado = self.estado_inicial

        while True:

            if estado in self.estados_finales:
                print("la palabra es aceptada")
                return True
            
            simbolo_actual = cinta[cabezal]

            if (estado, simbolo_actual) not in self.tranciciones:
                print("la palabra es rechazada")
                print("la tranciciosn " + str((estado, simbolo_actual)) + " no existe")
                return False
            

            resultado = self.tranciciones[(estado, simbolo_actual)]
            nuevo_estado = resultado[0]
            simbolo_escrito = resultado[1]
            direccion = resultado[2]

            cinta[cabezal] = simbolo_escrito
            estado = nuevo_estado

            if direccion == "D":
                cabezal += 1
                if cabezal >= len(cinta):
                    cinta.append(BLANCO)
            else:
                cabezal -= 1

transiciones = {
    ("q0", "a"): ("q1", "X", "D"),
    ("q0", "Y"): ("q3", "Y", "D"),
    ("q1", "a"): ("q1", "a", "D"),
    ("q1", "b"): ("q2", "Y", "I"),
    ("q1", "Y"): ("q1", "Y", "D"),
    ("q2", "a"): ("q2", "a", "I"),
    ("q2", "X"): ("q0", "X", "D"),
    ("q2", "Y"): ("q2", "Y", "I"),
    ("q3", "Y"): ("q3", "Y", "D"),
    ("q3", "B"): ("q4", "B", "I"),
}

mt = MaquinaDeTuring("q0", {"q4"}, transiciones)

mt.simular("aaab")
            