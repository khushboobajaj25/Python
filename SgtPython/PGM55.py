result = []
def  flatten(l) :
    for element in l :
        if type(element) is list:

            flatten(element)
        else:

            result.append(element)

input_list = [[[[1, 2, ['success'], [['perseverance'], 4, 5, [],[],[[[[['hardwork']]]]]]]]]]
flatten(input_list)
print(result)
