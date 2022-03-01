# Python code to implement Conway's Game Of Life
import argparse
from matplotlib.backend_bases import MouseEvent
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# setting up the values for the grid
ON = 1
OFF = 0
vals = [ON, OFF]


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


def addBlinker(i, j, grid):
    blinker = np.array([[1, 1, 1]])
    grid[i:i+1, j:j+3] = blinker


def addToad(i, j, grid):

    toad = np.array([[1, 1, 1, 0], [0, 1, 1, 1]])
    grid[i:i+2, j:j+4] = toad


def addUnbounded(i, j, grid):
    unbounded = np.array([[1, 1, 1, 0, 1],
                          [1, 0, 0, 0, 0],
                          [0, 0, 0, 1, 1],
                          [0, 1, 1, 0, 1],
                          [1, 0, 1, 0, 1]])
    grid[i:i+5, j:j+5] = unbounded


def addDiehard(i, j, grid):
    diehard = np.array([[0, 0, 0, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 1, 1]])
    grid[i:i+3, j:j+8] = diehard


def addLightspaceship(i, j, grid):
    lightspaceship = np.array([[0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 1],
                               [1, 0, 0, 0, 1],
                               [0, 1, 1, 1, 1]])
    grid[i:i+4, j:j+5] = lightspaceship


def addMediumspaceship(i, j, grid):
    mediumspaceship = np.array([[0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 1],
                               [1, 0, 0, 0, 0, 1],
                               [0, 1, 1, 1, 1, 1]])
    grid[i: i+4, j: j+6] = mediumspaceship


def addHeavypaceship(i, j, grid):
    heavyspaceship = np.array([[0, 0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 0, 1],
                               [1, 0, 0, 0, 0, 0, 1],
                               [0, 1, 1, 1, 1, 1, 1]])
    grid[i: i+4, j: j+7] = heavyspaceship


def addAcorn(i, j, grid):
    acorn = np.array([[0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0],
                      [1, 1, 0, 0, 1, 1, 1]])
    grid[i:i+3, j:j+7] = acorn


def addBlockswitch(i, j, grid):
    blockswitch = np.array([[0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1, 0, 1, 1],
                            [0, 0, 0, 0, 1, 0, 1, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0, 0],
                            [1, 0, 1, 0, 0, 0, 0, 0]])
    grid[i:i+6, j:j+8] = blockswitch


def addPentomino(i, j, grid):
    pentomino = np.array([[0, 1, 1],
                          [1, 1, 0],
                          [0, 1, 0]])
    grid[i:i+3, j:j+3] = pentomino


def addBeacon(i, j, grid):
    beacon = np.array([[0, 0, 1, 1],
                       [0, 0, 1, 1],
                       [1, 1, 0, 0],
                       [1, 1, 0, 0]])
    grid[i:i+4, j:j+4] = beacon


def addClock(i, j, grid):
    clock = np.array([[0, 1, 0, 0],
                      [0, 0, 1, 1],
                      [1, 1, 0, 0],
                      [0, 0, 1, 0]])
    grid[i: i+4, j: j+4] = clock


def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 1],
                      [1, 0, 1],
                      [0, 1, 1]])
    grid[i: i+3, j: j+3] = glider


def addLoaf(i, j, grid):
    loaf = np.array([[0, 1, 1, 0],
                    [1, 0, 0, 1],
                    [0, 1, 0, 1],
                    [0, 0, 1, 0]])
    grid[i: i+4, j: j+4] = loaf


def addBoat(i, j, grid):
    boat = np.array([[0, 1, 0],
                    [1, 0, 1],
                    [0, 1, 1]])
    grid[i: i+3, j: j+3] = boat


def addLongboat(i, j, grid):
    longboat = np.array([[0, 1, 0, 0],
                         [1, 0, 1, 0],
                         [0, 1, 0, 1],
                         [0, 0, 1, 1]])
    grid[i: i+4, j: j+4] = longboat


def addBeehive(i, j, grid):
    beehive = np.array([[0, 1, 0],
                       [1, 0, 1],
                       [1, 0, 1],
                       [0, 1, 0]])
    grid[i: i+4, j: j+3] = beehive


def addPond(i, j, grid):
    pond = np.array([[0, 1, 1, 0],
                     [1, 0, 0, 1],
                     [1, 0, 0, 1],
                     [0, 1, 1, 0]])
    grid[i: i+4, j: j+4] = pond


def addTub(i, j, grid):
    tub = np.array([[0, 1, 0],
                    [1, 0, 1],
                    [0, 1, 0]])
    grid[i: i+3, j: j+3] = tub


def addBarge(i, j, grid):
    barge = np.array([[0, 1, 0, 0],
                     [1, 0, 1, 0],
                     [0, 1, 0, 1],
                     [0, 0, 1, 0]])
    grid[i: i+4, j: j+4] = barge


def addLongbarge(i, j, grid):
    longbarge = np.array([[0, 1, 0, 0, 0],
                          [1, 0, 1, 0, 0],
                          [0, 1, 0, 1, 0],
                          [0, 0, 1, 0, 1],
                          [0, 0, 0, 1, 0]])
    grid[i: i+5, j: j+5] = longbarge


def addShip(i, j, grid):
    ship = np.array([[1, 1, 0],
                    [1, 0, 1],
                    [0, 1, 1]])
    grid[i: i+3, j: j+3] = ship


def addLongship(i, j, grid):
    longship = np.array([[1, 1, 0, 0],
                         [1, 0, 1, 0],
                         [0, 1, 0, 1],
                         [0, 0, 1, 1]])
    grid[i: i+4, j: j+4] = longship


def addNortonpinwheel(i, j, grid):
    pinwheel = np.array([[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                         [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
                         [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1],
                         [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                         [1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                         [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                         ])
    grid[i: i+12, j: j+12] = pinwheel


def addPulsar(i, j, grid):
    pulsar = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                      [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                       ])
    grid[i: i+5, j: j+15] = pulsar


def addHertzosc(i, j, grid):
    hertz = np.array([[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                      [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                      [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
                      [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]])
    grid[i: i+18, j: j+11] = hertz


def addFigeight(i, j, grid):
    figeight = np.array([[1, 1, 1, 0, 0, 0],
                         [1, 1, 1, 0, 0, 0],
                         [1, 1, 1, 0, 0, 0],
                         [0, 0, 0, 1, 1, 1],
                         [0, 0, 0, 1, 1, 1],
                         [0, 0, 0, 1, 1, 1]])
    grid[i: i+6, j: j+6] = figeight


def addPentadecathlon(i, j, grid):
    pentadec = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    grid[i: i+1, j: j+10] = pentadec


def addGosperGliderGun(i, j, grid):
    """adds a Gosper Glider Gun with top left
    cell at (i, j)"""
    gun = np.zeros(11*38).reshape(11, 38)

    gun[5][1] = gun[5][2] = 1
    gun[6][1] = gun[6][2] = 1

    gun[3][13] = gun[3][14] = 1
    gun[4][12] = gun[4][16] = 1
    gun[5][11] = gun[5][17] = 1
    gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 1
    gun[7][11] = gun[7][17] = 1
    gun[8][12] = gun[8][16] = 1
    gun[9][13] = gun[9][14] = 1

    gun[1][25] = 1
    gun[2][23] = gun[2][25] = 1
    gun[3][21] = gun[3][22] = 1
    gun[4][21] = gun[4][22] = 1
    gun[5][21] = gun[5][22] = 1
    gun[6][23] = gun[6][25] = 1
    gun[7][25] = 1

    gun[3][35] = gun[3][36] = 1
    gun[4][35] = gun[4][36] = 1

    grid[i: i+11, j: j+38] = gun


def update(frameNum, img, grid, N):

    # copy grid since we require 8 neighbors
    # for calculation and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):

            # compute 8-neighbor sum
            # using toroidal boundary conditions - x and y wrap around
            # so that the simulaton takes place on a toroidal surface.
            total = int((grid[i, (j-1) % N] + grid[i, (j+1) % N] +
                        grid[(i-1) % N, j] + grid[(i+1) % N, j] +
                        grid[(i-1) % N, (j-1) % N] + grid[(i-1) % N, (j+1) % N] +
                        grid[(i+1) % N, (j-1) % N] + grid[(i+1) % N, (j+1) % N])/1)

            # apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function


def main():

    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    global pa
    parser = argparse.ArgumentParser(
        description="Runs Conway's Game of Life simulation.")

    # add arguments
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--blinker', action='store_true', required=False)
    parser.add_argument('--toad', action='store_true', required=False)
    parser.add_argument('--unbounded', action='store_true', required=False)
    parser.add_argument('--diehard', action='store_true', required=False)
    parser.add_argument('--lightspaceship',
                        action='store_true', required=False)
    parser.add_argument('--mediumspaceship',
                        action='store_true', required=False)
    parser.add_argument('--heavyspaceship',
                        action='store_true', required=False)
    parser.add_argument('--acorn', action='store_true', required=False)
    parser.add_argument(
        '--blockswitch', action='store_true', required=False)
    parser.add_argument('--pentomino', action='store_true', required=False)
    parser.add_argument('--beacon', action='store_true', required=False)
    parser.add_argument('--loaf', action='store_true', required=False)
    parser.add_argument('--boat', action='store_true', required=False)
    parser.add_argument('--beehive', action='store_true', required=False)
    parser.add_argument('--clock', action='store_true', required=False)
    parser.add_argument('--tub', action='store_true', required=False)
    parser.add_argument('--pond', action='store_true', required=False)
    parser.add_argument('--ship', action='store_true', required=False)
    parser.add_argument('--barge', action='store_true', required=False)
    parser.add_argument('--longbarge', action='store_true', required=False)
    parser.add_argument('--longship', action='store_true', required=False)
    parser.add_argument('--longboat', action='store_true', required=False)
    parser.add_argument('--pinwheel', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    parser.add_argument('--hertz', action='store_true', required=False)
    parser.add_argument('--figeight', action='store_true', required=False)
    parser.add_argument('--pentadec', action='store_true', required=False)
    parser.add_argument('--pulsar', action='store_true', required=False)
    args = parser.parse_args()

    # set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # set animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    # declare grid
    grid = np.array([])

    # check if "glider" demo flag is specified
    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)
    elif args.blinker:
        grid = np.zeros(N*N).reshape(N, N)
        addBlinker(10, 10, grid)
    elif args.toad:
        grid = np.zeros(N*N).reshape(N, N)
        addToad(10, 10, grid)
    elif args.unbounded:
        grid = np.zeros(N*N).reshape(N, N)
        addUnbounded(50, 50, grid)
    elif args.diehard:
        grid = np.zeros(N*N).reshape(N, N)
        addDiehard(10, 10, grid)
    elif args.lightspaceship:
        grid = np.zeros(N*N).reshape(N, N)
        addLightspaceship(10, 10, grid)
    elif args.mediumspaceship:
        grid = np.zeros(N*N).reshape(N, N)
        addMediumspaceship(10, 10, grid)
    elif args.heavyspaceship:
        grid = np.zeros(N*N).reshape(N, N)
        addHeavypaceship(10, 10, grid)
    elif args.acorn:
        grid = np.zeros(N*N).reshape(N, N)
        addAcorn(50, 50, grid)
    elif args.blockswitch:
        grid = np.zeros(N*N).reshape(N, N)
        addBlockswitch(50, 50, grid)
    elif args.pentomino:
        grid = np.zeros(N*N).reshape(N, N)
        addPentomino(50, 50, grid)
    elif args.beacon:
        grid = np.zeros(N*N).reshape(N, N)
        addBeacon(10, 10, grid)
    elif args.loaf:
        grid = np.zeros(N*N).reshape(N, N)
        addLoaf(10, 10, grid)
    elif args.boat:
        grid = np.zeros(N*N).reshape(N, N)
        addBoat(10, 10, grid)
    elif args.beehive:
        grid = np.zeros(N*N).reshape(N, N)
        addBeehive(10, 10, grid)
    elif args.tub:
        grid = np.zeros(N*N).reshape(N, N)
        addTub(10, 10, grid)
    elif args.pond:
        grid = np.zeros(N*N).reshape(N, N)
        addPond(10, 10, grid)
    elif args.barge:
        grid = np.zeros(N*N).reshape(N, N)
        addBarge(10, 10, grid)
    elif args.longbarge:
        grid = np.zeros(N*N).reshape(N, N)
        addLongbarge(10, 10, grid)
    elif args.ship:
        grid = np.zeros(N*N).reshape(N, N)
        addShip(10, 10, grid)
    elif args.clock:
        grid = np.zeros(N*N).reshape(N, N)
        addClock(10, 10, grid)
    elif args.longship:
        grid = np.zeros(N*N).reshape(N, N)
        addLongship(10, 10, grid)
    elif args.longboat:
        grid = np.zeros(N*N).reshape(N, N)
        addLongboat(10, 10, grid)
    elif args.pinwheel:
        grid = np.zeros(N*N).reshape(N, N)
        addNortonpinwheel(32, 32, grid)
    elif args.pulsar:
        grid = np.zeros(N*N).reshape(N, N)
        addPulsar(32, 32, grid)
    elif args.hertz:
        grid = np.zeros(N*N).reshape(N, N)
        addHertzosc(32, 32, grid)
    elif args.figeight:
        grid = np.zeros(N*N).reshape(N, N)
        addFigeight(32, 32, grid)
    elif args.pentadec:
        grid = np.zeros(N*N).reshape(N, N)
        addPentadecathlon(32, 32, grid)
    elif args.gosper:
        grid = np.zeros(N*N).reshape(N, N)
        addGosperGliderGun(10, 10, grid)

    else:  # populate grid with random on/off -
        # more off than on
        grid = randomGrid(N)

    # set up animation
    # fig, ax = plt.subplots()
    # img = ax.imshow(grid, interpolation='nearest')
    # ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
    #                               frames=10,
    #                               interval=updateInterval,
    #                               save_count=50)

    class PauseAnimation:

        def __init__(self):
            fig, ax = plt.subplots()
            img = ax.imshow(grid, interpolation='nearest')
            self.paused = False
            self.animation = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                                     frames=10,
                                                     interval=updateInterval,
                                                     save_count=50)
            fig.canvas.mpl_connect('button_press_event', self.toggle_pause)
            if args.movfile:
                self.animation.save(args.movfile, fps=30, extra_args=[
                                    '-vcodec', 'libx264'])

        def toggle_pause(self, *args, **kwargs):
            if self.paused:
                self.animation.resume()
                self.paused = False
            else:
                self.animation.pause()
                self.paused = not self.paused
                print("else")

        def update(self, i):
            self.n0 += i / 100 % 5
            self.p.set_ydata(self.n0 % 20)
            return (self.p,)
    # # of frames?
    # set output file
    # if args.movfile:
    #         ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264']
    if __name__ == '__main__':
        pa = PauseAnimation()
    plt.show()


# call main
if __name__ == '__main__':
    main()
