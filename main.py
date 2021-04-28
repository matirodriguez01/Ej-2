import csv
import os

from ViajeroFrecuente import viajerofrec

def cero():
    print('Hasta luego')


def consultar(mm):
    print('\n-MILLAS ACUMULADAS-\n')
    print('Millas: ', lista[mm].retornamill())
    input('Presiona enter para continuar...')


def acumular(mm):
    print('\n-ACUMULAR MILLAS-\n')
    acum = int(input('Ingrese cantidad de millas que desea agregar: '))
    lista[mm].acummillas(acum)
    print("\nMillas actualizadas")
    print('\nCantidad de millas actuales: ', lista[mm].retornamill())
    input('Presiona enter para continuar...')


def canjear(mm):
    print('\n-CANJEAR MILLAS-\n')
    millascanj = int(input('\nIngrese la cantidad de millas que desea canjear: '))
    lista[mm].canjearmillas(millascanj)
    print('\nCantidad de millas actuales: ', lista[mm].retornamill())
    input('Presiona enter para continuar...')


switcher = {
    0: cero,
    1: consultar,
    2: acumular,
    3: canjear

}

def switch(opc, mm):
    func = switcher.get(opc, lambda: print('\nOpción incorrecta'))
    func(mm)

if __name__ == '__main__':

    lista = []

    archivo = open('Viajeros.csv')
    reader = csv.reader(archivo,delimiter = ",")
    for fila in reader:
        lista.append(viajerofrec(int(fila[0]), int(fila[1]), str(fila[2]), str(fila[3]), int(fila[4])))
    archivo.close()

    tam = len(lista)
    n = 1

    while n == 1:
        m = 0
        num = int(input("\nIngrese numero de viajero:"))
        while (m + 1) <= tam and lista[m].getnumero() != num:
            m += 1
        if m < tam:
            n = 0
            print("\nBienvenido", lista[m].getnombre())

        else:
            print("\nNumero de viajero ingresado, incorrecto.")


    r = False
    while not r:

        os.system('cls')
        print('\nMENÚ PRINCIPAL')
        print('\n1- Consultar cantidad de millas')
        print('\n2- Acumular millas')
        print('\n3- Canjear millas')
        print('\n0- Salir del menu')

        op = int(input('\nIngrese una opción: '))
        switch(op, m)
        r = int(op) == 0

