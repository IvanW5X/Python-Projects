'''
    Ivan Wong, Raymond Cen, Gabe Valdez
    GA3
    CS 325
'''


def find(parent, v):
    # Find the representative of the set containing v
    if parent[v] != v:
        parent[v] = find(parent, parent[v])  # Path compression
    return parent[v]

def union(parent, rank, u, v):
    # Union the sets containing u and v
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

def kruskal(num_vertices, edges, exclude_edge=None):
    # Kruskal's algorithm to find MST weight, optionally excluding a specific edge
    if exclude_edge:
        edges = [e for e in edges if e != exclude_edge]
    edges.sort()

    parent = list(range(num_vertices))
    rank = [0] * num_vertices

    mst_weight = 0
    edge_count = 0
    mst_edges = []

    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_weight += weight
            mst_edges.append((weight, u, v))
            edge_count += 1

            if edge_count == num_vertices - 1:
                break

    if edge_count != num_vertices - 1:
        return float('inf'), []  # No MST possible

    return mst_weight, mst_edges

def find_next_mst(num_vertices, edges, current_mst_edges, excluded_msts):
    candidates = []

    # Find the next unique MST with the minimum cost
    for edge in current_mst_edges:
        mst_weight, mst_edges = kruskal(num_vertices, edges, exclude_edge=edge)
        if mst_weight != float('inf') and mst_edges not in excluded_msts:
            candidates.append((mst_weight, mst_edges))

    if candidates:
        return min(candidates, key=lambda x: x[0])
    return float('inf'), []

def three_min_spanning_trees(input_file_path, output_file_path):
    with open(input_file_path, "r") as inFile:
        num_vertices = int(inFile.readline().strip())
        adjacency_matrix = []

        for _ in range(num_vertices):
            row = list(map(int, inFile.readline().strip().split(",")))
            adjacency_matrix.append(row)

    # Convert adjacency matrix to edge list
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):  # Avoid duplicates
            edges.append((adjacency_matrix[i][j], i, j))

    # Compute the first MST
    mst1_weight, mst1_edges = kruskal(num_vertices, edges)
    solutions = [(mst1_weight, mst1_edges)]
    excluded_msts = [mst1_edges]

    # Compute the second MST
    mst2_weight, mst2_edges = find_next_mst(num_vertices, edges, mst1_edges, excluded_msts)
    if mst2_weight != float('inf'):
        solutions.append((mst2_weight, mst2_edges))
        excluded_msts.append(mst2_edges)

    # Compute the third MST
    mst3_weight, mst3_edges = find_next_mst(num_vertices, edges, mst2_edges, excluded_msts)
    if mst3_weight != float('inf'):
        solutions.append((mst3_weight, mst3_edges))

    # Write the results to the output file
    with open(output_file_path, "w") as outFile:
        for weight, _ in solutions:
            outFile.write(str(weight) + "\n")

# Example usage
#three_min_spanning_trees("input.txt", "output.txt")