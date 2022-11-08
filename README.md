# Tab-to-Space

The program will ask the user to enter a strings having several tabs (‘\t’). 
Then you have to replace all tab into right number of spaces with the same output as when you print. When you see the output of the print(), 
one Tab is converted into (1 ~ K) spaces. (Since K depends on system, we get K as an input. But, usually 4 or 8. 
Afterwards, check by printing out string containing tabs and give right number into the input() function).

In other words, one Tab is converted into [K - (len(string) mod K)] spaces (‘ ‘),

Input → Output when you print() the input
a(tab) → a### (1)
ab(tab) → ab## (2)
abc(tab) → abc# (3)
abcd(tab) → abcd#### (4)
ab#cd(tab) → ab#cd### (5)

Input:
K (an integer)
- the number of spaces equal to tab in your idle when you
print, usually 4 or 8
- Note that, K is not manually defined by user. It only
depends on system. Please check K in your system and
use that K in your code.
- A string
Note that
- to enter tab, press [Shift + tab] instead of entering ‘/t’
- Input string can contain ‘ ‘(space) and (tab) both refer to
example (5) above

Output:
A Tab-to-space converted string
- actually, the output should be same with the input when
we see the printed output.
- you should not convert tab into ‘#’, but ‘ ‘
- The length of the Tab-to-space converted string
