from __future__ import division
def gcd(a, b):
    """
    Calculate the greatest common divisor.
    """
    while b:
        a, b = b, a%b
    return a

class Fraction(object):
    """
    A simple fraction class.
    """
    def __init__(self, numerator, denominator=1):
        """
        Creates a new fraction.
        """
        self._numerator = numerator
        self._denominator = denominator
  
    def __str__(self):
        """
        1. Print the fraction.
        """
        return str(self._numerator) + '/' + str(self._denominator)
      
    def __add__(self, other):
        """
        2. Print the result of adding two fractions.
        """
        return Fraction( ( ( self._numerator * other._denominator ) + ( self._denominator * other._numerator ) ) , ( self._denominator * other._denominator ) ).simplify()

    def invert(self):
        """
        3. Invert the fraction.
        """
        new_numerator = self._denominator
        new_denominator = self._numerator
        return Fraction(new_numerator,new_denominator).simplify()
 
    def to_float(self):
        """
        4. Decimal representation of a fraction. *Note: from __future__ import division*
        """
        return self._numerator / self._denominator
 
    def integer(self):
        """                                                                             
        5. Integer part of a fraction                                       
        """
        return int(self._numerator / self._denominator)
  
    def subtract(self, other):
        """
        6. Result of subtracing two fractions.
        """
        new_numerator = ( ( self._numerator * other._denominator ) - ( self._denominator * other._numerator ) )
        new_denominator = ( self._denominator * other._denominator )
        return Fraction(new_numerator,new_denominator).simplify()
            
    def multiply(self, other):
        """
        6. Result of multiplying two fractions.
        """
        new_numerator = ( self._numerator * other._numerator)
        new_denominator = ( self._denominator * other._denominator )
        return Fraction(new_numerator,new_denominator).simplify()
     
    def divide(self, other):
        """
        6. Result of dividing two fractions.
        """
        o_numerator = other._denominator                                                                                                                      
        o_denominator = other._numerator
        new_numerator = ( self._numerator * o_numerator)
        new_denominator = ( self._denominator * o_denominator )
        return Fraction(new_numerator,new_denominator).simplify() 

    def simplify(self):
        """                                                                                                                                                    
        7. Simplify a fraction                                                                                                              
        """                                                                                                                                                    
        GCD=gcd(self._numerator,self._denominator)
        new_numerator = int ( self._numerator / GCD)                                                       
        new_denominator = int ( self._denominator / GCD )                                                                                
        return Fraction(new_numerator,new_denominator) 
    def comparison(self, other):
        """
        8. Compare two fraction.
        """
        x = self.simplify()
        other = other.simplify()
        S = self._numerator * other._denominator
        O = self._denominator * other._numerator
        if S>O:
            print self , '>' , other
        elif S==O:
            print self , '==' , other
        else:
            print self , '<' , other
        return ""



         
