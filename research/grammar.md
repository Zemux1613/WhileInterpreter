While programmes are inductively defined as follows:
1. ```xi := xj + c``` is a while programm
2. If P1 and P2 are while programms, then ```P1;P2``` is a while programm
3. If P1 is a while programm, then ```while xi != 0 do P1 end``` is a while programm

Derived from this inductive definition, a context-free grammar for while-programmes is the following:

G = (N, A, P, programm) with <br>
N = {programm, operator, i},<br> 
A = {-, +, :=, ;, while, do, end, x, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9},<br> 
P = {<br>
programm -> ```xi := xi operator i``` | ```programm;programm``` | ```while xi != 0 do programm end```; <br>
i -> ```0``` | ```1``` | ```2``` | ```3``` | ```4``` | ```5``` | ```6``` | ```7``` | ```8``` | ```9``` | ```1i``` | ```2i``` | ```3i``` | ```4i``` | ```5i``` | ```6i``` | ```7i``` | ```8i``` | ```9i```;<br>
operator -> ```+``` | ```-```
<br>}