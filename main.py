import threading
import sys
from time import sleep
from game import init_game
from io import StringIO 
from contextlib import redirect_stdout

# class Capturing(list):
#     def __enter__(self):
#         self._stdout = sys.stdout
#         sys.stdout = self._stringio = StringIO()
#         return self
#     def __exit__(self, *args):
#         self.extend(self._stringio.getvalue().splitlines())
#         del self._stringio    # free up some memory
#         sys.stdout = self._stdout

f = StringIO()
with redirect_stdout(f):
    init_game(4)
map = f.getvalue()

# with Capturing() as map:
#     init_game(4)

for s in map:
    print('map:', s)
# trucks = map[0].split("trucks:")[1]
# width = map[1].split("width:")[1]
# height = map[2].split("height:")[1]
# print('trucks', trucks)
# print('width', width)
# print('height', height)

# truck = list
# for x in width:
#     for y in height:
#         truck.append()
