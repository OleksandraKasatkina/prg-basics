speeds = [48, 47, 54, 50, 42, 68, 39, 46]

high_speeds = list(filter(lambda speed: speed > 50, speeds))

print("Recorded values:", *speeds)
print("Speed too high:", *high_speeds)