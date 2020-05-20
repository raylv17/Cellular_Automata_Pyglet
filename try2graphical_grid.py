import numpy as np
import pyglet
import try2numerical_grid as ng
import time

window = pyglet.window.Window(600,600, resizable=False)
cell_size = 3
rows = window.get_size()[0]//cell_size
cols = window.get_size()[1]//cell_size
# position = np.array([0,0,cell_size, 0, 0, cell_size, cell_size, cell_size])
# original_position = np.copy(position)

def draw_square(pos):
    pos = tuple(pos)
    pyglet.graphics.draw_indexed(4, pyglet.graphics.gl.GL_TRIANGLES,
                                 [0,1,2,1,2,3],
                                 ('v2i', pos))

times_called = 0
def draw_grid():
    pos = np.array([0, 0, cell_size, 0, 0, cell_size, cell_size, cell_size])

    global times_called
    times_called += 1
    count_alive = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == 1:
                draw_square(pos)
                count_alive += 1
            pos[0::2] += cell_size
        pos[0::2] = -cols*cell_size + pos[0::2]
        pos[1::2] += cell_size

    print(times_called, count_alive)

print(rows, cols)
grid = ng.first_numerical_grid(rows, cols)
@window.event
def on_draw():
    window.clear()
    # t1 = time.time()
    draw_grid()
    # print("draw", time.time() - t1)


@window.event
def update(dt):
    global grid, i
    zeros_grid = ng.set_bc(grid)
    grid = ng.main_function(grid, zeros_grid)



pyglet.clock.schedule_interval(update, 1/30)
pyglet.app.run()

