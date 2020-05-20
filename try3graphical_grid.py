import numpy as np
import pyglet
import try3numerical_grid as ng
import time

window = pyglet.window.Window(600,600, resizable=False)
cell_size = 100
rows = window.get_size()[0]//cell_size
cols = window.get_size()[1]//cell_size
position = np.array([0,0,cell_size, 0, 0, cell_size, cell_size, cell_size])
# original_position = np.copy(position)

batch = pyglet.graphics.Batch()

grid = ng.first_numerical_grid(rows, cols)

def draw_grid(grid):
    vertex_list = pyglet.graphics.vertex_list(1024, 'v3f', 'c4B', 't2f', 'n3f')
    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == 1:
                vertex_list = batch.add_indexed(4, pyglet.gl.GL_TRIANGLES, None,
                                        [0,1,2,1,2,3],
                                        ('v2i', position))
                print(position)
            position[0::2] += cell_size
        position[0::2] = position[0::2] - cols*cell_size
        position[1::2] += cell_size
    position[1::2] = position[1::2] - rows*cell_size


draw_grid(grid)


@window.event
def on_draw():
    window.clear()
    # t1 = time.time()
    batch.draw()
    # print("draw", time.time() - t1)


@window.event
def update(dt):
    global grid
    draw_grid(grid)
    zeros_grid = ng.set_bc(grid)
    grid = ng.main_function(grid, zeros_grid)

pyglet.clock.schedule_interval(update, 1)
pyglet.app.run()

