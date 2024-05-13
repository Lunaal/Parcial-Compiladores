from terminalesNoTerminales import producciones
from terminalesNoTerminales import noTerminales
from terminalesNoTerminales import terminales

def calcularPrimeros(producciones, noTerminales, terminales):
    diccionarioPrimeros = {noTerminal: [] for noTerminal in noTerminales}
    enProceso = set()
    def añadirPrimeros(noTerminal, candidato):
        if candidato in terminales or candidato == 'ε':
            if candidato not in diccionarioPrimeros[noTerminal]:
                diccionarioPrimeros[noTerminal].append(candidato)
        elif candidato in noTerminales:
            if (noTerminal, candidato) not in enProceso:
                enProceso.add((noTerminal, candidato))
                idx = 0
                while idx < len(producciones):
                    produccionActual = producciones[idx].strip()
                    if produccionActual.startswith(candidato + ' ->'):
                        ladoDerecho = produccionActual.split('->')[1].strip().split()
                        if not ladoDerecho or ladoDerecho[0] == "''":
                            añadirPrimeros(noTerminal, 'ε')
                        else:
                            añadirPrimeros(noTerminal, ladoDerecho[0])
                    idx += 1
                enProceso.remove((noTerminal, candidato))
    idx = 0
    while idx < len(producciones):
        produccion = producciones[idx]
        if '->' in produccion:
            seccion = produccion.split('->')
            ladoIzquierdo = seccion[0].strip()
            ladoDerecho = seccion[1].strip().split()
        
            if not ladoDerecho or ladoDerecho[0] == "''":
                añadirPrimeros(ladoIzquierdo, 'ε')
            else:
                añadirPrimeros(ladoIzquierdo, ladoDerecho[0])
        idx += 1
    return diccionarioPrimeros


def calcularSiguientes(producciones, noTerminales, terminales, primeros):
    siguientes = {nt: set() for nt in noTerminales}
    siguientes[next(iter(noTerminales))].add('$')
    cambio = True
    while cambio:
        cambio = False
        idxProduccion = 0
        while idxProduccion < len(producciones):
            seccion = producciones[idxProduccion].split('->')
            if len(seccion) == 2:
                lhs = seccion[0].strip()
                rhs = seccion[1].strip().split()

                idx_rhs = 0
                while idx_rhs < len(rhs):
                    if rhs[idx_rhs] in noTerminales:
                        siguientes_primeros = set()
                        if idx_rhs + 1 < len(rhs):
                            idx_simbolo = idx_rhs + 1
                            while idx_simbolo < len(rhs):
                                simbolo = rhs[idx_simbolo]
                                if simbolo in terminales:
                                    siguientes_primeros.add(simbolo)
                                    break
                                else:
                                    siguientes_primeros.update(primeros[simbolo])
                                    if 'ε' not in primeros[simbolo]:
                                        break
                                idx_simbolo += 1
                            else:
                                siguientes_primeros.update(siguientes[lhs])
                        else:
                            siguientes_primeros.update(siguientes[lhs])

                        if 'ε' in siguientes_primeros:
                            siguientes_primeros.remove('ε')
                            siguientes_primeros.update(siguientes[lhs])

                        tamaño_anterior = len(siguientes[rhs[idx_rhs]])
                        siguientes[rhs[idx_rhs]].update(siguientes_primeros)
                        if len(siguientes[rhs[idx_rhs]]) > tamaño_anterior:
                            cambio = True
                    idx_rhs += 1
            idxProduccion += 1
    return siguientes

primeros = calcularPrimeros(producciones, noTerminales, terminales)
siguientes = calcularSiguientes(producciones, noTerminales, terminales, primeros)