# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as 
# rectangles on the screen. We then create an eraser rectangle which,
#  when dragged around the canvas, sets all of the rectangles
#  it is in contact with to white.



import tkinter as tk

# Window setup
root = tk.Tk()
root.title("Canvas Eraser")

# Canvas setup
canvas_width = 400
canvas_height = 400
cell_size = 40  # Size of each blue cell
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Store all blue cells in a dictionary with their coordinates
cells = {}

# Draw grid of blue cells
for row in range(0, canvas_width, cell_size):
    for col in range(0, canvas_height, cell_size):
        cell = canvas.create_rectangle(col, row, col + cell_size, row + cell_size, fill="blue", outline="white")
        cells[cell] = (col, row)  # Store coordinates of each cell

# Create eraser (white rectangle)
eraser_size = 50
eraser = canvas.create_rectangle(0, 0, eraser_size, eraser_size, fill="white", outline="black")

# Function to move eraser with mouse
def move_eraser(event):
    x, y = event.x, event.y
    canvas.coords(eraser, x, y, x + eraser_size, y + eraser_size)  # Move eraser

    # Check which cells eraser is touching and turn them white
    for cell, (col, row) in cells.items():
        if col < x + eraser_size and col + cell_size > x and row < y + eraser_size and row + cell_size > y:
            canvas.itemconfig(cell, fill="white")

# Bind mouse motion to eraser movement
canvas.bind("<B1-Motion>", move_eraser)  # Left-click and drag to erase

root.mainloop()
