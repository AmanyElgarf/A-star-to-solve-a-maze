import pickle
from Maze import Maze

size = 101
libOfMazes = Maze().generate_fifty_gridworlds(size)


mazeDataLibrary = []
for maze in libOfMazes:
    data = []
    for x in range(0, size):
        row = []
        for y in range(0, size):
            if maze[x][y].cost != 1:
                row.append(1)
            else:
                row.append(0)
        print(row)
        data.append(row)
    print()
    mazeDataLibrary.append(data)

f = open("SavedMazes", "wb")
pickle.dump(mazeDataLibrary, f)



