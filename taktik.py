import chess.pgn as pgn
import chess
import io
import engine
import random

mate_in_1 = []
mate_in_2 = []
mate_in_3 = []
mate_in_4 = []
mate_in_5 = []
mate_in_6 = []
mate_in_7 = []
mate_in_8 = []
mate_in_9 = []
mate_in_10 = []



def get_data():
    d = ""
    while "best" not in d:
        d += stockfish.engine.stdout.read(1)
    return d

stockfish = engine.Engine(r"C:\Users\Hacker\Desktop\Taktik\engine.exe")
stockfish.setoption("threads", 3)
data_pgn = open(r"C:\Users\Hacker\Desktop\Taktik\data.pgn", "r")
def get_one_pgn():
    _pgn = ""
    while "1." not in _pgn:
        _pgn += data_pgn.readline()
    return pgn.read_game(io.StringIO(_pgn))

def show_download(now, maxi, t):
    procent = int(now/maxi*100)
    if procent < 10:
        procent = "0"+str(procent)
    print(t+"  [{}{}] {}%          ".format("="*(int(procent)//10), " "*(10-(int(procent)//10)), procent), end="\r")

for l in range(200):
    show_download(l, 200, "Testing Games")
    pgn1 = get_one_pgn()
    board = chess.Board()
    for i in pgn1.mainline_moves():
        board.push(i)
        stockfish.position(fen=board.fen())
        stockfish.write("go depth 10")
        got = get_data()
        for i in range(1, 11):
            if f"mate {i}" in got:
                exec(f"mate_in_{i}.append(board.fen())")

print(mate_in_3)