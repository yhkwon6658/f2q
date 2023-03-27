import f2q
import random

# Data Set
floatArray = []

print("Test Data")
print("====================================")
for i in range(10):
    rand = random.uniform(-2.0,2.0)
    floatArray.append(rand)
    print(floatArray[i])
print("====================================")

# Converting
converter = f2q.converter(floatArray)
converter.tobin()

# Output
binArray = converter.binArray

print("Converted Data")
print("====================================")
for i in range(len(binArray)):
    if(len(binArray[i]) != 32) :
        print(f'binArray[{i}] length is {len(binArray[i])}')
        break
    
    print(binArray[i])
print("====================================")