import matplotlib.pyplot as plt
import sys

def Promedio(lista_de_listas,materias):
    print(separador)
    print("1=Quiero saber el promedio de todos los alumnos(los agrega a un .txt)\n2=Quiero saber el promedio de todos los alumnos y del grupo(los agrega a un .txt)")
    menu=int(input(":"))
    print(separador)
    promedioFinal=0
    listaP=[]
    archivoA=open("./archivos/Calificacion.txt" , 'a')
    if menu==1:
        contadorAl=0
        for nivel in lista_de_listas:
            suma=0
            contadorAl+=1
            for elemento in nivel:
                suma=suma+elemento
            promedio=suma/materias
            
            textoa=str(contadorAl)
            textop=str(promedio)
            archivoA.write("Promedio del Alumno "+ textoa+" = "+ textop +"\n" )
            listaP.append(promedio)
            print(f"El promedio del alumno {contadorAl} es: {promedio}")
            print(separador)
        archivoA.close()
        archivoB=open("./archivos/PromGrupal.txt" , 'a')
        archivoB.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoB.write("No elegiste la funcion de sacar el promedio Grupal"+"\n")
        archivoB.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoB.close()

            
        print("1=SI\n2=NO")
        submenu=int(input("Quieres Graficar lo promedio de todos los Alumnos : "))
        valores=[]
        alumnos2=[]
        print(separador)
            
        if submenu==1:
            
            colores=["red","green"]
            
            for promedio in listaP:
                valores.append(promedio)
            print(separador)
                
            for nombre in range(1,contadorAl+1):
                nom="alumno"
                alumnos=(f"{nom}{nombre}")
                alumnos2.append(alumnos)
            
            
            plt.grid(True)
            plt.xlabel("Alumnos:")
            plt.ylabel("Promedio de Alumno:")
            plt.title("PROMEDIO")    
            plt.bar(alumnos2,height=valores,color=colores,width=0.5)
            plt.show()
                
                
    
    elif menu==2:
        archivoA=open("./archivos/Calificacion.txt" , 'a')
        archivoB=open("./archivos/PromGrupal.txt" , 'a')
        contadorAl=0
        for nivel in lista_de_listas:
            suma=0
            contadorAl+=1

            for elemento in nivel:
                suma=suma+elemento
            promedio=suma/materias

            textoa=str(contadorAl)
            textop=str(promedio)
            archivoA.write("Promedio del Alumno "+ textoa+" = "+ textop +"\n" )
            
            listaP.append(promedio)        
            promedioFinal=promedioFinal+promedio
        promFinal=promedioFinal/contadorAl

        print(separador)
        print(f"Promedio Grupal :{promFinal}")
        print(separador)
        
        
        print("1=SI\n2=NO")
        submenu=int(input("Quieres Graficar el Promedio Grupal con el Promedio Individual : "))
        print(separador)
        valores=[promFinal]
        texto=["Promedio Grupal"]
            
        if submenu==1:
            colores=["yellow","orange","blue"]
            
            for promedio in listaP:
                valores.append(promedio)
            print(separador)
                
            for nombre in range(1,contadorAl+1):
                nom="alumno"
                alumnos=(f"{nom}{nombre}")
                texto.append(alumnos)

            
            plt.grid(True)
            plt.xlabel("Alumnos:")
            plt.ylabel("Promedio de Alumno:")
            plt.title("PROMEDIO")       
            plt.bar(texto,height=valores,color=colores,width=0.5)
            plt.show()

        textoa=str(contadorA)
        textop=str(promFinal)
        archivoB.write("Promedio de los "+ textoa+" Alumnos es "+" = "+ textop +"\n" )
        archivoB.write("-----------------------------------------------------------------" +"\n" )
        archivoB.close()
        

opcion=1
contador=1
try:
    while opcion==1:
        separador=("*"*40)
        lista_de_listas=[]
        contadorMate=0
        contadorA=0
        print("*"*20,"Menu Principal","*"*20)
        alumnos=int(input("Cuantos alumnos son : "))
        materias=int(input("Cuantas Materias llevan : "))
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
        contador=contador+1
    if opcion==1:
        archivoA=open("./archivos/Calificacion.txt" , 'a')
        contadort=str(contador)
        archivoA.write("-----------------------------------------------------------------" +"\n" )
        archivoA.close()
    else:
        archivoA=open("./archivos/Calificacion.txt" , 'a')
        contadort=str(contador)
        archivoA.write("-----------------------------------------------------------------" +"\n" )
        archivoA.close()
        
except:
    print("*"*30)
    print(f"Ocurrió un problema {sys.exc_info()[0]}")
    print(f"Ocurrió un problema {sys.exc_info()[1]}")
    print("Intenta respetar lo que se te pide :) ")
    print("*"*30)
    
finally:
    print("+"*30,"Fin del Programa","*"*30)

