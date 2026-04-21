"""
  Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation). 
  Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
"""
  
class Solution {
public:
    int minFlips(int a, int b, int c) {
         int flips = 0;
        
        for (int i = 0; i < 32; i++) {
            int bitA = (a >> i) & 1;
            int bitB = (b >> i) & 1;
            int bitC = (c >> i) & 1;
            
            if (bitC == 1) {
                // need at least one 1
                if (bitA == 0 && bitB == 0) {
                    flips += 1;
                }
            } else {
                flips += bitA + bitB;
            }
        }
        return flips;
    }
};
