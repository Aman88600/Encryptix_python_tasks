golbal_var = 10

def hello():
    # global local_var
    local_var = 20
    print(local_var)

print(golbal_var)
hello()
# print(local_var)