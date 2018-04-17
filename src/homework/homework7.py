'''
Problem
For two strings s1 and s2 of equal length, the p-distance between them, denoted dp(s1,s2), is the
proportion of corresponding symbols that differ between s1 and s2.
For a general distance function d on n taxa s1,s2,…,sn (taxa are often represented by genetic strings),
 we may encode the distances between pairs of taxa via a distance matrix D in which Di,j=d(si,sj).
Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given
in FASTA format.
Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that
your answer is allowed an absolute error of 0.001.
Sample Dataset
[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]
Sample Output
0.00000 0.40000 0.10000 0.10000
0.40000 0.00000 0.40000 0.30000
0.10000 0.40000 0.00000 0.20000
0.10000 0.30000 0.20000 0.00000
dif / len
get_p_distance_matrix([
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
])
'''
def get_p_distance_matrix(seq):
    rl = []
    d = 0
    k = 0
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    for w, x, y, z  in zip(seq[0],seq[1],seq[2],seq[3]):
        if w == w:
            a1 = 0
        if w != x:
            d += 1
            a2 = d / len(seq[0])
        if w != y:
            a3+=1
            a3 = a3 / len(seq[0])
        if w != z:
            a4+=1
            a4 = a4 / len(seq[0])
        if x != w:
            b1+=1
            b10 = b1 / len(seq[0])
        if x == x:
            b2 = 0
        if x != y:
            b3 += 1
            b30 = b3 / len(seq[0])
        if x != z:
            b4+=1
            b40 = b4 / len(seq[0])
        if y != w:
            c1 += 1
            c10 = c1 / len(seq[0])
        if y != x:
            c2 += 1
            c20 = c2 / len(seq[0])
        if y == y:
            c30 = 0
        if y != z:
            c4+=1
            c40 = c4 / len(seq[0])
        if z != w:
            d1 += 1
            d10 = d1 / len(seq[0])
        if z != x:
            d2 += 1
            d20 = d2 / len(seq[0])
        if z != y:
            d3 +=1
            d30 = d3 / len(seq[0])
        if z == z:
            d40 = 0

    rl = [
        [a1,a2,a3,a4],
        [b10,b2,b30,b40],
        [c10,c20,c30,c40],
        [d10,d20,d30,d40]
        ]
    return rl
