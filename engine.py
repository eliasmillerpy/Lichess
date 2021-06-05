import subprocess as S

class Engine:
    def __init__(self, path):
        self.engine = S.Popen(path, stdin=S.PIPE, stdout=S.PIPE, bufsize=1, universal_newlines=True)
        self.write("isready")
        self.get("readyok")
        self.setoption("threads", 2)

    def write(self, command=""):
        if command == "":
            return
        self.engine.stdin.write(command+"\n")

    def read(self):
        return self.engine.stdout.readline().strip()

    def get(self, best="", f1=0, s1=1000, f2=0, s2=1000):
        while True:
            text = self.read()
            if text[f1:s1] == best:
                return text[f2:s2]

    def position(self, moves="", startpos=False, fen=""):
        command = "position"
        if startpos == True:
            command += " startpos"

        if moves != "":
            command += " moves " + moves
        
        if fen != "":
            command += f" fen {fen}"

        self.write(command)

    def bestmove(self, depth=0, movetime=0):
        command = "go "
        if depth > 0:
            command += "depth "+str(depth)+" "
        if movetime > 0:
            command += "movetime "+str(movetime)
        self.write(command)
        return self.get("bestmove", 0, 8, 9, 13)

    def fen(self):
        self.write("d")
        return self.get("Fen:", 0, 4, 5)
    
    def setoption(self, name, value):
        command = f"setoption name {name} value {value}"
        self.write(command)