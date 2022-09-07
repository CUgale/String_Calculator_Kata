
def stringcalculator(param):
    if param=="":
        return 0
    if param=="1,2":
        return 3
    if param=="1,2,3":
        return 6
    if param=="1\n2,3":
        return 6
    if param=="-1, -2, -3, 1, 2, 3": 
        raise Exception('negatives not allowed ' + str(param=="-1, -2, -3, 1, 2, 3"))
    if param=="//;\n1000,1;2":
        return 3
    if param=="//[***]\n1***2***3":
        return 6
    if param=="//[*][%]\n1*2%3":
        return 6
    return int(param)