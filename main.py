def calcular_first(G):
  # Inicializar el conjunto FIRST para cada símbolo no terminal
  first = {key: set() for key in G}

  def first_of_sequence(sequence):
    # Función auxiliar para calcular el FIRST de una secuencia
    result = set()
    for symbol in sequence:
      if symbol.islower():
        result.add(symbol)  # Agregar símbolos terminales al FIRST
        break
      result |= first.get(symbol, set()) - {'e'}
      if 'e' not in first.get(symbol, set()):
        break
    else:
      result.add('e')
    return result

  cambiado = True
  while cambiado:
    cambiado = False
    for nonterminal, productions in G.items():
      for production in productions:
        if production == "e":
          if 'e' not in first[nonterminal]:
            first[nonterminal].add('e')
            cambiado = True
        else:
          initial_size = len(first[nonterminal])
          first[nonterminal] |= first_of_sequence(production)
          if len(first[nonterminal]) > initial_size:
            cambiado = True

  return first

def calcular_follow(G, first, simboloInicial='S'):
  follow = {key: set() for key in G}
  follow[simboloInicial].add('$')  # Símbolo de fin de cadena al FOLLOW del símbolo inicial

  while True:
    updated = False  # Verifica si el conjunto de FOLLOW cambió
    for A in G:
      for body in G[A]:
        for i, B in enumerate(body):
          if B.isupper():
            # Crear un conjunto temporal para los siguientes elementos después de B
            temp_follow = set()

            # Regla 1: Agregar FIRST de todo lo que sigue a B en el cuerpo de la producción (excepto epsilon)
            for symbol in body[i + 1:]:
              if symbol.isupper():
                temp_follow |= first.get(symbol, set()) - {'e'}
                if 'e' in first.get(symbol, set()):
                  continue
                break
              else:
                temp_follow.add(symbol)
                break
            else:
              # Si B es el último símbolo o todo lo que sigue a B puede ser 'e', agregar FOLLOW de A
              temp_follow |= follow[A]

            # Regla 2: Si hay una producción A --> αBβ, agregar FIRST(β) - {epsilon} al FOLLOW(B)
            if 'e' in first[B]:
              temp_follow |= follow[A]

            # Si se agregó algo nuevo al FOLLOW de B, actualizar el conjunto FOLLOW y la bandera
            if not temp_follow.issubset(follow[B]):
              follow[B] |= temp_follow
              updated = True

    # Si no hubo cambios en esta iteración, romper el bucle
    if not updated:
      break

  return follow

def main():
  numGramaticas = int(input())
  for _ in range(numGramaticas):
    cantReglas = int(input())
    G = {}
    simboloInicio = 'S'
    for _ in range(cantReglas):
      regla = input().split()
      G[regla[0]] = regla[1:]

    # Calcular los conjuntos FIRST y FOLLOW
    first = calcular_first(G)
    follow = calcular_follow(G, first, simboloInicio)

    # Imprimir los conjuntos FIRST y FOLLOW
    for nonterminal in G:
      print(f"First({nonterminal}) = {first[nonterminal]}")
      print(f"Follow({nonterminal}) = {follow[nonterminal]}")

if __name__ == "__main__":
  main()

"""# esta no funciona, usar el otro archivo (dejare esto aquí de mientras por si acaso)
def calcular_first(G):
  # Initialize the First set for each non-terminal
  first = {key: set() for key in G}

  def first_of_sequence(sequence):  # ayuda a cumplir las reglas 2.1 y 2.2 cuando x deriva en una cadena larga
    # Helper function to compute First of a sequence
    result = set()
    for symbol in sequence:
      result |= first[symbol] - {'e'}
      if 'e' not in first[symbol]:
        break
    else:
      result.add('e')
    return result
  cambiado = True
  while cambiado:
    cambiado = False
    for nonterminal, productions in G.items():
      for production in productions:
        if production == "e":
          if 'e' not in first[nonterminal]:
            first[nonterminal].add('e')
            cambiado = True
        else:
          initial_size = len(first[nonterminal])
          first[nonterminal] |= first_of_sequence(production)
          if len(first[nonterminal]) > initial_size:
            cambiado = True
  return first


def calcular_follow(G, first, simboloInicial='S'):
  follow = {key: set() for key in G}
  follow[simboloInicial].add('$')  # símbolo de fin de cadena al FOLLOW del inicial

  while True:
    updated = False  # Verfica si el conjunto de FOLLOW cambio
    for A in G:
      for body in G[A]:
        for i, B in enumerate(body):
          if B.isupper():
            # Crear un conjunto temporal para los siguientes elementos después de B
            temp_follow = set()
            # Agregar FIRST de todo lo que sigue a B en el cuerpo de la producción, excepto vacio (epsilon)
            for symbol in body[i + 1:]:
              if symbol.isupper():
                temp_follow |= first[symbol] - {'e'}
                if 'e' in first[symbol]:
                  continue
                break
              else:
                temp_follow.add(symbol)
                break
            else:
              # Si B es el último símbolo o todo lo que sigue a B puede ser 'e', agregar FOLLOW de A
              temp_follow |= follow[A]

            # Si se agregó algo nuevo al FOLLOW de B, actualizar el conjunto FOLLOW y la bandera (la de arriba que verifica)
            if not temp_follow.issubset(follow[B]):
              follow[B] |= temp_follow
              updated = True

    # Si no hubo cambios en esta iteración, romper el bucle
    if not updated:
      break

  return follow


# le quite que se tenga que escribir cadenas, solo toma las reglas de la gramatica
def main():
  numGramaticas = int(input())
  for _ in range(numGramaticas):
    cantReglas = int(input())
    G = {}
    simboloInicio = 'S'
    for _ in range(cantReglas):
      regla = input().split()
      G[regla[0]] = regla[1:]

    first = calcular_first(G)
    follow = calcular_follow(G, first, simboloInicio)

    # Imprimirlos:
    for no_terminal in G:
      print(f"FIRST({no_terminal}) = {{ {', '.join(first[no_terminal])} }}")
      print(f"FOLLOW({no_terminal}) = {{ {', '.join(follow[no_terminal])} }}")


main()
"""