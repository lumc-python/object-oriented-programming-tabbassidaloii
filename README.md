# Object Oriented Programming Assignment

Use the skeleton to implement a Fraction type (in the file `fraction.py`) containing two integers: `numerator` and `denominator`.
The file `test_fraction.py` can be edited and used to test the created class.

1. Add a member function to give a print representation for the class, e.g., `print Fraction(1, 2)` should yield in something like: `1/2`.

2. Add a member function to add to fractions, e.g., `print Fraction(1, 2) + Fraction(2, 3)` should yield `7/6`.

3. Add a member function to invert a fraction, e.g., `print Fraction(1, 2).invert()` should yield `2/1`.

4. Add a member function to give a decimal representation of a fraction, e.g., `print Fraction(1, 2).to_float()` should yield `0.5`.

5. Add member functions to subtract, multiply and divide fractions. Hint: can we reuse any of the member functions?

6. Add a member function to simplify a fraction, e.g., `print Fraction(2, 6).simplify()` should yield `1/3`.
  Hint: use a function to calculate the greatest common divisor.

7. Can we improve our arithmetic functions with our newly created simplification method?

8. How would you deal with negative fractions?

9. Can you add integer multiplication functionality, e.g., `print Fraction(1, 2) * 2` should yield `2/2`.

10. How can we prevent things like: `Fraction(0.4, 0.2)`?
