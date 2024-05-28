# Final Project - Compilers
## Names of the group members
* Laura Ortiz Usme
* Miguel Ángel Salgar Olarte
## System Information
### OS VERSION
Windows 11 Home Version 23H2
### Python VERSION
Python 3.12
### Tools Used
Replit to be able to code at the same time remotely.
## Instructions
1. To run the program you need to run the command 'python main.py' (or 'py main.py' depending on python installation) or use a python IDE and use the run button.
2. The program will wait for the user to input a number, this number indicates the number of cases or grammars you are going to input.
3. Afterwards the program will enter its main loop, first requesting to input a number, this number is how many rules or derivations the grammar will have.
4. The user will input however many rules they specified in step 3. The rules are written with the syntax 'S A B C' where the first character will be the nonterminal, and the rest will be its possible derivations, all separated by spaces (An example could be S aSb a b which would be equivalent to the written form S->aSB|a|b).
5. The process specified by steps 3 and 4 will be repeated however many times the number inputted in step 2 dictates.
6. After all the cases have been inputted properly, the program will compute the First and Follow of all the nonterminals of all the grammars that were inputted.
