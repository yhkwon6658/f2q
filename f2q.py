# Description : float to Q-format fixed-point converter
# Date : Mar. 27. 2023
# e-mail : yonghwankwon.6658@gmail.com
# Python version : 3.11.2

class converter:
    
    binArray = []
    hexArray = []
    
    def __init__(self, floatArray, fraction_bits=20):
        self.floatArray = floatArray
        self.fraction_bits = fraction_bits

    def tobin(self):
        
        int_bits = 32 - 1 - self.fraction_bits # default 11 bits
        
        for i in self.floatArray:
                    
            # sign bit
            if(i>=0):
                res = "0"
            else :
                res = "1"
                i = abs(i)
                
            # split
            integer, fraction = str(i).split(".")
            
            # integer
            integer = int(integer)
            integer = bin(integer).lstrip("0b")
            integer = list(reversed(integer))
            
            for i in range(int_bits - len(integer)):
                integer.append("0")
            
            integer = list(reversed(integer))
            integer = "".join(integer)
            
            res += integer
            
            # fraction
            fraction = int(fraction)
            
            while (fraction >= 1):
                fraction /= 10.0
            
            for i in range(self.fraction_bits):
                
                fraction *= 2
                
                if (fraction < 1) :
                    integer = "0"
                else :
                    integer = "1"
                    fraction -= 1
                
                res += integer
            
            # append result
            self.binArray.append(res)