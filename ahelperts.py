import os

def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

def borrarPantalla():
    os.system("cls")

def codPeriodo(periodos):
    ultimo=periodos[-1][0]
    if ultimo == "0": ultimo=202105
    else:
        anio=int(ultimo[0:4])
        mes=int(ultimo[4:])
        if mes==5: ultimo= str(anio)+"11"
        else: ultimo= str(anio+1)+"05"
    return ultimo