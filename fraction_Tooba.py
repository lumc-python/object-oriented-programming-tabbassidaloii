def gcd( a , b ):
    """
    Calculate the greatest common divisor.
    """
    while b:
        a , b = b , a%b
    return a

class Fraction( object ):
    """
    A simple fraction class.
    """
    def __init__( self , numerator , denominator = 1 ):
        """
        Creates a new fraction.
        """
        self._numerator = numerator
        self._denominator = denominator
  
    def __str__( self ):
        """
        1. Print the fraction.
        """
        return str( self._numerator ) + '/' + str( self._denominator )
      
    def __add__( self , other ):
        """
        2. Print the result of adding two fractions.
        """
        return Fraction( ( ( self._numerator * other._denominator ) + ( self._denominator * other._numerator ) ) , ( self._denominator * other._denominator ) ).simplify()

    def invert( self ):
        """
        3. Invert the fraction.
        """
        return Fraction( self._denominator , self._numerator ).simplify()
 
    def to_float( self ):
        """
        4. Decimal representation of a fraction.
        """
        return float( self._numerator ) / float( self._denominator )
 
    def integer( self ):
        """                                                                             
        5. Integer part of a fraction                                       
        """
        return int( self._numerator / self._denominator )
  
    def __sub__( self , other ):
        """
        6. Result of subtracing two fractions.
        """
        return Fraction( ( ( self._numerator * other._denominator ) - ( self._denominator * other._numerator ) ) , ( self._denominator * other._denominator ) ).simplify()
             
    def __mul__(self, other):
        """
        6. Result of multiplying two fractions.
        """
        return Fraction( self._numerator * other._numerator , self._denominator * other._denominator ).simplify()
     
    def __div__(self, other):
        """
        6. Result of dividing two fractions.
        """
        return Fraction(other.invert().__mul__(self))

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
        self, other = self.simplify(), other.simplify()
        S = self._numerator * other._denominator
        O = self._denominator * other._numerator
        if S>O:
            print self , '>' , other
        elif S==O:
            print self , '==' , other
        else:
            print self , '<' , other
        return ""



         
