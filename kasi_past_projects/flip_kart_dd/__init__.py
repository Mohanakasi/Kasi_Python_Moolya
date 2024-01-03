class Example:
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an instance of the class
obj = Example()

# Call the add method with different numbers of arguments
result1 = obj.add(1)
result2 = obj.add(1, 2)
result3 = obj.add(1, 2, 3)

print(result1)  # Output: 1
print(result2)  # Output: 3
print(result3)