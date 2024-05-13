import csv
from analizadorLexico import entrada
from tablaSintáctica import tablaCSV
from terminalesNoTerminales import noTerminales
from terminalesNoTerminales import terminales

def trazarParseo(entrada, terminales, noTerminales, rutaTabla):
    tabla_parseo = {}
    with open(rutaTabla, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            no_terminal = fila['Nonterminal']
            tabla_parseo[no_terminal] = {t: fila[t] for t in terminales + ['$']}
    pila = ['$']
    pila.append(next(iter(noTerminales)))
    tokens_entrada = entrada.split() + ['$']
    traza = []
    aceptada = False
    indice = 0
    while pila:
        tope = pila[-1]
        entrada_actual = tokens_entrada[indice]
        traza.append((pila.copy(), tokens_entrada[indice:]))
        if tope == entrada_actual:
            if tope == '$':
                traza.append(("Accept", ""))
                aceptada = True
                break
            else:
                pila.pop()
                indice += 1
        elif tope in noTerminales:
            regla = tabla_parseo[tope][entrada_actual]
            if regla:
                pila.pop()
                if regla != 'ε':
                    elementos_regla = regla.split()
                    pila.extend(reversed(elementos_regla))
                traza.append(("Apply rule", tope + " -> " + regla))
            else:
                traza.append(("Error", "No rule"))
                break
        else:
            traza.append(("Error", "Mismatch"))
            break
    with open('Tabla Parseada.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Stack", "Input", "Action"])
        i = 0
        while i < len(traza):
            t = traza[i]
            if isinstance(t[0], list):
                escritor.writerow([' '.join(t[0]), ' '.join(t[1]), ""])
            else:
                escritor.writerow(['', '', t[0] + ": " + t[1]])
            i += 1
    if aceptada:
        print("Entrada correcta")
    else:
        print("Entrada incorrecta")

    return "Trace parsing generado en 'Tabla de parseo.csv'"

entry = "identificador oper_equal Boolean oper_dotc if left_p identificador doper_equal Boolean right_p Key_left print left_p literal right_p oper_dotc Key_right"
tabla = 'Tabla Sintáctica.csv'
trazarParseo(entrada, terminales, noTerminales, tabla)

# print(entry)