def add(string):
    if string == "":
        return 0

    else:
        minus_lis = []
        string_lis = string.split(',')
        int_string = [int(x) for x in string_lis]
        for i in int_string:
            if i > 1000:
                int_string.remove(i)

            if i < 0:
                minus_lis.append(i)

        if len(minus_lis) == 0:
            return sum(int_string)
        
        else:
            return "Negatives not allowed:"+str(minus_lis)[1:-1]

         

def test_inputs():
    assert add("") == 0
    assert add("1") == 1
    assert add("1,2") == 3
    assert add("1,2,3,4,5") == 15
    assert add("10,2,5,22,1,1") == 41
    assert add("1001,2") == 2
    assert add("-1,2") ==  "Negatives not allowed:-1"
    assert add("2,-4,3,-5") ==  "Negatives not allowed:-4, -5"



    

