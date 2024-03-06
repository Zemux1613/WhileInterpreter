# Grammar
While programmes are inductively defined as follows:
1. ```xi := xj + c``` and ```print x``` is a while programm.
2. ``print xi`` is a while programm.
3. If P1 and P2 are while programms, then ```P1;P2``` is a while programm.
4. If P1 is a while programm, then ```while xi != 0 do P1 end``` is a while programm.

Derived from this inductive definition, a context-free grammar for while-programmes is the following:

G = (N, A, P, programm) with <br>
N = {programm, operator, i},<br>
A = {-, +, :=, ;, while, do, end, x, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, print},<br>
P = {<br>
programm -> ```xi = xi operator i``` | ```programm;programm``` | ```while xi != 0 do programm end``` | ```print xi```; <br>
i -> ```0``` | ```1``` | ```2``` | ```3``` | ```4``` | ```5``` | ```6``` | ```7``` | ```8``` | ```9``` | ```1i``` | ```2i``` | ```3i``` | ```4i``` | ```5i``` | ```6i``` | ```7i``` | ```8i``` | ```9i```;<br>
operator -> ```+``` | ```-```
<br>}

# Parsing
https://en.wikipedia.org/wiki/Parsing <br><br>
![asd](https://upload.wikimedia.org/wikipedia/commons/d/d6/Parser_Flow%D5%B8.gif)

# Research
- [Vorlesung Compilerbau](https://www.eti.uni-siegen.de/ti/lehre/ss15/compilerbau/compilerbau.html)
- [Compilerbau – eine Einührung](https://homepages.thm.de/~hg52/lv/compiler/skripten/compilerskript/pdf/compilerskript.pdf)
- [Compilerbau Vorlesung WS](https://imweb.imn.htwk-leipzig.de/~waldmann/edu/ss22/cb/folien/skript.pdf)