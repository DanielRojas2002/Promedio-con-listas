def Promedio(lista_de_listas,materias):
    
    print("1=Quiero saber el promedio de todos los alumnos\n2=Quiero saber el promedio del grupo")
    menu=int(input(":"))
    promedioFinal=0
    listaP=[]
    if menu==1:
        contadorAl=0
        for nivel in lista_de_listas:
            suma=0
            contadorAl+=1
            for elemento in nivel:
                suma=suma+elemento
                promedio=suma/materias
                listaP.append(promedio)
            print(f"El promedio del alumno {contadorAl} es: {promedio}")
    
    elif menu==2:
        contadorAl=0
        for nivel in lista_de_listas:
            suma=0
            contadorAl+=1
            for elemento in nivel:
                suma=suma+elemento
            promedio=suma/materias
            promedioFinal=promedioFinal+promedio
        promFinal=promedioFinal/contadorAl
        print(f"Promedio Grupal :{promFinal}")


opcion=1

while opcion==1:
    separador=("*"*40)
    lista_de_listas=[]
    contadorMate=0
    contadorA=0
    print("*"*20,"Menu Principal","*"*20)
    materias=int(input("Cuantas Materias llevas : "))
    alumnos=int(input("Cuantos alumnos son : "))
    print(separador)
    for alumno in range(alumnos):
        contadorA+=1
        print(f"Alumno {contadorA}:")
        listaNota=[]
        lista_de_listas.append(listaNota)
        contadorMate=0
        for materia in range(materias):
            contadorMate+=1
            nota=int(input(f"Calificacion {contadorMate} : "))
            print(separador)
            listaNota.append(nota)
    Promedio(lista_de_listas,materias)
    print("1=SI\n2=NO")
    opcion=int(input("Quieres seguir con el programa : "))
