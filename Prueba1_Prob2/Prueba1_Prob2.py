import math

entrada = [float(x) for x in input().split()]

areaSolar = entrada[0]**2
areaBebedero = entrada[1]**2
areaCharca = (math.pi * (entrada[2]/2)**2)

print(areaSolar-(areaBebedero + areaCharca))
