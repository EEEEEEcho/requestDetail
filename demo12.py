import os
print(os.getcwd())
if not os.path.exists('test'):
    os.mkdir('test')

with open(os.getcwd() + "/test/" + 'test1.txt','w') as f:
    f.write("Hello world")

