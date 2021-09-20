from ahelperts import borrarPantalla, codPeriodo, gotoxy
from aarchivos import Aarchivos
from entidadesUnemi import *
from acomponentes import *
import time

def carreras():
   borrarPantalla()     
   gotoxy(20,2); print("MANTENIMIENTO DE CARRERAS")
   gotoxy(10,4); print("Codigo: ")
   gotoxy(10,5); print("Descripción Carrera: ")
   gotoxy(31,5); descarrera = input()
   archiCarrera = Aarchivos("carrera.txt",";")
   carreraDatos = archiCarrera.leer()
   idSig = int(carreraDatos[-1][0])+1
   gotoxy(18,4); print(idSig,"\n"*2)
   carrera = Carrera(idSig,descarrera)
   datos = carrera.getCarrera()
   datos = ';'.join(datos)
   archiCarrera.escribir([datos],"a")

def materias():
   borrarPantalla()     
   gotoxy(20,2);print("INGRESO DE MATERIAS")
   gotoxy(10,4);print("Codigo: ")
   gotoxy(10,5);print("Descripcion Materias: ")
   gotoxy(33,5); desmateria = input()
   archiMateria = Aarchivos("materia.txt",";")
   materiaDatos = archiMateria.leer()
   idSig = int(materiaDatos[-1][0])+1
   gotoxy(18,4); print(idSig,"\n"*2)
   materia = Materia(idSig,desmateria)
   datos = materia.getMateria()
   datos = ';'.join(datos)
   archiMateria.escribir([datos],"a") 

def periodos():
   borrarPantalla()     
   gotoxy(20,2);print("INGRESO DE PERIODOS")
   gotoxy(10,4);print("Codigo: ")
   gotoxy(10,5);print("Descripcion Periodos: ")
   gotoxy(33,5); desperiodo = input()
   archiPeriodo = Aarchivos("periodo.txt",";")
   periodoDatos = archiPeriodo.leer()
   idSig = codPeriodo(periodoDatos)
   gotoxy(18,4); print(idSig,"\n"*2)
   periodo = Periodo(idSig,desperiodo)
   datos = periodo.getPeriodo()
   datos = ';'.join(datos)
   archiPeriodo.escribir([datos],"a")

def profesores():
    borrarPantalla()
    validar = Valida()     
    gotoxy(20,2); print("INGRESO DE PROFESORES")
    gotoxy(15,4); print("Nombre  : ")
    gotoxy(15,5); print("Cedula  : ")
    gotoxy(15,6); print("Titulo  : ")
    gotoxy(15,7); print("Telefono: ")
    gotoxy(15,8); print("Carrera ID[    ]: ")
    nom= validar.vLetras(26,4,"Ingrese un nombre correcto")
    ced= validar.vCedulas(26,5,"Ingrese una cédula válida")
    tit= validar.vLetras(26,6,"Ingrese título correcto")
    tel= validar.vNumeros(26,7,"Ingrese solo caracteres numéricos")
    archiCarrera = Aarchivos("carrera.txt",";") 
    lisCarrera,entCarrera = [],None
    while not lisCarrera:
        id = validar.poscod(27,8,"Solo números")
        lisCarrera = archiCarrera.buscar(id)
        if lisCarrera:
            salir=1
            if lisCarrera[0]!=-1:
                entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
                gotoxy(33,8);print(entCarrera.descripcion)
            else: salir=-1
        else: 
            gotoxy(33,8); print("No existe Carrera con ese codigo[{}]:".format(id))
            time.sleep(1); gotoxy(27,8); print("   "); gotoxy(33,8); print(" "*40)
    if salir != -1: 
        gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
        grabar= validar.sn(55,10,"Solo 'S' o 'N'")
        if grabar == "s":
            archiProfesor = Aarchivos("profesor.txt",";")
            lisProfesores = archiProfesor.leer()
            idSig = int(lisProfesores[-1][0])+1
            entProfesor = Profesor(idSig,nom,ced,entCarrera,tit,tel)
            datos = entProfesor.getProfesor()
            datos = ';'.join(datos)
            archiProfesor.escribir([datos],"a")                 
            gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione ENTER para continuar...")
        else: gotoxy(15,11);input("Registro No fue Grabado\n presione Enter para continuar...")     
    else: print("\nAún no se ah creado el registro carrera\nVuelva a intentarlo")

def estudiantes():
    borrarPantalla()
    validar = Valida()
    gotoxy(20,2);print("INGRESO DE ESTUDIANTES ")
    gotoxy(15,4);print("Nombre   : ")
    gotoxy(15,5);print("Cedula   : ")
    gotoxy(15,6);print("Dirección: ")
    gotoxy(15,7);print("Telefono : ")
    gotoxy(15,8);print("Carrera ID[    ]: ")
    nom= validar.vLetras(26,4,"Ingrese un nombre correcto")
    ced= validar.vCedulas(26,5,"Ingrese una cédula válida")
    gotoxy(26,6);dire = input()
    tel=validar.vNumeros(26,7,"Ingrese solo caracteres numéricos")
    archiCarrera = Aarchivos("carrera.txt",";")
    lisCarrera,entCarrera = [],None
    while not lisCarrera:
        id = validar.poscod(26,8,"Solo números")
        lisCarrera = archiCarrera.buscar(id)
        if lisCarrera:
            salir= 1
            if lisCarrera[0]!=-1:
                entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
                gotoxy(33,8);print(entCarrera.descripcion)
            else: salir= -1
        else: 
            gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
            time.sleep(1); gotoxy(26,8); print("  "); gotoxy(33,8);print(" "*40)
    if salir != -1:
        gotoxy(15,10); print("Esta seguro de Grabar El registro(s/n):")
        grabar= validar.sn(55,10,"Solo 'S' o 'N'")
        if grabar == "s":
            archiEstudiante = Aarchivos("estudiante.txt",";")
            lisEstudiantes = archiEstudiante.leer()
            idSig = int(lisEstudiantes[-1][0])+1
            entEstudiante = Estudiante(idSig,nom,ced,dire,tel)
            datos = entEstudiante.getEstudiante()
            datos = ';'.join(datos)
            archiEstudiante.escribir([datos],"a")                 
            gotoxy(15,11); input("Registro Grabado Satisfactoriamente\n Presione ENTER para continuar...")
        else: gotoxy(15,11); input("Registro No fue Grabado\n presione ENTER para continuar...")
    else: print("\nAún no se ah creado el registro carrera\nVuelva a intentarlo")

def matriculas():
    borrarPantalla()
    validar = Valida()     
    gotoxy(20,2);print("INGRESO DE MATRICULA ")
    gotoxy(15,4);print("Periodo ID[       ]: ")
    gotoxy(15,5);print("Estudiante ID[    ]: ")
    gotoxy(15,6);print("Valor: ")
    gotoxy(15,7);print("Carrera ID   [    ]: ")
    archiPeriodo= Aarchivos("periodo.txt",";")
    lisPeriodo,entPeriodo = [],None
    while not lisPeriodo:
        perId=validar.poscod(27,4,"Solo números")
        lisPeriodo = archiPeriodo.buscar(perId)
        if lisPeriodo:
            salir=1
            if lisPeriodo[0]!=-1:
                entPeriodo = Periodo(lisPeriodo[0],lisPeriodo[1]) 
                gotoxy(37,4);print(entPeriodo.descripcion)
            else: salir=-1
        else: 
            gotoxy(36,4); print("No existe Periodo con ese codigo[{}]:".format(perId))
            time.sleep(1); gotoxy(30,4); print("   "); gotoxy(36,4); print(" "*40);
    if salir != -1:
        archiEstudiante= Aarchivos("estudiante.txt",";")
        lisEstudiante,entEstudiante = [],None
        while not lisEstudiante:
            estId=validar.poscod(30,5,"Solo números")
            lisEstudiante = archiEstudiante.buscar(estId)
            if lisEstudiante:
                salir=1
                if lisEstudiante[0]!=-1:
                    entEstudiante = Estudiante(lisEstudiante[0],lisEstudiante[1],lisEstudiante[2],lisEstudiante[3],lisEstudiante[4]) 
                    gotoxy(37,5);print(entEstudiante.nombre)
                else: salir=-1
            else: 
                gotoxy(36,5); print("No existe Estudiante con ese codigo[{}]:".format(estId))
                time.sleep(1); gotoxy(30,5); print("   "); gotoxy(36,5); print(" "*40)
    if salir != -1:
        val=validar.vDecimales(23,6,"Solo valores numéricos")
        archiCarrera= Aarchivos("carrera.txt",";")
        lisCarrera,entCarrera = [],None
        while not lisCarrera:
            carId=validar.poscod(30,7,"Solo números")
            lisCarrera = archiCarrera.buscar(carId)
            if lisCarrera:
                salir=1
                if lisCarrera[0]!=-1:
                    entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
                    gotoxy(37,7);print(entCarrera.descripcion)
                else: salir=-1
            else: 
                gotoxy(36,7); print("No existe Carrera con ese codigo[{}]:".format(carId))
                time.sleep(1); gotoxy(30,7); print("   "); gotoxy(36,7); print(" "*40)
    if salir != -1:
        gotoxy(15,10); print("Esta seguro de Grabar El registro(s/n):")
        grabar= validar.sn(55,10,"Solo 'S' o 'N'")
        if grabar == "s":
            archiMatricula = Aarchivos("matricula.txt",";")
            lisMatriculas = archiMatricula.leer()
            idSig = int(lisMatriculas[-1][0])+1
            entMatricula = Matricula(idSig,entEstudiante,entCarrera,entPeriodo,val)
            datos = entMatricula.getMatricula()
            datos = ';'.join(datos)
            archiMatricula.escribir([datos],"a")                 
            gotoxy(15,11); input("Registro Grabado Satisfactoriamente\n Presione ENTER para continuar...")
        else: gotoxy(15,11); input("Registro No fue Grabado\n presione ENTER para continuar...")
    else: print("\nFaltan reguistros por crearse")

def notas():
    borrarPantalla()
    validar = Valida()     
    gotoxy(20,1);print("INGRESO DE NOTAS ")
    gotoxy(15,3);print("Periodo ID[       ]: ")
    gotoxy(15,4);print("Estudiante ID[    ]: ")
    gotoxy(15,5);print("Materia ID   [    ]: ")
    gotoxy(15,6);print("Profesor ID  [    ]: ")
    gotoxy(15,7);print("nota1: ")
    gotoxy(15,8);print("nota2: ")
    gotoxy(15,9);print("Carrera ID   [    ]: ")
    archiPeriodo= Aarchivos("periodo.txt",";")
    lisPeriodo,entPeriodo = [],None
    while not lisPeriodo:
        perId=validar.vNumeros(26,3,"Solo números")
        lisPeriodo = archiPeriodo.buscar(perId)
        if lisPeriodo:
            salir=1
            if lisPeriodo[0]!=-1:
                entPeriodo = Periodo(lisPeriodo[0],lisPeriodo[1]) 
                gotoxy(37,3);print(entPeriodo.descripcion)
            else: salir=-1
        else: 
            gotoxy(36,3); print("No existe Periodo con ese codigo[{}]:".format(perId))
            time.sleep(1); gotoxy(30,3); print("   "); gotoxy(36,3); print(" "*40)
    if salir != -1:
        archiEstudiante= Aarchivos("estudiante.txt",";")
        lisEstudiante,entEstudiante = [],None
        while not lisEstudiante:
            estId=validar.poscod(30,4,"Solo números")
            lisEstudiante = archiEstudiante.buscar(estId)
            if lisEstudiante:
                salir=1
                if lisEstudiante[0]!=-1:
                    entEstudiante = Estudiante(lisEstudiante[0],lisEstudiante[1],lisEstudiante[2],lisEstudiante[3],lisEstudiante[4]) 
                    gotoxy(37,4);print(entEstudiante.nombre)
                else: salir=-1
            else: 
                gotoxy(36,4); print("No existe Estudiante con ese codigo[{}]:".format(estId))
                time.sleep(1); gotoxy(30,4); print("   "); gotoxy(36,4); print(" "*40)
    if salir != -1:
        archiMateria= Aarchivos("materia.txt",";")
        lisMateria,entMateria = [],None
        while not lisMateria:
            matId=validar.poscod(30,5,"Solo números")
            lisMateria = archiMateria.buscar(matId)
            if lisMateria:
                salir=1
                if lisMateria[0]!=-1:
                    entMateria = Materia(lisMateria[0],lisMateria[1]) 
                    gotoxy(37,5);print(entMateria.descripcion)
                else: salir=-1
            else: 
                gotoxy(36,5); print("No existe Materia con ese codigo[{}]:".format(matId))
                time.sleep(1); gotoxy(30,5); print("   "); gotoxy(36,5); print(" "*40)
    if salir != -1:
        archiProfesor= Aarchivos("profesor.txt",";")
        lisProfesor,entProfesor = [],None
        while not lisProfesor:
            prfId=validar.poscod(30,6,"Solo números")
            lisProfesor = archiProfesor.buscar(prfId)
            if lisProfesor:
                salir=1
                if lisProfesor[0]!=-1:
                    entProfesor = Profesor(lisProfesor[0],lisProfesor[1],lisProfesor[2],lisProfesor[3],lisProfesor[4],lisProfesor[5]) 
                    gotoxy(37,6);print(entProfesor.nombre)
                else: salir=-1
            else: 
                gotoxy(36,6); print("No existe Profesor con ese codigo[{}]:".format(prfId))
                time.sleep(1); gotoxy(30,6); print("   "); gotoxy(36,6); print(" "*40)
    if salir != -1:
        nota1= validar.vDecimales(22,7,"Solo valores numéricos")
        nota2= validar.vDecimales(22,8,"Solo valores numéricos")
        archiCarrera= Aarchivos("carrera.txt",";")
        lisCarrera,entCarrera = [],None
        while not lisCarrera:
            carId=validar.poscod(30,9,"Solo números")
            lisCarrera = archiCarrera.buscar(carId)
            if lisCarrera:
                salir=1
                if lisCarrera[0]!=-1:
                    entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
                    gotoxy(37,9);print(entCarrera.descripcion)
                else: salir=-1
            else: 
                gotoxy(36,9); print("No existe Carrera con ese codigo[{}]:".format(carId))
                time.sleep(1); gotoxy(30,9); print("   "); gotoxy(36,9); print(" "*40)
    if salir != -1:
        gotoxy(15,11); print("Esta seguro de Grabar El registro(s/n):")
        grabar= validar.sn(55,11,"Solo 'S' o 'N'")
        if grabar == "s":
            archiNota = Aarchivos("nota.txt",";")
            lisnotas = archiNota.leer()
            idSig = int(lisnotas[-1][0])+1
            entNota = Nota(idSig,entPeriodo,entEstudiante,entMateria,entProfesor,nota1,nota2)
            datos = entNota.getNota()
            datos = ';'.join(datos)
            archiNota.escribir([datos],"a")                 
            gotoxy(15,12); input("Registro Grabado Satisfactoriamente\n Presione ENTER para continuar...")
        else: gotoxy(15,12); input("Registro No fue Grabado\n presione ENTER para continuar...")
    else: print("\nFaltan reguistros por crearse")



opc=-1
while opc !=4:  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Matriculacion","3) Notas","4) Salir"],20,10)
    opc = menu.menu()
    if opc == 1:
        opc1 = ''
        while opc1 !=6:
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Carrera","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == 1:
                carreras()
                input("Regusitro Agregado\nPresione una tecla para continuar")
            elif opc1 == 2:
                materias()
                input("Regusitro Agregado\nPresione una tecla para continuar")
            elif opc1 == 3:
                periodos()
                input("Regusitro Agregado\nPresione una tecla para continuar")
            elif opc1 == 4:
                profesores()
            elif opc1 == 5:
                estudiantes()
                        
    elif opc == 2:
            borrarPantalla()
            menu2 = Menu("Menu Matriculacion",["1) Matricula","2) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == 1:
                matriculas()
        
    elif opc == 3:
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == 1:
                notas()
            
    elif opc == 4:
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 


input("Presione una tecla para salir")
borrarPantalla()
