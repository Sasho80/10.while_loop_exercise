target_steps = 10000

total_steps = 0
last_steps = 0
diff = 0

while total_steps < target_steps:
    command = input()
    if command == "Going home":
        last_steps = int(input())
        total_steps += last_steps
        break
    steps = int(command)
    total_steps += steps

diff = abs(target_steps - total_steps)

if total_steps >= target_steps:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
