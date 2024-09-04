# fun-with-logits
A fun time working with logits, because who doesn't love logits?


Objective
The goal of this exercise is to understand the softmax function, implement it in Python, and apply it to a set of raw scores (also called logits). Softmax is commonly used in multi-class classification problems to convert raw scores into probabilities.

Softmax Function
Softmax takes a vector of real numbers and normalizes it into a probability distribution, where the sum of all probabilities is 1. Mathematically, for an input vector 
𝑧
z, the softmax of element 
𝑧
𝑖
z 
i
​
  is defined as:

softmax
(
𝑧
𝑖
)
=
𝑒
𝑧
𝑖
∑
𝑗
=
1
𝑛
𝑒
𝑧
𝑗
softmax(z 
i
​
 )= 
∑ 
j=1
n
​
 e 
z 
j
​
 
 
e 
z 
i
​
 
 
​
 
where:

𝑧
𝑖
z 
i
​
  is the i-th raw score in the input vector.
𝑒
𝑧
𝑖
e 
z 
i
​
 
  is the exponential function applied to 
𝑧
𝑖
z 
i
​
 .
∑
𝑗
=
1
𝑛
𝑒
𝑧
𝑗
∑ 
j=1
n
​
 e 
z 
j
​
 
  is the sum of exponentials of all the elements in the input vector.
