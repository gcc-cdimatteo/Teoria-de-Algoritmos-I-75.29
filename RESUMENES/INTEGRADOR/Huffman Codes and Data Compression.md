## Problem
Encode symbols using bits: encode schemes that take text written in richer alphabets and convert it into long strings of bits.
## Solution
### Variable-Length Encoding Schemes
As the Morse code, one can think in dots (which are short pulses) as zeros and dashes (which are long pulses) as ones. Morse proposed that one could communicate more efficiently by encoding frequent letters with short strings.
### Prefix Codes
The Morse code arise the problem of ambiguity because there exist pairs of letters where the bit string that encodes one letter is a prefix of the bit string that encodes another.
For this reason, a prefix code for a set $S$ of letters is a function $γ$ that maps each letter $x ∈ S$ to some sequence of zeros and ones, in such a way that for distinct $x, y ∈ S$, the sequence $γ (x)$ is not a prefix of the sequence $γ (y)$.
#### Algorithm
1. Scan the bit sequence from left to right.
2. Match the encode with the bits read as long as it's a correct match actually.
3. Delete the corresponding set of bits from the front of the message and iterate.
### Optimal Prefix Codes
Because of some letters are more frequent than others, these can have shorter encodings. 
Given an alphabet and a set of frequencies for the letters, one would like to produce a prefix code that is as efficient as possible meaning that it minimizes the average number of bits per letter $ABL(γ)=\sum_{x\in S}{f_x|γ(x)|}$.