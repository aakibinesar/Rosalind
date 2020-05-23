import sys
from rosalind_utility import rev_comp


def deBruijn(dna_strings):
    long_mers = set()
    for string in dna_strings:
        long_mers.add(string)
        long_mers.add(rev_comp(string))
    result = []
    for mer in long_mers:
        result.append((mer[:len(mer) - 1], mer[1:]))
    return result


if __name__ == "__main__":
    
    input_lines = open('rosalind_dbru.txt','r').read().splitlines()

    result = deBruijn(input_lines)

    for r in result:
        print("(" + r[0] + ", " + r[1] + ")")