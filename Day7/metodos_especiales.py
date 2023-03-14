class CD:
    def __init__(self, title, artist, tracks):
        self.title = title
        self.artist = artist
        self.tracks = tracks
    
    def __str__(self):
        return f"Album: {self.title} by {self.artist}"
    
    def __len__(self):
        return self.tracks
    
    def __del__(self):
        print("CD Deleted")

cd1 = CD("The Dark Side of the Moon", "Pink Floyd", 10)
print(cd1)
print(len(cd1))
del cd1
print(cd1)