import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

# Recursive algorithm for the Tower of Hanoi
def hanoi_recursive(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append((source, target))
    else:
        hanoi_recursive(n - 1, source, auxiliary, target, moves)
        moves.append((source, target))
        hanoi_recursive(n - 1, auxiliary, target, source, moves)

# New implementation of the iterative algorithm for the Tower of Hanoi
def hanoi_iterative(num_disks, source, target, auxiliary, moves):
    rods = {source: list(reversed(range(1, num_disks + 1))), auxiliary: [], target: []}
    smallest_move_rod = source
    even_num_disks = num_disks % 2 == 0

    for _ in range(1, 2 ** num_disks):
        # Move smallest disk
        next_rod = get_next_rod(smallest_move_rod, even_num_disks)
        move_disk(rods, smallest_move_rod, next_rod, moves)
        smallest_move_rod = next_rod

        # Make only one other legal move
        if check_end_condition(rods, target, num_disks):
            break
        make_legal_move(rods, moves, smallest_move_rod)

def get_next_rod(current_rod, even_num_disks):
    order = ['A', 'B', 'C'] if even_num_disks else ['A', 'C', 'B']
    return order[(order.index(current_rod) + 1) % 3]

def move_disk(rods, from_rod, to_rod, moves):
    disk = rods[from_rod].pop()
    rods[to_rod].append(disk)
    moves.append((from_rod, to_rod))

def make_legal_move(rods, moves, exclude_rod):
    possible_moves = [(rod, other) for rod in rods for other in rods if rod != other and rod != exclude_rod]
    for from_rod, to_rod in possible_moves:
        if rods[from_rod] and (not rods[to_rod] or rods[to_rod][-1] > rods[from_rod][-1]):
            move_disk(rods, from_rod, to_rod, moves)
            return

def check_end_condition(rods, target, num_disks):
    return len(rods[target]) == num_disks

# GUI class for the Tower of Hanoi
class TowerOfHanoiGUI:
    def __init__(self, root):
        self.master = root
        self.master.title("Tower of Hanoi")

        self.num_disks = 3
        self.move_speed = 500
        self.moves = []
        self.animation_in_progress = False

        self.canvas = tk.Canvas(self.master, width=600, height=400, bg='white')
        self.canvas.pack()

        self.setup_game()
        self.start_button_recursive = ttk.Button(self.master, text="Start Recursive Solution", command=lambda: self.solve('recursive'))
        self.start_button_recursive.pack(side=tk.LEFT, padx=(50, 20))

        self.start_button_iterative = ttk.Button(self.master, text="Start Iterative Solution", command=lambda: self.solve('iterative'))
        self.start_button_iterative.pack(side=tk.RIGHT, padx=(20, 50))

        self.move_count_label = tk.Label(self.master, text="Moves: 0")
        self.move_count_label.pack()

        self.move_count = 0

    def setup_game(self):
        self.canvas.delete("all")
        self.rods = {'A': 150, 'B': 300, 'C': 450}
        self.rod_coords = {}
        self.disk_coords = {}
        for rod, x_center in self.rods.items():
            self.rod_coords[rod] = self.canvas.create_rectangle(x_center - 5, 50, x_center + 5, 350, fill='grey', outline='black')
            self.disk_coords[rod] = []

        self.draw_disks(self.num_disks)

    def draw_disks(self, num_disks):
        self.disk_labels = []
        for i in range(num_disks):
            disk_width = (num_disks - i) * 20 + 20
            x1 = self.rods['A'] - disk_width // 2
            x2 = self.rods['A'] + disk_width // 2
            y1 = 350 - (i + 1) * 20
            y2 = 350 - i * 20
            self.disk_labels.append(self.canvas.create_rectangle(x1, y1, x2, y2, fill='gold', outline='black'))
            self.disk_coords['A'].append((i, self.disk_labels[i]))

    def animate_move(self, move_from, move_to):
        if self.moves:
            disk_index, disk_label = self.disk_coords[move_from][-1]
            self.disk_coords[move_from].pop()
            x0, y0, x1, y1 = self.canvas.coords(disk_label)
            drop_height = 350 - (len(self.disk_coords[move_to]) + 1) * 20
            self.canvas.move(disk_label, self.rods[move_to] - (x0 + x1) / 2, drop_height - y0)
            self.disk_coords[move_to].append((disk_index, disk_label))
            self.moves.pop(0)
            self.move_count += 1
            self.update_move_count()
            self.master.after(self.move_speed, self.continue_animation) 

    def continue_animation(self):
        if self.moves:
            move = self.moves[0]
            self.animate_move(*move)

    def update_move_count(self):
        self.move_count_label.config(text=f"Moves: {self.move_count}")

    def solve(self, method):
        if self.animation_in_progress:
            messagebox.showwarning("Patience!", "The animation is already in progress.")
            return

        self.num_disks = simpledialog.askinteger("Disks", "Enter number of disks to solve for:", minvalue=1, maxvalue=8)
        if self.num_disks is None:
            return
        
        self.setup_game()
        self.moves.clear()
        if method == 'recursive':
            hanoi_recursive(self.num_disks, 'A', 'C', 'B', self.moves)
        else:
            hanoi_iterative(self.num_disks, 'A', 'C', 'B', self.moves)
        self.move_count_label.config(text="Moves: 0")
        self.animation_in_progress = True
        self.move_count = 0  # Reset move count
        self.update_move_count()
        self.continue_animation()

# Main application setup
if __name__ == "__main__":
    root = tk.Tk()
    TowerOfHanoiGUI(root)
    root.mainloop()
