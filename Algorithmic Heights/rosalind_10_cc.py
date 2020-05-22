from collections import defaultdict

def connected_component_count(n, edges):
    '''Performs a BFS to get the number of connected components.'''
    # Build the graph.
    graph = defaultdict(list)
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    # Traverse the graph to find the number of connected components.
    component_count = 0
    remaining = set(range(1, n+1))
    while remaining:
        component_count += 1
        queue = {remaining.pop()}
        while queue:
            current = queue.pop()
            new_nodes = {node for node in graph[current] if node in remaining}
            queue |= new_nodes
            remaining -= new_nodes

    return component_count


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    input_data = open('rosalind_cc.txt').readlines() 
    vertices, edges = (int(val) for val in input_data[0].split())
    my_data = [[int(val) for val in line.split()] for line in input_data[1:]]
    # Get the minimum distances.
    count = connected_component_count(vertices, my_data)
    # Print and save the answer.
    print (count)

    #with open('output.txt', 'w') as output_data:
    #    output_data.write(min_dist)

if __name__ == '__main__':
	main()