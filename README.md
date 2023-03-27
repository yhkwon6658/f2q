# f2q
floating point to q-format fixed point converter in python 3.11.2  
you can convert 1-D floating point array using this code  
the output is 1-D string array  

```python
floatArray = []
for i in range(10):
  rand = random.uniform(-2.0,2.0)
  floatArray.append(rand)

converter = f2q.converter(floatArray)
converter.tobin()
```

# fractional bits selection
Default fraction bits are 20  

```python

# Converting
converter = f2q.converter(floatArray,fraction_bits=20)
converter.tobin()

```
