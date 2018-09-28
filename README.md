# Cunningham.py

If the command is run without any arguments, the script will find chains starting with a number between 1 and 91304653283578934559359 with a minimum length of 3 numbers. Otherwise, the command accepts two arguments. The first specifies the minimum length of the chain. This will not return any chains with a length less than 6.

```
$ ./cunningham.py 6

1st : [89, 179, 359, 719, 1439, 2879]
1st : [63419, 126839, 253679, 507359, 1014719, 2029439]
1st : [127139, 254279, 508559, 1017119, 2034239, 4068479]
1st : [405269, 810539, 1621079, 3242159, 6484319, 12968639]
1st : [810809, 1621619, 3243239, 6486479, 12972959, 25945919]
...
```
The second accepted argument is a maximum number value. The default (91304653283578934559359) is a reference to Jaroslaw Wroblewski, but you can use this argument to specify your own limit.
```
$ ./cunningham.py 6 123456789

1st : [89, 179, 359, 719, 1439, 2879]
1st : [63419, 126839, 253679, 507359, 1014719, 2029439]
1st : [127139, 254279, 508559, 1017119, 2034239, 4068479]
1st : [405269, 810539, 1621079, 3242159, 6484319, 12968639]
1st : [810809, 1621619, 3243239, 6486479, 12972959, 25945919]
1st : [1069199, 2138399, 4276799, 8553599, 17107199, 34214399]
1st : [1122659, 2245319, 4490639, 8981279, 17962559, 35925119, 71850239]
1st : [1178609, 2357219, 4714439, 9428879, 18857759, 37715519]
1st : [1333889, 2667779, 5335559, 10671119, 21342239, 42684479]
1st : [1598699, 3197399, 6394799, 12789599, 25579199, 51158399]
...
```
You can read more about Cunningham chains and the largest recorded chains [here](https://en.wikipedia.org/wiki/Cunningham_chain).
