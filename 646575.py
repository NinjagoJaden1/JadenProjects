def if_taxicab_number(n):
    cubeRoot = int(n ** (1/3))
    difference = n-(cubeRoot ** 3)
    newCubeRoot = int(difference ** (1/3))
    print(newCubeRoot,cubeRoot,difference,n)
    for i in range(cubeRoot-newCubeRoot):
        if newCubeRoot != 0:
            cubeRoot = cubeRoot-1
            newDifference = n-(cubeRoot ** 3)
            newCubeRoot = newDifference ** (1/3)
        else:
            print(("a", newCubeRoot), ("b", cubeRoot))
print(if_taxicab_number(5000))
