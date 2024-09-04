# fun-with-logits
A fun time working with logits, because who doesn't love logits?


## Objective
The goal of this exercise is to understand the softmax function, implement it in Python, and apply it to a set of raw scores (also called logits). Softmax is commonly used in multi-class classification problems to convert raw scores into probabilities.

## Softmax Function
Softmax takes a vector of real numbers and normalizes it into a probability distribution, where the sum of all probabilities is 1. Mathematically, for an input vector 

is defined as:

## softmax

 
 
​
 
where:


​
is the exponential function applied to 

is the sum of exponentials of all the elements in the input vector.
