#import math
#print("******* operadores logicos.\n\n")
#and, or, not


#print ("\n\n **** volumen esfera **** ")
#radio = float (input("\n ingresa radio: ")) #comentario
#pi = 3.14159
#vol = 40 / 30 * pi *radio ** 3
#print ('el volumen es ', vol, 'cm3')


#print ("\n\n\n **** area y perimetro ****\n")
#base = float(input("\n ingresa base rec: "))
#altura = float(input("\n ingresa altura rec: "))
#perimetro = (2*base) + (2*altura)
#area = base * altura
#print(f"\n el perimetro es {perimetro}")
#print(f"\n el area es {area}")


#print ("\n\n\n **** area triangle ****\n")
#baseT = float (input("\n ingresa base Triangle: "))
#alturaT = float (input("\n ingresa altura Triangle: "))
#areaT = (baseT * alturaT) / 2
#print (f"area of triangle is {areaT}")


#print ("\n\n\n **** perimetro y area triangle **** \n")
#lado1 = float (input ("\n ingresa lado a: "))
#lado2 = float (input ("\n ingresa lado b: "))
#lado3 = float (input ("\n ingresa lado c: "))
#perimetroT2 = lado1 + lado2 + lado3
#s = (perimetroT2) / 2
#areaT2 = math.sqrt( s * (s - lado1)* (s - lado2) * (s-lado3) )
#print (f"perimetro es {perimetroT2}")
#print (f"area es {areaT2}")


#print ("\n\n\n **** area triangle scalen**** \n")
#ladoA = float (input("\ningrese lado a: "))
#ladoB = float (input("\ningrese lado b: "))
#angle = float (input("\ningrese angle: "))
#div = angle / 180
#rad = math.sin(angle) #python trabaja en radianes .25   180° = pi * rad 
#print (f"seno {rad}")
#areaEscaleno = (ladoA * ladoB) * (rad)
#print ('area es ' , areaEscaleno)


#exponente (x**y)
#print ("\n\n\n *** tasa de interes - capital **** \n")
#cantidadEuros = float (input ("\n ingresa cantidad de euros: "))
#tasaInteres = float (input ("\n ingresa % de la tasa de interes: "))
#aniosTranscurridos = float (input ("\n años transcurridos: "))
#capital = cantidadEuros * ((1 + tasaInteres / 100) ** aniosTranscurridos)
#final = str(round(capital,2))
#print (f"capital actual es {final}")


#print ("\n\n\n ***¨concatenacion nombre **** \n")
#cadena = input ("ingresa el nombre: ")
#form = (cadena + ' ') * 100
#print (f"{form} ")


#print ("\n\n\n\n *** nombre de usuario *** \n")
#nombre = input ("\n ingresa tu nombre de usuario: ")
#numero = int (input ("\n ingresa un numero entero: "))
#repetir = (nombre + ' ') * numero
#print(f"{repetir}")


#upper() devuelve una copia en mayusculas de la variable original pero no la modifica
#print ("\n\n\n\n **** tamaño de nombre **** \n")
#nombre = input ("\n ingresa tu nombre: ")
#tamanioNombre = nombre.upper() + " tiene " + str(len(nombre)) + " letras"
  #0 -> tamanioNombre = len(nombre)
#print (f"{tamanioNombre}")


#print("\n\n\n\n **** operacion aritmetica **** \n")
#numero1 = int (input ("\n ingresa numero entero 1: "))
#numero2 = int (input (" ingresa numero entero 2: "))
#numero3 = int (input (" ingresa numero entero 3: "))
#numero4 = int (input (" ingresa numero entero 4: "))
#operacionAritmetica = ((numero1 + numero2) / (numero3 * numero4)) ** 2
#print(f"el resultado es {operacionAritmetica}")


#print ("\n\n\n\n **** Indice Masa Corporal (IMC) **** \n")
#pesoUsuario = float (input (" ingresa tu peso (kg): "))
#alturaUsuario = float (input (" ingresa tu altura (mts): "))
#indiceMasaCorporal = str(round( (pesoUsuario / alturaUsuario**2) , 2)) #round(cifra, numero de digitos despues del punto)
# O --> indiceMasaCorporal = pesoUsuario / alturaUsuario
#print (f"Tu indice de masa corporal es {indiceMasaCorporal}.")


#// divide solo en enteros
#print ("\n\n\n\n **** division **** \n")
#numero1 = int (input ("ingresa numero 1 entero: "))
#numero2 = int (input ("ingresa numero entero menor que numero 1: "))
#division = str( numero1 // numero2) 
#residuo = numero1 % numero2
#print (f"{numero1} entre {numero2} da un cociente {division} y un resto {residuo}.")


#print ("\n\n\n\n **** contraseña **** \n")
#newUser = input(" insert new user: ")
#newPassword = input(" insert new password: ")
#print("* " * 1000)
#user = input("\n\n insert user: ")
#password = input("insert password: ")
#if ((newUser == user) and (newPassword == password) ): #password.lower() 
#    print ("\n ***** Login successful *****")
#else:
#    print ("\n ***** Login Error *****")


#print ("\n\n\n\n **** mayor o menor **** \n")
#edad = int (input(" ingresa tu edad: "))
#if (edad >=18 ):
#    print ("\n ***** ERES MAYOR DE EDAD *****\n ")
#else:
#    print ("\n ***** ERES MENOR DE EDAD***** \n")


#print ("\n\n\n\n ***** division ***** ")
#contador1 = 0
#contador2 = 0
#numero1 = int (input("\n ingresa 1er numero entero: "))
#while (numero1<=0):
#    print ("\n ***** ERROR ***** \n ***** el numero es menor o igual a 0 ***** \n")
#    if (numero1 <= 0):
#        numero1 = int (input ("\n ingresa 1er numero entero: "))
#        contador1 = contador1 + 1
#    else:
#        break
#numero2 = int (input("\n ingresa 2o numero entero: "))
#while (numero2 <= 0 ):
#    print ("\n ***** ERROR ***** \n ***** el numero es menor o igual a 0 ***** \n")
#    if (numero2 <= 0 ):
#        numero2 = int (input ("\n ingresa 1er numero entero: "))
#        contador2 = contador2 + 1
#    else:
#        break
#division = numero1 / numero2
#print (f" el resultado de {numero1}/{numero2} es {division}")


#print ("\n\n\n\n ***** TRIBUTARIO ***** ")
#contadorEdad = 0
#contadorCapital = 0
#edad = int (input ("\n ingresa tu edad: "))
#while (edad < 16):
#    print (" ***** Tu edad es menor a 16 ***** ")
#    if(edad<=16):
#        edad = int (input ("\n ingresa tu edad: "))
#        contadorEdad = contadorEdad + 1
#    else:
#        break
#capital = float (input ("\n ingreso mensual: "))
#while (capital <= 1000):
#    print (" ***** el capital es menor o igual a 1000 ***** ")
#    if (capital<=1000):
#        capital = float (input ("\n ingreso mensual: "))
#        contadorCapital = contadorCapital + 1
#    else:
#        break
#print (f" tu edad es {edad} y capital mensual es {capital}. ")
#if ( (edad >= 16) and (capital >= 1000)):
#    print ("\n ****** TRIBUTARIO ****** ")
#else:
#    print ("\n ****** NO TRIBUTARIO ****** ")
#edad = int (input ("\n ingresa tu edad: "))
#capital = float (input ("\n ingreso mensual: "))
#if ( (edad >= 16) and (capital >= 1000)):
#    print ("\n ****** TRIBUTARIO ****** ")
#else:
#    print ("\n ****** NO TRIBUTARIO ****** ")



#los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al
#sexo y al nombre. El grupo A esta formado por las mujeres con un nombre
#anterior a la M y los hombres con un nombre posterior a la N y el grupo B
#por el resto
#------------------------------------------------------------------------------
#print ("\n\n\n ***** Alumnos de curso ***** ")
#alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'#27
#nombre = input("\n ingresa tu nombre: ").upper()
#sexo = input(" sexo (F/M): ").upper()
#if (((nombre[0] <= alfabeto[12]) and (sexo == 'F')) or ((nombre[0] >= alfabeto[13]) and (sexo == 'M')) ):
#    print("\t\t\t ***** GRUPO A *****")
#    print(f"\n nombre: {nombre}  -- sexo[{sexo}]")
#    #print(f" nombre[0] -- {nombre[0]} -- alfabeto[12] -- {alfabeto[12]}")
#else:
#    print("\t\t\t ***** GRUPO B *****")
#    print(f"\n nombre: {nombre}  -- sexo[{sexo}]")
#    #print(f"\n nombre {nombre[0]} -- {alfabeto[12]}")



#los tramos impositivos para la declaracion de la renta en un determinado pais
#son los sig:
#
# |---------------------|-----------------| 
# |        renta        | Tipo impositivo |
# |---------------------|-----------------|
# |Menos de 10000       |        5%       |
# |entre 10000 y 20000  |       15%       |
# |entre 20000 y 35000  |       20%       |
# |entre 35000 y 60000  |       30%       |
# |mas de 60000         |       45%       |
# |---------------------|-----------------|
#print ("\n\n\n ***** TIPO DE IMPOSITIVO ***** ")
#renta = float(input("\n ingresa tu renta: "))
#if(renta <10000):
#    print(f"\n Impositivo: 5% ")
#else:
#    if ((renta>=10000) or (renta<20000)):
#        print(f"\n Impositivo: 15% ")
#    else:
#        if ((renta>=20000) or (renta<35000)):
#            print(f"\n Impositivo: 20% ")
#        else:
#            if ((renta>=35000) or (renta<60000)):
#                print(f"\n Impositivo: 30% ")
#            else:
#                if(renta>60000):
#                    print(f"\n Impositivo: 45% ")
                    


#---------------------------------------------------
#print ("\n\n\n ***** COMPARADOR DE AÑOS ***** ")
#anioActual = int( input( "año actual: " ) )
#anio = int ( input( "escribe un año cualquiera: " ) )
#if (anio > anioActual):
#    restaFuturo = anio - anioActual
#    print(f'para llegar al año {anio} faltan {restaFuturo} años.')
#else:
#    if (anio < anioActual):
#        restaPaasdo = anioActual - anio
#        print(f'Desde el año {anio} han pasado {restaPaasdo} años.')
#    else:
#        if(anio == anioActual):
#            print(f'es el mismo año!')



#en una determinada empresa, sus empleados son evaluados al final de cada año. los
#que pueden obtener en la evaluacion comienan en 0.0 y pueden ir aumentando, traduciendose
#en mejores beneficios. los puntos que pueden conseguir los empleados pueden ser 0.0,
#0.4 o 0.6 o mas, pero no valores intermedios entre las cifra mencionadas.
#tabla con niveles correspondientes a cada puntuacion.
#la cantidad de dinero conseguida en cada nivel es de 2,400 multiplicada por la puntuacion
#del nivel
# |---------------------|-----------------| 
# |        nivel        |    puntuacion   |
# |---------------------|-----------------|
# |inaceptable          |       0.0       |
# |aceptable            |       0.4       |
# |meritorio            |    0.6 o mas    |
# |---------------------|-----------------|
#programa que lea la puntuacion del usuario e indique su nivel de rendimeinto, asi como
#la cantidad de dinero  que recibira el usuario 
#print("\n\n\n ***** SCORE USERS ***** ")
#user = input("nombre: ")
#evaluation = float(input("puntuacion en evaluacion: "))
#sueldo = evaluation * 2400 
#if (evaluation == 0.0):
#    print(f' Nombre: {user}\n Rendimiento: inaceptable\n Sueldo: {sueldo}')
#else:
#    if (evaluation == 0.4):
#        print(f' Nombre: {user}\n Rendimiento: aceptable\n Sueldo: {sueldo}')
#    else:
#        if (evaluation >= 0.6):
#            print(f' Nombre: {user}\n Rendimiento: meritorio\n Sueldo: {sueldo}')

               

#programa para una empresa que tiene salas de juegos para todas las edades y
#quiere calcular automaticamente el precio que debe cobrar a sus cliente4s por
#entrar. el programa debe preguntar al usuario la edad del cliente y mostrar el
#precio de la entrada. si el cliente es menor d 4 años puede entrar gratis, si
#tiene entre 4 y 18 años debe pagar 5 y si es mayor de 18 años 10.
#print("\n\n\n ***** VIDEO GAMES STORE ***** ")
#intentos = 0
#young = 5
#adult = 10
#user = input ("ingresa nombre: ")
#age = int(input("ingresa edad: "))
#while(age<0):
#    print ("error age")
#    age = int(input("ingresa edad: "))
#if ( age >= 19 ):
#    print(f'\tUser: {user}\n\tAge: {age}\n\tPrecio: {adult}')
#else:
#    if (age >=4):
#        print(f'\tUser: {user}\n\tAge: {age}\n\tPrecio: {young}')
#    else:
#        if (age <= 3):
#            print(f'\tUser: {user}\n\tAge: {age}\n\tPrecio: Free')



#la pizzeria bella napoli ofrece pizzas vegetarianas y no vegetarianas a sus
#clientes. los ingredientes para cada tipo de piza aparecen acontinuacion:
#   ingredientes vegetarianos: pimiento y tofu
#   ingredientes no vegetarianos: peperoni, jamon y salmon
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana
#o no, en funcion de su respuesta le muestre el menu con los ingredientes
#disponibles para que elija. solo se puede elegir un ingrediente ademas de la
#mozzarella y el tomate que estan en todas las pizzas. al final se debe mostrar
#en pantalla si la pizza elegida en pantalla es vegetariana y todos los
#ingredientes que lleva.
#print("\n\n\t\t ***** PIZZERIA BELLA NAPOLI ***** ")
#print("\tTipos: ")
#print("\t\t1. Pizza Vegetariana")
#print("\t\t2. Pizza No Vegetariana")
#opcionTipo = int(input("\n\tingresa tipo de pizza[1] ó [2]: "))
#print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
#if (opcionTipo == 1):
#    print("\n\tPizzas Vegetarianas:")
#    print("\t\t1. Pimiento")
#    print("\t\t2. Tofu")
#    opcionIngrediente = int (input("\n\t ingresa ingrediente [1] ó [2]: ") )
#    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
#    print("\n\tPIZZA VENDIDA")
#    print("\n\tIngredientes: ")
#    if (opcionIngrediente == 1):
#        print("\t\t-> Pimiento.\n\t\t-> Mozzarella.\n\t\t-> Tomate.")
#    elif (opcionIngrediente == 2):
#        print("\t\t-> Tofu.\n\t\t-> Mozzarella.\n\t\t-> Tomate.")
#elif (opcionTipo == 2):
#    print("\n\tPizzas No Vegetarianas:")
#    print("\t\t1. Jamón")
#    print("\t\t2. Pepperoni")
#    print("\t\t2. Salmón")
#    opcionIngrediente = int (input("\n\t ingresa ingrediente [1], [2] ó [3]: ") )
#    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *") 
#    print("\n\tPIZZA VENDIDA")
#    print("\n\tIngredientes: ")
#    if (opcionIngrediente == 1):
#        print("\t\t-> Jamón.\n\t\t-> Mozzarella.\n\t\t-> Tomate.")
#    elif (opcionIngrediente == 2):
#        print("\t\t-> Pepperoni.\n\t\t-> Mozzarella.\n\t\t-> Tomate.")
#    elif(opcionIngrediente == 3):
#        print("\t\t-> Salmón.\n\t\t-> Mozzarella.\n\t\t-> Tomate.")





#  ******    **    **    ******    **         ********    ******
#  *******   **    **   ********   **         ********   ********
#  **   **   **    **   **    **   **         **         **    **
#  ******    **    **   **         **         ********   *****
#  ******    **    **   **         **         ********      *****
#  **   **   **    **   **    **   **         **         **    **
#  ******     ******    ********   ********   ********   ********
#  *****       ****      ******    ********   ********    ******


        #bucles condicionales (while)

        #pregunta al usuario un numero hasta que se ingrese un 0 
        #************************************************************
        #num = None
        #while (num != 0):
        #    num = int(input("introduce un numero: "))
        #************************************************************
        #while(True):
        #    num = int(input("ingresa un numero: "))
        #    if(num == 0):
        #        break


        #bucles iterativos (for)

        #range(fin): genera una secuencia de numeros enteros desde 0 hasta fin-1
        #range(inicio, fin, salto): genera una secuencia de nuemeros enteros
        #desde inicio hasta fin-1 con un incremento de salto.
        #palabra = 'Python'
        #for letra in palabra:
        #    print(letra)    
        #for i in range(1, 10, 2):
        #    print(i, end=", ")
        
        # str -> convertir numero a cadena


#Escribir un programa que pida al usuario una palabra y la muestre por la
#pantalla 10 veces
#print("\n\n\t\t ***** PALABRA 10 VECES ***** ")
#word = input("\ningresa una palabra: ")
#for i in range (1,11,1):
#    print(i,". " + word )



#escribe un programa que pregunte al usuario su edad y muestre por pantalla
#todos los años que ha cumplido
#print("\n\n\t\t ***** AÑOS CUMPLIDOS ***** ")
#age = int(input("\ningresa tu edad: "))
#while(age<=0):
#    print("edad no valida")
#    age = int(input("\ningresa tu edad: "))
#for i in range( 1, age+1, 1):
#    print( str(i) + "años") 



#Escribir un programa que pida al usuario un numero entero positivo y muestre
#por pantalla todos los numeros impares desde 1 hasta ese numero separados por
#comas
#print("\n\n\t ***** NUMEROS IMPARES ***** ")
#number = int(input("ingresa un numero: "))
#while(number <= 0):
#    print("**** ERROR - INGRESA NUMEROS POSITIVOS ****")
#    number = int(input("ingresa un numero: "))
#for i in range(1, number+1, 2):
#    print(i, end=", ")



#Escribir un programa que pida al usuario un numero entero positivo y muestre
#por pantalla la cuenta atras desde ese numero hasta cero separado por comas
#print("\n\n\t ***** CUENTA REGRESIVA ***** ")
#number = int(input("\ningresa un numero: "))
#while(number<=0):
#    print("\n\t**** ERROR - INGRESA NUMEROS POSITIVOS ****")
#    number = int(input("\ningresa un numero: "))
#for i in range(number, -1, -1):
#    print(i, end=", ")



#Escribir un programa que pregunte al usuario una cantidad a invertir, el intere
#anual y el numero de años y muestre por pantalla el capital obtenido en la
#inversion cada año que dura la inversion.
#print("\n\n\t ***** CAPITAL ***** ")
#capital = int(input("\nCapital a invertir: "))
#interesAnual = int(input("Interes anual: "))
#anios = int(input("Numero de años: "))
#for i in range(1, anios+1, 1):
#    capital *= 1 + interesAnual / 100
#    print("anio " + str(i) + " capital obtenido " + str(capital) + ".")



#Escribir un programa que pida al usuario un numero entero y muestre por pantalla
#un triangulo rectangulo de altura el nuemro introducido como se muestra abajo:
#     *
#     **
#     ***
#     ****
#     *****
#print("\n\n\t ***** TRIANGULO RECTANGULO ***** ")
#triangle = int(input("ingresa un numero: "))
#while(triangle<=0):
#    print("\n\t**** ERROR - INGRESA NUMEROS POSITIVOS ****")
#    triangle = int(input("\ningresa un numero: "))
#for i in range(1, triangle+1, 1):
#    for j in range(1, i+1, 1):
#       print("*",end=" ")
#    print("")



#Escribir un programa que muestee en pantalla las tablas de multiplicar de 1 al
#10.
#print("\n\n\t ***** TABLAS DE MULTIPLICAR ***** \n")
#for i in range( 1, 10+1, 1):
#    for j in range( 1, 10+1, 1):
#        multiplicacion = i * j
#        print(f'{j}*{i}=',multiplicacion, end=f'\t')
#    print("\t")



#escribir un programa que pida al usuario un numero entero y muestre en pantalla
#un triangulo como el de abajo
#   1
#   3 1
#   5 3 1
#   7 5 3 1
#   9 7 5 3 1
#print("\n\n\t ***** TRIANGULO DE NUMEROS ***** ")
#number = int(input("\nInsert a number: "))
#while(number<=0):
#    print("\n\t**** ERROR - INSERT NUMBER POSITIVE ****")
#    number = int(input("\nInsert a number: "))
#for i in range(1, number+1, 2):
#    for j in range(i, 0, -2):
#        print(j, end=' ')
#    print("")



#Escribe un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña hasta que introduzca la
#contraseña correcta
#print("\n\n\t ***** PASSWORD ***** ")
#newPass = 'juancarlos'
#password = input("\nInsert Password: ")
#while(newPass != password):
#    print("\t***** PASSWORD DENEGED ***** ")
#    password = input("\nInsert Password: ")
#print("********************************************************************")
#print("\t ***** PASSWORD SUCCESSFUL")



#Escribir un programa que pida al usuario un numero entero y muestre en pantalla
#si es numero primo o no 
#print("\n\n\t ***** NUMEROS PRIMOS ***** ")
#number = int(input("\nInsert a number: "))
###############################example while
#i = 2
#while (number % i != 0):
#    i+=1   
#if(i==number):
#    print(str(number) + " es primo")
#else:
#    print(str(number) + " no es primo")
##############################example for
#for i in range(2,number,1):
#    if (number % i == 0):
#        break
#if ((i+1) == number):
#    print(str(number) + " es primo.")
#else:
#    print(str(number) + " no es primo.")



#escribir un programa que pida al usuario una palabra y luego muestre en pantalla
#una a una a letras de la palabra introducida empezando por la ultima.
#print("\n\n\t ***** LETTER ***** ")
#word = input("\nInsert word: ")
#for i in range(len(word)-1, -1, -1):
#    print(word[i])

   

#Escribe un programa en el que se pregunte al usuario por una frase y una letra
#y muestre por pantalla el numero de veces que aparece la letra en la frase
#print("\n\n\t ***** NUMERO DE LETRAS ***** ")
#frase = input("\nIngresa una frase: ")
#letra = input("\nIngresa una letra: ")
#contador = 0
#for i in frase:
#    if (i == letra):
#        contador = contador + 1
#print(f'cantidad de letras {letra}: {contador}')


        
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca
#hasta que el usuario escriba "salir que terminara"
#print("\n\n\t ***** ECO ***** ")
#while(True):
#    eco = input("\nWrite: ")
#    if((eco == 'salir') or (eco == 'SALIR')):
#        break
#print("FINISHED")
    




#        **        ********   ******   ********   ******    ******
#        **        ********  ********  ********  ********  ********
#        **           **     **    **     **     **    **  **    **
#        **           **      ****        **     **    **   ****
#        **           **        ****      **     ********     ****
#        **           **     **    **     **     ********  **    **
#        ********  ********  ********     **     **    **  ********
#        ********  ********   ******      **     **    **   ******




#     caracteristicas:
#       -> tiene orden
#       -> contiene elementos de distintos tipos
#       -> son mutables, pueden alterarse durante la ejecucion de un programa
#
#     LISTA VACIA
#       type([])
#       <class 'list'>
#       Lista con elementos de distintos tipos
#       [1, "dos", True]
#       Listas anidadas
#       [1, [ 2, 3], 4]
#
#     ACCESO A LOS ELEMENTOS DE UNA LISTA
#       -> Se utilizan los mismos operadores de accesso que para cadenas de
#          caracteres
#       -> l[i]: devuelve el elemento de la lista l con el indice i.
#
#            a = ['p', 'y', 't', 'h', 'o', 'n']
#            for i in range(1,len(a)+1,1):
#               print(a[i-1])
#
#     SUBLISTA
#       -> l[i:j:k]: devuelve la sublista desde el elemento de l con el indice i
#               hasta elemento anterior al indice j, tomando elementos cada k.
#
#           a = ['p', 'y', 't', 'h', 'o', 'n']
#           num1 = int(input("\nIngresa rango inicial: "))
#           num2 = int(input("Ingresa rango final: "))
#           num3 = int(input("\nIngresa intervalo: "))
#           print(f'tipo 1 ---->  a[{num1}:{num2}] ---->' + str(a[num1:num2]))
#           print(f'tipo 2 ---->  a[:-{num2}] ---->' + str(a[:-num2]))
#           print(f'tipo 3 ---->  a[:] ---->' + str(a[:]))
#           print(f'tipo 4 ---->  a[{num1}:{num2}:{num3}] ---->' + str(a[num1:num2:num3]))
#
#     OPERACIONES QUE NO MODIFICAN UNA LISTA
#       -> len(l): devuelve el numero de elementos de la lista l.
#       -> min(l): devuelve el minimo elemento de la lista  l siempre que los
#                  datos sean comparables.
#       -> max(l): devuelve el maximo elemento de la lista l siempre que los
#                  datos sean comparables.
#       -> sum(l): devuelve la suma de los elementos de la lista l, simpre que
#                  los datos se puedan sumar.
#       -> dato in l: devuelve True si el dato pertenece a la lista l y falso en
#                  caso encontrario
#       -> l.index(dato): devuelve la posicion que ocupa en la lista l el
#                  primer elemento con valor dato.
#       -> l.count(dato): devuelve el numero de veces que el valor dato esta
#                  contenido en la lista l
#       -> all(l): devuelve True si todos los elementos de la lista l son True y
#                  False en caso contrario
#       -> any(l): devuelve True si algun elemento de la lista l es True y False
#                  en caso contrario
#
#           l = [1, 2, 2, 3, 4, 2]
#           print("l = [1, 2, 2, 3, 4, 2]")
#           print("operacion len(l): " + str(len(l)))
#           print("operacion min(l): " + str(min(l)))
#           print("operacion max(l): " + str(max(l)))
#           print("operacion sum(l): " + str(sum(l)))
#           print("operacion dato in l: " + str(2 in l))
#           print("operacion l.index(dato): " + str(l.index(2)))
#           print("operacion l.count(dato): " + str(l.count(2)))
#           print("operacion all(l): " + str(all(l)))
#           print("operacion any([0, False, 3<2]): " + str(any([0, False, 3<2])))
#
#     OPERACIONES QUE MODIFICAN UNA LISTA
#       -> l1 + l2: crea una nueva lista concatenando los elementos de la lista
#                  l1 y l2.
#       -> l.append(dato): añade dato al final de la lista l.
#       -> l.extend(secuencia): añade los datos de secuencia al final de la
#                  lista l.
#       -> l.insert(indice, dato): inserta dato en la posicion indice de la lista
#                  l y desplaza los elementos una posicion a partir de la posicion
#                  indice
#       -> l.remove(dato): elimina el primer elemento con valor dato en la lista
#                  l y desplaza los que estan por detras de el una posicion hacia
#                  delante.
#       -> l.pop([indice]): devuelve el dato en la posicion indice y lo elimina
#                  de la lista l, desplazando los elementos por atras de el una
#                  posicion hacia delante.
#       -> l.sort(): ordena los elementos de la lista l deacuerdo al orden
#                  predefinido, siempre que los elementos sean comparables.
#       -> l.reverse(): invierte el orden de los elementos de la lista l.
#
#     COPIAS DE LISTAS
#       -> Copiar por referencia l1 = l2: asocia la variable l1 la misma lista
#                  que tiene asociada la variable l2, ambas variables apunta a 
#                  la misma direccion de memoria. cualquier cambio que hagamos
#                  a traves de l1 o l2 afectara a la misma lista.
#       -> Copia por valor l1 = list(l2): crea una copia de la lista asociada a
#                  l2 en una direccion de memoria diferente y se le asocia a l1.
#                  las variables apuntan a direcciones de memoria diferentes que
#                  contienen los mismos datos. cualquier cambio que hagamos a
#                  traves de l1 no afectara a la lista de l2 y viceversa.
#
#           a = [ 1, 2, 3]
#           b = a
#           print(b)
#           c = list(a)
#           print(c)





#       ********  **    **  ******    **          ****     ******
#       ********  **    **  *******   **         ******   ********
#          **     **    **  **    **  **        **    **  **    **
#          **     **    **  *******   **        **    **   ***    
#          **     **    **  ******    **        ********      ***
#          **     **    **  **        **        ********  **    **
#          **      ******   **        ********  **    **  ********    
#          **       ****    **        ********  **    **   ******




#     -> Una tupla es una secuencia ordenadas de objetos de distintos tipos.
#     -> Se contruye poniendo los elementos entre corchetes [] separados por ",".
#
#     Caracteristicas:
#       -> tiene orden
#       -> pueden contener elementos de distintos tipos
#       -> son inmutables, no pueden alterarse durante la ejecucion de un program
#
#     -> Se usan para representar colecciones de datos una determinada estructura
#        semantica, como un vector o una matriz.
#
#     TUPLA VACIA
#       >>> type(())
#           <class 'tuple'>
#
#     TUPLA CON ELEMENTOS DE DISTINTOS TIPOS
#       >>> (1, "dos", True )
#
#     VECTOR      
#       >>> ( 1, 2, 3)
#
#     MATRIZ
#       >>> (( 1, 2, 3), ( 4, 5, 6))
#
#     CREACION DE TUPLAS MEDIANTE LA FUNCION "tuple"
#
#     -> tuple(c): crea una tupla con los elementos de la secuencia o coleccion
#                  "c".
#     -> Se pueden indicar los elementos separados por comas, mediante una
#        cadena, o mediante una colección de elementos iterables.
#       
#       >>> tuple()
#           ()
#
#       >>> tuple([ 1, 2, 3])
#           (1,2,3)
#
#       >>> tuple("Python")
#           ('P', 'y', 't', 'h', 'o', 'n')
#
#     OPERACIONES CON TUPLAS
#
#     -> El acceso a los elementos de una tupla se realiza del mismo modo que en
#        las listas. Tambien se pueden obtener subtuplas de la misma manera que
#        las sublistas.
#     -> Las operaciones de listas que no modifican la lista tambien son aplicables
#        a las tuplas.
#
#       >>> a = (1, 2, 3)
#       >>> a[1]
#           2
#
#       >>> len(a)
#           3
#
#       >>> a.index(3)
#           2
#
#       >>> 0 in a
#           False
#
#    MATRIX
#       >>> b = ((1,2,3) ,(4,5,6))
#       >>> b[1]
#           (4,5,6)
#
#     -> b[vector_j][posicion_i]
#       >>> b[1][2]
#           6


#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matematicas, Fisica, Quimica, Historia y Lengua) en una lista y la muestre por
#pantalla.
#print("\n\n\t ***** ASIGNATURAS ***** ")
#asignaturas = [] #generar cadena vacia
#for i in range(0,5,1):
#    asignatura = input("\nIngresa asignatura: ")
#    asignaturas.append(asignatura)
#print(asignaturas)



#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matematicas, Fisica, Quimica, Historia y Lengua) en una lista y la muestre por
#pantalla el mensaje:
#           "yo estudio <asignatura>"
#donde asignatura es cad una de las asignaturas de la lista
#print("\n\n\t ***** YO ESTUDIO ***** ")
#asignaturas = [] #generar cadena vacia
#for i in range(0,5,1):
#    asignatura = input("\nIngresa asignatura: ")
#    asignaturas.append(asignatura)
#print(asignaturas)
#print("\n\n")
#for j in range(1,len(asignaturas)+1,1):
#    print("yo estudio " + (asignaturas[j-1]))



#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matematicas, Fisica, Quimica, Historia y Lengua) en una lista, pregunte al
#usuario la nota que ha sacado en cada asignatura, despues las muestre en
#en pantalla con el mensaje
#           "en <asignatura> has sacado <nota>
#donde asignatura es cada una de las asignaturas de la lista y nota cada una de
#las correspondientes notas introducidas por el usuario
#print("\n\n\t ***** CALIFICACIONES ***** ")
#asignaturas = [] #generar cadena vacia
#for i in range(0,5,1):
#    asignatura = input("\nIngresa asignatura: ")
#    asignaturas.append(asignatura)
#print(asignaturas)
#print("\n")
#calificaciones = []
#for j in range(0,len(asignaturas),1):
#    calificacion = int(input("\nIngresa calificacion {" + str(asignaturas[j]) + "]: "))
#    calificaciones.append(calificacion)
#print(calificaciones)
#print("\n")
#for k in range(0,len(asignaturas),1):
#    print("En " + str(asignaturas[k]) + " has sacado " + str(calificaciones[k] ))



#Escribe un programa que pregunte al usuario los numeros ganadores de la loteria
#primitiva los almacene en una lista y los muestre por pantalla ordenados de
#menor a mayor.
#import random #libreria para generar numeros random
#print("\n\n\t ***** LOTERIA PRIMITIVA ***** \n")
#winner = [] #generar cadena vacia
#for i in range(0,6,1):
#    #numbers = input("\nIngresa numero: ")
#    numbers = random.randint(1,49)
#    winner.append(numbers)
#print("Winner number: \n")
#print("\t" + str(winner))
#winner.sort() #ordena que menor a mayor 
#print("\nNumeros ordenados: " + str(winner))



#Escribe un programa que almacene en una lista los numeros del 1 al 10 y los
#muestre por pantalla en orden inverso separados por comas.
#print("\n\n\t ***** LISTA NUMEROS 1-10 [opcion. 1]***** \n")
#numeros = [1,2,3,4,5,6,7,8,9,10]
#for i in  range(1,11,1):
#    reversa = numeros[-i]
#    print(reversa, end = " ,")
#print("\n\n\t ***** LISTA NUMEROS 1-10 [opcion. 2]***** \n")
#numeros = [1,2,3,4,5,6,7,8,9,10]
#print(numeros)
#numeros.reverse()
#for numero in numeros:
#    print(numero, end=" ,")



#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matematicas, Fisica, Quimica, Historia y Lengua) en una lista, pregunte la nota
#que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas
#al final el programa debe mostrar por pantalla las asignaturas que el ususario  
#tiene que repetir.
#print("\n\n\t ***** CALIFICACIONES ***** ")
#asignaturas = [] #generar cadena vacia
#for i in range(0,5,1):
#    asignatura = input("\nIngresa asignatura: ")
#    asignaturas.append(asignatura)    
#print(asignaturas)
#calificaciones = []
#reprobadas = []
#posicion = 0
#for posicion in range(0, len(asignaturas), 1):
#    calificacion = int(input( "\nIngresa calificacion {" + str(asignaturas[posicion]) + "]: " ))
#    calificaciones.append(calificacion)
#    if (calificacion <= 5):
#        reprobadas.append(posicion)     
#print(calificaciones)
#print("\n materias reprobadas ubicadas en posicion: " + str(reprobadas))
#print("\n\t---------Materias---------")
#for k in range(0,len(asignaturas),1):
#    print("En " + str(asignaturas[k]) + " has sacado " + str(calificaciones[k] ))
#print("\n\t---------Materias a Recursar ---------")
#for m in range(0, len(asignaturas), 1):
#    for n in reprobadas:
#        if (m == n):
#            print("Materia: " + asignaturas[m] + " \tCalificacion: " + str(calificaciones[n]))


 
#Escribir un programa que almacene el abecedario en una lista, elimine de la
#lista las letras que ocupen posiciones multiplos de 3, y muestre en pantalla la
#lista resultante
#print("\n\n\t ***** ABECEDARIO MULTIPLO DE 3 ***** ")
#abecedario = []
#multiplo3 = 3
#letraMultiplo = []
#eco = input("\nWrite: ")
#for i in range( 0, len(eco), 1):
#    abecedario.append(eco[i])
#print(abecedario)
#for posicion in range(len(abecedario)-1,-1,-1):
#    #print( str(posicion) + ".- " + abecedario[posicion])
#    residuo =  posicion % multiplo3
#    if(residuo == 0):
#        print( str(posicion) + ".- " + abecedario[posicion])
#        #print("multiplo de 3: " + str(j))
#        abecedario.pop(posicion)
#print(abecedario)



#Escribir un programa que pida al usuario una palabra y mmuestre en pantalla si
#es un palindromo.
#print("\n\n\t ***** PALINDROMO ***** ")
#palabra1 = []
#palabra2= []
#teclado = input("\nWrite: ")
#for i in range(0, len(teclado), 1):
#    palabra1.append(teclado[i])    
#print(palabra1)
#for j in range(len(palabra1)-1,-1,-1):
#    print(str(j) + " " + palabra1[j])
#    palabra2.append(palabra1[j])
#print(palabra2)
#_________________________________________________posible function 2
#teclado = input("Introduce una palabra: ")
#reversed_word = teclado
#teclado = list(teclado)
#reversed_word = list(reversed_word)
#reversed_word.reverse()
#__________________________________________________________________________
#if (palabra1 == palabra2):
#    print("Palindromo")
#elif (palabra1 != palabra2):
#    print("no es palindromo")



#Escribir un programa que pida al usuario una palabra y muestre por pantalla el
#numero de veces que contiene cada vocal.
#print("\n\n\t ***** VECES VOCAL ***** ")
#palabra = input("\nWrite: ")
#--------------------------------------------------------opcion1
#contador1 = 0
#contador2 = 0
#contador3 = 0
#contador4 = 0
#contador5 = 0
#for j in range( 0, len(palabra), 1):
#    print(palabra[j])
#    if((palabra[j] == 'a') or (palabra[j] == 'A')):
#        contador1 = contador1 + 1
#    elif ((palabra[j] == 'e') or (palabra[j] == 'E')):
#        contador2 = contador2 + 1
#    elif ((palabra[j] == 'i') or (palabra[j] == 'I')):
#        contador3 = contador3 + 1
#    elif ((palabra[j] == 'o') or (palabra[j] == 'O')):
#        contador4 = contador4 + 1
#    elif ((palabra[j] == 'o') or (palabra[j] == 'U')):
#        contador5 = contador5 + 1
#print("vocal a = " + str(contador1))
#print("vocal e = " + str(contador2))
#print("vocal i = " + str(contador3))
#print("vocal o = " + str(contador4))
#print("vocal u = " + str(contador5))
#--------------------------------------------------------------------fin1
#-------------------------------------------------------------opcion2
#vocales = [ 'a', 'e', 'i', 'o', 'u']
#con = [ 0, 0, 0, 0, 0]
#for i in range( 0, len(vocales), 1):
#    #print(vocales[i])
#    for j in range(0, len(palabra), 1):
#        #print(palabra[j])
#        if ( palabra[j] == vocales[i]):
#            con[i] = con[i] + 1
#    print("vocal " + str(vocales[i]) + ": " + str(con[i]))
#--------------------------------------------------------------------fin2



#Escribir un programa que almacene en una lista los siguientes precios: 50, 75,
#46, 22, 80, 65, 8, y muestre por pantalla el menor y mayor de los precios
#print("\n\n\t ***** PRECIOS ALTOS Y BAJOS ***** ")
#numeroProductos = int(input("\nIngresa la cantidad de productos: "))
#precios = []
#for i in range(0, numeroProductos, 1):
#    valor = float(input("\nPrecio: "))
#    precios.append(valor)
#print(precios)
#print( "Precio minimun: " + str(min(precios)))
#print( "Precio miximun: " + str(max(precios)))



#Escribir un programa que almacene los vectores(1,2,3) y (-1,0,2) en dos listas
#y muestre por pantalla su producto escalar
#formula para calcula el producto escalar de dos vectores
#     ->    ->    ->   ->
#     u  .  v =  |u| . |v| cos alpha
#print("\n\n\t ***** PRODUCTO ESCALAR ***** ")
#vector1 = [ 1, 2, 3]
#vector2 = [-1, 0, 2]
#resultadoMultiplicacion = []
#alpha = float(input("\nInsett alpha: "))
#for i in range( 0, len(vector1), 1):
#    #print(vector1[i])
#    for j in range(0, len(vector2), 1):
#        #print(vector2[j])
#        if(i == j):
#            multiplicacion = vector1[i] * vector2[j]
#            print("[" + str(i) + "] * [ " + str(j) + "]: " + str(multiplicacion))
#            resultadoMultiplicacion.append(multiplicacion)
#            print( "suma " + str(sum(resultadoMultiplicacion)))



#Escribir un programa que almacene las matrices
#         | 1  2  3 |           | -1  0 |
#     A = |         |       B = |  0  1 |
#         | 4  5  6 |           |  1  1 |
#en una lista y muestre por pantalla su producto
#NOTA: Para representar matrices mediante listas usar listas anidadas,
#representando cada vector fila en una lista.
#print("\n\n\t ***** PRODUCTO DE MATRICES ***** ")
#a = [ (1, 2, 3),
#      (4, 5, 6)]
#b = [ (-1, 0),
#      (0, 1),
#      (1, 1)]
#result = [[0,0],
#          [0,0]]
#for i in range(0, len(a), 1):
#    print("i[" + str(i) + "]")
#    #print(a[i])
#    #print("\n")
#    for j in range(0, len(b[i]), 1):
#        print("j[" + str(j) + "]")
#        #print(b[j])
#        #print("\n")
#        for k in range(len(b)):
#            #print("k[" + str(k) + "]")
#            #print(b[k])
#            result[i][j] += a[i][k] * b[k][j]
#            print( "resultado= "+ str(result[i][j]))
#for i in range(len(result)):
#    result[i] = tuple(result[i])
#result = tuple(result)
#for i in range(len(result)):
#    print(result[i])
    


#Escribir un programa que pregunte por una muestra de numeros, separados por
#comas, los guarde en una lista y muestre por pantalla su media y desviacion
#tipica
#________________________________________________________________miOpcion
#print("\n\n\t ***** PRODUCTO DE MATRICES ***** ")
#import math
#muestra = []
#teclado =  input("Escribe la muestra: ")
#for i in range(0, len(teclado), 1):
#    if(teclado[i] != ','):
#        muestra.append(float(teclado[i]))
#print(muestra)
#suma = 0
#suma = sum(muestra)
#sumResta = 0
#for j in range(0, len(muestra),1):
#    #print("pos["+ str(j) + "]= " + str(muestra[j]))
#    #suma += muestra[j]
#    media = suma / len(muestra)
#    #suma = sum(muestra) / (len(muestra))
#    resta = ((muestra[j] - media)**2)
#    sumResta += resta
#    #print("resta [" + str(j)+ "]" + str(resta))
##print( "Suma= " + str(suma))
##print( "Suma Resta= "+ str(sumResta))
#print( "Media= " + str(media))
#division = (sumResta) / (len(muestra))
#raizCuadrada = math.sqrt(division)
#print("Division= " + str(division))
#print("Desviacion Estandar= " + str(raizCuadrada))
#______________________________________________________________miOpcionFin
#_______________________________________________________________Otraopcion
#sample = input("Introduce una muestra de números separados por comas: ")
#sample = sample.split(',')
#n = len(sample)
#for i in range(n):
#    sample[i] = int(sample[i])
#sample = tuple(sample)
#sum = 0
#sumsq = 0
#for i in sample:
#    sum += i
#    sumsq += i**2
#mean = sum/n
#stdev = (sumsq/n-mean**2)**(1/2)
#print('La media es', mean, ', y la desviación típica es', stdev)
#_____________________________________________________________OtraOpcionFin






# *****    ********  ******   ******  ********  ******  **    **   ****   ******   ********  ******   ******
# ******   ******** ******** ******** ******** ******** ***   **  ******  *******  ******** ******** ********
# **   **     **    **    ** **    **    **    **    ** ****  ** **    ** **    **    **    **    ** **    **
# **    **    **    **    ** **    **    **    **    ** ** ** ** **    ** **    **    **    **    **  ****
# **    **    **    **       **          **    **    ** ** ** ** ******** *******     **    **    **    ****
# **   **     **    **    ** **    **    **    **    ** **  **** ******** *******     **    **    ** **    **          
# ******   ******** ******** ******** ******** ******** **   *** **    ** **   **  ******** ******** ********
# *****    ********  ******   ******  ********  ******  **    ** **    ** **    ** ********  ******   ******                   




#     ->Diccionario: es una colección de pares formados por una clave y un valor
#                    asociado a la clave.
#     
#     ->Se construye poniendo los pares entre llaves "{}" separados por comas, y
#       separando la clave del valor con dos puntos ":".
#
#     ->Se caracteriza por:
#          -No tienen orden.
#          -Pueden contener elementos de distintos tipos.
#          -Son mutables, es decir, pueden alterarse durante la ejecución de un
#            programa.
#          -Las claves son únicas, es decir, no pueden repetirse en un mismo
#            diccionario, y pueden ser de cualquier tipo de datos inmutables.
#
#     DICCIONARIO VACIO
#       >>> type({})      
#           <class 'dict'>
#     
#     DICCIONARIO CON ELEMENTOS DE DISTINTOS TIPOS
#       {'nombre':'Alfredo', 'despacho': 218, 'email':'carlos@gmail.com'}
#
#     DICCIONARIOS ANIDADOS
#       {'nombre_completo': {'nombre': 'carlos', 'Apellidos': 'guillermo'}}
#
#     ACCESO A LOS ELEMENTOS DE UN DICCIONARIO
#        -> d[clave]: devuelve el valor del diccionario "d" asociado a la clave 
#                     "clave". Si en el diccionario no existe esa clave devuelve
#                     un error.
#        -> d.get(clave,valor): devuelve el valor del diccionario "d" asociado a
#                     la clave "clave". Si en el diccionario no existe esa clave
#                     devuelve "valor", y si no se especifica un valor por
#                     defecto devuelve "None
#
#     EJEMPLO
#       a = {'nombre': 'Carlos', 'despacho': 128, 'email': 'carlos@gmail.com'}
#       print(a)
#       nom = a['nombre']
#       desp = a['despacho']
#       print(nom)
#       print(desp)
#       a['despacho'] = 210 #---> se modifica el valor de despacho 128 a 210.
#       print(a) 
#       obtener = a.get('email') -->obtiene el email
#       print(obtener)
#       obtener1 = a.get('universidad', 'gmail')
#       print(obtener1)
#
#     OPERACIONES QUE NO MODIFICAN UN DICCIONARIO
#       -> len(d): devuelve el número de elementos del diccionario "d".
#       -> min(d): devuelve la mínima clave del diccionario "d" siempre que las
#                  claves sean comparables.
#       -> max(d): devuelve la máxima clave del diccionario "d" siempre que las
#                  claves sean comparables.
#       -> sum(d): devuelve la suma de las claves del diccionario "d", siempre
#                  que las claves se puedan sumar.
#       -> clave in d: devuelve "True" si la clave "clave" pertenece al
#                  diccionario "d" y "False" en caso contrario.
#       -> d.keys(): devuelve un iterador sobre las claves de un diccionario.
#       -> d.values(): devuelve un iterador sobre los valores de un diccionario.
#       -> d.items(): devuelve un iterador sobre los pares clave-valor de un 
#                  diccionario. 
#       
#     EJEMPLOS
#       d = {'nombre': 'Carlos', 'despacho': 128, 'email': 'carlos@gmail.com'}
#       longitud = len(d)        #--> devueve la cantidad de items(articulos)
#       minimo = min(d)
#       clavein = 'email' in d   #--> busca la palabra 'email' in d y devuelve si existe o no  
#       claves = d.keys()        #--> devuelve las claves
#       valores = d.values()     #--> devuelve los valores de las llaves
#       articulos = d.items()    #--> devuelve informacion de cada articulo
#       print(longitud)
#       print(minimo)
#       print(clavein)
#       print(claves)
#       print(valores)
#       print(articulos)
#
#     OPERACIONES QUE MODIFICAN UN DICCIONARIO
#       -> d[clave] = valor: Añade al diccionario "d" el par formado por la
#                   clave "clave" y el valor "valor".
#       -> d.update(d2): Añade los pares del diccionario "d2" al diccionario "d".
#       -> d.pop(clave, alternativo): devuelve del valor asociado a la clave
#               "clave" del diccionario "d" y lo elimina del diccionario. Si la 
#               clave no está, devuelve el valor "alternativo".
#       -> d.popitem(): devuelve la tupla formada por la clave y el valor del
#               ultimo par añadido al diccionario "d" y lo elimina del diccionario.
#       -> del d[clave]: elimina del diccionario "d" el par con la clave "clave".
#       -> d.clear(): elimina todos los pares del diccionario "d" de manera que
#               se queda vacía.
#                       
#     EJEMPLOS
#       d = {'nombre': 'Carlos', 'despacho': 128, 'email': 'carlos@gmail.com'}
#       print(d)
#       d['universidad'] = 'CUE'
#       print(d)
#       eliminar = d.pop('despacho') #--> Elimina el articulo especificando la clave a borrar
#       print(eliminar)
#       print(d)
#       eliminarItem = d.popitem()   #--> Se elimina todo el item('varaible', 'valor')
#       print(eliminarItem)
#       print(d)
#       del d['email']      #--> Borrar el email 
#       print(d)
#       limpiarTodo = d.clear()      #--> Limpia todo el diccionario 
#       print(limpiarTodo)
#       print(d)
#
#     COPIA DE DICCIONARIOS
#       -> copia por referencia [d1 = d2]:
#               - Asocia la variable d1 el mismo diccionario que tiene asociado
#                 la variable "d2", es decir, ambas variables apuntan a la misma
#                 direccion de memoria. Cualquier cambio que hagamos a tráves de
#                 l1 o l2 afectará al mismo diccionario.
#       EJEMPLO
#            d1 = {1:'A', 2:'B', 3:'C'}
#            d2 = d1
#            print(d2)
#            copiarXreferencia = d2.pop(2)
#            print(copiarXreferencia)
#            print(d2)
#            print(d1)
#
#       -> copia por valor [d1 = list(2)]:
#               - Crea una copia del diccionario asociado a "d2" en una direccion
#                 de memoria diferente y se la asocia a "d1". Las variables
#                 apuntan a direcciones de memoria diferentes que contienen los
#                 mismos datos. Cualquier cambio que hagamos a tráves de l1 no
#                 afectará al diccionario de l2 y viceversa.
#
#       EJEMPLO
#           d1 = {1:'A', 2:'B', 3:'C'}
#           d2 = dict(d1)
#           print(d2)
#           copiarXvalor = d2.pop(2)
#           print(copiarXvalor)
#           print(d2)
#           print(d1)


#Escribir un programa que guarde en una variable el diccionario:
#       {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
#, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso
#si la divisa no está en el diccionario.
#_____________________________________________________________________miOpcion
#print("\n\n\t ***** SIMBOLO DE DIVISAS ***** ")
#diccionarioDivisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
#teclado = input("\nIngresa el tipo de Divisa: ")
#if (teclado in diccionarioDivisas):
#    imprimirValor = diccionarioDivisas[teclado]
#    print("Símbolo: " + imprimirValor)
#else:
#    print("\t\t !!!!!!La divisa no se encuentra!!!!!!")
#__________________________________________________________________miOpcionFin
#__________________________________________________________________otraOpcion
#print("\n\n\t ***** SIMBOLO DE DIVISAS ***** ")
#diccionarioDivisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
#ingresaDivisa = input("\nIngresa el tipo de Divisa: ")
#div = ingresaDivisa.title() #--> Coloca la primera letra en mayuscula y las demas minusculas
#print(div)
#div1 = diccionarioDivisas.get(div, "!!!!!!!La divisa no está!!!!!!!")
#print("Símbolo: " + div1)
#________________________________________________________________otraOpcionFin



#Escribir un programa que pregunte al usuario su nombre, edad, direccion y
#telefono y lo guarde en una direccion. Despues debe mostrar por pantalla el
#mensaje.
# <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>
#print("\n\n\t ***** INFORMACIÓN PERSONAL ***** ")
#_______________________ nulo = None
#datoNombre = input("\nIngresa el nombre: ")
#datoEdad = int(input("\nIngresa la edad: "))
#datoNacionalidad = input("\nIngresa la nacionalidad: ")
#datoTelefono = int(input("\nIngresa el telefono: "))
#informacionPersona = {'Nombre': datoNombre,
#                      'Edad': datoEdad,
#                      'Nacionalidad': datoNacionalidad,
#                      'Telefono': datoTelefono}
#print(informacionPersona)
#obtenerNombre = informacionPersona['Nombre']
#obtenerEdad = informacionPersona['Edad']
#obtenerNacionalidad = informacionPersona['Nacionalidad']
#obtenerTelefono = informacionPersona['Telefono']
#print(obtenerNombre + " tiene " + str(obtenerEdad) + " años. vive en " + obtenerNacionalidad + " y su numero es " + str(obtenerTelefono))



#Escribir un programa que guarde en un diccionario los precios de las frutas de
#la tabla, pregunte al usuario por una fruta, un numero de kilos y muestre por
#pantalla el precio de ese número de kilos de fruta. si la fruta no está en el
#diccionario debe mostrar un mensaje informando de ello.
#       |-----------|------------|
#       |   fruta   |   Precio   |
#       |-----------|------------|
#       |  Plátano  |    1.35    |
#       |  Manzana  |    0.80    |
#       |  Pera     |    0.85    |
#       |  Naranja  |    0.70    |
#       |-----------|------------|
#print("\n\n\t ***** PRECIOS NUEVOS DE FRUTA ***** ")
#diccionarioFrutas = {'Platano':None, 'Manzana':None, 'Pera': None, 'Naranja':None}
#print(diccionarioFrutas)
#precioPlatano = float(input("\nIngresa el precio($)xKg de Platano: "))
#diccionarioFrutas['Platano'] = precioPlatano
#precioManzana = float(input("\nIngresa el precio($)xKg de Manzana: "))
#diccionarioFrutas['Manzana'] = precioManzana
#precioPera = float(input("\nIngresa el precio($)xKg de Pera: "))
#diccionarioFrutas['Pera'] = precioPera
#precioNaranja = float(input("\nIngresa el precio($)xKg de Naranja: "))
#diccionarioFrutas['Naranja'] = precioNaranja
#print(diccionarioFrutas)
#mult = 0
#kilogramo = 0
#while(True):
#    print("\n------------------------------------------------------------")
#    elegirOpcion = input("\n\t> Nombre de Producto Fruta: ")
#    elegirFruta = elegirOpcion.title()
#    if(elegirFruta in diccionarioFrutas):
#        kilogramo = float(input("\t> Kilos a Comprar: " ))
#        #print(diccionarioFrutas[elegirFruta])
#        mult = kilogramo * (diccionarioFrutas[elegirFruta])
#        print("\t>Total = " + str(mult))
#    elif((elegirOpcion == 'salir') or (elegirOpcion == 'SALIR')):
#        break
#print("FINISHED")



#Escribir un programa que pregunte una fecha en formato: "dd/mm/aaaa" y muestre
#por pantalla la misma fecha en formato: "dd de <mes> de aaaa donde <mes> es el
#nombre del mes.
#print("\n\n\t ***** FECHA ***** ")
#dicMes = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio',
#       7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Novimbre', 12:'Diciembre'}
#dicMesDias = {"Enero":31, "Febrero":28, "Marzo":31, "Abril":30, "Mayo":31, "Junio":30,
#       "Julio":31, "Agosto":31, "Septiembre":30, "Octubre":31, "Noviembre":30, "Diciembre":31}
#vec = []
#vecFech = []    
#while(True):
#    print("\n------------------------------------------------------------")
#    fecha = input("\n>Ingresa fecha(dd/mm/aaaa): ")
#    if (len(fecha) == 10):
#        #print("\nLongitud de la fecha es = 10 ")
#        vector = fecha.split('/') #--->> [split(simbolo)]divide una cadena deacuerdo a su simbolo 
#        for j in range(0, len(fecha), 1):
#            vecFech.append(fecha[j])
#        #print(vecFech)    
#        if((vecFech[2] == '/') and (vecFech[5] =='/')):
#            #print(vecFech[2] + "== /" )
#            for i in range(0, len(vector), 1):
#                vec.append(int(vector[i]))
#            #print(vec)
#            if(vec[1] in dicMes ):
#                mes = dicMes[vec[1]]
#                dias = dicMesDias[mes]
#                #print(dias)
#                if((vec[0] <= dias)):
#                    print("\nDia correcto")
#                    print( str(vec[0]) + " de " + mes + " de " + str(vec[2]))
#                else:
#                    print("\nDia no existe en " + mes)
#            else:
#                print("\nEl mes esta incorrecto.")
#        else:
#            print("\n ! estan mal colocados los [/] !!! ")
#    else:
#        print("\nLongitud diferente de 10")        
#    if((fecha == 'salir') or (fecha == 'SALIR')):
#        break
#print("FINISHED")



#Escribir un programa que almacene el diccionario con los créditos de las
#asignaturas de un curso {'Matematicas':5, 'Física':4, 'Química':6} y después
#muestre por pantalla los créditos de cada asignatura en el formato <asignatura>
#tiene <créditos> crédtios, donde <asignatura> es cada una de las asignaturas
#del curso, y <créditos> son sus créditos. Al final debe mostrar también el
#número de créditos del curso.
#_____________________________________________________________________miOpcion
#print("\n\n\t ***** CURSO ESCOLAR ***** ")
#dicAsig = {}
#dicCredi = {}
#for i in range(0, 3, 1):
#    nomMater = input("\nIngresa la materia: ")
#    dicAsig[i+1] = nomMater
##print(dicAsig)
#print("\n")
#for j in range(0, len(dicAsig), 1):
#    posAsig = dicAsig[j+1]
#    valCredi = float(input("Ingresa número de créditos en " + posAsig + ": "))
#    dicCredi[posAsig] = valCredi 
#print(dicCredi)
#print("\n")
#for k in range(0, len(dicAsig),1):
#    posAsig1 = dicAsig[k+1]
#    posCred1 = dicCredi[posAsig1]
#    print( "\t- " + posAsig1 + " tienes " + str(int(posCred1)) + " créditos.")
#sumaCreditos = sum(dicCredi.values())
#print("\n\t> Total Créditos del Curso: " + str(sumaCreditos))
#__________________________________________________________________miOpcionFin
#__________________________________________________________________otraOpcion
#course = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
#total_credits = 0
#for subject, credits in course.items():
#    print(subject, 'tiene', credits, 'créditos')
#    total_credits += credits
#print('Número total de créditos del curso: ', total_credits)
#_________________________________________________________________otraOpcionFin



#Escribir un programa que cree un diccionario vacío y la vaya llenando con
#información sobre una persona(por ejemplo nombre, edad, sexo, telefono, email, etc.)
#que le pida al usuario. Cada vez que se añada un nuevo dato debe imprimir el
#contenido del diccionario.
#print("\n\n\t ***** INFORMACION PERSONAL ***** ")
#dicPersons = {}
#dicEdad = {}
#dicSexo = {}
#dicPhone = {}
#dicEmail = {}
#opcion = input("\n¿Deseas ingresar información de otra persona?\n\t\t[si/no] \n\t\t > ").title()
#contador = 0
#while(opcion == 'Si'):
#    contador += contador
#    print("\n_________________________Ingresar datos personales_________________________")
#    nomPersona = input("\n   > Ingresa nombre: ").title()
#    dicPersons[contador+1] = nomPersona
#    nomPersona1 = dicPersons[contador+1]
#    edadPersona = int(input("   > Edad: "))
#    dicEdad[nomPersona1] = edadPersona
#    sexoPersona = input("   > Sexo[F/M]: ").title()
#    dicSexo[nomPersona1] = sexoPersona
#    phonePersona = input("   > Número telefonico: ")
#    while((len(phonePersona)) != 10):
#        phonePersona = input("   > Número telefonico: ")
#    dicPhone[nomPersona1] = int(phonePersona)
#    emailPersona = input("   > Email: ")
#    dicEmail[nomPersona1] = emailPersona
#    print("___________________________________________________________________________")
#    opcion = input("\n¿Deseas ingresar información de otra persona?\n\t\t[si/no] \n\t\t > ").title()
#print(dicPersons)
#print(dicEdad)
#print(dicSexo)
#print(dicPhone)
#print(dicEmail)



#Excribir un programa que cree un diccionario simulando una cesta de la compra.
#El programa debe preguntar el artículo y su precio y añadir el par al diccionario
#hasta que el usuario decida terminar. Después se debe mostrar por pantalla la
#lista de la compra y el coste total, con el siguiente formato.
#
#           |----------------------------------|
#           |        Lista de la compra        |
#           |----------------------------------|
#           |nombre del articulo  |   Precio   |
#           |---------------------|------------|
#           | Articulo 1          |   Precio1  |
#           | Articulo 2          |   Precio2  |
#           | Articulo 3          |   Precio3  |
#           | ....                |   ....     |
#           | Total               |   Costo    |
#           |----------------------------------|
#print("\n\n\t ***** MINISUPER ***** ")
#dicIndi = {}
#dicProd = {}
#print("\n********************************************************************")
#opCompra = input("\n\t Realizar compra [SI/NO]: \n\t\t > ").title()
#contador = 0
#print("\n********************************************************************")
#while(opCompra == 'Si'):
#    contador += contador
#    nombProducto = input("\t> Nombre Producto o finalizar[Fin]: ").title()
#    if(nombProducto == 'Fin'):        
#        break
#    precProducto = float(input("\t> Precio: "))
#    dicProd[nombProducto] = precProducto
##print(dicProd)
#print("\n********************************************************************")
#impTicket = input("\n\t Imprimir Ticket [SI/NO]: \n\t\t > ").title()
#print("\n********************************************************************")
#costoTotal = 0
#print("\n\t\tLISTA DE COMPRAS ")
#print("\n\t |----------------------------|")
#print("\t       PRODUCTO    |  PRECIO   ")
#print("\t |-----------------|----------|")
#for (nombProducto, precProducto) in dicProd.items():
#    print("\t  > " + nombProducto + "......... $" + str(precProducto))
#    costoTotal += precProducto    
#print("\t |----------------------------|")    
#print("\t        Total      | $" + str(costoTotal) )
#print("\t |----------------------------|")



#Escribir un programa que cree un diccionario de traducción español-inglés. El
#usuario introducirá las palabras en español e ingles separadas por dos puntos,
#y cada para <palabra>:<traducción> separados por comas. El programa debe crear
#un diccionario con las palabras y sus traducciones.después pedirá una frase en
#español y utilizará el diccionario para traducirla palabra a palabra. si una
#palabra no está en el diccionario debe dejarla sin traducir.
#dicTraduccion = {}
#dividirPalabra = []
#while(True):
#    print("\n\n\t\t ********** TRADUCTOR ********** ")
#    print('\t\t      " ESPAÑOL - INGLÉS "')
#    print("\n\t\t 1. Agregar Palabra. ")
#    print("\t\t 2. Traducción. ")
#    print("\t\t 3. Salir. ")
#    opcion = int(input("\n\t\t      Número de opcion: \n\t\t      > "))
#    print("\t\t ******************************* ")
#    while(opcion == 1):
#        print("\t\t       1. AGREGAR PALABRA.")
#        print("\n\t\t      Formato para agregar: ")
#        print("\t\t      > [Español]:[ingles]")
#        print("\n\t\t      Para salir ingresa [*] ")
#        while(True):
#            palabra = input("\n\t\t > ")
#            if(palabra == '*'):
#                break
#            if(':' in palabra):
#                dividirPalabra = palabra.split(':')
#                dicTraduccion[dividirPalabra[0]] = dividirPalabra[1]
#                #print(dicTraduccion)
#            elif((':' in palabra) == False):
#                print("\t\t !!! Formato incorrecto!!!")
#        break
#    while(opcion == 2):
#        print("\t\t         2. Traducción.")
#        print("\n\t\t         Forma de uso: ")
#        print("\t\t  Ingresa una frase en español.")
#        print("\t\t     Para salir ingresa [*]")
#        while(True):
#            print('_'*83)
#            frase = input("\n > ")
#            if(frase == "*"):
#                break
#            dividirFrase = frase.split(' ')
#            #print(dividirFrase)
#            print("Traduccion: ")
#            for j in dividirFrase:
#                if(j in dicTraduccion):
#                    traduccion = dicTraduccion[j]
#                    print(traduccion, end=' ')
#                else:
#                    print(j, end=' ')
#            print("")
#        break
#    if(opcion == 3):
#        print("\n\t\t   !!!!!!!! GOOD BYE !!!!!!!!")
#        break
#    elif(opcion>3):
#        print("\t\t   !!!! NUMBER INCORRECT !!!!")
#        print("\t\t ******************************* ")



#Escribir un programa que gestinone las facturas pendientes de cobro de una
#empresa. Las facturas se almacenarán en un diccionario donde la clave de cada
#factura será el número de factura y el valor el coste de la factura. El
#programa debe preguntar al usuario si quiere añadir una nueva factura, pagar
#una existente o terminar.Si desea añadir una nueva fatura se preguntará por el
#número de factura y su coste y se añadirá al diccionario. Si se dedsea pagar
#una factura se preguntará por el número de factura y se eliminará del
#diccionario. Después de cada operación el programa debe mostrar por pantalla la
#cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
#dicIndFacturas = {}
#dicFacTotal = {}
#dicFacPagadas = {}
#while(True):
#    print("\n\t\t ********** GESTIÓN DE FACTURAS ********** ")
#    print("\n\t\t 1. Añadir nueva factura. ")
#    print("\t\t 2. Pagar factura. ")
#    print("\t\t 3. Información del día. ")
#    print("\t\t 4. Terminar. ")
#    opcMenu = input("\n\t\t Elige un opción:\n\t\t\t > ")
#    if(opcMenu == '4'):
#        print("\n\t\t ***************************************** ")
#        print("\n\t\t          !!! VUELVAOS PRONTO !!!")
#        break
#    while(opcMenu == '1'):
#        print("\n\t\t ***************************************** ")
#        print("\t\t 1. Añadir nueva factura. ")
#        print("\n\t\t       NOTA: Para Salir ingresa [*].")
#        serFactura = input("\n\t\t Serie de factura: ")
#        if((serFactura == '*')):
#            break
#        canFactura = input("\t\t Cantidad a pagar: ")
#        dicIndFacturas[serFactura] = float(canFactura)
#        dicFacTotal[serFactura] = float(canFactura)
#        #print(dicIndFacturas)
#        print("\n\t\t ***************************************** ")
#    while(opcMenu == '2'):
#        print("\n\t\t ***************************************** ")
#        print("\t\t 2. Pagar factura. ")
#        print("\n\t\t       NOTA: Para Salir ingresa [*].")
#        pagFactura = input("\n\t\t Ingresa serie de factura: \n\t\t > ")
#        if(pagFactura == "*"):
#            break
#        if(pagFactura in dicIndFacturas):
#            opcPagFact = input("\t\t ¿Desea pagar factura? \n\t\t [Si|No] > ").title()
#            busFactura = dicIndFacturas[pagFactura]
#            if(opcPagFact == 'Si'):
#                print("\n\t\t         !!!! Factura PAGADA !!!!")
#                eliminar = dicIndFacturas.pop(pagFactura)
#                #print(dicIndFacturas)
#                dicFacPagadas[pagFactura] = busFactura
#                #print(dicFacPagadas)
#            elif(opcPagFact == 'No'):
#                print("\n\t\t         !!!! Factura NO pagada!!!!")
#        else:
#            print("\n\t\t      !!!! Factura no encontrado !!!!")
#    if(opcMenu == '3'):
#        print("\n\t\t ***************************************** ")
#        print("\t\t 3. Información del día. \n")
#        print("\t\t    " + ('-')*35)
#        print("\t\t            Facturas SIN pagar." +("\n\t\t    " + ('-')*35))
#        print("\t\t       No. Factura   |    Cantidad")
#        print("\t\t    " + ('-')*35)
#        for i in dicIndFacturas:
#            print("\t\t\t   " + i + "      |   $ " + str(round(dicIndFacturas[i],2)))
#        suma1 = sum(dicIndFacturas.values())
#        print("\t\t    " + ('-')*35)
#        print("\t\t          Total      |   $ " + str(round(suma1,2)))
#        print("\t\t    " + ('-')*35)
#        print("\n\n")
#        print("\t\t    " + ('-')*35)
#        print("\t\t             Facturas PAGADAS." +("\n\t\t    " + ('-')*35))
#        print("\t\t       No. Factura   |    Cantidad")
#        print("\t\t    " + ('-')*35)
#        for j in dicFacPagadas:
#            print("\t\t\t   " + j + "      |   $ " + str(round(dicFacPagadas[j],2)))
#        suma2 = sum(dicFacPagadas.values())
#        print("\t\t    " + ('-')*35)
#        print("\t\t          Total      |   $ " + str(round(suma2,2)))
#        print("\t\t    " + ('-')*35)
#        print("\n\n")
#        suma3 = sum(dicFacTotal.values())
#        print("\t\t    " + ('-')*35)
#        print("\t\t       Información General Facturas." +("\n\t\t    " + ('-')*35))
#        print("\t\t     Total del dia   |   $ " + str(round(suma3,2)))
#        print("\t\t     Total pagado    |   $ " + str(round(suma2,2)))
#        print("\t\t     Total sin pagar |   $ " + str(round(suma1,2)))
#        print("\t\t    " + ('-')*35)
#        salir1 = input("\n\t\t Presiona [ENTER] para SALIR.")
#    print("\n\t\t ***************************************** ")



#Escribir un programa que permita gestionar la base de datos de clientes de una
#empresa. Los clientes se guardarán en un diccionario en el que la clave de cada
#cliente será su NIF, y el valor será otro diccionario con los datos del cliente
#(nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el
#valor "True" si se trata de un cliente preferente. El programa debe preguntar
#al usuario por una opción del siguiente menú:
#       1. Añadir cliente.
#       2. Eliminar cliente.
#       3. Mostrar cliente.
#       4. Listar todos los clientes.
#       5. listar clientes preferentes.
#       6. Terminar
#en función de la opción elegida el programa tendrá que hacer lo siguiente:
#   1. Preguntar los datos del cliente, crear un diccionario con los datos y
#      añadirlo a la base de datos.
#   2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#   3. Preguntar por el NIF del cliente y mostrar sus datos.
#   4. Mostrar listas de todos los clientes de la base de datos con su NIF y
#      nombre.
#   5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y
#      nombre.
#   6. Terminar el programa.
#dicNIFclientes = {}; dicDirecc = {}; dicTelefo = {}; dicCorreo = {}; dicPrefer = {}
#while(True):
#    print("\n\t   " + (('*')*51))
#    print("\t   **************** EMPRESA: CLIENTES **************** ")    
#    print("\n\t\t     1. Añadir cliente. ")
#    print("\t\t     2. Eliminar cliente. ")
#    print("\t\t     3. Mostrar cliente. ")
#    print("\t\t     4. Lista general de clientes. ")
#    print("\t\t     5. Lista de clientes preferentes. ")
#    print("\t\t     6. Terminar. ")
#    opcMenu = input("\n\t\t            Elige un opción:\n\t\t\t    > ")
#    if((opcMenu == '1') or (opcMenu == '2') or (opcMenu == '3') or (opcMenu == '4') or (opcMenu == '5')):
#        print("\n\t   " + (('*')*51))
#        while(opcMenu == '1'):
#            print("\t   " + (('*')*51))
#            print("\t   1. Añadir cliente.")
#            opcNuevo = input("\t   Ingresar nuevo cliente [Si|No]: ").title()
#            if(opcNuevo == 'Si'):
#                while(True):
#                    ingrNIF = input("\n\t\tNIF: ")
#                    while(ingrNIF in dicNIFclientes):
#                        print("\t\t    !!! NIF YA EXISTE, INGRESE OTRO NIF !!!")
#                        ingrNIF = input("\n\t\tNIF: ")
#                    while(ingrNIF == ""):
#                        print("\t\t    !!! NO HAY INFORMACION !!!")
#                        ingrNIF = input("\n\t\tNIF: ")
#                    if((len(ingrNIF)) == 8):
#                        break
#                    elif((len(ingrNIF)) != 8):
#                        print("\t\t    !!! FORMATO INCORRECTO !!!")
#                while(True):
#                    ingrNombre = input("\t\tNombre: ").title()
#                    while(ingrNombre == ""):
#                        print("\t\t    !!! NO HAY INFORMACION !!!")
#                        ingrNombre = input("\t\tNombre: ").title()
#                    if(ingrNombre != ""):
#                        break
#                while(True):
#                    ingrDireccion = input("\t\tDirección: ")
#                    while(ingrDireccion == ""):
#                        print("\t\t    !!! NO HAY INFORMACION !!!")
#                        ingrDireccion = input("\t\tDirección: ")
#                    if(ingrDireccion != ""):
#                        break
#                while(True):
#                    ingrTelefono = input("\t\tTeléfono: ")
#                    while(ingrTelefono == ""):
#                        print("\t\t    !!! NO HAY INFORMACION !!!")
#                        ingrTelefono = input("\t\tTeléfono: ")
#                    if((len(ingrTelefono)) == 10):
#                        break
#                    elif((len(ingrTelefono)) != 10):
#                        print("\t\t    !!! FORMATO INCORRECTO !!!")
#                while(True):
#                    ingrCorreo = input("\t\tCorreo: ")
#                    while(ingrCorreo == ""):
#                        print("\t\t    !!! NO HAY INFORMACION !!!")
#                        ingrCorreo = input("\t\tCorreo: ")
#                    if( '@' in ingrCorreo):
#                        break
#                    else:
#                        print("\t\t    !!! FORMATO INCORRECTO !!!")
#                while(True):
#                    ingrPreferencia = input("\t\tPreferencia [Alta(A)|Baja(B)]: ").title()
#                    while(ingrPreferencia == ""):
#                        print("\t\t    !!! NO HAY INFORMACION !!!")
#                        ingrPreferencia = input("\t\tPreferencia [Alta(A)|Baja(B)]: ").title()
#                    if((ingrPreferencia == 'Alta') or (ingrPreferencia == 'A') or (ingrPreferencia == 'Baja') or (ingrPreferencia == 'B')):
#                        break
#                    elif((ingrPreferencia != 'Alta') or (ingrPreferencia != 'A') or (ingrPreferencia != 'Baja') or (ingrPreferencia != 'B')):
#                        print("\t\t    !!! FORMATO INCORRECTO !!!")
#                dicNIFclientes[ingrNIF] = ingrNombre
#                dicDirecc[ingrNombre] = ingrDireccion
#                dicTelefo[ingrNombre] = ingrTelefono
#                dicCorreo[ingrNombre] = ingrCorreo
#                if((ingrPreferencia == 'Alta') or(ingrPreferencia == 'A')):
#                    dicPrefer[ingrNombre] = True
#                elif((ingrPreferencia == 'Baja') or(ingrPreferencia == 'B')):
#                    dicPrefer[ingrNombre] = False
#                #print(dicNIFclientes); print(dicDirecc); print(dicTelefo); print(dicCorreo); print(dicPrefer)
#            elif(opcNuevo == 'No'):
#                break
#        while(opcMenu == '2'):
#            print("\t   " + (('*')*51))
#            print("\t   2. Eliminar cliente. ") 
#            while(True):
#                opcElimCliente = input("\n\t      Inserta [Si|No] para eliminar: \n\t      > ").title()
#                while(opcElimCliente == ''):
#                    print("\t       !!! NO INGRESASTE OPCION !!!")
#                    opcElimCliente = input("\n\t      Inserta [Si|No] para eliminar: \n\t      > ").title()
#                if((opcElimCliente == 'No') or (opcElimCliente == 'N')):
#                    break
#                if((opcElimCliente == 'Si') or (opcElimCliente == 'S')):
#                    elimCliente = input("\t      Ingresa NIF: \n\t\t\t  > ")
#                    if(elimCliente in dicNIFclientes):
#                        print("\t                   !!! NIF encontrado !!!")
#                        eliminarCliente = dicNIFclientes.pop(elimCliente)
#                        eliminarDireccion = dicDirecc.pop(eliminarCliente)
#                        eliminarTelefono = dicTelefo.pop(eliminarCliente)
#                        eliminarCorreo = dicCorreo.pop(eliminarCliente)
#                        eliminarPreferencia = dicPrefer.pop(eliminarCliente)
#                        #print(eliminarCliente)
#                        #print(dicNIFclientes); print(dicDirecc); print(dicTelefo); print(dicCorreo); print(dicPrefer)
#                    else:
#                        print("\t                   !!! NIF NO encontrado !!!")
#                elif((opcElimCliente != 'No') or (opcElimCliente != 'N') or (opcElimCliente != 'Si') or (opcElimCliente != 'S')):
#                    print("\t       !!! NO EXISTE OPCION !!!")
#            break
#        while(opcMenu == '3'):
#            print("\t   " + (('*')*51))
#            print("\t   3. Mostrar cliente. ")
#            while(True):
#                opcMostCliente = input("\n\t      Inserta [Si|No] para nostrar: \n\t      > ").title()
#                while(opcMostCliente == ''):
#                    print("\t       !!! NO INGRESASTE OPCION !!!")
#                    opcMostCliente = input("\n\t      Inserta [Si|No] para mostrarr: \n\t      > ").title()
#                if((opcMostCliente == 'No') or (opcMostCliente == 'N')):
#                    break
#                if((opcMostCliente == 'Si') or (opcMostCliente == 'S')):
#                    mostCliente = input("\t      Ingresa NIF: \n\t\t\t  > ")
#                    if(mostCliente in dicNIFclientes):
#                        print("\t                   !!! NIF encontrado !!!")
#                        mostrarCliente = dicNIFclientes[mostCliente]
#                        mostrarDireccion = dicDirecc[mostrarCliente]
#                        mostrarTelefono = dicTelefo[mostrarCliente]
#                        mostrarCorreo = dicCorreo[mostrarCliente]
#                        mostrarPreferencia = dicPrefer[mostrarCliente]
#                        print("\t      " + (('_')*45))
#                        print("\t                INFORMACION DEL CLIENTE. ")
#                        print("\n\t       Nombre: " + mostrarCliente)
#                        print("\t       Dirección: " + mostrarDireccion)
#                        print("\t       Teléfono: " + mostrarTelefono)
#                        print("\t       Correo: " + mostrarCorreo)
#                        print("\t       Preferencia: " + str(mostrarPreferencia))
#                        print("\t      " + (('_')*45))
#                    else:
#                        print("\t                   !!! NIF NO encontrado !!!")
#                elif((opcMostCliente != 'No') or (opcMostCliente != 'N') or (opcMostCliente != 'Si') or (opcMostCliente != 'S')):
#                    print("\t       !!! NO EXISTE OPCION !!!")
#            break
#        while(opcMenu == '4'):
#            print("\t   " + (('*')*51))
#            print("\t   3. Lista general de clientes. ")
#            print("\n\t      " + (('-')*12) + "|" + (('-')*32))
#            print("\t           NIP    |  NOMBRE")
#            print("\t      " + (('-')*12) + "|" + (('-')*32))
#            for i in dicNIFclientes:
#                print( "\t        " + i + "  |  " +(dicNIFclientes[i]))
#            print("\t      " + (('-')*12) + "|" + (('-')*32))#45
#            salirListaclientes = input("\n\t      Presiona [Enter] para salir de la lista.")
#            break
#        while(opcMenu == '5'):
#            print("\t   " + (('*')*51))
#            print("\t   5. Lista de clientes preferente. ")
#            print("\n\t      " + (('-')*12) + "|" + (('-')*32))
#            print("\t           NIP    |  NOMBRE")
#            print("\t      " + (('-')*12) + "|" + (('-')*32))
#            for k in dicPrefer:
#                if(dicPrefer[k] == True):
#                    for l in dicNIFclientes:
#                        if(k == dicNIFclientes[l]):
#                            print( "\t        " + l + "  |  " +(dicNIFclientes[l]))
#            print("\t      " + (('-')*12) + "|" + (('-')*32))
#            salirListaclientesPreferenter = input("\n\t      Presiona [Enter] para salir de la lista.")
#            break
#    elif(opcMenu == '6'):
#        print("\n\t   " + (('*')*51))
#        print("\n\t\t !!! VUELVA PRONTO !!!")
#        break
#    else:
#        print("\t\t\t !!! OPCION NO VALIDA !!!")
#        print("\n\t   " + (('*')*51))






# ******** **    ** **    **  ******  ********  ******  **    ** ********  ******
# ******** **    ** ***   ** ******** ******** ******** ***   ** ******** ********
# **       **    ** ****  ** **    **    **    **    ** ****  ** **       **    **
# ******** **    ** ** ** ** **          **    **    ** ** ** ** ******    ****
# ******** **    ** ** ** ** **          **    **    ** ** ** ** ******      ****  
# **       **    ** **  **** **    **    **    **    ** **  **** **       **    **
# **        ******  **   *** ******** ******** ******** **   *** ******** ********
# **         ****   **    **  ******  ********  ******  **    ** ********  ******     




#     ->FUNCIONES(def)
#         -Función: es un bloque de código que tiene asociado un nombre, de
#                   manera que cada vez que se quiera ejecutar el bloque de
#                   código basta con invocar el nombre de la función.                
#         -Para declarar una función se utiliza la siguiente sintaxis:
#            def <nombre-función> (<parámetros>):
#                bloque código
#                return <objeto>
#         
#         -EJEMPLO
#            def bienvenida():
#               print("!Bienvenido a python!")
#               return
#            j = type(bienvenida)
#            print(j)
#            bienvenida()
#
#     ->PARÁMETROS DE UNA FUNCIÓN
#         -Una función puede recibir valores cuando se invoca a través de unas
#          variables conocidas como "parámetros" que se definen entre paréntesis
#          en la declaración de la función. En el cuerpo de la función se pueden
#          usar estos parámetros como si fuesen variables.
#
#          EJEMPLO
#            def bienvenida(nombre):
#                print("¡Bienvedido a Python " + nombre + "!")
#                return
#            nombre = input("\nEscribe tu nombre: ")
#            bienvenida(nombre)
#
#     ->ARGUMENTOS DE LA LLAMADA A UNA FUNCIÓN
#         -Los valores que se pasan a la función en una llamada o invocación
#          concreta de ella se conocen como "argumentos" y se asocian a los
#          parámetros de la declaración de la función.
#         -Los argumentos se pueden indicar de dos formas:
#            ->Argumentos posicionales: Se asocian a los parámetros de la función
#              en el mismo orden que aparecen en la definición de la función.
#            ->Argumentos por nombre: Se indica explícitamente el nombre del
#              parámetro al que se asocia un argumento de la forma
#              "parametro = argumento".
#                
#          EJEMPLO
#            def bienvenidad(nombre, apellido):
#                print("¡Bienvenido a Python", nombre, apellido + "!")
#                return
#            nom = input("\nIngresa nombre: ")
#            ape = input("\nIngresa apellido: ")
#            bienvenidad(nom, ape)
#
#     ->RETORNO A UNA FUNCIÓN
#         -Una función puede devolver un objeto de cualquier tipo tras su
#          invocación. Para ello el objeto a devolver debe escribirse detrás de
#          la palabra reservada "return". Sino se indica ningun objeto, la función
#          no devolverá nada.
#
#          EJEMPLO
#            def areaTriangulo(base,altura):
#                area = (base*altura)/2
#                return print(area)
#            bas = int(input("\nIngresa Base: "))
#            alt = int(input("\nIngresa Altura: "))
#            areaTriangulo(bas,alt)
#       
#     ->ARGUMENTOS POR DEFECTO
#         -En la definición de una función se puede asignar a cada parámetro un
#          argumento por defecto, de manera que si se invoca la función sin pro-
#          porcionar ningún argumento para ese parámetro, se utiliza el argumen-
#          to por defecto.
#
#          EJEMPLO
#            def bienvenido(nombre, lenguaje = "Python"):
#                print("¡Bienvenido a", lenguaje, nombre + "!" )
#                return
#            nomb = input("\nIngresa tu nombre: ")
#            bienvenido(nomb)
#            leng = input("\nIngresa el lenguje: ")
#            bienvenido(nomb, leng)
#
#     ->PASAR UN NÚMERO INDETERMINADO DE ARGUMENTOS
#         -Por último, es posible un número variable de argumentos a un parámetro.
#          Esto se puede hacer de dos formas:
#            -> (*parámetro): Se antepone un asterisco al nombre del parámetro y
#                            en la invocación de la función se pasa el número
#                            variable de argumentos separados por comas. Los
#                            argumentos se guardan en una (lista) que se asocia 
#                            al parámetro.
#            -> (**parámetro): Se anteponen dos asteriscos al nombre del parámetro
#                            y en la invocación de la función se pasa el número
#                            variable de argumentos por pares "nombre = valor",
#                            separados por comas. Los argumentos se guardan en un
#                            (diccionario) que se asocia al parámetros.
#                           
#          EJMPLO
#            def menu(*platos):
#                print("Hoy tenemos: ", end="")
#                for plato in platos:
#                print(str(plato), end= ", ")
#                return
#            menu('pasta','pizza','ensalada')
#
#     ->ÁMBITO DE LOS PARÁMETROS Y VARIABLES DE UNA FUNCIÓN
#         -Los parámetros y las variables declaradas dentro de una función son de
#          "ámbito local", mientras que las definidas fuera de ella son de "ámbito
#          global".
#         -Tanto los parámetros como las variables del ámbito local de una función
#          sólo están accesibles durante la ejecución de la función, es decir,
#          cuando termina la ejecución de la función estas variables desaparecen
#          y no son accesibles desde fuer de la función.
#
#          EJEMPLO
#            def bienvenida(nombre):
#                lenguaje = "Python"
#                print("¡Bienvenido a", lenguaje, nombre + "!")
#                return
#            nom = input("\nIngresa nombre")
#            bienvenida(nom)
#            print(lenguaje)
#
#         -Si en el ámbito local de una función existe una variable que también
#          existe en el ámbito global, durante la ejecución de la función la
#          variable global queda eclipsada por la variable local y no es accesi-
#          ble hasta que finaliza la ejecución de la función.
#
#          EJEMPLO
#            lenguaje = input("\nIngresa lenguaje")
#            def bienvenida():
#                lenguaje = "Python"
#                print("¡Bienvenido a", lenguaje + "!")
#                return
#            bienvenida()
#            print(lenguaje)
#
#     ->PASO DE ARGUMENTOS POR REFERENCIA
#         -En Python el paso de argumentos a una función es siempre por referen-
#          cia, es decir, se pasa una referencia al objeto del argumento, de ma-
#          nera que cualquier cambio que se haga dento de la función mediante el
#          parámetro asociado afectará al objeto original, siempre y cuando este
#          sea mutable.
#
#          EJEMPLO
#            primer_curso = [ 'Matematicas', 'Fisica']
#            def añade_asignatura(curso, asignatura):
#                curso.append(asignatura)
#                return
#            añade_asignatura(primer_curso,"Qumica")
#            print(primer_curso)
#
#     ->DOCUMENTACIÓN DE FUNCIONES (docstring)
#         -Una práctica muy recomendable cuando se define una función es descri-
#          bir lo que la función hace en un comentario
#         -En Python esto se hace con un "docstring" que es un tipo de comentario
#          especial se hace en la línea siguiente al encabezado de la función en-
#          tre comillas simples <<'''>>  o dobles <<""">>
#         -Después se puede acceder a la documentación de la función con la fun-
#          ción "help(<nombre-función>)"
#
#          EJEMPLO
#            def areaTriangulo(base,altura):
#                '''
#                    Función que calcula el área de un triángulo.
#                    Parámetros:
#                        - base: La base del triángulo.
#                        - altura: La altura del triángulo.
#                    Resultado:
#                        El área del triángulo con la base y altura especificadas.
#                '''
#                area = (base*altura)/2
#                return print(area)
#            bas = int(input("\nIngresa Base: "))
#            alt = int(input("\nIngresa Altura: "))
#            help(areaTriangulo)
#            areaTriangulo(bas,alt)
#
#     ->FUNCIONES RECURSIVAS
#         -Función recursiva: Es una función que en su cuerpo contiene una llama
#                             a si misma.
#         -La recursión es una práctica común en la mayoría de los lenguajes de
#          programación ya que permite resolver las tareas recursivas de manera
#          más natural.
#         -Para garantizar el final de una función recursiva, las sucesivas lla-
#          madas tienen que reducir el grado de complejidad del problema, hasta
#          que este pueda resolverse directamente sin necsidad de volver a llamar
#          a la función.
#
#          EJEMPLO
#            def factorial(n):
#                if(n==0):
#                    return 1
#                else:
#                    formula = n * factorial(n-1)
#                    return formula
#            num = int(input("\nIngresa un numero: "))
#            print(factorial(num))
#               
#     ->FUNCIONES RECURSIVAS MÚLTIPLES
#         -Una función recursiva puede invorcarse a si misma tantas veces como
#          quiera en su cuerpo.
#           
#          EJEMPLO
#            def fibonacci(n):
#                if(n<=1):
#                    return n
#                else:
#                    for1 = fibonacci(n-1)
#                    for2 = fibonacci(n-2)
#                    formula = for1 + for2
#                    print(str(for1) + " " + str(for2) + " " + str(formula))
#                    return formula
#            num = int(input("\nIngresa un numero: "))
#            print("\n")
#            print(fibonacci(num))
#               
#     ->LOS RIESGOS DE LA RECURSIÓN
#         -Aunque la recursión permite resolver las tareas recursivas de forma 
#          más natural, hay que tener cuidado con ella porque suele consumir
#          bastante memoria, ya que cada llamada a la función crea un nuevo
#          ámbito local con las variables y los parámetros de la función.
#         -En muchos casos es más eficiente resolver la tarea recursiva de forma
#          iterativa usando bucles. 
#
#          EJEMPLO
#            def fibonacci(n):
#                a, b = 0, 1
#                for i in range(n):
#                    a, b = b, a + b
#                    print(a, b, a + b)
#                return a
#            num = int(input("\nIngresa un numero: "))
#            print(fibonacci(num))


#Escribir una funcion que muestre por pantalla el saludo "¡Hola mundo!" cada vez
#que se la invoque.
#def saludo():
#    print("¡Hola mundo!")
#    return
#while(True):
#    print("\n\t   **************** SALUDO **************** ")    
#    decision = input("\nInserta [Si|No] para mostrar saludo: ").title()
#    if((decision == 'Si') or (decision == 'S')):
#        saludo()
#    elif((decision == 'No') or (decision == 'N')):
#        break
#    elif(decision == ""):
#        print("\t !!! No Agregaste nada !!!")
#    else:
#        print("\t !!! Opcion no valida !!!")
       


#Escribir una función a la que se le pase una cadena "nombre" y muestre por
#pantalla el saludo "¡Hola <nombre>!".
#def saludo(nombre="amigo"):
#    print("¡HOLA, bienvenido(a)", nombre + "!")
#    return
#while(True):
#    print("\n\t   **************** SALUDO **************** ")    
#    decision = input("\nInserta [Si|No] para mostrar saludo: ").title()
#    if((decision == 'Si') or (decision == 'S')):
#        nom = input("\nIngresa tu nombre: ")
#        if(nom==""):
#            saludo()
#        else:
#            saludo(nom)
#    elif((decision == 'No') or (decision == 'N')):
#        break
#    elif(decision == ""):
#        print("\t !!! No Agregaste nada !!!")
#    else:
#        print("\t !!! Opcion no valida !!!")
       


#Escribir una función que reciba un número entero positivo y devuelva su
#factorial.
#def factorial(n):
#    if(n==0):
#        return 1
#    else:
#        temporal = 1
#        for i in range(n)
#            temporal *= i + 1
#        return temporal
#while(True):
#    print("\n\t   **************** FACTORIAL **************** ")    
#    decision = input("\nInserta [Si|No] para mostrar factorial: ").title()
#    if((decision == 'Si') or (decision == 'S')):
#        while(True):
#            numero = input("\nIngresa un número: \n\t\t > ")
#            if(numero == ""):
#                print("\t\t !!! NO AGREGASTE NÚMERO !!!")
#            elif((int(numero)) < 0):
#                print("\t\t !!! AGREGAR SOLO NÚMEROS POSITIVOS !!!")
#            else:
#                resultado = factorial(int(numero))
#                print("\t\t Resultado: " + str(resultado))
#                break        
#    elif((decision == 'No') or (decision == 'N')):
#        break
#    elif(decision == ""):
#        print("\t !!! No Agregaste nada !!!")
#    else:
#        print("\t !!! Opcion no valida !!!")



#Escribir una función que calcule el total de una factura tras aplicarle el IVA.
#La función debe resivir la cantidad sin IVA y el porcentaje de IVA a aplicar, y
#devolver el total de la factura. Si se invoca la función sin pasarle el
#porcentaje de IVA, deberá aplicar un 21%.
#def funcionIVA(cantidad,valorIVA):
#    if (not valorIVA):
#        valorIVA = 21
#        formula = float(cantidad) + ((float(cantidad)/100) * float(valorIVA))
#        return formula
#    else:
#        formula = float(cantidad) + ((float(cantidad)/100) * float(valorIVA))
#        return formula
#while(True):
#    print("\n\t   **************** FACTURA **************** ")    
#    decision = input("\nInserta [Si|No] para crear factura: ").title()
#    if((decision == 'Si') or (decision == 'S')):
#        while(True):
#            numFactura = input("\nIngresar No. de factura: \n\t\t  > ")
#            if(not numFactura):
#                print("\t\t !!! AGREGA NO. DE FACTURA !!!")
#            else:
#                while(True):
#                    cantidad = input("\nIngresa cantidad: ")
#                    if(not cantidad):
#                        print("\t\t !!! CANTIDAD NO AGREGADA !!!")
#                    elif((float(cantidad)) < float(0) ):
#                        print("\t\t !!! CANTIDAD NO VÁLIDA !!!")
#                    else:
#                        while(True):
#                            iva = input("\nIngresa el iva %: ")
#                            if(not iva):
#                                print("\t\t !!! IVA del 21% !!!")
#                                funcion = funcionIVA(cantidad,iva)
#                                print("\n\t\t Total a Pagar: $" + str(funcion))
#                                break
#                            elif((float(iva)) < 0):
#                                print("\t\t !!! IVA NO VÁLIDA !!!")
#                            else:
#                                funcion = funcionIVA(cantidad,iva)
#                                print("\n\t\t Total a Pagar: $" + str(round(funcion,2)))
#                                break
#                        break
#                break        
#    elif((decision == 'No') or (decision == 'N')):
#        break
#    elif(decision == ""):
#        print("\t !!! No Agregaste nada !!!")
#    else:
#        print("\t !!! Opcion no valida !!!")



#Escribir una función que calcule el área de un círculo y otra que calcule el
#volumen de un cilindro usando la primera función.
#import math
#def areaCirculo(perimetro):
#    '''
#        Función que calcula el áreadel circulo:
#            AreaCirculo = pi * radio^2
#        Donde:
#            pi = 3.1416
#    '''
#    pip = math.pi
#    area = pip * (pow(float(perimetro),2))
#    redondeo = round(area,5)
#    return redondeo
#def volumenCilindro(altura, redondeo):
#    '''
#        Función que calcula el volumen de un cílindro:
#            volumenCilindro = Ab * Altura
#        Donde:
#            Ab = Area de la base
#                 se llama al valor de la funcion "AreaCirculo"
#    '''
#    vol = redondeo * float(altura)
#    return vol
#while(True):
#    print("\n\n\t  ***************** ÁREA Y VOLUMEN ***************** ")    
#    decision = input("\n\t   Inserta [Si|No] para crear realizar operaciones.\n\t\t     > ").title()
#    if((decision == 'Si') or (decision == 'S')):
#        print("\t  " + ("_" * 50) )
#        print("\t   ÁREA CÍRCULO")
#        print("\n\t   Ingresa perímetro(cm) círculo.")
#        while(True):
#            valPerim = input("\t   > ")
#            if(not valPerim):
#                print("\t       !!! NO AGREGASTE NADA !!!")
#            elif((float(valPerim)) < (float(0))):
#                print("\t       !!! PERIMETRO NO VÁLID0 !!!")
#            else:
#                ar = areaCirculo(valPerim)
#                print("\t     Área del círculo: " + str(ar) + " cm^2")
#                print("\t  " + ("-" * 50))
#                print("\t   Calcular volumen de cílindro [Si|No].")
#                while(True):
#                    opc = input("\t   > ").title()
#                    if((opc == "Si") or (opc == "S")):
#                        print("\t  " + ("-" * 50) )
#                        print("\t  " + ("_" * 50) )
#                        print("\t   VOLUMEN CÍLINDRO")
#                        print("\n\t   Ingresa altura del cílindro: ")
#                        while(True):
#                            alt = input("\t   > ").title()
#                            if(not alt):
#                                print("\t     !!! NO AGREGASTE NADA !!!")
#                            elif((float(alt)) < (float(0))):
#                                print("\t       !!! ALTURA NO VÁLID0 !!!")
#                            else:
#                                volume = volumenCilindro(alt,ar)
#                                print("\t     Volumen del cílindro: " + str(volume) + " cm^2")
#                                print("\t  " + ("_" * 50) )
#                                break
#                        break
#                    elif((opc == 'No') or (opc == 'N')):
#                        break
#                    elif(not opc):
#                        print("\t     !!! NO AGREGASTE NADA !!!")
#                    else:
#                        print("\t     !!! OPCION NO VÁLIDA !!!")
#                break        
#    elif((decision == 'No') or (decision == 'N')):
#        break
#    elif(not decision):
#        print("\t\t       !!! NO AGREGASTE NADA !!!")
#        print("\n\t  " + ("*" * 50) )
#    else:
#        print("\t\t       !!! OPCION NO VÁLIDA !!!")
#        print("\n\t  " + ("*" * 50) )



#Escribir una función que reciba una muestra de números en una lista y devuelva
#su media.
#def operacionLista(numeros):
#    sumatoria = 0
#    for j in range(0, len(numeros), 1):
#        sumatoria += numeros[j]
#    media = sumatoria / (len(numeros))
#    return round(media,4)
#listaNumeros = []
#while(True):
#    print("\n\n\t  ***************** CALCULO DE MEDIA ***************** ")    
#    print("\n\t\t     Nota: Ingresa [*] para SALIR.")
#    canNum = input("\n\t  Ingresa lista de numeros separando por comas: \n\t   > ")
#    if(not canNum):
#        print("\t\t      !!! NO INGRESASTE NADA !!!")
#    elif(canNum == "*"):
#        print("\t  " + "_"*53)
#        print("\t\t\t !!! VUELVA PRONTO !!!")
#        break
#    else:
#        divCanNum = canNum.split(",")
#        for i in range(0, len(divCanNum),1):
#            listaNumeros.append(float(divCanNum[i]))    
#        imprimirResultado = operacionLista(listaNumeros)
#        print("\n\t\t\t    MEDIA: " + str(imprimirResultado))



#Escribir una función que reciba una muestra de números en una lista y devuelva
#otra lista con sus cuadrados.
#def operacionLista(numeros):
#    listaNumCuadra = []
#    for j in range(0, len(numeros), 1):
#        cuadrados =  pow(numeros[j] ,2)
#        listaNumCuadra.append(float(round(cuadrados,4)))
#    return listaNumCuadra
#listaNumeros = []
#while(True):
#    print("\n\n\t  ***************** NÚMEROS AL CUADRADO ***************** ")    
#    print("\n\t\t     Nota: Ingresa [*] para SALIR.")
#    canNum = input("\n\t  Ingresa lista de numeros separando por comas: \n\t   > ")
#    if(not canNum):
#        print("\t\t      !!! NO INGRESASTE NADA !!!")
#    elif(canNum == "*"):
#        print("\t  " + "_"*53)
#        print("\t\t\t !!! VUELVA PRONTO !!!")
#        break
#    else:
#        divCanNum = canNum.split(",")
#        for i in range(0, len(divCanNum),1):
#            listaNumeros.append(float(divCanNum[i]))    
#        imprimirResultado = operacionLista(listaNumeros)
#        print("\n\t\t\t    NUMEROS Al CUADRADO: \n")
#        for n in range(0, len(imprimirResultado), 1):
#            print ("\t\t\t    [" + str(listaNumeros[n]) +"] ^ 2= "+ str(imprimirResultado[n]))



#Escribir una funcion que reciba una muestra de números en una lista y devuelva
#un diccionario con su media, varianza y desviación típica.
#import math
#def operacionLista(numeros):
#    '''
#        FUNCIÓN QUE CALCULA:
#            - Media
#            - Varianza
#            - Desviación Típica
#    '''
#    diccEstadis = {}
#    sumMed = 0
#    sumVar = 0
#    tamNum = len(numeros)
#    for j in range(0, tamNum, 1):
#        sumMed += numeros[j]
#    media = sumMed / tamNum
#    mediaRound = round(media,4)
#    diccEstadis['Media'] = mediaRound
#    for k in range(0, tamNum, 1):
#        form1 = pow((numeros[k] - mediaRound),2)
#        sumVar += form1
#    varianza = sumVar / tamNum
#    varianzaRound = round(varianza,4)
#    diccEstadis['Varianza'] = varianzaRound
#    desviacionEstandar = math.sqrt(varianzaRound)
#    desviacionEstandarRound = round(desviacionEstandar,4)
#    diccEstadis['Desviación Estandar'] = desviacionEstandarRound
#    return diccEstadis
#while(True):
#    print("\n\n\t  *************** ESTADISTICA DE MUESTRA *************** ")    
#    print("\n\t\t     Nota: Ingresa [*] para SALIR.")
#    canNum = input("\n\t  Ingresa lista de numeros separando por comas: \n\t   > ")
#    if(not canNum):
#        print("\t\t      !!! NO INGRESASTE NADA !!!")
#    elif(canNum == "*"):
#        print("\t  " + "_"*53)
#        print("\t\t\t !!! VUELVA PRONTO !!!")
#        break
#    else:
#        listaNumeros = []
#        divCanNum = canNum.split(",")
#        for i in range(0, len(divCanNum),1):
#            listaNumeros.append(float(divCanNum[i]))    
#        imprimirResultado = operacionLista(listaNumeros)
#        print("\t  " + "-"*54)
#        print('\t\t\t     " ESTADISTICA " \n')
#        for i in imprimirResultado:
#            if(i == 'Varianza'):
#                print("\t\t       " + str(i) + ": "+str(imprimirResultado[i]) + " u^2")
#            else:
#                print("\t\t       " + str(i) + ": "+str(imprimirResultado[i]))
#        print("\t  " + "-"*54)



#Escribir una función que calcule el máximo común divisor de dos números y otra
#que calcule el mínimo común múltiplo.
#def mcd(n, m):
#    """Función que calcula el máximo común divisor de dos números.
#    Parámetros:
#        - n: Es un número entero.
#        - m: Es un número entero.
#    Devuelve:
#        El máximo común divisor de n y m.
#    """
#    rest = 0
#    while(m > 0):
#        rest = m
#        m = n % m
#        n = rest
#    return n
#def mcm(n, m):
#    """Función que calcula el mínimo común múltiplo de dos números.
#    Parámetros:
#        - n: Es un número entero.
#        - m: Es un número entero.
#    Devuelve:
#        El mínimo común múltiplo de n y m.
#    """
#    if n > m:
#        greater = n
#    else:
#        greater = m
#    while (greater % n != 0) or (greater % m != 0):
#        greater += 1
#    return greater
#print(mcd(24,36))
#print(mcm(24,36))



#Escribir una función que convierta un número decimal en binario y otra que
#convierta un número binario en decimal.
#def binarioDecimal(binario):
#    vecBin = []
#    arreglo = []
#    suma = 0
#    for i in range(0,15,1):
#        n = pow(2,i)
#        arreglo.append(n)
#    for i in range(len(binario), 0, -1):
#        vecBin.append(binario[i-1])
#    for a in range(0, len(vecBin), 1):
#        if(vecBin[a] == "1"):
#            suma += arreglo[a]
#    return suma
#def decimalBinario(decimal):
#    binary = []
#    while decimal > 0:
#        mod = decimal % 2
#        binary.append(str(mod))
#        decimal //= 2 # // -->operador división entera el resultado que se devuelve es solo la parte entera.
#    binary.reverse()
#    cadena = ''.join(binary)
#    return cadena
#def menu():
#    print("\n\n\t  " + ("*"*51))
#    print("\t  ******************** CONVERSOR ******************** ")    
#    print("\n\t\t  1. Convertir de decimal a binario. ")
#    print("\t\t  2. Convertir de binario a decimal. ")
#    print("\t\t  3. salir. ")
#    return
#while(True):
#    menu()
#    opc = input("\n\t\t     Ingresa el número de opción: \n\t\t\t> ")
#    if(opc == "1"):
#        print("\n\t  " + ("*"*51))
#        print("\t  " + ("*"*51))
#        print("\n\t  " + ("_"*51))
#        print("\t  " + ("_"*51))
#        print("\t  BINARIO A DECIMAL.")
#        print("\n\t\t     Nota: Ingresa [*] para SALIR.")
#        print("\n\t    Ingresa un valor binario: ")
#        while(True):
#            num = input("\t     > ")
#            if(num == "*"):
#                print("\t  " + ("_"*51))
#                print("\t  " + ("_"*51))
#                break
#            elif(not num):
#                print("\t       !!! NO AGREGASTE BINARIO !!!\n")
#            else:
#                impDec = binarioDecimal(num)
#                print("\t       Decimal: " + str(impDec))
#    elif(opc == "2"):
#        print("\n\t  " + ("*"*51))
#        print("\t  " + ("*"*51))
#        print("\n\t  " + ("_"*51))
#        print("\t  " + ("_"*51))
#        print("\t  DECIMAL A BINARIO.")
#        print("\n\t\t     Nota: Ingresa [*] para SALIR.")
#        print("\n\t    Ingresa un valor binario: ")
#        while(True):
#            num1 = input("\t     > ")
#            if(not num1):
#                print("\t       !!! NO AGREGASTE BINARIO !!!\n")
#            elif(num1 == "*"):
#                print("\t  " + ("_"*51))
#                print("\t  " + ("_"*51))
#                break
#            else:
#                impBin = decimalBinario(int(num1))
#                print("\t       Binario: " + impBin)
#    elif(opc == "3"):
#        print("\n\t  " + ("*"*51))
#        print("\t  " + ("*"*51))
#        print("\n\t\t\t!!! VUELVAOS PRONTO !!!")
#        print("\n\t  " + ("*"*51))
#        print("\t  " + ("*"*51))
#        break
#    else:
#        print("\t\t       !!! OPCIÓN NO VÁLIDA !!! ")
#        print("\n\t  " + ("*"*51))
#        print("\t  " + ("*"*51))



#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
#con cada palabra que contiene y su frecuencia. Escribir otra función que reciba
#el diccionario generado con la función anterior y devuelva una tupla con la
#palabra más repetida y su frecuencia.
#def functionDiccionario(escribir):
#    dic = {}
#    tecla = escribir.split()
#    for i in range(0, len(tecla), 1):
#        if(tecla[i] in dic):
#            dic[tecla[i]] = dic[tecla[i]] + 1  
#        elif(tecla[i] not in dic):
#            dic[tecla[i]] = 1
#    return dic
#def functionFrecuencia(diccionario):
#    maxi = max(diccionario.values())
#    tupla = ()
#    for j in diccionario:
#        imp = diccionario[j]
#        if(imp >= maxi):
#            tupla = ([j,imp])
#    return tupla
#while(True):
#    print("_"*80)
#    print("WRITE NEW MESSAGE. [Para salir no ingresar nada y da [ENTER].")
#    teclado = input("> ")
#    if(not teclado):
#        break
#    else:
#        imprimir = functionDiccionario(teclado)
#        print("-"*80)
#        print("Total de palabras:")
#        for numero in imprimir:
#            print("      " + str(numero) + " - " + str(imprimir[numero]))
#        imprimirFrec = functionFrecuencia(imprimir)
#        print("Palabra más frecuente: ")
#        print("      " + str(imprimirFrec))
#        print("-"*80 + "\n")






# ******   *******   ******   ******  *******    ****   **    **   ****    ******  ********  ******  **    **
# ******** ******** ******** ******** ********  ******  ***  ***  ******  ******** ******** ******** ***   ** 
# **    ** **    ** **    ** **       **    ** **    ** ***  *** **    ** **    **    **    **    ** ****  **
# ******** *******  **    ** **  **** *******  **    ** ** ** ** **    ** **          **    **    ** ** ** **
# ******   ******   **    ** **  **** ******   ******** ** ** ** ******** **          **    **    ** ** ** **
# **       **  **   **    ** **    ** **  **   ******** **    ** ******** **    **    **    **    ** **  ****
# **       **   **  ******** ******** **   **  **    ** **    ** **    ** ******** ******** ******** **   ***
# **       **    **  ******   ******  **    ** **    ** **    ** **    **  ******  ********  ******  **    **
#
# ******** **    ** **    **  ******  ********  ******  **    **   ****   **
# ******** **    ** ***   ** ******** ******** ******** ***   **  ******  **
# **       **    ** ****  ** **    **    **    **    ** ****  ** **    ** **
# ******** **    ** ** ** ** **          **    **    ** ** ** ** **    ** **
# ******** **    ** ** ** ** **          **    **    ** ** ** ** ******** **
# **       **    ** **  **** **    **    **    **    ** **  **** ******** **
# **        ******  **   *** ******** ******** ******** **   *** **    ** ********
# **         ****   **    **  ******  ********  ******  **    ** **    ** ********




#     PROGRAMACIÓN FUNCIONAL
#        -> En Python las funciones son objetos de primera clase, es decir, que
#           pueden pasarse como argumentos de una función, al igual que el resto
#           de los tipos de datos.
#
#           EJEMPLO
#              def aplica(funcion, argumento):
#                  return funcion(argumento)
#              def cuadrado(n):
#                  return n*n
#              def cubo(n):
#                  return n**3
#              apli = aplica(cuadrado,5)
#              print(apli)
#              apli1 = aplica(cubo,5)
#              print(apli1)
#       
#     FUNCIONES ANÓNIMAS(LAMBDA)
#        -> Existe un tipo especial de funciones que no tienen nombre asociado y
#           se conocen como funciones anónimas o funciones lambda
#        -> La sintaxis para definir una función anónima es:
#              lambda <parámetros> : <expresión>
#           
#           EJEMPLO
#              area = lambda base, altura : base * altura
#              imprimir = area(4,5)
#              print(imprimir)
#
#     APLICAR UNA FUNCIÓN A TODOS LOS ELEMENTOS DE UNA COLECCIÓN ITERABLE(MAP)
#        -> map(f,c): Devuelve un objeto iterable con los resultados de aplicar
#                     la función "f" a los elementos de la colección "c". Si la  
#                     función "f" requiere "n" argumentos entonces deben pararse
#                     "n" colecciones con los argumentos. Para convertir el 
#                     objeto en una lista, tupla o diccionario hay que aplicar  
#                     explícitamente las funciones "list()", "tuple()" o "dic()"  
#                     respectivamente.  
#
#           EJEMPLO #1
#              def cuadrado(n):
#                  return n*n
#              map1 = map(cuadrado, [1, 2, 3])
#              lista = list(map1)
#              print(lista)
#
#           EJEMPLO #2
#              def rectangulo(a,b):
#                  area = a * b
#                  return area
#              map1 = map(rectangulo, (1, 2, 3), (4, 5, 6))
#              tupla = tuple(map1)
#              print(tupla)
#
#     FILTRAR LOS ELEMENTOS DE UNA COLECCIÓN ITERABLE(FILTER)
#        -> filter(f,c): Devuelve un objeto iterable con los elementos de la 
#                        colección "c" que devuelven "True" al aplicarse la 
#                        función "f". Para convertir el objeto en una lista, 
#                        tupla o diccionario hay que aplicar explícitamente las
#                        funciones "list()", "tuple()" o "dic()" respectivamente.
#        -> "f" debe ser una función que recibe un argumento y devuelve un valor
#           booleano.
#           
#           EJEMPLO
#              def par(n):
#                  mod = n % 2
#                  return mod == 0
#              filtro = filter(par, range(10))
#              lista = list(filtro)
#              print(lista)   
#               
#     COMBINAR LOS ELEMENTOS DE VARIAS COLECCIONES ITERABLES(ZIP)
#        -> zip(c1,c2,...): Devuelve un objeto iterable cuyos elementos son 
#                           tuplas formadas por los elementos que ocupan la misma
#                           posición en las colecciones "c1", "c2", etc. El 
#                           número de elementos de las tuplas es el número de 
#                           colecciones que se pasen. Para convertir el objeto 
#                           en una lista, tupla o diccionario hay que aplicar
#                           explícitamente las funciones "list()", "tuple()" o
#                           "dic()" respectivamente.
#                   
#           EJEMPLO
#              asignaturas = ["Matemáticas", "Física", "Química", "Economía"]
#              calificaciones = [6.0, 3.5, 7.5, 8.0]
#              zip1 = zip(asignaturas, calificaciones)
#              lista = list(zip1)
#              print(lista)
#              zipDic = zip(asignaturas, calificaciones[:3])
#              diccionario = dict(zipDic)
#              print(diccionario)
#                   
#     OPERAR TODOS LOS ELEMENTOS DE UNA COLECCIÓN ITERABLE(REDUCE)
#        -> reduce(f,l): Aplicar la función "f" a los dos primeros elementos de 
#                        la secuencia "l". Con el valor obtenido vuelve a aplicar
#                        la función "f" a ese valor y el siguiente de la secuen-
#                        cia, y así hasta que no quedan más elementos en la lista.
#                        Devuelve el valor resultado de la última aplicación de
#                        la función "f".
#        -> La función "reduce" está definida en el módulo "functools"
#               
#           EJEMPLO
#              from functools import reduce
#              def producto(n,m):
#                  multi = n * m
#                  #print(str(multi) + " - " + str(n) + " * " + str(m))
#                  return multi
#              reduce1 = reduce(producto, range(1,5))
#              print( "reduce "+ str(reduce1))



#Escribir una función que aplique un descuento a un precio y otra que aplique el
#IVA a un precio. Escribir una tercera función que reciba un diccionario con los
#precios y porcentajes de una cesta de la compra, y una de las funciones anterio
#res, y utilice la función pasada para aplicar los descuentos o el IVA a los pro-
#ductos de la cesta y devolver el precio final de la cesta.
#def aplicarDescuento(pre, porcent):
#    descuentoTotal =  (pre/100) * porcent
#    precTotal = pre - descuentoTotal
#    redondeo2 = round(precTotal, 2)
#    return redondeo2
#def aplicarIVA(prec , porcentaje):
#    ivaTotal = (prec/100) * porcentaje
#    precioTotal = round(ivaTotal, 2) + round(prec,2)
#    redondeo1 = round((float(precioTotal)), 2)
#    return redondeo1
#def diccionarioCesta(producto, iva, imp1):
#    for i in range(0, contador, 1):
#        diccionario[producto] = imp1
#    return diccionario
#diccionario = {}
#contador  = 0
#while(True):
#    opc = input("Ingresa nuevo producto[si|no]: ").lower()
#    if(not opc):
#        print("!!! NO AGREGASTE OPCIÓN !!!")
#    elif((opc == "si") or (opc == "s")):
#        contador += 1
#        producto = input("Nombre de producto[" + str(contador) + "]: ")
#        precio = float(input("Precio($): "))
#        iva = float(input("I.V.A.(%): "))
#        imp1 = aplicarIVA(precio,iva)        
#        imp3 = diccionarioCesta(producto, iva, imp1)
#        suma = 0
#        for j in imp3:
#            suma += imp3[j]
#        print( "Total a pagar: " + str(suma))
#    elif((opc == "no") or (opc == "n")):
#        opc1 = input("Agregar descuento[si|no]: ").lower()
#        if((opc1 == "si") or (opc1 == "s")):
#            descuento = float(input("Descuento(%): "))
#            imp2 = aplicarDescuento(suma, descuento)
#            print( "Total a pagar con descuento: " + str(imp2))
#        elif((opc1 == "no") or (opc1 == "n")):
#            break
#        elif(not opc1):
#            print("!!! NO AGREGASTE OPCIÓN !!!")
#        else:
#            print("!!! OPCIÓN NO VÁLIDA !!!")
#    else:
#        print("!!! OPCIÓN NO VÁLIDA !!!")



#Escribir una función que simule una calculadora cientifíca que permita calcular 
#el seno, coseno, tangente, exponencial y logaritmo neperiano. La función pregun-
#tará al usuario el valor y la función a aplicar, y mostrará por pantalla una ta-
#bla con los enteros de 1 al valor introduciodo y el resultado de aplicar la fun-
#ción a esos enteros.
#from math import sin, cos, tan, exp, log
#def calculator(function1, numero):
#    diccionario = {'sen':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
#    result = []
#    for i in range(0, int(numero), 1):
#        result1 = diccionario[function1](float(i+1))
#        result.append(result1)
#    return result
#def menu():
#    print("\n\t  *************** CALCULADORA CIENTIFÍCA *************** ")
#    print("\n\t\t      > Función SENO (sen). ")
#    print("\t\t      > Función COSENO (cos). ")
#    print("\t\t      > Función TANGENTE (tan). ")
#    print("\t\t      > Exponencial (exp). ")
#    print("\t\t      > Logaritmo neperiano (log). ")
#    print("\t\t      > (SALIR).")
#    return
#while(True):
#    menu()
#    print("\n\t  " + ("*"*54))
#    print("\n\t  Insert Function [sen | cos | tan | exp | log | SALIR]: ")
#    function = input("\t  > ").lower()
#    if(function == "salir"):
#        print("\n\t  " + ("*"*54))
#        print("\n\t\t\t     !!! GOOD BYE !!!")
#        break
#    else:
#        print("\n\t  Insert number: """)
#        number = input("\t  > ")
#        printCalculator =  calculator(function, number)
#        print("\n\t  " + ("-"*54))
#        print("\t  " + function + " v")
#        for i in range(0, len(printCalculator), 1):
#            print("\t      "+ str(i+1) + " = " + str(printCalculator[i]))
#        print("\n\t  " + ("-"*54))

   

#Escribir una función que reciba otra función y una lista, y devuelva otra lista
#con el resultado de aplicar la función dada a cada uno de los elementos de la 
#lista.
#def principalFunction(function, lista):
#    newList = []
#    for i in range(0, len(lista), 1):
#        newList.append(function(lista[i]))
#    return newList
#def functionSquare(num):
#    square = num * num
#    return square
#listInitial = []
#print("\n*************** OPERACION CUADRATICA *************** ")
#print("\nInsert Numeros: ")
#while(True):
#    number = input(" > ")
#    if(not number):
#        break
#    else:
#        listInitial.append(float(number))
##print(listInitial)
#operation1 = principalFunction(functionSquare, listInitial)
#print(operation1)



#Escribir una función que reciba otra función booleana y una lista, y devuelva
#otra lista con los elementos de la lista que devuelva "True" al aplicarse la
#función booleana.
#_________________________________________________________________miOpcionInicio
#def par(n):
#    mod = n % 2
#    print("  " + str(mod) + " - " + str(n))
#    return mod == 0    
#print("mod - n")
#filtro = filter(par, range(7))
#lista = list(filtro)
#print(lista)
#_________________________________________________________________miOpcionFin
#______________________________________________________________otraOpcionInicio
#def filtra_lista(funcion, lista):
#    l = []
#    for i in lista:
#        if funcion(i):
#            l.append(i)
#    return l
#def par(n):
#    mod = n % 2
#    return mod == 0
#filtro = filtra_lista(par, [1, 2, 3, 4, 5, 6])
#print(filtro)
#______________________________________________________________otraOpcionFin



#Escribir una función que reciba una frase y devuelva un diccionario con las 
#palabras que contiene y su longitud.
#def receivePhrase1(phrase):
#    words = []
#    quantity = []
#    dictionary = {}    
#    cutPhraseEach = phrase.split(" ")
#    for i in cutPhraseEach:
#        if(i not in words):
#            words.append(i)
#    for i in range(0, len(words), 1):
#        quantity.append(0)  
#    for i in range( 0, len(words), 1):
#        for j in range(0, len(cutPhraseEach), 1):
#            if (cutPhraseEach[j] == words[i]):
#                quantity[i] = quantity[i] + 1
#    zipDic = zip(words, quantity)
#    dictionary = dict(zipDic)
#    return dictionary
#def receivePhrase2(phrase):
#    words = []
#    length = []
#    dictionary = {}    
#    cutPhraseEach = phrase.split(" ")
#    for i in cutPhraseEach:
#        if(i not in words):
#            words.append(i)
#    for i in range(0, len(words), 1):
#        length.append(len(words[i]))  
#    zipDic = zip(words, length)
#    dictionary = dict(zipDic)
#    return dictionary
#while(True):
#    print("\n" +  ("_"*80))
#    keyboard = input("\nWrite: ")
#    if(keyboard == "*"):
#        break
#    elif(not keyboard):
#        print("YOU DIDN'T ADD ANYTHING ")
#    else:
#        function1 =  receivePhrase1(keyboard)
#        function2 =  receivePhrase2(keyboard)
#        print("\n" +  ("-"*80))
#        print("Frecuency of words")
#        for i in function1:
#            print("\t" + str(i) + " - " + str(function1[i]))
#        print("\nLength of words")
#        for j in function2:
#            print("\t" + str(j) + " - " + str(function2[j]))
#        print(("-"*80))
#        print(("_"*80))



#Escribir una función que reciba una lista de notas y devuelva la lista de
#calificaciones correspondientes a esas notas.
#dictionaryStudents = {}
#def addStudentDictionary(name1):
#    dictionaryStudents[name1] = None
#    return dictionaryStudents
#def addSubjectsNone(subjects1, notes1):
#    array = []
#    for i in range(0, notes1, 1):
#        array.append(None)
#    zipDic = zip(subjects1, array)
#    dictionarySubjects = dict(zipDic)
#    return dictionarySubjects
#def menu():
#    print("\n\t " + ("*"*57))
#    print("\t ********************* RATING SYSTEM ********************* ")
#    print("\n\t\t\t      1. Add student.")
#    print("\t\t\t      2. Add subjects.")
#    print("\t\t\t      3. Add Notes.")
#    print("\t\t\t      4. Student grades.")
#    print("\t\t\t      5. EXIT.")
#    print("\n\t\t\t     Choose an option:  ")
#    return
#while(True):
#    menu()
#    option = input("\t\t\t     > ")
#    if(not option):
#        print("\t\t       !!! YOU DIDN'T ADD OPTION !!! ")
#    elif(option == "1"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 1. Add student.")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Add name of new student[yes|no]:")
#            option1 = input("\t    > ").lower()
#            if(not option1):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option1 == "yes"):
#                while(True):
#                    print("\t    " + ("-"*51))
#                    nameStudent =  input("\t    Enter student's name: ").title()
#                    if(not nameStudent):
#                        print("\t\t     !!! YOU DIDN'T ADD STUDENT'S NAME !!! ")
#                        print("\t    " + ("-"*51))
#                    else:
#                        addStudentPrint1 = addStudentDictionary(nameStudent)
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#            elif(option1 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")
#    elif(option == "2"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 2. Add subjects.")
#        print("\n\t    NOTE: Add subjects separated by commas(,).")
#        print("\t          For example: mathematics, physics, chemistry,")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Add name of new student[yes|no]:")
#            option2 = input("\t    > ").lower()
#            if(not option2):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option2 == "yes"):
#                while(True):
#                    print("\t    " + ("-"*51))
#                    searchStudent2 = input("\t    Enter student's name: ").title()
#                    if(searchStudent2 in dictionaryStudents):
#                        print("\t    " + ("."*51))
#                        print("\t    Subjects to take: ")
#                        arraySubjects = []
#                        subjects =  input("\t    > ").lower()
#                        subSplit = subjects.split(", ")
#                        for i in range(0, len(subSplit), 1):
#                            eraseComma = subSplit[i].replace(",", "")
#                            arraySubjects.append(eraseComma)
#                        for j in range(0, len(arraySubjects), 1):
#                            if(arraySubjects[j] == ""):
#                                arraySubjects.pop()
#                        addSubjectsPrint = addSubjectsNone(arraySubjects, len(arraySubjects))
#                        #print(addSubjectsPrint)
#                        dictionaryStudents[searchStudent2] = addSubjectsPrint
#                        print("\t    " + ("."*51))
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#                    elif(searchStudent2 not in dictionaryStudents):
#                        print("\n\t\t         !!! STUDENT NOT FOUND !!!")
#                        print("\t    " + ("-"*51) + "\n")
#            elif(option2 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")        
#    elif(option == "3"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 3. Add notes.")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Place students grades[yes|no]: ")
#            option3 = input("\t    > ").lower()
#            if(not option3):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option3 == "yes"):
#                while(True):
#                    print("\n\t    " + ("-"*51))
#                    searchStudent3 =  input("\t    Enter student's name: ").title()
#                    if(searchStudent3 in dictionaryStudents):
#                        print("\t    " + ("."*51))
#                        print("\t\t    Add qualifications: \n")
#                        dictionaryPersonal = dictionaryStudents[searchStudent2]
#                        for i in dictionaryPersonal:
#                            calif = float(input( "\t\t        > "+ i + ": "))
#                            dictionaryPersonal[i] = calif
#                        print("\t    " + ("."*51))
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#                    elif(searchStudent3 not in dictionaryStudents):
#                        print("\n\t\t         !!! STUDENT NOT FOUND !!!")
#                        print("\t    " + ("-"*51) + "\n\n")
#            elif(option3 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")
#    elif(option == "4"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 4. Student grades.")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Place students grades[yes|no]: ")
#            option4 = input("\t    > ").lower()
#            if(not option4):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option4 == "yes"):
#                while(True):
#                    print("\n\t    " + ("-"*51))
#                    searchStudent3 =  input("\t    Enter student's name: ").title()
#                    if(searchStudent3 in dictionaryStudents):
#                        print("\t    " + ("."*51))
#                        print("\t\t    Student grades: \n")
#                        dictionaryPersonal = dictionaryStudents[searchStudent2]
#                        summation = 0
#                        for i in dictionaryPersonal:
#                            print("\t\t        > " + str(i) + ": "+ str(dictionaryPersonal[i]))
#                            summation += dictionaryPersonal[i]
#                        generalAverage = summation / (len(dictionaryPersonal))
#                        print("\n\t\t    > General Average: " + str(round(generalAverage,2)))
#                        print("\t    " + ("."*51))
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#                    elif(searchStudent3 not in dictionaryStudents):
#                        print("\n\t\t         !!! STUDENT NOT FOUND !!!")
#                        print("\t    " + ("-"*51) + "\n\n")
#            elif(option4 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")
#    elif(option == "5"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t\t\t      !!! GOOD BYE!!!")
#        print("\t\t\t   !!! COME BACK SOON !!!")
#        print("\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        break
#    else: 
#        print("\t\t          !!! INVALID OPTION !!!")



#Escribir una función que reciba un diccionario con las asignaturas y las notas
#de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y
#las calificaciones correspondientes a las notas.
# A+ = 4.00 = 10.0 = sobresaliente
# A  = 3.67 = 9.18 = sobresaliente
# B+ = 3.33 = 8.32 = notable(alto)
# B  = 3.00 = 7.50 = notable
# B- = 2.67 = 6.67 = notable(bajo)
# C+ = 2.33 = 5.83 = bien
# C  = 2.00 = 5.00 = suficiente
# C- = 1.67 = 4.17 = sufiente(bajo)
# D+ = 1.33 = 3.33 = Insuficiente
# D  = 1.00 = 2.50 = Insuficiente
# D- = 0.67 = 1.68 = Insuficiente
# F  = 0.00 = 0.00 = muy deficiente-suspenso
#dictionaryNotes = {"A+":4.00,
#                   "A":3.67,
#                   "B+":3.33,
#                   "B":3.00,
#                   "B-":2.67,
#                   "C+":2.33,
#                   "C":2.00,
#                   "C-":1.67,
#                   "D+":1.33,
#                   "D":1.00,
#                   "D-":0.67,
#                   "F":0.00}
#dictionaryStudents = {}
#def addStudentDictionary(name1):
#    dictionaryStudents[name1] = None
#    return dictionaryStudents
#def addSubjectsNone(subjects1, notes1):
#    array = []
#    for i in range(0, notes1, 1):
#        array.append(None)
#    zipDic = zip(subjects1, array)
#    dictionarySubjects = dict(zipDic)
#    return dictionarySubjects
#def notesAverage(AverageToNote):
#    if( 3.67 < AverageToNote <= 4.00):
#        return "\n\t\t    > General Note: A+"
#    elif(3.33 < AverageToNote <= 3.67):
#         return "\n\t\t    > General Note: A"
#    elif(3.00 < AverageToNote <= 3.33):
#        return "\n\t\t    > General Note: B+"
#    elif(2.67 < AverageToNote <= 3.00):
#        return "\n\t\t    > General Note: B"
#    elif(2.33 < AverageToNote <= 2.67):
#        return "\n\t\t    > General Note: B-"
#    elif(2.00 < AverageToNote <= 2.33):
#        return "\n\t\t    > General Note: C+"
#    elif(1.67 < AverageToNote <= 2.00):
#        return "\n\t\t    > General Note: C"
#    elif(1.33 < AverageToNote <= 1.67):
#        return "\n\t\t    > General Note: C-"
#    elif(1.00 < AverageToNote <= 1.33):
#        return "\n\t\t    > General Note: D+"
#    elif(0.67 < AverageToNote <= 1.00):
#        return "\n\t\t    > General Note: D"
#    elif(0.00 < AverageToNote <= 0.67):
#        return "\n\t\t    > General Note: D-"
#    elif(AverageToNote == 0 ):
#        return "\n\t\t    > General Note: F"
#def approvedSubjects(k, note):
#    return "\t\t        > " + str(k) + ": " + str(note)
#def menu():
#    print("\n\t " + ("*"*57))
#    print("\t ********************* RATING SYSTEM ********************* ")
#    print("\n\t\t\t      1. Add student.")
#    print("\t\t\t      2. Add subjects.")
#    print("\t\t\t      3. Add notes of subjects.")
#    print("\t\t\t      4. Student grades.")
#    print("\t\t\t      5. EXIT.")
#    print("\n\t\t\t     Choose an option:  ")
#    return
#while(True):
#    menu()
#    option = input("\t\t\t     > ")
#    if(not option):
#        print("\t\t       !!! YOU DIDN'T ADD OPTION !!! ")
#    elif(option == "1"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 1. Add student.")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Add name of new student[yes|no]:")
#            option1 = input("\t    > ").lower()
#            if(not option1):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option1 == "yes"):
#                while(True):
#                    print("\t    " + ("-"*51))
#                    nameStudent =  input("\t    Enter student's name: ").title()
#                    if(not nameStudent):
#                        print("\t\t     !!! YOU DIDN'T ADD STUDENT'S NAME !!! ")
#                        print("\t    " + ("-"*51))
#                    else:
#                        addStudentPrint1 = addStudentDictionary(nameStudent)
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#            elif(option1 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")
#    elif(option == "2"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 2. Add subjects.")
#        print("\n\t    NOTE: Add subjects separated by commas(,).")
#        print("\t          For example: mathematics, physics, chemistry,")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Add name of student[yes|no]:")
#            option2 = input("\t    > ").lower()
#            if(not option2):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option2 == "yes"):
#                while(True):
#                    print("\t    " + ("-"*51))
#                    searchStudent2 = input("\t    Enter student's name: ").title()
#                    if(searchStudent2 in dictionaryStudents):
#                        print("\t    " + ("."*51))
#                        print("\t    Subjects to take: ")
#                        arraySubjects = []
#                        subjects =  input("\t    > ").upper()
#                        subSplit = subjects.split(", ")
#                        for i in range(0, len(subSplit), 1):
#                            eraseComma = subSplit[i].replace(",", "")
#                            arraySubjects.append(eraseComma)
#                        for j in range(0, len(arraySubjects), 1):
#                            if(arraySubjects[j] == ""):
#                                arraySubjects.pop()
#                        addSubjectsPrint = addSubjectsNone(arraySubjects, len(arraySubjects))
#                        #print(addSubjectsPrint)
#                        dictionaryStudents[searchStudent2] = addSubjectsPrint
#                        print("\t    " + ("."*51))
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#                    elif(searchStudent2 not in dictionaryStudents):
#                        print("\n\t\t         !!! STUDENT NOT FOUND !!!")
#                        print("\t    " + ("-"*51) + "\n")
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#            elif(option2 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")        
#    elif(option == "3"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 3. Add notes.")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Record students grades[yes|no]: ")
#            option3 = input("\t    > ").lower()
#            if(not option3):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option3 == "yes"):
#                while(True):
#                    print("\n\t    " + ("-"*51))
#                    searchStudent3 =  input("\t    Enter student's name: ").title()
#                    if(searchStudent3 in dictionaryStudents):
#                        print("\t    " + ("."*51))
#                        print("\t\t    Add qualifications: \n")
#                        dictionaryPersonal = dictionaryStudents[searchStudent3]
#                        for i in dictionaryPersonal:
#                            calif = input( "\t\t        > "+ i + ": ").upper()
#                            while(calif not in dictionaryNotes):
#                                calif = input( "\t\t        > "+ i + ": ").upper()
#                            if(calif in dictionaryNotes):
#                                dictionaryPersonal[i] = calif
#                        print("\t    " + ("."*51))
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#                    elif(searchStudent3 not in dictionaryStudents):
#                        print("\n\t\t         !!! STUDENT NOT FOUND !!!")
#                        print("\t    " + ("-"*51) + "\n\n")
#            elif(option3 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")
#    elif(option == "4"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 4. Student grades.")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Place students grades[yes|no]: ")
#            option4 = input("\t    > ").lower()
#            if(not option4):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option4 == "yes"):
#                while(True):
#                    print("\n\t    " + ("-"*51))
#                    searchStudent3 =  input("\t    Enter student's name: ").title()
#                    if(searchStudent3 in dictionaryStudents):
#                        print("\t    " + ("."*51))
#                        print("\t\t    STUDENT´S OVERALL GRADES: \n")
#                        dictionaryPersonal = dictionaryStudents[searchStudent3]
#                        summation = 0
#                        for i in dictionaryPersonal:
#                            valueNote = dictionaryNotes[dictionaryPersonal[i]]
#                            noteToQualif = (valueNote*10) / 4
#                            print("\t\t        > " + str(i) + ": " + str(dictionaryPersonal[i]) + " : " + str(valueNote) + " : " + str(noteToQualif))
#                            summation += noteToQualif
#                        generalAverage = summation / (len(dictionaryPersonal))
#                        roundAverage = round(generalAverage,2)
#                        print("\n\t\t    > General Average: " + str(roundAverage))
#                        AverageToNote = (roundAverage*4)/10
#                        notesPrint = notesAverage(AverageToNote)
#                        print(notesPrint)
#                        print("\t    " + ("."*51))
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#                    elif(searchStudent3 not in dictionaryStudents):
#                        print("\n\t\t         !!! STUDENT NOT FOUND !!!")
#                        print("\t    " + ("-"*51) + "\n\n")
#            elif(option4 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")
#    elif(option == "5"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t\t\t      !!! GOOD BYE!!!")
#        print("\t\t\t   !!! COME BACK SOON !!!")
#        print("\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        break
#    else: 
#        print("\t\t          !!! INVALID OPTION !!!")



#Escribir una función que reciba un diccionario con las asignaturas y las notas 
#de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y 
#las calificaciones correspondientes a las notas aprobadas.
#dictionaryNotes = {"A+":4.00, "A":3.67, "B+":3.33, "B":3.00, "B-":2.67, "C+":2.33,
#                   "C":2.00, "C-":1.67, "D+":1.33, "D":1.00, "D-":0.67, "F":0.00}
#dictionaryStudents = {}
#dictionaryApprovedSubjects = {}
#dictionaryFailedSubjects = {}
#def addStudentDictionary(name1):
#    dictionaryStudents[name1] = None
#    dictionaryApprovedSubjects[name1] = None
#    dictionaryFailedSubjects[name1] = None
#    return dictionaryStudents, dictionaryApprovedSubjects, dictionaryFailedSubjects
#def addSubjectsNone(subjects1, notes1):
#    array = []
#    for i in range(0, notes1, 1):
#        array.append(None)
#    zipDic = zip(subjects1, array)
#    dictionarySubjects = dict(zipDic)
#    return dictionarySubjects
#def notesAverage(AverageToNote):
#    if( 3.67 < AverageToNote <= 4.00):
#        return "\t\t    > General Note: A+"
#    elif(3.33 < AverageToNote <= 3.67):
#        return "\t\t    > General Note: A"
#    elif(3.00 < AverageToNote <= 3.33):
#        return "\t\t    > General Note: B+"
#    elif(2.67 < AverageToNote <= 3.00):
#        return "\t\t    > General Note: B"
#    elif(2.33 < AverageToNote <= 2.67):
#        return "\t\t    > General Note: B-"
#    elif(2.00 < AverageToNote <= 2.33):
#        return "\t\t    > General Note: C+"
#    elif(1.67 < AverageToNote <= 2.00):
#        return "\t\t    > General Note: C"
#    elif(1.33 < AverageToNote <= 1.67):
#        return "\t\t    > General Note: C-"
#    elif(1.00 < AverageToNote <= 1.33):
#        return "\t\t    > General Note: D+"
#    elif(0.67 < AverageToNote <= 1.00):
#        return "\t\t    > General Note: D"
#    elif(0.00 < AverageToNote <= 0.67):
#        return "\t\t    > General Note: D-"
#    elif(AverageToNote == 0 ):
#        return "\t\t    > General Note: F"
#def addApprovedFailedSubjects(calif, i):
#    if((calif == "A+") or (calif == "A") or (calif == "B+") or (calif == "B") or (calif == "B-")):
#        dictionaryPersonalApproved[i] = calif
#        dictionaryReturn1 = dictionaryPersonalApproved[i]
#        return dictionaryReturn1 
#    elif((calif == "C+") or (calif == "C") or (calif == "C-") or (calif == "D+") or (calif == "D") or (calif == "D-") or (calif == "F")):
#        dictionaryPersonalFailed[i] = calif
#        dictionaryReturn2 = dictionaryPersonalFailed[i]
#        return dictionaryReturn2
#def menu():
#    print("\n\t " + ("*"*57))
#    print("\t ********************* RATING SYSTEM ********************* ")
#    print("\n\t\t\t      1. Add student.")
#    print("\t\t\t      2. Add subjects.")
#    print("\t\t\t      3. Add notes of subjects.")
#    print("\t\t\t      4. Student grades.")
#    print("\t\t\t      5. EXIT.")
#    print("\n\t\t\t     Choose an option:  ")
#    return
#while(True):
#    menu()
#    option = input("\t\t\t     > ")
#    if(not option):
#        print("\t\t       !!! YOU DIDN'T ADD OPTION !!! ")
#    elif(option == "1"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 1. Add student.")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Add name of new student[yes|no]:")
#            option1 = input("\t    > ").lower()
#            if(not option1):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option1 == "yes"):
#                while(True):
#                    print("\t    " + ("-"*51))
#                    nameStudent =  input("\t    Enter student's name: ").title()
#                    if(not nameStudent):
#                        print("\t\t     !!! YOU DIDN'T ADD STUDENT'S NAME !!! ")
#                        print("\t    " + ("-"*51))
#                    else:
#                        addStudentPrint1 = addStudentDictionary(nameStudent)
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#            elif(option1 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")
#    elif(option == "2"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 2. Add subjects.")
#        print("\n\t    NOTE: Add subjects separated by commas(,).")
#        print("\t          For example: mathematics, physics, chemistry,")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Add name of student[yes|no]:")
#            option2 = input("\t    > ").lower()
#            if(not option2):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option2 == "yes"):
#                while(True):
#                    print("\t    " + ("-"*51))
#                    searchStudent2 = input("\t    Enter student's name: ").title()
#                    if(searchStudent2 in dictionaryStudents):
#                        print("\t    " + ("."*51))
#                        print("\t    Subjects to take: ")
#                        arraySubjects = []
#                        subjects =  input("\t    > ").upper()
#                        subSplit = subjects.split(", ")
#                        for i in range(0, len(subSplit), 1):
#                            eraseComma = subSplit[i].replace(",", "")
#                            arraySubjects.append(eraseComma)
#                        for j in range(0, len(arraySubjects), 1):
#                            if(arraySubjects[j] == ""):
#                                arraySubjects.pop()
#                        addSubjectsPrint = addSubjectsNone(arraySubjects, len(arraySubjects))
#                        dictionaryStudents[searchStudent2] = addSubjectsPrint
#                        dictionaryApprovedSubjects[searchStudent2] = dict()
#                        dictionaryFailedSubjects[searchStudent2] = dict()
#                        print("\t    " + ("."*51))
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#                    elif(searchStudent2 not in dictionaryStudents):
#                        print("\n\t\t         !!! STUDENT NOT FOUND !!!")
#                        print("\t    " + ("-"*51) + "\n")
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#            elif(option2 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")        
#    elif(option == "3"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 3. Add notes.")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Record students grades[yes|no]: ")
#            option3 = input("\t    > ").lower()
#            if(not option3):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option3 == "yes"):
#                while(True):
#                    print("\n\t    " + ("-"*51))
#                    searchStudent3 =  input("\t    Enter student's name: ").title()
#                    if(searchStudent3 in dictionaryStudents):
#                        print("\t    " + ("."*51))
#                        print("\t\t    Add qualifications: \n")
#                        dictionaryPersonal = dictionaryStudents[searchStudent3]
#                        dictionaryPersonalApproved = dictionaryApprovedSubjects[searchStudent3]
#                        dictionaryPersonalFailed = dictionaryFailedSubjects[searchStudent3]
#                        for i in dictionaryPersonal:
#                            calif = input( "\t\t        > "+ i + ": ").upper()
#                            while(calif not in dictionaryNotes):
#                                calif = input( "\t\t        > "+ i + ": ").upper()
#                            if(calif in dictionaryNotes):
#                                dictionaryPersonal[i] = calif
#                                addApprovedFailedSubjects(calif, i)
#                        print("\t    " + ("."*51))
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#                    elif(searchStudent3 not in dictionaryStudents):
#                        print("\n\t\t         !!! STUDENT NOT FOUND !!!")
#                        print("\t    " + ("-"*51) + "\n\n")
#            elif(option3 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")
#    elif(option == "4"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t 4. Student grades.")
#        while(True):
#            print("\t    " + ("_"*51))
#            print("\t    Place students grades[yes|no]: ")
#            option4 = input("\t    > ").lower()
#            if(not option4):
#                print("\t      !!! YOU DIDN'T ADD OPTION !!! ")
#                print("\t    " + ("_"*51) + "\n\n")
#            elif(option4 == "yes"):
#                while(True):
#                    print("\n\t    " + ("-"*51))
#                    searchStudent3 =  input("\t    Enter student's name: ").title()
#                    if(searchStudent3 in dictionaryStudents):
#                        print("\t    " + ("."*51))
#                        print("\t\t    STUDENT´S OVERALL GRADES: \n")
#                        dictionaryPersonal = dictionaryStudents[searchStudent3]
#                        summation = 0
#                        for i in dictionaryPersonal:
#                            valueNote = dictionaryNotes[dictionaryPersonal[i]]
#                            noteToQualif = (valueNote*10) / 4
#                            print("\t\t        > " + str(i) + ": " + str(dictionaryPersonal[i]) + " : " + str(valueNote) + " : " + str(noteToQualif))
#                            summation += noteToQualif
#                        generalAverage = summation / (len(dictionaryPersonal))
#                        roundAverage = round(generalAverage,2)
#                        print("\n\t\t    > General Average: " + str(roundAverage))
#                        AverageToNote = (roundAverage*4)/10
#                        notesPrint = notesAverage(AverageToNote)
#                        print(notesPrint)
#                        print("\n\n\t\t    APPROVED SUBJECTS: \n")
#                        dictionaryPersonalApproved = dictionaryApprovedSubjects[searchStudent3]
#                        for i in dictionaryPersonalApproved:
#                            valueNote = dictionaryNotes[dictionaryPersonalApproved[i]]
#                            noteToQualif = (valueNote*10) / 4
#                            print("\t\t        > " + str(i) + ": " + str(dictionaryPersonalApproved[i]) + " : " + str(valueNote) + " : " + str(noteToQualif))
#                        print("\n\n\t\t    FAILED SUBJECTS: \n")
#                        dictionaryPersonalFailed = dictionaryFailedSubjects[searchStudent3]
#                        for i in dictionaryPersonalFailed:
#                            valueNote = dictionaryNotes[dictionaryPersonalFailed[i]]
#                            noteToQualif = (valueNote*10) / 4
#                            print("\t\t        > " + str(i) + ": " + str(dictionaryPersonalFailed[i]) + " : " + str(valueNote) + " : " + str(noteToQualif))
#                        print("\t    " + ("."*51))
#                        print("\t    " + ("-"*51) )
#                        print("\t    " + ("_"*51) + "\n\n")
#                        break
#                    elif(searchStudent3 not in dictionaryStudents):
#                        print("\n\t\t         !!! STUDENT NOT FOUND !!!")
#                        print("\t    " + ("-"*51) + "\n\n")
#            elif(option4 == "no"):
#                print("\t    " + ("_"*51))
#                print("\n\t " + ("*"*57))
#                print("\t " + ("*"*57) + "\n")
#                break
#            else:
#                print("\t      !!! INVALID OPTION !!!")
#                print("\t    " + ("_"*51) + "\n\n")
#    elif(option == "5"):
#        print("\n\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        print("\t\t\t      !!! GOOD BYE!!!")
#        print("\t\t\t   !!! COME BACK SOON !!!")
#        print("\t " + ("*"*57))
#        print("\t " + ("*"*57))
#        break
#    else: 
#        print("\t\t          !!! INVALID OPTION !!!")



#Escribir una función que calcule el módulo de un vector.
#   ->      ___________
# | v | = _| x^2 + y^2
#
#import math
#alphabet = """abcdefghijklmnñopqrstuvwxyz|°¬!"#$%&/=?'\¡¿´¨*+~[^{]`};:_"""
#def menu():
#    print("\n\t " + ("*"*62))
#    print("\t ********************* MODULE OF A VECTOR ********************* ")
#    print("\n\t\t        1. Calculate modulus of a vector.")
#    print("\t\t        2. EXIT.")
#    print("\n\t\t\t       Choose an option:  ")
#    return    
#def moduleVector(vector):
#    summation = 0
#    for i in range(0, len(vector), 1):
#        summation += (vector[i] **2)
#    squareRoot = math.sqrt(summation)
#    return squareRoot
#while(True):
#    menu()
#    option = input("\t\t\t       > ")
#    if(not option):
#        print("\t\t     |-----------------------------------|")
#        print("\t\t     |   !!! YOU DIDN'T ADD OPTION !!!   |")
#        print("\t\t     |-----------------------------------|")
#        print("\n\t " + ("*"*62))
#        print("\t " + ("*"*62) + "\n\n")
#    elif(option == "1"):
#        print("\n\t " + ("*"*62))
#        print("\t " + ("*"*62) + "\n\n")
#        print("\t " + ("*"*62))
#        print("\t " + ("*"*62))
#        print("\t 1. Calculate modulus of a vector.")
#        print("\n\t    Section information: This section calculates the modulus")
#        print("\t\t\t\t of a vector in 2 and 3 axes with a")
#        print("\t\t\t\t point at the origin(0).")
#        print("\n\t    How to use: Enter the vector in R2(x,y) or R3(x,y,z).")
#        print("\t\t        For example: ")
#        print("\t\t\t\t    In R2: Vector> (2,3)")
#        print("\t\t\t\t    In R3: Vector> (2,3,-1)")
#        while(True):
#            print("\n\t     " + ("-"*54))
#            option1 = input("\t     Enter vector?[yes|no]: ").lower()
#            if(not option1):
#                print("\n\t\t     |-----------------------------------|")
#                print("\t\t     |   !!! YOU DIDN'T ADD OPTION !!!   |")
#                print("\t\t     |-----------------------------------|")
#                print("\t     " + ("-"*54))
#            elif(option1 == "yes"):
#                arrayVector = []
#                arrayStringVector = []
#                vector1 = input("\n\t        Vector > ")
#                while(not vector1):
#                    print("\t\t     !!! YOU DIDN'T ADD VECTOR !!!")
#                    vector1 = input("\n\t        Vector > ")
#                if(vector1):
#                    for i in range(0, len(vector1),1):
#                        if(vector1[i] in alphabet):
#                            print("\t\t        !!! YOU ADDED INVALID CHARACTERS !!!")
#                            break
#                        elif(vector1[i] not in alphabet):
#                            arrayStringVector.append(vector1[i])
#                    if(("(" == (arrayStringVector[0])) and ("," in arrayStringVector) and (")" == (arrayStringVector[(len(arrayStringVector))-1])) ):
#                        joinArray = "".join(arrayStringVector)
#                        erace1= joinArray.replace("(", "")
#                        erace2 = erace1.replace(")", "") 
#                        newArray = list(erace2.split(","))
#                        for i in range(0, len(newArray), 1):
#                            TransformStrToFloat = float(newArray[i])
#                            arrayVector.append(TransformStrToFloat)
#                        if(((len(arrayVector)) == 2) or ((len(arrayVector)) == 3)):
#                            function1 = moduleVector(arrayVector)
#                            print("\t\t       > Module Vector: " + str(round(function1,4)))
#                            print("\t     " + ("-"*54))
#                        else:
#                            print("\t\t        !!! INVALID VECTOR !!!")
#                            print("\t     " + ("-"*54))
#                    else:
#                        print("\t\t        !!! INVALID VECTOR !!!")
#                        print("\t     " + ("-"*54))
#            elif(option1 == "no"):
#                print("\t     " + ("-"*54))
#                print("\n\t " + ("*"*62))
#                print("\t " + ("*"*62) + "\n\n")
#                break
#            else:
#                print("\n\t\t\t |----------------------------|")
#                print("\t\t\t |   !!! INVALID OPTION !!!   |")
#                print("\t\t\t |----------------------------|")
#                print("\t     " + ("-"*54))
#    elif(option == "2"):
#        print("\n\t " + ("*"*62))
#        print("\t " + ("*"*62))
#        print("\n\n\t " + ("*"*62))
#        print("\t " + ("*"*62))
#        print("\t\t\t      !!! GOOD BYE!!!")
#        print("\t\t\t   !!! COME BACK SOON !!!")
#        print("\t " + ("*"*62))
#        print("\t " + ("*"*62))
#        break
#    else:
#        print("\t\t\t|----------------------------|")
#        print("\t\t\t|   !!! INVALID OPTION !!!   |")
#        print("\t\t\t|----------------------------|")
#        print("\n\t " + ("*"*62))
#        print("\t " + ("*"*62) + "\n\n")



#Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
#  [ {'año':2000, 'metros':100, 'habitaciones':3, 'garaje': True, 'zona': 'A'},
#    {'año':2012, 'metros': 60, 'habitaciones':2, 'garaje': True, 'zona': 'B'},
#    {'año':1980, 'metros':120, 'habitaciones':4, 'garaje':False, 'zona': 'A'},
#    {'año':2005, 'metros': 75, 'habitaciones':3, 'garaje': True, 'zona': 'B'},
#    {'año':2015, 'metros': 90, 'habitaciones':2, 'garaje':False, 'zona': 'A'} ]
#Construir una función que permita hacer búsqueda de inmuebles en función de un  
#presupuesto dado. La función recibirá como entrada la lista de inmuebles y un
#precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva
#deben incorporar un nuevo par a cada diccionario con el precio del inmueble,
#donde el precio de un inmueble se calcula con la siguiente fórmula en función 
#de la zona:
# zona A:
#  precio=(metros*1000)+(habitaciones*5000)+(garaje*15000)+(1-antiguedad/100)
# zona B:
#  precio=(metros*1000)+(habitaciones*5000)+(garaje*15000)+(1-antiguedad/100)*1.5
alphabet = """abcdefghijklmnñopqrstuvwxyz|°¬!"#$%&/=?'\¡¿´¨*+~[^{]`};:_-(),"""
estateDatabasePrin = {"propiedad 1":{'año':2000, 'metros':100, 'habitaciones':3, 'garaje': True, 'zona': 'A'},
                      "propiedad 2":{'año':2012, 'metros': 60, 'habitaciones':2, 'garaje': True, 'zona': 'B'},
                      "propiedad 3":{'año':1980, 'metros':120, 'habitaciones':4, 'garaje':False, 'zona': 'A'},
                      "propiedad 4":{'año':2005, 'metros': 75, 'habitaciones':3, 'garaje': True, 'zona': 'B'},
                      "propiedad 5":{'año':2015, 'metros': 90, 'habitaciones':2, 'garaje':False, 'zona': 'A'}}
def addProperty():
    nameProperty = input("\t    Enter property name: ").lower()
    while(not nameProperty):
        print("no agregaste nombre")
        nameProperty = input("\t    Enter property name: ").lower()
    while(nameProperty in estateDatabasePrin):
        print("nombre de propiedad ya existe.")
        nameProperty = input("\t    Enter property name: ").lower()
    
    metersProperty = input("\t    Enter the average of the property(meters): ")
    while(not metersProperty):
        print("no agregaste metros")
        metersProperty = input("\t    Enter the average of the property(meters): ")
    arrayMeters = []

    for i in range(0, len(metersProperty),1):
        print(str(i) + " - " + str(metersProperty[i]))
        
        
    


    
    numberRoomProperty = input("\t    Enter number of rooms of property: ")

    garajeProperty = input("\t    Do you have a gareje? Enter[yes|no]: ").lower()
    while(not garajeProperty):
        print("no agregaste nada")
        garajeProperty = input("\t    Do you have a gareje? Enter[yes|no]: ").lower()
    

    zoneProperty =  input("\t    Enter zone[A|B]: ").upper()
    while(not zoneProperty):
        print("no agregaste nombre")
        zoneProperty =  input("\t    Enter zone[A|B]: ").upper()
    
    return

def estateSearh():
    return
def menu():
    print("\n\t " + ("*"*55))
    print("\t ********************* REAL ESTATE ********************* ")
    print("\t 1. Add property. ")
    print("\t 2. Update information property.")
    print("\t 3. Delete property. ")
    print("\t 4. Search property.") 
    print("\t 5. Property information. ")
    print("\t 6. EXIT.")
    print("\n\t Choose an option: ")
    return
while(True):
    menu()
    option = input("\t\t\t > ")
    if(not option):
        print("no agregaste opcion")
    elif(option == "1"):
        print("\n\t " + ("*"*55))
        print("\t " + ("*"*55) + "\n\n")
        print("\t " + ("*"*55))
        print("\t " + ("*"*55))
        print("\t 1. Add property. ")
        while(True):
            print("\n\t    Do you want to add a new property?")
            option1 = input("\t    [yes|no]> ").lower()
            if(not option1):
                print("no agregaste nada")
            elif(option1 == "yes"):
                addProperty()
                print
            elif(option1 == "no"):
                print("\t " + ("*"*55))
                print("\t " + ("*"*55) + "\n")
                break
            else:
                print("invalid option")
        
    elif(option == "2"):
        
        print("\t 2. Update information property. ")
        
    elif(option == "3"):
        print("\t 3. Delete property. ")
        
    elif(option == "4"):
        print("\t 4. Search property. ")
        
    elif(option == "5"):
        print("\t 5. Property information. ")
        
    elif(option == "6"):
        print("\n\t " + ("*"*62))
        print("\t " + ("*"*62))
        print("\n\n\t " + ("*"*62))
        print("\t " + ("*"*62))
        print("\t\t\t      !!! GOOD BYE!!!")
        print("\t\t\t   !!! COME BACK SOON !!!")
        print("\t " + ("*"*62))
        print("\t " + ("*"*62))
        break
    else:
        print("")
        print("\t\t\t|----------------------------|")
        print("\t\t\t|   !!! INVALID OPTION !!!   |")
        print("\t\t\t|----------------------------|")
        print("\n\t " + ("*"*62))
        print("\t " + ("*"*62) + "\n\n")

#for i in range(0, len(estateDatabasePrin), 1):
#    estate = estateDatabasePrin[i]
#    print("\n"+ "-"*20)
#    for i in estate:
#        print(str(i) + ": " + str(estate[i]))
#for i in range(0, len(estateDatabasePrin), 1):
#    estate = estateDatabasePrin[i]
#    if(estate["zona"] == "A"):
#        metrosA = estate["metros"] * 1000
#        habitacionesA = estate["habitaciones"] * 5000
#        garajeA = int(estate["garaje"]) * 15000
#        antiguedadA = 1 - estate["año"] / 100
#        precio = metrosA + habitacionesA + garajeA + antiguedadA
#        estate["precio"] = precio
#    elif(estate["zona"] == "B"):
#        metrosA = estate["metros"] * 1000
#        habitacionesA = estate["habitaciones"] * 5000
#        garajeA = int(estate["garaje"]) * 15000
#        antiguedadA = 1 - estate["año"] / 100
#        precio = metrosA + habitacionesA + garajeA + antiguedadA * 1.5
#        estate["precio"] = round(precio,2)
#print("\n\n\n")
#for i in range(0, len(estateDatabasePrin), 1):
#    estate = estateDatabasePrin[i]
#    print("\n"+ "-"*20)
#    for i in estate:
#        print(str(i) + ": " + str(estate[i]))







#Escribir una función que reciba una muestra de números y devuelva los valores 
#atípicos, es decir, los valores cuya puntuación típica se mayor que 3 o menor
#que -3. Nota: La puntuación típica de un valor se obtiene restando la media y
#dividiendo por la desviación típica de la muestra.



