# Fantasy Name Generator

The program generates a fantasy firstname and lastname.

It runs in Python 3+.


It conforming to the following rules:

Consider position x in string.

1) If x-1 does not exist, set x to either consonant or vowel

2) If x-1 does exist:

>a) If x-1 is consonant:

>>1) If x-2 does not exist, set x to vowel

>>2) If x-2 does exist:

>>>a) If x-2 is consonant, set x to vowel

>>>b) If x-2 is vowel, set to either

>b) If x-1 is vowel:

>>1) If x-2 does not exist, set x to consonant

>>2) If x-2 does exist:

>>>a) If x-2 is consonant, set to either

>>>b) If x-2 is vowel, set to consonant
