# Recursive Python function to solve tower of hanoi


# def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
#     if n == 0:
#         return
#     TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
#     print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
#     TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# # Driver code
# N = 3

# # A, C, B are the name of rods
# TowerOfHanoi(N, 'A', 'C', 'B')

# OR

def tower_of_hanoi(n, source, auxiliary, target):
    """
    Solves the Tower of Hanoi problem and prints the steps.

    Parameters:
    n (int): Number of disks
    source (str): The name of the source rod
    auxiliary (str): The name of the auxiliary rod
    target (str): The name of the target rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)

# Example usage:
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'B', 'C')
