# Cellular-Automata
A flexible Cellular Automata generator with default settings for Conway's Game Of Life.

#### There are two files:
- numerical_grid.py
- graphical_grid.py

numerical_grid generates a square matrix of 1s and 0s and returns it to graphical_grid. The arrangement of 1s and 0s is determined by the methods used inside numerical_grid.py.

Once the grid is generated it is passed to graphical_grid.py. This uses pyglet library to generate graphical representation of the matrix.
Here, 1 is represented by a white cell and 0 by black. The grid is again passed into the numerical_grid functions to be updated for the next iteration.
The whole process is repeated under an infinite loop.

### Other methods
By default, all functions return values so that the end result is to represent Conway's Game Of Life. The default methods are specified in the default_parameters.txt file. These methods can be changed to generate different Cellular Automata models as instructed in numerical_grid.py

under numerical_grid.py are 3 main functions:
 1) `first_numerical_grid()`
 2) `sum33()`
 3) `rules()`

`first_numerical_grid()` acts as an initial condition. The very first grid that is generated by default is a random arrangement of 1s and 0s. This can be changed by either using one of the other initail condition methods inside this `first_numerical_grid()`, or you can introduce your own method.

`sum33()` is a way to take the sum of a 3x3 matrix within the larger matrix. it contains different methods of summing within the 9 element matrix

'rules()' determine how the central cell should behave (whether be 1 or 0) based on the summed value obtained fro `sum33()`

IS THIS ALRIGHT?
