def split_same_sum(multiset: list) -> bool:
    if sum(multiset)%2 == 0:
        target = sum(multiset)/2
        
        return True
    else:
        return False
    
if __name__ == '__main__':
    assert split_same_sum((15, 5, 20, 10, 35, 15, 10)) == True, '[15, 5, 20, 10, 35, 15, 10] could split it up into [15, 5, 10, 15, 10] and [20, 35]'
    assert split_same_sum((15, 5, 20, 10, 35)) == False, "(15, 5, 20, 10, 35) cannot split it up"
    print("All test cases passed!")

