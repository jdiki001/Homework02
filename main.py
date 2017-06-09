def integrate_HW2(f,a,b,N):
    """
    Integrate f from a to b using Simpson's rule with N steps
    """
    
    # Your code goes here!
    sample = deltax/2.0
    total = 0.0
    while(sample<1):
        total = total + f(sample)*deltax
        sample = sample + deltax

    return total
