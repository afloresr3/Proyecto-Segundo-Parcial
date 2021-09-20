class Aarchivos:

    def __init__(self,nombre,separador):
        self.__nombreArch=nombre
        self.__separar=separador

    def leer(self):
        try:
            with open(self.__nombreArch,"r",encoding="UTF=8") as file:
                lista=[]
                for linea in file: 
                    line = linea[:-1].split(self.__separar)
                    lista.append(line)
        except IOError: lista=[["0"]]
        return lista

    def escribir(self,datos,modo):
        with open(self.__nombreArch,modo,encoding="UTF-8")as file:
            for dato in datos: file.write(dato+"\n")

    def eswritbir(self,datos,modo):
        with open(self.__nombreArch,modo,encoding="UTF-8") as file:
            for dato in datos:
                linea=""
                for dat in dato:
                    if type(dat) == int or float: linea+=str(dat)+self.__separar
                    else: linea+= dat+ self.__separar
                file.write(linea[:-1]+"\n")

    def buscar(self,buscado):
        try:
            resultado=[]
            with open(self.__nombreArch,mode='r',encoding='UTF-8') as file:
                for linea in file:
                    if linea[:-1].split(self.__separar)[0] ==buscado:
                        resultado = linea[:-1].split(self.__separar)
        except: resultado=[-1]
        return resultado

    def buscarLista(self,buscado):
        resultado = []
        with open(self.__nombreArch, mode='r', encoding='utf-8') as file:
            for linea in file:
                registro = linea[:-1].split(self.__separar) 
                if registro[0] == buscado:
                    resultado.append(registro)
        return resultado
    
    def buscar2(self,buscado1,buscado2,pos1,pos2):
        resultado = []
        with open(self.__nombreArch, mode='r', encoding='utf-8') as file:
            for linea in file:
                registro = linea[:-1].split(self.__separar) 
                if registro[pos1] == buscado1 and registro[pos2] == buscado2:
                    resultado = registro
        return resultado