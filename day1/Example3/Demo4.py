class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
print(MathUtils.add(2, 3)) # 5

m = MathUtils()
print(m.add(2, 3))          # 5 ✅ (but not recommended stylistically)