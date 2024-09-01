---
category: reversing
points: "65"
---
# Given
A PNG file:
![[maybe_assembly.png]]

# Solution
- First thought was that it reminds of ASSEMBLY like code yet there are some gaps. Just in case if here is part of stenography we check this file with  [Aperi'Solve](https://www.aperisolve.com/12d32921f371e06fb1e8f4b2e77b3991). It did not return anything strange with colors. In *Binwalk* section it saw zip file. We downloaded it and with *gunzip* decompressed it (`gunzip -d ./5B-0`). We got another file that contained same picture, so there were no any hidden details.
- Then we focused more on the commands. With *Google reverse image search*:
![[Pasted image 20240830111203.png]]
We got more similar images with descriptions. The table we have in the given file is actually an *Assembly* trace table. In first column we have labels, in the second operation commands and in third arguments. 
- After close examination, we have concluded that there are 3 variables involved: `FLAG`, `CODETIGER` and `ORZ`. However program was not making sense as in parts of `BL` and `BU` (*Branch Linked* and *Branch Unconditional*) were also referencing the constants. After opening eyes, we have noticed that there are separate "goto" labels -  `C0DETIGER` and `0RZ` that use zero symbol in the place of o.
- Then we interpreted the algorithm on the photo in python. Due to "game" with "goto" labels, there is an endless cycle with conditional break statement that is not mentioned.  As lines backward there was subtraction and in labels is used zero, we have tried to make that condition that `ORZ <= 0`.
Python result:
![[Pasted image 20240830112007.png]]
- We ran the program (`python codetiger.py`) and have received the output:
![[Pasted image 20240830112106.png]]
So we got our flag `NKI{5149}`!
