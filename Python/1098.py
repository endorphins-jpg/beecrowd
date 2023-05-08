# copiei de allysson

for i in range (0,11):
    for j in range(1,4):
        x= i/5
        z= j+(i/5)
        if i==0 or i==5 or i== 10:
            x = int(x)
            z = int(z)

        print("I={} J={}".format(x,z))