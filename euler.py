import math

dydx = input("Differential equation:")
xi = float(input("Initial x: "))         #initial x
yi = float(input("Initial y: "))         #initial y
step = float(input("Step size: "))       #delta x
n = float(input("Steps: "))              #subdivisions

def yprime(x, y):           #function for finding derivative
    return(eval(dydx))

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
