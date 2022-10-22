# Tek kheng - 20210801205
# pengulangan for 
loop_cthArray = ["data1","data2","data3",4,5,6]
def p_for():
    print("For".center(30,"="))
    for i in loop_cthArray:
        print(i)
p_for()

# pengulangan nested for 
def p_for2():
    print("For_2".center(30,"="))
    listCity = ['Kalimantan', 'Sumatra', 'Sulawesi']
    listPlace = ['West', 'North', 'South']
    for city in listCity:
        for place in listPlace:
            print(f"Provinsi: {city} {place}")

p_for2()

# pengulangan while dengan continue,break
def while_b_c():
    print("While Continue,Break".center(30,"="))
    a = 1
    while True:
        a+=1
        print(a)
        
        if a==5:
            continue
        elif a >=10:
            break
while_b_c()

# pengulangan while tak hingga
def while_i():
    print("While infinity".center(20,"="))
    w = 1
    while True:
        w+=1
        print(w)
