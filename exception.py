class PathNotFoundException(Exception):
    def __init__(self):
        super().__init__("A path does not exist between the specified start and end points")