import random
import math
x = "da"
while(x == "da"):
    print("Un numar aleatoriu este:")

    def urand():
        return random.random()
    print("\nNumar aleatoriu : " + str(urand()))

    print("\nDistributiile simulate sunt:\n")

    def Bernoulli(p):
        if p > urand():
            return 1
        else:
            return 0
    print("Distributia Bernoulli: " + str(Bernoulli(0.5)))

    def Geom1(p):
        k = 0
        u = 1
        while u > p:
            u = urand()
            k = k+1
            return k
    print("Distributia geometrica1: " + str(Geom1(0.5)))

    def Geom2(p):
        u = urand()
        return int(math.log(1-u)/math.log(1-p))+1
    print("Distributia geometrica2: " + str(Geom2(0.5)))

    def SimDiscretU(n):
        u = urand()
        k = int(n*u)
        return k
    print("Distributia unif discreta: " + str(SimDiscretU(5)))

    def SimulExp(theta):
        u = urand()
        x = -theta*math.log(1-u)
        return x
    print("Distributia exponentiala: " + str(SimulExp(-2)))

    def SimulExpN(theta):
        u = urand()
        x = -theta*math.log(u)
        return x
    print("Distributia exponentiala: " + str(SimulExpN(-2)))

    def urandLog():
        u = 0
        while u == 0:
            u = urand()
            return u

    def Simlogist(u):
        x = math.log(u/(1-u))
        return x
    print("Distributia logistica: " + str(Simlogist(urandLog())))

    print("\nRezultatul problemelor este:\n")

    u = random.randint(-2, 2)
    print("Raspuns problema 1: " + str(u))

    X = random.randrange(2, 12, 2)
    Y = X/2+5
    print("Raspuns problema 2: X= " + str(X) + " Y=" + str(Y))

    u1 = random.uniform(-2, 1)
    u2 = random.uniform(-1, 1)
    print("Raspuns problema 3: [-2:1)= " + str(u1) + " (-2;1)=" + str(u2))

    X = urand()
    if X >= 0.1 and X < 1:
        Y = 1/(X*math.log(10))  # (F(x))^(-1)=1/(Y*ln(10))
    else:
        Y = 0
    print("Raspuns problema 4: X=" + str(X) + " Y=" + str(Y))

    X = random.uniform(0, 5)
    if X >= 0.0 and X < 1.0:
        Y = -math.pow(X/5, 1/4)+1
    else:
        Y = 0
    print("Raspuns problema 5: X=" + str(X) + " Y=" + str(Y))

    x = input("Doriti sa mai rulati o data programul?(da/nu) ")
    while(x != "da" and x != "nu"):
        x = input("Va rog sa introduceti da sau nu ")
    print("\n\n\n")
