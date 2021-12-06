# PDA-Simulator

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A Pushdown Automata Simulator built using Python

## About
We are implementing Pushdown Automata Simulator. Pushdown Automata (PDA) is a Finite Automata with extra memory called stack which helps it to recognize Context Free Language (CFL). Finite Automata is used to recognize patterns in which, it takes a string of symbols as input and when the symbol is found, then the transition occurs. After it has successfully traversed through the string, if it reaches the final state, then the string will be accepted. Context-Free Grammar (CFG) is a formal grammar which is used to generate the strings in a given formal language. CFL is a language generated by the CFG which gets accepted by a Pushdown Automata. A Pushdown Automata can be defined as a septuple - tuple with seven elements

The transition functions of the PDA can be notated using  Instantaneous Description (ID). It's an informal way of describing how a PDA "computes" an input text and decides whether it should be accepted or rejected. The constituents of an ID are (q, w, z), where q - The current state, w - The input symbol under consideration and z - The current stack top symbol 

## Getting Started
### Prerequisites
-  `python3` should be installed 

## Procedure to run the code
The PDA Simulator can be used to verify a CFG is valid or not. The simulator can be run by using the following command.
```python runner.py -i <Language No.>```

### Help option
```python runner.py -h```

## Contributors
The contributors for this project are :

 - Anand Balaji	
 - Anjith Prakash
 - Sreerag K Vivek
 - Vivek Haridas
