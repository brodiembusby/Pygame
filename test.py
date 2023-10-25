def isValid(s: str) -> bool:
    size = len(s)
    # What geos in last must come out first
    # If it is not even then it wont be True
    if size % 2 != 0:
        return False
    for i, j in zip(range(0,size),range(size -1, 0,-1)):
        # Check first charchter to next simplist
        if s[i] == "(" and s[i+1] == ")":
            return True
        #Check first against 
        if s[i] == "(" and s[j] == ")":
            return True
        if s[i] == "[" and s[i+1] == "]":
            return True
        #Check first against 
        if s[i] == "[" and s[j] == "]":
            return True
        if s[i] == "{" and s[i+1] == "}":
            return True
        #Check first against 
        if s[i] == "{" and s[j] == "}":
            return True

    return False

isValid("(){}}{")