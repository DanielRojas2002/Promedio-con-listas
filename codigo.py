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