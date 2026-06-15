BLANCO = "B"
LIMITE_PASOS = 10000  # evita loops infinitos si la MT no termina


class MaquinaDeTuring:
    def __init__(self, estado_inicial, estados_finales, transiciones):
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales
        self.transiciones = transiciones

    def simular(self, entrada):
        cinta = list(entrada) if entrada else [BLANCO]
        cabezal = 0
        estado = self.estado_inicial
        pasos = []

        for _ in range(LIMITE_PASOS):
            pasos.append("Cinta: " + "".join(cinta) + " estado: " + estado)

            if estado in self.estados_finales:
                return True, pasos

            simbolo_actual = cinta[cabezal]

            if (estado, simbolo_actual) not in self.transiciones:
                return False, pasos

            resultado = self.transiciones[(estado, simbolo_actual)]
            nuevo_estado = resultado[0]
            simbolo_escrito = resultado[1]
            direccion = resultado[2]

            cinta[cabezal] = simbolo_escrito
            estado = nuevo_estado

            if direccion == "D":
                cabezal += 1
                if cabezal >= len(cinta):
                    cinta.append(BLANCO)
            else:  # "I"
                if cabezal == 0:
                    cinta.insert(0, BLANCO)
                else:
                    cabezal -= 1

        pasos.append("Se alcanzó el límite de pasos ({}). Posible loop infinito.".format(LIMITE_PASOS))
        return False, pasos