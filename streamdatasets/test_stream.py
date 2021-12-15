from .stream import Stream

s = Stream('', '/tmp')
res = s._download('https://rueberg.eu/graphs/test/b.plantuml.png', '1.bin', part_start=50, part_end=100)
print(res)