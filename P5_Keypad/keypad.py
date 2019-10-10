'''Keypad class, with functions'''


class Keypad:

    print('test changing one file')
    print("Testing the revert function")
    print("Testing the revert function2")


d = {1: "hei", 2: "på", 3: "deg", 4: "din", 5: ["sei", "ja", "jaaaaa"]}

for k, v in d.items():
    if type(v) == list:
        for i in v:
            print(i)
    print("key: ", k, "\tValue: ", v)
