
################ Category ###############
## list, dictionary, while True, break ##
#########################################


def show_list_logic():
    list1 = [10,20,30,40,50]
    print("\n*** Now List : {}".format(list1))
    print('\n')

    for index, data in enumerate(list1):
        print('▶ index : {0:^10}    ▷ data : {1:^10}'.format(index, data))

def show_list_logic_locNum():
    list1 = [10,20,30,40,50]
    print("\n*** Now List : {}".format(list1))
    print("- index : location number")
    print("- type : list1[ index ]")
    print('\n')

    for index in range(len(list1)):
        print('▶ index : {0:^10}    ▷ data : {1:^10}'.format(index, list1[index]))

def show_list_logic_data():
    list1 = [10,20,30,40,50]
    print("\n*** Now List : {}".format(list1))
    print("- data : list's data")
    print('- type : data')
    print('\n')

    for data in list1 :
        print('▶ index : {0:^10}    ▷ data : {1:^10}'.format(list1.index(data), data))

def show_dic_logic_items():
    dic1 = {'1' : 'Red', '2': 'Orange', '3': 'Yellow', '4': 'Green', '5': 'Blue'}
    print("\n*** Now Dictionary : {}".format(dic1))
    print('\n')

    for key, value in dic1.items():
        print("▶ key : {0:^10}     ▷ value : {1:^10}".format(key, value))

def show_dic_logic_keys():
    dic1 = {'1': 'Red', '2': 'Orange', '3': 'Yellow', '4': 'Green', '5': 'Blue'}
    print("\n*** Now Dictionary : {}".format(dic1))
    print("- key : dic = { ★key : 'Red' }")
    print('- type : dic1[ key ]')
    print('\n')

    for key in dic1.keys():
        print("▶ key : {0:^10}     ▷ value : {1:^10}".format(key, dic1[key]))

def show_dic_logic_values():
    dic1 = {'1': 'Red', '2': 'Orange', '3': 'Yellow', '4': 'Green', '5': 'Blue'}
    print("\n*** Now Dictionary : {}".format(dic1))
    print("- value : dic = { '1' : ★value }")
    print('- type : value ')

    for value in dic1.values():
        print("▶ key : {0:^10}     ▷ value : {1:^10}".format("can't find by value", value))

def show_while_True_logic():
    print("\n-- HELP : This program is running untill you enter the 'break'\n")

    while True:
        enter_data = input("▶ enter the data : ")

        if enter_data == 'break':
            print('-- Finish Program --')
            break
        else :
            print('>>> {}'.format(enter_data))

show_while_True_logic()