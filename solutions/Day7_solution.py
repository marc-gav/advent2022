from solutions.SolutionBaseClass import AdventSolution
import networkx as nx


class Solution(AdventSolution):
    def __init__(self):
        super().__init__(day=7)

    def create_input(self, number_cases: int):
        pass

    def provide_example(self):
        with open("problem_inputs/day7.example.txt") as f:
            return f.read()

    def reader_parser(self, problem_string):
        return problem_string.splitlines()

    def part1(self, problem_string):
        problem_string = self.reader_parser(problem_string)
        G = nx.DiGraph()

        current_node = "/"
        G.add_node(current_node, weight=0, directory=True)
        for line in problem_string:
            if line.startswith("$"):
                # its a command
                if line.startswith("$ ls"):
                    continue
                elif line.startswith("$ cd"):
                    new_node = line.split(" ")[2]
                    if new_node == "/":
                        current_node = new_node
                    elif new_node == "..":
                        parent = list(G.predecessors(current_node))[0]
                        current_node = parent
                    else:
                        current_node = add_new_node(
                            G, current_node, new_node, 0, True
                        )

            else:
                if line.startswith("dir"):
                    # add it as a node
                    new_node = line.split(" ")[1]
                    new_node_full_dir = f"{current_node}/{new_node}"
                    if new_node_full_dir not in G.successors(current_node):
                        add_new_node(G, current_node, new_node, 0, True)
                else:
                    node_weight = int(line.split(" ")[0])
                    new_node = line.split(" ")[1]
                    add_new_node(G, current_node, new_node, node_weight, False)

        # make sure that no node has more than 1 parent
        assert (
            len(
                [
                    node
                    for node in G.nodes
                    if len(list(G.predecessors(node))) > 1
                ]
            )
            == 0
        ), "More than 1 parent for some node"

        cumm_weight(G, "/")
        self.cache['graph'] = G
        # get the nodes with a weight <= 1000
        nodes = [
            node
            for node in G.nodes
            if G.nodes[node]["weight"] <= 100000 and G.nodes[node]["directory"]
        ]

        return sum([G.nodes[node]["weight"] for node in nodes])

    def part2(self, problem_string) -> int:
        G = self.cache['graph']
        # need free space of 30000000
        total_size = 70000000
        update_size = 30000000
        used_space = G.nodes['/']['weight']
        unused_space = total_size - used_space
        at_least = update_size - unused_space
        # find the first directory that is bigger than need_to_free
        nodes = sorted([
                    node
                    for node in G.nodes
                    if G.nodes[node]["weight"] >= at_least and G.nodes[node]["directory"]
                ], key=lambda x: G.nodes[x]['weight'])
        return G.nodes[nodes[0]]['weight']

    def original_length(self):
        return len(self.problem_string)


def add_new_node(G, current_node, new_node, weight, is_directory):
    new_node_full_dir = f"{current_node}/{new_node}"
    if not new_node_full_dir in G.successors(current_node):
        G.add_node(new_node_full_dir, weight=weight, directory=is_directory)
        G.add_edge(current_node, new_node_full_dir)

    return new_node_full_dir


visited_nodes = set()


def cumm_weight(graph: nx.DiGraph, current_node: str):
    # the parent nodes have the sum of the weight of the children
    # this is a recursive function
    if current_node in visited_nodes:
        return graph.nodes[current_node]["weight"]
    visited_nodes.add(current_node)
    if len(list(graph.successors(current_node))) < 1:
        return graph.nodes[current_node]["weight"]
    node_sum = 0
    for child in graph.successors(current_node):
        node_sum += cumm_weight(graph, child)
    # change the current node weight
    graph.nodes[current_node]["weight"] = node_sum
    return node_sum
