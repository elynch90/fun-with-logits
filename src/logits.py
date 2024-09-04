import numpy as np

def softmax(logits):
    """
    Compute the softmax of a list of raw scores (logits).
    
    Parameters:
    logits (list or numpy array): A list or array containing raw scores (logits).

    Returns:
    numpy array: A numpy array containing the probabilities, where each value
                 represents the probability of the corresponding logit.
    """

    # Step 1: Subtract the max logit for numerical stability
    # ---------------------------------------------
    # Numerical stability is critical when applying the softmax function.
    # Exponentiating large values can lead to very large numbers, which may 
    # overflow and result in incorrect computations.
    # To prevent this, we subtract the maximum logit from each logit. This does
    # not affect the relative differences between the logits, but it prevents 
    # overflow.
    max_logit = np.max(logits)
    shifted_logits = logits - max_logit  # Shift the logits for stability

    # Step 2: Compute exponentials of the shifted logits
    # ---------------------------------------------
    # Here, we exponentiate each element of the shifted logits. The exponential
    # function emphasizes larger values by making them even larger, which 
    # ensures that the highest raw score will map to the highest probability.
    exp_logits = np.exp(shifted_logits)

    # Step 3: Sum the exponentials
    # ---------------------------------------------
    # After computing the exponentials, we need to sum them. This sum will be 
    # used as the denominator when normalizing the probabilities.
    sum_exp_logits = np.sum(exp_logits)

    # Step 4: Compute the softmax probabilities
    # ---------------------------------------------
    # The softmax probability for each logit is computed by dividing its 
    # exponential by the sum of all exponentials. This ensures that the output 
    # probabilities will sum to 1.
    probabilities = exp_logits / sum_exp_logits

    return probabilities

# Test the softmax function with a list of logits
logits = [2.0, 1.0, 0.1]

# Print the raw logits (before applying softmax)
print("Logits:", logits)

# Step 5: Apply the softmax function
probabilities = softmax(logits)

# Print the output probabilities (after applying softmax)
print("Softmax Probabilities:", probabilities)

# Step 6: Verify that the probabilities sum to 1 (as required by the softmax)
print("Sum of Probabilities:", np.sum(probabilities))
