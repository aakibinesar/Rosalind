from Newick_trees import Newick

with open('rosalind_nwck.txt') as input_data:
    trees = [line.split('\n') for line in input_data.read().strip().split('\n\n')]

# The majority of the work is done by the Newick class in the Data Structures script.
distances = [str(Newick(tree[0]).distance(*tree[1].split())) for tree in trees]

# Print and save the answer.
print ' '.join(distances)
with open('output.txt', 'w') as output_data:
    output_data.write(' '.join(distances))