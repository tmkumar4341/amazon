import re

exp = "^/w+/d+$"
inp = "siva 3434"

out = re.search(exp,inp)
print(out)