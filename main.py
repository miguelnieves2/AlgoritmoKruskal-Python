import networkx as nx
import matplotlib.pyplot as plt

def dibujar_grafo(G, color_aristas='black'):
    posicion = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, posicion)
    nx.draw_networkx_labels(G, posicion)
    nx.draw_networkx_edges(G, posicion, edgelist=G.edges(), edge_color=color_aristas)
    etiquetas_peso = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, posicion, edge_labels=etiquetas_peso)
    plt.show()

def algoritmo_kruskal(G):
    # Convierte las aristas del grafo en una lista para poder trabajar con ellas.
    aristas = list(G.edges(data=True))
    # Ordena la lista de aristas por peso. Aquí es donde el programa determina qué arista es "más corta".
    # La función 'sort' organiza elementos de menor a mayor.
    # 'key=lambda x: x[2]['weight']' le dice a la función 'sort' que use el peso de la arista para ordenar.
    aristas.sort(key=lambda x: x[2]['weight'])
    # Crea un nuevo grafo para almacenar el camino más corto.
    camino_mas_corto = nx.Graph()
    # Crea una estructura de datos que hace un seguimiento de los componentes conectados del camino más corto.
    componentes_conectados = nx.utils.union_find.UnionFind(G)

    # Mira cada arista, empezando por la más corta.
    for arista in aristas:
        # 'arista' es una tupla que se ve así: (nodo1, nodo2, { "weight": 3 })
        # 'nodo1' y 'nodo2' son los nodos que la arista conecta.
        nodo1, nodo2 = arista[0], arista[1]

        # Si los nodos de la arista no están ya conectados en el camino más corto...
        if componentes_conectados[nodo1] != componentes_conectados[nodo2]:
            # Añade la arista al camino más corto.
            camino_mas_corto.add_edge(nodo1, nodo2, weight=arista[2]['weight'])
            # Une los dos componentes conectados en uno solo.
            componentes_conectados.union(nodo1, nodo2)

    return camino_mas_corto

G = nx.Graph()
G.add_edge('A', 'B', weight=6)
G.add_edge('A', 'G', weight=8)
G.add_edge('A', 'D', weight=10)
G.add_edge('B', 'E', weight=15)
G.add_edge('B', 'H', weight=13)
G.add_edge('B', 'C', weight=11)
G.add_edge('C', 'H', weight=3)
G.add_edge('D', 'E', weight=6)
G.add_edge('E', 'F', weight=2)
G.add_edge('F', 'G', weight=4)
G.add_edge('F', 'I', weight=6)
G.add_edge('G', 'H', weight=5)
G.add_edge('G', 'I', weight=5)
G.add_edge('H', 'I', weight=7)

print("Grafo Original")
dibujar_grafo(G)

camino_mas_corto = algoritmo_kruskal(G)

print("Camino más corto ó arbol de expansión minima")
dibujar_grafo(camino_mas_corto, color_aristas='blue')

print("Grafo completo demarcando el arbol")
dibujar_grafo(G, color_aristas=['red' if edge in camino_mas_corto.edges() else 'black' for edge in G.edges()])

# Cálculo de la longitud mínima
longitud_minima = sum(nx.get_edge_attributes(camino_mas_corto, 'weight').values())
print(f"Longitud mínima del camino: {longitud_minima}")