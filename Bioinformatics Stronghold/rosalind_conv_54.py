import sys


def Minkowski_difference(set1, set2):
    diff_multiset = []
    for s1 in set1:
        for s2 in set2:
            diff_multiset.append(round(s1 - s2, 5))

    multiplicities = {}
    for item in diff_multiset:
        multiplicities[item] = diff_multiset.count(item)

    max_val = -1
    for item, count in multiplicities.items():
        if count > max_val:
            max_val = count
            max_x = item

    return max_val, max_x


if __name__ == "__main__":
    
    input_lines = open('rosalind_conv.txt','r').read().splitlines()

    S1 = [float(x) for x in input_lines[0].split()]
    S2 = [float(x) for x in input_lines[1].split()]

    res = Minkowski_difference(S1, S2)
    print(res[0])
    print(res[1])