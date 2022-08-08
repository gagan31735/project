# RANDOM FUNCTION
import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist = ["jadeja","ashwin","rehana","shami","dhoni","virat"]
mylist1={"jadeja","ashwin","rehana","shami","dhoni","virat"}
print(random.choice(mylist))
random.shuffle(mylist)
print(mylist)