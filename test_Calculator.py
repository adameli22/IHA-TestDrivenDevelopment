def add(num):
    if num == "":
        return 0

    elif len(num) == 1:
        return int(num)


    else:
        sum_num = 0
        for i in num:
            if i.isdigit():
                i = int(i)
                sum_num += i
        return sum_num
                




# print(add(""))
# print(add("1"))
# print(add("1,2"))

def test_inputs():
    assert add("") == 0
    assert add("1") == 1
    assert add("1,2") == 3