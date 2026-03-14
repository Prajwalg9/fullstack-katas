S="hfuwHGS3727^&@(({{]f/dhhcushdusuzahkukwhauhUHUKHUKDHHUHDHWUIH^^@^^@^@%%#**!~nhfjjd***3jeuh"
List=['Z', '2', 'R', '%', 'x', ',', '^', 'c', 'j', '\\', 'R', 'm', '_', 's', '6', 's', 'Z', '+', 'q', ';', 'A', '8', '}', 'Y', 'h', 'H', 'y', ']', '.', '#', ',', 'l', '@', ')', '%', ':', ')', '0', 'K', '2', '}', 'w', 'o', 'w', 'g', ':', '"', 'G', 'k', 'L']
hashdict={}
frequency_map={}

for char in S:
    if char in hashdict:
        hashdict[char] += 1
    else:
        hashdict[char] = 1

for char in List:
    if char in hashdict:
        frequency_map[char] = hashdict[char]
    else:
        frequency_map[char] = 0

print(frequency_map)