# Q2: Direct-mapped cache simulation with 8 cache lines

NUM_LINES = 8
cache = [None] * NUM_LINES          # None means the line is empty
accesses = [3, 11, 3, 19, 11, 27, 3]

hits = 0
misses = 0

print(f"{'Block':<7}{'Line':<6}{'Result':<8}Cache contents")
print("-" * 60)

for block in accesses:
    line = block % NUM_LINES        # cache line = block number % number of lines

    if cache[line] == block:
        result = "HIT"
        hits += 1
    else:
        result = "MISS"
        misses += 1
        cache[line] = block         # load the block (replace old one if any)

    print(f"{block:<7}{line:<6}{result:<8}{cache}")

total = hits + misses
print("-" * 60)
print("Total hits   :", hits)
print("Total misses :", misses)
print("Hit ratio    :", hits / total, f"({hits / total * 100:.2f}%)")
