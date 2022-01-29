class Solution:
    def noOfSteps(self, N):
        return (2 ** N - 1)
    def toh(self, n, from_rod, to_rod, aux_rod):
        if n == 0:
            return
        self.toh(n - 1, from_rod, aux_rod, to_rod)
        print("move disk", n, "from rod", from_rod, "to rod", to_rod)
        self.toh(n - 1, aux_rod, to_rod, from_rod)
        return self.noOfSteps(n)
