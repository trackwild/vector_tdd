class Vector:
    
    def __init__(self, nums):
        self.nums = nums
        self.dims = len(nums)
        self.norm = self.length()

    def length(self):
        return sum([c**2 for c in self.nums])**0.5

    def unit_vector(self):
        return Vector([c/self.length() for c in self.nums])

    def scale_vector(self, size):
        return Vector([c * size for c in self.nums])

    def __eq__(self, other):
        return self.nums == other.nums