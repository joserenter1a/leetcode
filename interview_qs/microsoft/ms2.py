"""
Find Well Structured Words

Author: Jose Renteria
"""

from collections import defaultdict
 
MOD = 1000000007
 
def factorial(n):
    res = 1
    for i in range(2, n+1):
        res = (res*i)%MOD
    return res
 
def modulo_inverse(num):
    return pow(num, MOD-2, MOD)
 
def modulo_division(num, denom):
    return (num*modulo_inverse(denom))%MOD
 
def findPermutations(freqs, ct):
    res = factorial(ct)
    for size in freqs.values():
        res = modulo_division(res, factorial(size))
    
    return res
 
def find_well_structured_words(S):
    vowels = {'A','E','I','O','U'}
    
    vowel_freq = defaultdict(int)
    vowel_count = 0
    
    consonant_freq = defaultdict(int)
    consonant_count = 0
    
    for char in S:
        if char in vowels:
            vowel_freq[char] += 1
            vowel_count += 1
        else:
            consonant_freq[char] += 1
            consonant_count += 1
    
    res1 = findPermutations(vowel_freq, vowel_count)
    res2 = findPermutations(consonant_freq, consonant_count)
    
    return 0 if consonant_count < vowel_count else (res1*res2) % MOD
 
# TEST CASES
print(find_well_structured_words("BAR"))
print(find_well_structured_words("AABB"))
print(find_well_structured_words("AABCY"))
