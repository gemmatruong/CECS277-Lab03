import map

class Map:
    """The map of the dungeon maze"""
    _instance = None
    _initilized = False
    _map = []
    _revealed = []

    def __new__(cls):
        # Constructs the map as a singleton
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        # Load the map from the file if the map has not initialized
        if not Map._initilized:
            try:
                with open("map.txt", "r") as map_file:
                    for line in map_file:
                        if line.strip():
                            Map._map.append(list(line.strip()))
            except FileNotFoundError:
                raise FileNotFoundError("Map file not found. Make sure 'map.txt' exists.")
            
            Map._revealed = [[False for _ in row] for row in Map._map]
            Map._initilized = True
    
    def __getitem__(self, row):
        # overload the number of rows on the map
        return Map._map[row]
    
    def __len__(self):
        # return the number of rows on the map
        return len(Map._map)
    
    def show_map(self, loc):
        # String representation of the map with the location of the hero
        output = ""

        for i in range(len(Map._map)):
            for j in range(len(Map._map[i])):
                if [i, j] == loc:
                    output += "* "
                elif Map._revealed[i][j]:
                    output += Map._map[i][j] + " "
                else:
                    output += "x "
            output += "\n"
        
        return output

    def reveal(self, loc):
        # reveal the location on the map
        row, col = loc
        Map._revealed[row][col] = True

    def remove_at_loc(self, loc):
        # Remove the character on the map and replace it with an 'n'
        row, col = loc
        Map._map[row][col] = "n"