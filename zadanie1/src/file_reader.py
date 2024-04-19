# Dane w plikach /data
# w pierwszej linii ilosc wierzcholkow (n), ilosc polaczen (m) oraz x i y punktu startowego (fabryki)
# w kolejnych n liniach wierzcholki
# w kolejnych liniach dwa wierzcholki (x, y) tworzace krawedz oraz jej przepustowosc

# Przyklad
"""
11 3 3 4
1 2
3 4
4 3 
5 4
4 5
2 6
1 4
2 4
3 3
5 5
6 6
3 4 2 4 1
3 4 3 3 1
2 4 1 4 1
"""

class File_reader:
    def __init__(self, filename):
        self.filename = filename

    def readKluby(self):
        pass

    def readPoints(self):
        if not self.filename:
            return []
        
        data = {"adjList": {}, "start": None}
        currLine = 0
        startX = 0
        startY = 0
        endX = 0
        endY = 0

        with open(self.filename, 'r') as file_in:
            for line in file_in:
                line = line.rstrip()

                if currLine == 0:
                    n, m, startX, startY, endX, endY = line.split()
                    numOfVertices = int(n)
                    numOfEdges = int(m)
                    currLine += 1
                    continue

                if currLine <= numOfVertices:
                    x, y = line.split()
                    data["adjList"][(int(x), int(y))] = []
                    currLine += 1
                    continue
                
                x, y, w, z, flow = line.split() 
                
                pointA = (int(x), int(y))
                pointB = (int(w), int(z))

                if pointA not in data["adjList"]:
                    data["adjList"][pointA] = []
                if pointB not in data["adjList"]:
                    data["adjList"][pointB] = []
                
                data["adjList"][pointA].append((pointB, int(flow)))

        data["start"] = (int(startX), int(startY))
        data["end"] = (int(endX), int(endY))

        return data


def main():
    fr = File_reader('../data/przyklad3.txt')
    data = fr.read()
    print(data)

if __name__ == '__main__':
    main()