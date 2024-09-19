print("Clases V2 Daniel Uribe")
# zona de clase
class Datos:
    # el constructor funcion
    def __init__(self,  estatura, peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts,   Peso: {self.peso}kg")
    def mi_lista(self):
        dias=["lunes", "martes", "miercoles","jueves","viernes","sabado","domingo"]
        print(dias)
        for semana in dias:
            print(semana)
    def mi_tupla(self):
        numeros=("1","2","3","4", "5")
        print(numeros)
        for num in numeros:
            print(num)
    def mi_diccionario(self):
        comida= {
        "Tacos": 4,
        "Burritos": 4,
        "Enchiladas": 5
        }
        print(comida)
        for x, y in comida.items():
            print(x,y)
    def mi_set(self):
        colores={"rojo","azul","verde"}
        print(colores)
        for color in colores:
            print(color)
# creacion de objetos info
info=Datos(1.7, 65)

# utilizando objetos. info
info.mostrar_datos()
print(" Lista de dias Daniel Uribe")
info.mi_lista()
print(" Tupla de numeros Daniel Uribe")
info.mi_tupla()
print(" Diccionario de comida Daniel Uribe")
info.mi_diccionario()
print(" set de colores Daniel Uribe")
info.mi_set()
