import math

print("LOOK TO YOUR LEFT AND ENTER THE DIFF. EQ.")
print("LOOK FOR THE # AND CAPS AT LINE 15")
print()

xi = float(input("initial x: "))               #initial x
yi = float(input("initial y: "))               #initial y
step = float(input("how big is your step: "))  #delta x
n = float(input("how many steps: "))           #subdivisions

def yprime(x, y):       #function for finding derivative

    #ENTER YOUR DIFF EQ HERE, LOOK UP PYTHON SYNTAX FOR MATH
    
    dy_dx = x+(y)    # <--- LOOK HERE
    
    #multiplication *
    #division /
    #addition +
    #subtraction -
    # y^2  would be  y**2
    # x^3  would be  x**3 and so on
    # sqrt(x) would be math.sqrt(x)
    
    return (dy_dx)

def euler(xi, yi, step):    #eulers logic
    xi = float(xi)
    yi = float(yi)
    step = float(step)
    dy = float(yprime(xi, yi))
    deltay = step*dy
    xf = xi + step
    yf = yi + deltay
    return (xf, yf, dy, deltay)

def steps(x, y, step, n):     #make the steps happens
    counter = 0
    xlist = []
    ylist = []
    dylist = []
    change = []
    while (counter<n):
        eulernum = euler(x, y, step)
        xp=round(eulernum[0], 5)
        yp=round(eulernum[1], 5)
        dyp=round(eulernum[2], 5)
        deltap=round(eulernum[3], 5)
        x = str(round(eulernum[0], 5))
        y = str(round(eulernum[1], 5))
        dy = str(round(eulernum[2], 5))
        delta = str(round(eulernum[3], 5))
        xlist.append(x)
        ylist.append(y)
        dylist.append(dy)
        change.append(delta)
        counter += 1
    return (xlist, ylist, dylist, change)

def printer(list):
    for i in range(0, (len(list)) ):
        print(list[i].rjust(8), " | ", end='')
    print("")

def program(xi, yi, step, n):
  package = steps(xi, yi, step, n)
  xlist = ["x"] + package[0]
  ylist = ["y"] + package[1]
  dylist = ["dy/dx"] + package[2]
  deltalist = ["deltay"] + package[3]
  print()
  printer(xlist)
  printer(dylist)
  printer(deltalist)
  printer(ylist)
  print()
  initdy=round(yprime(xi, yi), 5)
  print("y = " + str(initdy) + "( x - " + str(xi) + ") + " + str(yi))
  
  for i in range(1, (len(dylist)-1)):
    nextdy=dylist[i+1]
    print("y = "+ str(nextdy) + "( x - " + xlist[i]+" ) + "+ylist[i])

program(xi, yi, step, n)
