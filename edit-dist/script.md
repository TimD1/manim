Intro
-----
> display title with some background music

Problem Statement: Minimum Edit Distance
----------------------------------------

The edit distance between two strings is defined as the minimum number of edits requiredto transform one string to another.
In genomics, these two strings are typically the expected DNA sequence (reference R), and the measured DNA sequence (query Q).
> show two sequences, label

Edits can take the form of substitutions (where a single character is exchanged for another), insertions (where a new character is added), or deletions (where a character is removed from the sequence).
> color changes for SUB/INS/DEL in real time
> SUB = blue
> INS = green
> DEL = red

There are always multiple ways to transform the query to the reference. 
For example, we could always delete the entire query sequence and insert the whole reference. 
We are looking for the minimum possible number of edits.
> three examples

Intuition: Dynamic Programming
------------------------------

Example
-------




