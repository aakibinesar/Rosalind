from Bio import Phylo
import random

def CharacterTable(tree):
    def create_character(split_species):
        character=[]
        for s in species:
            character.append(1 if s in split_species else 0)
        return ''.join([str(c) for c in character])
    
    species=[spec.name for spec in tree.find_elements(terminal=True)]
    species.sort()

    clades=[clade for clade in tree.find_clades(terminal=False)]
    # we iterate over all Clades except the root
    return [create_character([spec.name for spec in split.find_elements(terminal=True)]) for split in clades[1:]]

if __name__=='__main__': 
    tree = Phylo.read('rosalind_ctbl.txt', 'newick')
    for ch in CharacterTable(tree):
        print (ch)