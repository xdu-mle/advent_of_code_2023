import math

res = 0

with open('input.txt', 'r', encoding = 'utf-8') as f:
    total_time = 0
    for c in f.readline().replace('Time:', '').strip():
        if c.isdigit():
            total_time = total_time*10+int(c)
    total_distance = 0
    for c in f.readline().replace('Distance:', '').strip():
        if c.isdigit():
            total_distance = total_distance*10+int(c)
    a = math.sqrt(total_time**2-4*total_distance)    
    res = int(math.floor((total_time+a)/2))-int(math.floor((total_time-a)/2))
print(res)