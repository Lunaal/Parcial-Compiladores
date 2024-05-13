def noTerminales(producciones):
    noTs = []
    for produccion in producciones:
        seccion = produccion.split('->')
        noT = seccion[0].strip()
        if noT not in noTs:
            noTs.append(noT)
    return noTs

def terminales(producciones):
    ts = []
    for produccion in producciones:
        seccion = produccion.split('->')
        if len(seccion) > 1:
            ladoDerecho = seccion[1].strip().split()
            for terminal in ladoDerecho:
                if terminal not in noTerminales and terminal not in ts and terminal != "''":
                    ts.append(terminal)
    return ts

with open('grammarLL1.txt', 'r') as file:
    producciones = file.readlines()

noTerminales = noTerminales(producciones)
terminales = terminales(producciones)

