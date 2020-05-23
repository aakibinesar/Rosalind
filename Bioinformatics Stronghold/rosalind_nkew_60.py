from Newick_trees import WeightedNewick

with open('rosalind_nkew.txt') as input_data:
    trees = [line.split('\n') for line in input_data.read().strip().split('\n\n')]

# The majority of the work is done by the Weighted Newick class in the Data Structures script.
distances = [str(WeightedNewick(tree[0]).distance(*tree[1].split())) for tree in trees]

# Print and save the answer.
print ' '.join(distances)
with open('output.txt', 'w') as output_data:
    output_data.write(' '.join(distances))