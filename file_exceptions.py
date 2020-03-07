
filename = 'ss.txt'

# with open(filename) as f_obj:
#     contents = f_obj.read()

# print(contents)

# with open(filename) as f_obj:
#     for line in f_obj:
#         print(line.rstrip())

# with open(filename) as f_obj:
#     lines = f_obj.readlines()

# for line in lines:
#     print(line.rstrip())

with open(filename, 'w') as f:
    f.write("Mey Purnama Sari\n")
    f.write("Universitas Airlangga Surabaya\n")
    f.write("You're my first sunshine")