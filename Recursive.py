def hanoi_recursive(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append((source, target))
        return
    hanoi_recursive(n-1, source, auxiliary, target, moves)
    moves.append((source, target))
    hanoi_recursive(n-1, auxiliary, target, source, moves)

# Example usage:
moves = []
hanoi_recursive(3, 'A', 'C', 'B', moves)
print("Recursive Moves:", moves)
