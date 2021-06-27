# Points to remember
#Lists are ordered sequence tha can hold a variety of object types
#They use brackets and commas to seprate objecs in the list EXAMPLE: [1,2,3,4,5]
#As we saw in string Lists also support slicing and indexing\
def simple_lists():
    my_list_1 = [1,2,3,4,5] #same data type
    my_list_2= ['Hello',1,3.14] #different data type
    #lenght of the list
    print("The Length of the same datatype list is: {}".format(len(my_list_1)))
    print("The Length of the same different type list is: {}".format(len(my_list_2)))

def slicing_and_indexing(index,slicing):
    my_list=['one','two','three']
    print(my_list[index])
    print(my_list[slicing:])
#Concatenate 2 lists and produce a new lists
def concatenate_lists():
    list_a=[1,2,3]
    list_b=[4,5,6]
    list_c=list_a+list_b
    print("Getting index from list c {}".format(list_c[3:]))
#Append new value in given list
def append_list(value):
    my_list = ['Hello',100,2.1]
    print("Length before appending {}".format(len(my_list)))
    print("Appending new value to the list {}".format(value))
    my_list.append(value)
    print("Length after appending {}".format(my_list.__hash__))
    print("Printing new list: {}".format(len(my_list)))
#popping is nothing put removing the value from list consider popping collections of balloons from a child
#Default pop is last value
#pop can be done on specific value by passing index as a param
def pop_list(value):
    my_list = ['Hello', 100, 2.1]
    print("Length before appending {}".format(len(my_list)))
    print("Appending new value to the list {}".format(value))
    my_list.append(value)
    print("Length after appending {}".format(my_list.__hash__))
    print("Printing new list: {}".format(my_list))
    my_list.pop()
    print("After popping:{}".format(my_list))

def common_methods():
    my_list = [1,2,3,5,6,6,9,8,21]
    my_list.sort()
    print("Sorted list: {}".format(my_list))
    my_list.reverse()
    print("Reverse List: {}".format(my_list))
if __name__ == '__main__':
    simple_lists()
    slicing_and_indexing(0,1)
    concatenate_lists()
    append_list(200)
    pop_list(200)
    common_methods()


