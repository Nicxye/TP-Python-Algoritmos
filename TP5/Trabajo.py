from Clases.arbol_binario import BinaryTree, get_value_from_file
from random import randint

# EJERCICIO 5
    # Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
    # (MCU), desarrollar un algoritmo que contemple lo siguiente:
        # a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
        # que indica si es un villano o un héroe, True y False respectivamente;

        # b. listar los villanos ordenados alfabéticamente;

        # c. mostrar todos los superhéroes que empiezan con C;

        # d. determinar cuántos superhéroes hay el árbol;

        # e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
        # encontrarlo en el árbol y modificar su nombre;

        # f. listar los superhéroes ordenados de manera descendente;

        # g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
        # los villanos, luego resolver las siguiente tareas:

        # I. determinar cuántos nodos tiene cada árbol;

        # II. realizar un barrido ordenado alfabéticamente de cada árbol.
print("\nEJERCICIO 5")
from Clases.superheroe import Superheroe

arbol = BinaryTree()

lista_heroes = [
    {"name": "Loki", "hero": False},
    {"name": "Thanos", "hero": False},
    {"name": "Ultron", "hero": False},
    {"name": "Goblin", "hero": False},
    {"name": "Mysterio", "hero": False},
    {"name": "Doctor Strager", "hero": True},
    {"name": "Iron Man", "hero": True},
    {"name": "Captain America", "hero": True},
    {"name": "Hulk", "hero": True},
    {"name": "Captain Marvel", "hero": True},
    {"name": "Doctor Octopus", "hero": False},
    {"name": "Deadpool", "hero": True},
]

for heroe in lista_heroes:
    arbol.insert_node(heroe["name"], heroe["hero"])

print("\nB:")
arbol.inorden_heroe_o_villano(False)

print("\nC:")
arbol.starts_with('C')

print("\nD:")
print(f"Hay {arbol.contar_heroes(True)} superheroes en el arbol.")

print("\nE:")
#arbol.search_by_coincidence("Do")
#value = input("Ingresar el nombre incorrecto: ")

pos = arbol.search("Doctor Strager") #(value)
if pos:
    print("Nombre encontrado...")
    is_hero = pos.other_values
    arbol.delete_node("Doctor Strager")
    arbol.insert_node("Doctor Strange", is_hero)
else:
    print("Ese nombre no se encuentra.\n")

print()
arbol.inorden()

print("\nF:")
arbol.inorden_heroe_o_villano(True)

print("\nG:")
superheroes = BinaryTree()
villanos = BinaryTree()

arbol.get_heroe_villano(superheroes, villanos)

print("i:")
print(f"El arbol de superheroes tiene {superheroes.contar_heroes(True)} personajes y el de villanos {villanos.contar_heroes(False)}\n")

print("ii: \n")
superheroes.inorden()
print("----------")
villanos.inorden()

#EJERCICIO 6
# Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de nacimiento,
# color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
# tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
# siguientes consignas:
# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
# b. realizar un barrido inorden del árbol por nombre y ranking;
# c. realizar un barrido por nivel de los árboles por ranking y especie;
# d. mostrar toda la información de Yoda y Luke Skywalker;
# e. mostrar todos los Jedi con ranking “Jedi Master”;
# f. listar todos los Jedi que utilizaron sabe de luz color verde;
# g. listar todos los Jedi cuyos maestros están en el archivo;
# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.

print("\nEJERCICIO 6:")

name_tree = BinaryTree()
rank_tree = BinaryTree()
species_tree = BinaryTree()

file_jedi = open("jedis.txt")
read_lines = file_jedi.readlines()
file_jedi.close()

read_lines.pop(0)

ARCHIVO = "jedis.txt"

#a:
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop()
    name_tree.insert_node(jedi[0], index+2) 
    rank_tree.insert_node(jedi[1], index+2)
    species_tree.insert_node(jedi[2], index+2)

print("\nB:")
rank_tree.inorden_file_by_rank(ARCHIVO)

print("\nC:")
rank_tree.order_by_level()
print("-----")
species_tree.order_by_level()

print("\nD:")
pos = name_tree.search("yoda")
if pos:
    print(get_value_from_file(ARCHIVO, pos.other_values))
else:
    print(f"Ese personaje no esta en la lista.")

pos = name_tree.search("luke skywalker")
if pos:
    print(get_value_from_file(ARCHIVO, pos.other_values))
else:
    print("Ese nombre no esta en la lista.")

print("\nE:")
rank_tree.inorden_file_by_specific_rank(ARCHIVO, "jedi master")

print("\nF:")
name_tree.inorden_file_by_lightsaber(ARCHIVO, "green")

print("\nG:")
name_tree.inorden_file_master_in_file(ARCHIVO)

print("\nH:")
name_tree.inorden_file_by_togruta_cerean(ARCHIVO)

print("\nI:")
name_tree.inorden_file_starts_with_and_dash(ARCHIVO)


# EJERCICIO 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
                # resuelva las siguientes consultas:

                # a. listado inorden de las criaturas y quienes la derrotaron;
                # b. se debe permitir cargar una breve descripción sobre cada criatura;
                # c. mostrar toda la información de la criatura Talos;
                # d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
                # e. listar las criaturas derrotadas por Heracles;
                # f. listar las criaturas que no han sido derrotadas;
                # g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
                # o dios que la capturo;
                # h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
                # Erimanto indicando que Heracles las atrapó;
                # i. se debe permitir búsquedas por coincidencia;
                # j. eliminar al Basilisco y a las Sirenas;
                # k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
                # derroto a varias;
                # l. modifique el nombre de la criatura Ladón por Dragón Ladón;
                # m. realizar un listado por nivel del árbol;
                # n. muestre las criaturas capturadas por Heracles.

print("\nEJERCICIO 23")

creature_tree = BinaryTree()
defeated_by_tree = BinaryTree()

CRIATURAS = "criaturas.txt"

file_creatures = open(CRIATURAS)
creature_lines = file_creatures.readlines()
file_creatures.close()
creature_lines.pop(0)

for index, linea in enumerate(creature_lines):
    creature = linea.split(';')
    creature.pop()
    creature_tree.insert_node(creature[0], index+2)
    defeated_by_tree.insert_node(creature[1], index+2)

print("\nA:")
defeated_by_tree.inorden_file_by_rank(CRIATURAS)

# print("\nB:")
# nombre = input("Ingrese la criatura, en minuscula, de la que quiera cargar descripción:")
# encontrado = creature_tree.search("laquesis")

# if encontrado:
#     desc = input("Agregue la descripcion: ")
#     with open(CRIATURAS, 'a') as file:
#         for linea in creature_lines:
#             if linea.startswith("laquesis"):
#                 linea =linea + desc + ";\n"
#                 print(linea)
#             file.write("\n")
#             file.write(linea)
#         file.close()
# else:
#     print("No se ha encontrado esa criatura.")

print("\nC:")
buscar = creature_tree.search("talos")
if buscar:
    print(get_value_from_file(CRIATURAS, buscar.other_values))
else:
    print("No se encuentra en el arbol.")

# print("\nD:")
# print(defeated_by_tree.contar("talos"))

print("\nE:")
creature_tree.inorden_defeated_by(CRIATURAS, "heracles")

print("\nF:")
creature_tree.inorden_undefeated(CRIATURAS)

# print("\nH:")

print("\nI:")
creature_tree.search_by_coincidence("tal")

print("\nJ:")
creature_tree.delete_node("basilisco")
creature_tree.delete_node("sirenas")

creature_tree.inorden()

# print("\nK:")
# print(creature_tree.root.other_values)

print("\nL:")
dragon = creature_tree.search("ladon")
if dragon:
    other_values = dragon.other_values
    creature_tree.delete_node("ladon")
    creature_tree.insert_node("dragon ladon", other_values)

print("\nM:")
creature_tree.order_by_level()

print("\nN:") ##############
creature_tree.captured_by_heracles(CRIATURAS)