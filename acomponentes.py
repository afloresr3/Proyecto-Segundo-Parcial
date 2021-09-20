from ahelperts import gotoxy
import time

class Menu:

    def __init__(self,titulo,opciones,col,fil):
        self.titulo= titulo
        self.opciones= opciones
        self.col= col
        self.fil= fil
    
    def menu(self):
        gotoxy(self.col,self.fil); print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil+=1
            gotoxy(self.col,self.fil); print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc=int(input("Elija la opción del 1 al {} que desea escoger: ".format(len(self.opciones))))
        while opc > len(self.opciones):
            gotoxy(self.col+5,self.fil); opc=int(input("Elija la opción del 1 al {} que desea escoger: ".format(len(self.opciones))))
        return opc
    

class Valida:

    def vNumeros(self,col,fil,msjError):
        while True:
            gotoxy(col,fil); valor= input()
            try:
                if int(valor) >  0: break
            except:
                gotoxy(col,fil); print(msjError); time.sleep(1)
                gotoxy(col,fil); print(" "*len(msjError))
        return valor

    def vLetras(self,col,fil,msjError):
        while True:
            gotoxy(col,fil); valor= input()
            if valor.isalpha(): break
            else:
                gotoxy(col,fil); print(msjError); time.sleep(1)
                gotoxy(col,fil); print(" "*len(msjError))
        return valor

    def vDecimales(self,col,fil,msjError):
        while True:
            gotoxy(col,fil); valor= input()
            try:
                if float(valor) > float(0): break
            except:
                gotoxy(col,fil); print(msjError); time.sleep(1)
                gotoxy(col,fil); print(" "*len(msjError))
        return valor

    def vCedulas(self,col,fil,msjError):
        while True:
            gotoxy(col,fil); valor= self.vNumeros(col,fil,"Ingrese solo números enteros")
            suma=0
            for i in range(len(valor)-1):
                x= int(valor[i])
                if i%2 == 0:
                    x*= 2
                    if x > 9: x-=9
                suma+= x
            verificar= 10 - (suma%10)
            if verificar == int(valor[-1]): break
            else:
                gotoxy(col,fil); print(msjError); time.sleep(1)
                gotoxy(col,fil); print(" "*len(msjError))
        return valor

    def sn(self,col,fil,msjError):
        while True:
            gotoxy(col,fil); valor= input()
            if valor.lower() == "s" or valor.lower()=="n" : break
            else:
                gotoxy(col,fil); print(msjError); time.sleep(1)
                gotoxy(col,fil); print(" "*len(msjError))
        return valor.lower()

    def poscod(self,col,fil,msjError):
        while True:
            gotoxy(col,fil); valor= input()
            try:
                if int(valor) >  0: break
            except:
                gotoxy(col+6,fil); print(msjError); time.sleep(1)
                gotoxy(col+6,fil); print(" "*len(msjError))
        return valor