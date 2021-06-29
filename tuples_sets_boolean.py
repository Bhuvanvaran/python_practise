#Tuples are like list but it is immutable
#Tuplse syntax (1,2,3)
#List Syntac [1,2,3]
#Dictionary syntax {1,2,3}

def tuples():
    my_tuples = (1,2,3)
    print("Getting tuple value {}".format(my_tuples[1]))
def alter_tuple():
    my_tuple = (1,2,3)
    print("Trying to alter tuples")
    my_tuple[0]="New"
    #it will fail because tuples are immutable

#Sets
#Sets will not allow any duplicate value
def my_set():
    my_set = set()
    my_set.add(1)
    my_set.add(2)
    my_set.add(3)
    my_set.add(3)
    print("Accessing my set {}".format(my_set))
def add_list_to_set():
    my_list = [1,2,3,4,5,5,5,5,5,56,6,6,6]
    my_set = set([1,2,3,4,4])
    print(my_set)

#Boolean should be either (T)rue or (F)alse


if __name__ == '__main__':
    tuples()
    #alter_tuple()
    my_set()
    add_list_to_set()

