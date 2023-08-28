from Clases.lista import Lista
from Clases.superheroe import Superheroe

# EJERCICIO 6   Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
                # casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias
                # para poder realizar las siguientes actividades:
                # a. eliminar el nodo que contiene la información de Linterna Verde;
                # b. mostrar el año de aparición de Wolverine;
                # c. cambiar la casa de Dr. Strange a Marvel;
                # d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
                # “traje” o “armadura”;
                # e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
                # sea anterior a 1963;
                # f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
                # g. mostrar toda la información de Flash y Star-Lord;
                # h. listar los superhéroes que comienzan con la letra B, M y S;
                # i. determinar cuántos superhéroes hay de cada casa de comic.

print("\nEJERCICIO 6")
superheroes = Lista()

personaje_1 = Superheroe("Doctor Strange", 1963, "DC", "se lastimo y consiguio poderes magicos en medio oriente")
personaje_2 = Superheroe("Linterna Verde", 1940, "DC", "tiene un anillo re potente pero tiene miedo al color amarillo")
personaje_3 = Superheroe("Wolverine", 1974, "Marvel", "mutante que no puede dar masajes")
personaje_4 = Superheroe("Wonder Woman", 1941, "DC", "tiene una armadura rara")
personaje_5 = Superheroe("Capitana Marvel", 1968, "Marvel", "tuvo como 5 nombres antes de ser capitana")
personaje_6 = Superheroe("Star-Lord", 1980, "Marvel", "le gusta el rock")
personaje_7 = Superheroe("Flash", 1940, "DC","traje rojo")
personaje_8 = Superheroe("Batman", 1939, "DC", "No la necesita")

superheroes.insert(personaje_1, "nombre")
superheroes.insert(personaje_2, "nombre")
superheroes.insert(personaje_3, "nombre")
superheroes.insert(personaje_4, "nombre")
superheroes.insert(personaje_5, "nombre")
superheroes.insert(personaje_6, "nombre")
superheroes.insert(personaje_7, "nombre")
superheroes.insert(personaje_8, "nombre")


def borrar_linterna(lista):
    lista.delete("Linterna Verde", "nombre")

print("a:")
borrar_linterna(superheroes)
print(superheroes.barrido())


print()
print("b:")
pos = superheroes.search("Wolverine", "nombre")
if pos >= 0:
    value = superheroes.get_element_by_index(pos)
    print("Wolverine aparecio en", value.anio_aparicion)


print()
print("c:")
pos = superheroes.search("Doctor Strange", "nombre")
if pos is not None:
    value = superheroes.get_element_by_index(pos)
    value.casa = "Marvel"
    print(f"La casa de Doctor Strange ahora es correctamente {value.casa}")

print()
print("d:")
superheroes.barrido_armadura()

print()
print("e:")
superheroes.barrido_1963()

print()
print("f:")
marvel = superheroes.search("Capitana Marvel", "nombre")
wonder = superheroes.search("Wonder Woman", "nombre")
if marvel is not None:
    capitana = superheroes.get_element_by_index(marvel)
    print(f"Capitana Marvel pertenece a {capitana.casa}")
if wonder is not None:
    woman = superheroes.get_element_by_index(wonder)
    print(f"Wonder Woman pertenece a {woman.casa}")

print()
print("g:")
flash = superheroes.search("Flash", "nombre")
starlord = superheroes.search("Star-Lord", "nombre")
if flash is not None:
    infoflash = superheroes.get_element_by_index(flash)
    print(infoflash)
if starlord is not None:
    infostar = superheroes.get_element_by_index(starlord)
    print(infostar)

print()
print("h:")
superheroes.barrido_letras()

print()
print("i:")
superheroes.contar_casa()



#EJERCICIO 15 
# 
# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas.
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo.
# Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

from Clases.lista_lista import Lista
from Clases.entrenador import Entrenador
from Clases.pokemon import Pokemon
from random import randint

print("\nEJERCICIO 15")

e1 = Entrenador('Juan', ct_ganados=randint(1, 10), cb_perdidas=randint(1, 10), cb_ganadas=randint(1, 10))
e2 = Entrenador('Maria', ct_ganados=randint(1, 10), cb_perdidas=randint(1, 10), cb_ganadas=randint(1, 10))
e3 = Entrenador('Ana', ct_ganados=randint(1, 10), cb_perdidas=randint(1, 10), cb_ganadas=randint(1, 10))

entrenadores = [e1, e2, e3]

lista_entrenadores = Lista()

p1 = Pokemon('Pikachu', 'electrico', randint(1, 20))
p2 = Pokemon('Jolteon', 'electrico', randint(1, 20))
p3 = Pokemon('Vaporeon', 'agua', randint(1, 20))
p4 = Pokemon('Flareon', 'fuego', randint(1, 20))
p5 = Pokemon('Leafeon', 'planta', randint(1, 20))
p6 = Pokemon('Wingull', 'agua', randint(1, 20), 'volador')
p7 = Pokemon("Tyrantrum", "roca", randint(1, 20), "dragon")
p8 = Pokemon("Terrakion", "roca", randint(1, 20), "lucha")

pokemons = [p1, p2, p3, p4, p5, p6, p7, p8]

#! lista principal
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

#! lista secundaria
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


lista_entrenadores.barrido_entrenadores()


print("\na:")
pos = lista_entrenadores.search('Juan', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')


print("\nb:")
lista_entrenadores.barrido_cantidad_torneos_ganados(6)


print("\nc:")
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
pos_mayor = 0

for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.ct_ganados

valor = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = valor[0], valor[1]

if sublista.size() > 0:

    pokemon_mayor = sublista.get_element_by_index(0)
    for pos in range(1, sublista.size()):
        pokemon = sublista.get_element_by_index(pos)
        if pokemon.nivel > pokemon_mayor.nivel:
            pokemon_mayor = pokemon

    print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} al nivel {pokemon_mayor.nivel} ')


print("\nd:")
lista_entrenadores.barrido()


print("\ne:")
for i in range(0, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(i)[0]
    porcentaje = round((entrenador.cb_ganadas) * 100 / (entrenador.cb_ganadas + entrenador.cb_perdidas), 2)
    if porcentaje > 79:
        print(f"El porcentaje de victorias de {entrenador.nombre} es {porcentaje}")
    else:
        print(f"El porcentaje de victorias de {entrenador.nombre} es menor al 79% ({porcentaje})")

    
print("\nf:")
for i in range(0, lista_entrenadores.size()):
    # entrenador = lista_entrenadores.get_element_by_index(i)[0]
    # pokes = lista_entrenadores.get_element_by_index(i)[1]
    dato = lista_entrenadores.get_element_by_index(i)
    entrenadores, pokes = dato[0], dato[1]
    for p in range(pokes.size()):
        pokemon = pokes.get_element_by_index(p)
        if pokemon.tipo == "fuego" or pokemon.tipo == "planta":
            print(f"{entrenadores.nombre} tiene un {pokemon.nombre}, que es de tipo {pokemon.tipo}")
        if pokemon.tipo == "agua" and pokemon.subtipo == "volador":
            print(f"{entrenadores.nombre} tiene un {pokemon.nombre}, que es de tipo {pokemon.tipo}/{pokemon.subtipo}")


print("\ng:")
index = lista_entrenadores.search("Juan", "nombre")
if index is not None:
    dato = lista_entrenadores.get_element_by_index(index)
    entrenador, pokes = dato[0], dato[1]
    if pokes.size() > 0:
        niveles = 0
        for p in range(pokes.size()):
            pokemon = pokes.get_element_by_index(p)
            niveles += pokemon.nivel
        
        promedio = niveles / pokes.size()

        print(f"El promedio de nivel de los Pokemon de {entrenador.nombre} es {promedio}")
    else:
        print(f"{entrenador.nombre} no tiene ningun pokemon.")

print("\nh:")
buscado = "Pikachu"
con = 0
for i in range(lista_entrenadores.size()):
    dato = lista_entrenadores.get_element_by_index(i)
    entrenador, poke = dato[0], dato[1]
    if poke.search(buscado, "nombre") is not None:
        con += 1
print(f"{con} entrenadores tienen a {buscado}")

print("\ni:")
for i in range(lista_entrenadores.size()):
    con = 1
    dato = lista_entrenadores.get_element_by_index(i)
    entrenador, poke = dato[0], dato[1]
    anterior = poke.get_element_by_index(0)
    for x in range(1, poke.size()-1):
        p = poke.get_element_by_index(x)
        if p.nombre == anterior.nombre:
            con += 1
    if con > 1:
        print(f"{entrenador} tiene {con} {anterior.nombre}")
    else:
        print(f"{entrenador.nombre} no tiene repetidos.")

print("\nj:")
buscados = ["Tyrantrum", "Wingull", "Terrakion"]
for i in range(lista_entrenadores.size()):
    dato = lista_entrenadores.get_element_by_index(i)
    entrenador, poke = dato[0], dato[1]
    if poke.search("Tyrantrum", "nombre"):
        print(f"{entrenador.nombre} tiene un Tyrantrum.")
    if poke.search("Wingull", "nombre"):
        print(f"{entrenador.nombre} tiene un Wingull.")
    if poke.search("Terrakion", "nombre"):
        print(f"{entrenador.nombre} tiene un Terrakion.")

print("\nk:")
entrenador_buscado = input("Escriba un nombre de entrenador: ")
if (lista_entrenadores.search(entrenador_buscado, "nombre")) is None:
    print(f"{entrenador_buscado} no aparece en la lista de entrenadores.")
    exit()
poke_buscado = input("Escriba un nombre de pokemon: ")
dato = lista_entrenadores.search(entrenador_buscado, "nombre")
lista = lista_entrenadores.get_element_by_index(dato)
entre, poke = lista[0], lista[1]
buscar = poke.search(poke_buscado, "nombre")
if buscar is not None:
    print(f"{entrenador_buscado} tiene a {poke_buscado}!")
    print(f"Datos del entrenador: {entre}\nDatos del Pokemon: {poke.get_element_by_index(buscar)}")
else:
    print(f"{entrenador_buscado} no tiene a {poke_buscado}")
