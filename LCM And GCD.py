# LCM of two numbers (say A and B) can be calculated using the formula: -
# A × B = LCM(A,B) × HCF(A,B)
class Solution:
    def lcmAndGcd(self, A , B):
        gcd = self.gcd(A , B)
        lcm = A * B // gcd
        return lcm , gcd
    def gcd(self, A, B):
        if (B == 0):
            return A
        return self.gcd(B, A%B)  
