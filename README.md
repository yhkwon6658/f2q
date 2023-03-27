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

# Result
```
Test Data
====================================
1.9250502144400348
1.794209499929007
-1.9342741186256265
-0.7614433373841143
0.7894027848421299
1.759796095056645
-0.6186446790823479
0.10851338709643343
-0.7969203552493669
1.7003159395961305
====================================
Converted Data
====================================
00000000000111101100110100000001
00000000000111001011010100010101
10000000000111101111001011001001
10000000000011000010111011011111
00000000000011001010000101100100
00000000000111000010100000011111
10000000000010011110010111110111
00000000000000011011110001111000
10000000000011001100000000101111
00000000000110110011010001111110
====================================
```
