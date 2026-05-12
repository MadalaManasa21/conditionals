# Heart (Love Symbol) Pattern

n = 6

# Upper part of heart
for i in range(n // 2, n + 1, 2):
    # Left half-circle
    for j in range(1, n - i, 2):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")

    # Space between two half-circles
    for j in range(1, n - i + 1):
        print(" ", end="")

    # Right half-circle
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Lower part of heart
for i in range(n, 0, -1):
    for j in range(i, n):
        print(" ", end="")
    for j in range(1, (i * 2)):
        print("*", end="")
    print()