def hanoi_iterative(num_disks, source, target, auxiliary, moves):
    rods = {source: list(reversed(range(1, num_disks + 1))), auxiliary: [], target: []}
    
    if num_disks % 2 == 0:
        target, auxiliary = auxiliary, target

    for i in range(1, 2 ** num_disks):
        if i % 3 == 1:
            move_disk(rods, source, target, moves)
        elif i % 3 == 2:
            move_disk(rods, source, auxiliary, moves)
        else:
            move_disk(rods, auxiliary, target, moves)

def move_disk(rods, from_rod, to_rod, moves):
    if rods[from_rod] and (not rods[to_rod] or rods[to_rod][-1] > rods[from_rod][-1]):
        disk = rods[from_rod].pop()
        rods[to_rod].append(disk)
        moves.append((from_rod, to_rod))

# Example usage:
moves = []
hanoi_iterative(3, 'A', 'C', 'B', moves)
print("Iterative Moves:", moves)
