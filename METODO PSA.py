#-------------------------------------------------------------------------------
#FUNCIONES ESTAS FUNCIONES SON LLAMADAS POR COMANDOS MAS ADELANTE
#-------------------------------------------------------------------------------
def psa_method(valor_inicial):
    menos_1 = round(valor_inicial / 2, 2)
    mas_1 = round(valor_inicial * 1.5, 2)

    print("| \033[31m    ", format(menos_1,'.2f'), "  \033[m   |   ", format(valor_inicial,'.2f'), " |    ", "\033[32m", format(mas_1,'.2f'), "  \033[0m |")
    eleccion = input("____________________________________________ - o +  :")
    if eleccion == "+":
        return round((valor_inicial + mas_1) / 2, 2)
    elif eleccion == "-":
        return round((valor_inicial + menos_1) / 2, 2)
#-------------------------------------------------------------------------------
def psa_method_p2(paso_2):
    menos_1 = round(paso_2 * 0.6, 2)
    mas_1 = round(paso_2 * 1.4, 2)

    print("|    \033[31m ", format(menos_1,'.2f'), "    \033[0m |   ", format(paso_2,'.2f'), " |   \033[32m ",format(mas_1,'.2f'), "  \033[0m  |")
    eleccion = input("____________________________________________ - o +  :")
    if eleccion == "+":
        return round((paso_2 + mas_1) / 2, 2)
    elif eleccion == "-":
        return round((paso_2 + menos_1) / 2, 2)
#-------------------------------------------------------------------------------
def psa_method_p3(paso_3):
    menos_2 = round(paso_3 * 0.7, 2)
    mas_2 = round(paso_3 * 1.3, 2)

    print("|  \033[31m   ", format(menos_2,'.2f'), " \033[0m    |   ", format(paso_3,'.2f'), " |  \033[32m  ", format(mas_2,'.2f'), "\033[0m    |")
    eleccion = input("____________________________________________ - o +  :")
    if eleccion == "+":
        return round((paso_3 + mas_2) / 2, 2)
    elif eleccion == "-":
        return round((paso_3 + menos_2) / 2, 2)
#-------------------------------------------------------------------------------
def psa_method_p4(paso_4):
    menos_2 = round(paso_4 * 0.8, 2)
    mas_2 = round(paso_4 * 1.2, 2)

    print("|  \033[31m   ", format(menos_2,'.2f'), " \033[0m    |   ", format(paso_4,'.2f'), " |  \033[32m  ", format(mas_2,'.2f'), "\033[0m    |")
    eleccion = input("____________________________________________ - o +  :")
    if eleccion == "+":
        return round((paso_4 + mas_2) / 2, 2)
    elif eleccion == "-":
        return round((paso_4 + menos_2) / 2, 2)
#-------------------------------------------------------------------------------
def psa_method_p5(paso_5):
    menos_2 = round(paso_5 * 0.9, 2)
    mas_2 = round(paso_5 * 1.1, 2)

    print("|     \033[31m", format(menos_2,'.2f'), "\033[0m     |   ", format(paso_5,'.2f'), " |    \033[32m", format(mas_2,'.2f'), "\033[0m    |")
    eleccion = input("____________________________________________ - o +  :")
    if eleccion == "+":
        return round((paso_5 + mas_2) / 2, 2)
    elif eleccion == "-":
        return round((paso_5 + menos_2) / 2, 2)
#-------------------------------------------------------------------------------
def psa_method_p6(paso_6):
    menos_2 = round(paso_6 * 0.95, 2)
    mas_2 = round(paso_6 * 1.05, 2)

    print("|     \033[31m", format(menos_2,'.2f'), "\033[0m     |   ", format(paso_6,'.2f'), " |    \033[32m", format(mas_2,'.2f'), "\033[0m    |")
    eleccion = input("____________________________________________ - o +  :")
    if eleccion == "+":
        return round((paso_6 + mas_2) / 2, 2)
    elif eleccion == "-":
        return round((paso_6 + menos_2) / 2, 2)
#-------------------------------------------------------------------------------
#INTRODUCCION O PARTE DE INICIO DEL PROGRAMA
#-------------------------------------------------------------------------------

print(f"\033[32m██████╗ ███████╗ █████╗     \033[0m\033[31m███╗   ███╗███████╗████████╗██╗  ██╗ ██████╗ ██████╗ \033[0m")
print(f"\033[32m██╔══██╗██╔════╝██╔══██╗    \033[0m\033[31m████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗\033[0m")
print(f"\033[32m██████╔╝███████╗███████║    \033[0m\033[31m██╔████╔██║█████╗     ██║   ███████║██║   ██║██║  ██║\033[0m")
print(f"\033[32m██╔═══╝ ╚════██║██╔══██║    \033[0m\033[31m██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██║  ██║\033[0m")
print(f"\033[32m██║     ███████║██║  ██║    \033[0m\033[31m██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝\033[0m")
print(f"\033[32m╚═╝     ╚══════╝╚═╝  ╚═╝    \033[0m\033[31m╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ \033[0m")
                                                                                 
                                                
print("METODO QUE SIRVE PARA ENCONTRAR TU SENCIBILIDAD PERFECTA")

#-------------------------------------------------------------------------------
#ESTO ES EL NUMERO QEUE PONE EL USUARIO
#-------------------------------------------------------------------------------
numero = round(float(input("Pon aca tu sencibilidad de 360°:  ")),2)

#-------------------------------------------------------------------------------
#PARTE DE ARRIBA DE LA TABLA
#-------------------------------------------------------------------------------
print("____________________________________________")
print("|" ,"Menos sensible", "|", "  BASE  ", "|", "Mas sensible", "|")


#-------------------------------------------------------------------------------
#PARTE DE LLAMADO DE LAS FUNCIONES, LA PRIMERA LA LLAMA 2 VECES PORQUE ES EL
#MISMO PROCEDIMIENTO Y LAS DEMAS SOLO 1 VEZ 
# ADEMAS PRIMERO EN resultado_1 = numero, resultado_1 ADOPTA LA CANTIDAD DE numero
#-------------------------------------------------------------------------------
resultado_1 = numero
for i in range(2):
    resultado_1 = psa_method(resultado_1)

resultado_2 = resultado_1
for i in range(1):
    resultado_2 = psa_method_p2(resultado_2)

resultado_3 = resultado_2
for i in range(1):
    resultado_3 = psa_method_p3(resultado_3)

resultado_4 = resultado_3
for i in range(1):
    resultado_4 = psa_method_p4(resultado_4)

resultado_5 = resultado_4
for i in range(1):
    resultado_5 = psa_method_p5(resultado_5)

resultado_6 = resultado_5
for i in range(1):
    resultado_6 = psa_method_p6(resultado_6)

#-------------------------------------------------------------------------------
#IMPRIME EL RESULTADO FINAL
#-------------------------------------------------------------------------------
print("Resultado final: ", resultado_6)

#-------------------------------------------------------------------------------
#ESTO ES EL DICCIONARIO DE NUMERO, RE PONE ANTES DE USARLO
#-------------------------------------------------------------------------------

numeros_ascii = {
    '0': '''
 ██████╗ 
██╔═████╗
██║██╔██║
████╔╝██║
╚██████╔╝
 ╚═════╝ 
''',
    '1': '''
 ██╗
███║
╚██║
 ██║
 ██║
 ╚═╝
''',
    '2': '''
██████╗ 
╚════██╗
 █████╔╝
██╔═══╝ 
███████╗
╚══════╝
''',
    '3': '''
██████╗ 
╚════██╗
 █████╔╝
 ╚═══██╗
██████╔╝
╚═════╝ 
''',
    '4': '''
██╗  ██╗
██║  ██║
███████║
╚════██║
     ██║
     ╚═╝
''',
    '5': '''
███████╗
██╔════╝
███████╗
╚════██║
███████║
╚══════╝
''',
    '6': '''
 ██████╗ 
██╔════╝ 
███████╗ 
██╔═══██╗
╚██████╔╝
 ╚═════╝ 
''',
    '7': '''
███████╗
╚════██║
    ██╔╝
   ██╔╝ 
   ██║  
   ╚═╝  
''',
    '8': '''
 █████╗ 
██╔══██╗
╚█████╔╝
██╔══██╗
╚█████╔╝
 ╚════╝ 
''',
    '9': '''
 █████╗ 
██╔══██╗
╚██████║
 ╚═══██║
 █████╔╝
 ╚════╝ 
''',
    '.': '''  
██╗
╚═╝
''',
}

#-------------------------------------------------------------------------------
#SE CONVIERTE EL RESULTTADO FINAL A STR
#-------------------------------------------------------------------------------
resultado_final_str = str(resultado_6)

#-------------------------------------------------------------------------------
#for es una palabra clave en Python que se utiliza para crear un bucle que itera
#sobre un iterable, como una lista, una tupla, un diccionario, etc.
#-------------------------------------------------------------------------------


for c in resultado_final_str:
   print(numeros_ascii[c])

#-------------------------------------------------------------------------------
#PARA QUE NO DESAPAREZCA AL INSTANTE
#-------------------------------------------------------------------------------

input("Preciona ENTER para finalizar")