# Ejecutar con python test.py desde el shell


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
  listaGramatica = []  # creamos una lista
  numGramaticas = int(input())
  for _ in range(numGramaticas):
    cantReglas = int(input())
    G = {}
    for _ in range(cantReglas):
      regla = input().split()
      G[regla[0]] = regla[1:]

    listaGramatica.append(G)  # añadir la gramática que acabamos de crear

  for gram in listaGramatica:
    # Calcular los conjuntos FIRST y FOLLOW
    first = calcular_first(gram)
    follow = calcular_follow(gram, first, 'S')
    # Imprimir los conjuntos FIRST y FOLLOW
    for nonterminal in gram:
      print(f"First({nonterminal}) = {first[nonterminal]}")
      print(f"Follow({nonterminal}) = {follow[nonterminal]}")
    

if __name__ == "__main__":
  main()
