from collections import defaultdict


def minimum_dist_bfs(n, edges):
    '''Performs a BFS to get the minimum distance to all nodes starting at node 1.'''
    # Build the graph.
    graph = defaultdict(list)
    for n1, n2 in edges:
        graph[n1].append(n2)

    # BFS to find the minimum distance to each node from node 1.
    min_dist = [0] + [-1]*(n-1)
    remaining = set(range(2, n+1))
    queue = [1]
    while queue:
        current = queue.pop(0)
        for node in graph[current]:
            if node in remaining:
                queue.append(node)
                remaining.discard(node)
                # Rosalind starts indices at 1 instead of 0.
                min_dist[node-1] = min_dist[current-1] + 1

    return min_dist


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    input_data = open('rosalind_bfs.txt').readlines() 
    vertices, edges = (int(val) for val in input_data[0].split())
    my_data = [[int(val) for val in line.split()] for line in input_data[1:]]
    # Get the minimum distances.
    min_dist = minimum_dist_bfs(vertices, my_data)
    # Print and save the answer.
    print (' '.join(str(num) for num in min_dist))

    with open('output.txt', 'w') as output_data:
        output_data.write(' '.join(str(num) for num in min_dist))

if __name__ == '__main__':
	main()