def compare(one,two,three):
    if one != two and two != three and three != one:
        return False
    else:
        return True


############## extra credit !   ###################
print(compare(6,5,int('5')))