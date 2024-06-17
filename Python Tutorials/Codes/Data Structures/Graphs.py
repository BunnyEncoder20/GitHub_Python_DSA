class Graph():
    """docstring for Graph Class."""

    def __init__(self,edges):
        self.edges = edges
        self.graphDict = {}

        for start,end in self.edges:
            if(start in self.graphDict):
                self.graphDict[start].append(end)
            else : 
                self.graphDict[start] = [end]
        
        print("Graph :")
        print(self.graphDict)
    
    def getPaths(self, start, end, path=[]): 
        paths = []



if __name__ == "__main__":
    routes = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Toronto")
    ]

    graph = Graph(routes)

    start = 'Mumbai'
    end = "Mumbai"
    # Getting the paths from start to end 
    print(f"Routes between {start} and {end} : ",graph.getPaths(start,end))
