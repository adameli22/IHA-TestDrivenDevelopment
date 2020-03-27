def add(string):
    if string == "":
        return 0

    else:
        # sum_num = 0
        string_lis = string.split(',')
        int_string = [int(x) for x in string_lis]
        return sum(int_string)
         

                


def test_inputs():
    assert add("") == 0
    assert add("1") == 1
    assert add("1,2") == 3
    assert add("1,2,3,4,5") == 15
    assert add("10,2,5,22,1,1") == 41
    

