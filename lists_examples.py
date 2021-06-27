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
def concatenate_lists():
    list_a=[1,2,3]
    list_b=[4,5,6]
    list_c=list_a+list_b
    print("Getting index from list c {}".format(list_c[3:]))

if __name__ == '__main__':
    simple_lists()
    slicing_and_indexing(0,1)
    concatenate_lists()

