'''
    Ivan Wong
    Raymond Cen
    Gabe Valdez
    CS 325
    GA 4
    Amir Nayyeri
'''

from collections import defaultdict

def can_turn_off_lights(input_file_path, output_file_path):
    def getInput(data):
        instances = data.split('***')[1:]
        instance_arr = []
        for instance in instances:
            if instance.strip():
                lns = instance.strip().split('\n')
                n, m = map(int, lns[0].split(','))
                light_states = list(map(int, lns[1].split(',')))
                switch_connections = [list(map(int, ln.split(','))) for ln in lns[2:]]
                instance_arr.append((n, m, light_states, switch_connections))
        return instance_arr

    def getClause(n, m, light_states, switch_connections):
        clauses = []
        for light_idx, state in enumerate(light_states, start=1):
            switches = [
                switch_idx + 1
                for switch_idx, connected_lights in enumerate(switch_connections)
                if light_idx in connected_lights
            ]
            if len(switches) != 2:
                raise ValueError(f"Light {light_idx} does not have exactly two switches.")
            if state == 1:
                clauses.append([switches[0], switches[1]])
                clauses.append([-switches[0], -switches[1]])
            else:
                clauses.append([switches[0], -switches[1]])
                clauses.append([-switches[0], switches[1]])
        return clauses

    class dir_graph:
        def __init__(self):
            self.graph = defaultdict(set)
            self.nodes = set()

        def addEdge(self, u, v):
            self.graph[u].add(v)
            self.nodes.add(u)
            self.nodes.add(v)

    class two_cnf:
        def __init__(self):
            self.con = []

        def add_clause(self, clause):
            if len(clause) <= 2:
                self.con.append(clause)

    def DFS(graph, visited, stack):
        def explore(node):
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    explore(neighbor)
                stack.append(node)

        for node in list(graph.keys()):  # Fix: Use a static list of keys
            if node not in visited:
                explore(node)

    def transpose_graph(graph):
        t_graph = defaultdict(set)
        for node in graph:
            for neighbor in graph[node]:
                t_graph[neighbor].add(node)
        return t_graph

    def strongly_connected_components(graph):
        stack = []
        visited = set()
        DFS(graph, visited, stack)

        t_graph = transpose_graph(graph)
        visited.clear()
        sccs = []

        while stack:
            node = stack.pop()
            if node not in visited:
                scc = []
                explore_stack = [node]
                while explore_stack:
                    current = explore_stack.pop()
                    if current not in visited:
                        visited.add(current)
                        scc.append(current)
                        explore_stack.extend(t_graph[current])
                sccs.append(scc)
        return sccs

    def find_contradiction(sccs):
        for scc in sccs:
            literals = set(scc)
            for literal in literals:
                if -literal in literals:  # Check for contradiction
                    return True
        return False

    def two_sat_solver(cnf):
        graph = defaultdict(set)
        for clause in cnf.con:
            if len(clause) == 2:
                u, v = clause
                graph[-u].add(v)
                graph[-v].add(u)
            elif len(clause) == 1:
                u = clause[0]
                graph[-u].add(u)
        sccs = strongly_connected_components(graph)
        return not find_contradiction(sccs)

    def create_clauses(n, m, light_states, switch_connections):
        cnf = two_cnf()
        clauses = getClause(n, m, light_states, switch_connections)
        for clause in clauses:
            cnf.add_clause(clause)
        return cnf

    # Read input and parse instances
    with open(input_file_path, 'r') as f:
        data = f.read()
    instances = getInput(data)

    # Process each instance and determine satisfiability
    results = []
    for n, m, light_states, switch_connections in instances:
        cnf = create_clauses(n, m, light_states, switch_connections)
        if two_sat_solver(cnf):
            results.append("yes")
        else:
            results.append("no")

    # Write results to output file
    with open(output_file_path, 'w') as f:
        f.write("\n".join(results) + "\n")

# can_turn_off_lights('input.txt', 'output.txt')
