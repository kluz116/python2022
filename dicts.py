student = {'Name':'Allan Musembya','age':45,'std_class':'S5'}

for key, value in student.items():
    print('{} = {}'.format(key,value))

student['std_class']='s.3'

print(student['std_class'])