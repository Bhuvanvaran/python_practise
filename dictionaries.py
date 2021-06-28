#Dictionaries are uncoded mapping for storing objects
#List stores objects in sequence
#While Dictionaries store object as key-value pair

def dictionary_example(value):
    my_dict = {'apple': 'fruit','cat':'animal','mango':'fruit', 'dog':'animal'}
    print('Retrieve from dict family {}'.format(my_dict[value]))
# Yes we can have nested dictionaries
def nested_dictionaries():
    my_dict = {'key1':'value1','nest_dict':{'inside_dict':'nested_value'}}
    print(my_dict['nest_dict']['inside_dict'])
def list_dict():
    my_dict = {'dict1':'value1','lst':['1','2','3']}
    print(my_dict['lst'].index('1'))

if __name__ == '__main__':
    dictionary_example('cat')
    nested_dictionaries()
    list_dict()
    common_methods()

