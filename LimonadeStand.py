from typing import List

def lemonade(bills: List[int]):
    """
    At a lemonade stand, each lemonade costs $5. 
    Customers pay with $5, $10, or $20 bills, and we must provide correct change. 
    This function return True if we can give correct change to all customers in the queue, otherwise return False.
    """
    change = [] 
    print(bills)
    for bill in bills:
        print(f"Current bill: {bill}, Current change: {change}")
        if bill == 5:
            change.append(5)
        elif bill == 10:
            if 5 in change:
                change.remove(5)
                change.append(10)
            else:
                return False
        elif bill == 20:
            if 5 in change:
                change.remove(5)
                if 10 in change:
                    change.remove(10)
                elif len(change) >= 2 and 5 in change:
                    change.remove(5)
                    change.remove(5)
                else:
                    return False
            else:
                return False
    print(f"END: current change: {change}")
    return True


print(lemonade([5, 5, 5, 10, 20]))  # Output: True
print(lemonade([5, 5, 10, 10, 20]))  # Output: False
print(lemonade([10, 10]))  # Output: False
print(lemonade([5, 5, 10]))  # Output: True
