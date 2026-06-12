BLANCO = "B"

class MaquinaDeTuring:

    def __init__(self, estado_inicial, estados_finales, trancisiones):
        self.estado_inicial  = estado_inicial
        self.estados_finales = estados_finales
        self.tranciciones    = trancisiones

    def simular(self, entrada):
        cinta    = list(entrada) if entrada else [BLANCO]
        cabezal  = 0
        estado   = self.estado_inicial
        pasos    = []

        while True:

            pasos.append("Cinta: " + "".join(cinta) + "  estado: " + estado)

            #izquierda = "".join(cinta[:cabezal])
            #derecha   = "".join(cinta[cabezal:])
            #pasos.append(izquierda + " " + estado + " " + derecha)

            if estado in self.estados_finales:
                return True, pasos

            simbolo_actual = cinta[cabezal]

            if (estado, simbolo_actual) not in self.tranciciones:
                return False, pasos

            resultado        = self.tranciciones[(estado, simbolo_actual)]
            nuevo_estado     = resultado[0]
            simbolo_escrito  = resultado[1]
            direccion        = resultado[2]

            cinta[cabezal] = simbolo_escrito
            estado         = nuevo_estado

            if direccion == "D":
                cabezal += 1
                if cabezal >= len(cinta):
                    cinta.append(BLANCO)
            else:
                cabezal -= 1