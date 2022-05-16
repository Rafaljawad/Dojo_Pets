from ninga import Ninga
from pet import Pet
from pet import Dog
pet1=Pet("Lily","cat","Sit. Sit on the floor with a clicker in one hand","Meow")
bob=Ninga("Bob","Dani"," Salmon Treat"," Pizza",pet1)
pet2=Dog("nina","dog","sit .sit","woof")
rafal=Ninga("rafal","jawad"," Salmon Treat"," Pizza",pet2)

print(bob.feed())
print(bob.walk())
print(bob.bathe())

#testing the bonus section
print(pet2.name)
print(pet2.sound)
print(rafal.feed())
print(rafal.walk())
print(rafal.bathe())