def div_by(n,d) :
    """ 
    n and d are positive integers
    Returns True if d divides n evenly, returns False otherwise
    """
    return n % d == 0

print(div_by(int(input("chose n : ")), int(input("chose d : "))))