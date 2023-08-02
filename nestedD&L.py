# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] ='Andres'
print(sports_directory)

z[0]['y'] =30
print(z)





#2 Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for i in range(0,len(students),1):
        print(students[i])
iterateDictionary(students)





#3 Get Values from a List of Dictionaries

def iterateDictionary2(key_name,some_list):
    for i in range(0,len(some_list),1):
        result=(some_list[i][key_name])
        print(result)

iterateDictionary2('first_name',students)





#4 Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    print((len('locations'))-1 , "Locations")
    print(dojo['locations'])
    print((len('instructors'))-1 , "Instrcuctors")
    print(dojo['instructors'])
printInfo(dojo)





