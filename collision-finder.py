import importlib, random, string, time, math  
pwordalt = importlib.import_module("memorable-pword")
BIGNUM = 3**3**8*(369**369)*(92781**9)

moveUp = lambda n:print(f'\033[{n}A', end="")
clear = lambda n:print(("\b" * n) + (" " * n) + ("\b" * n), end="")
anagrams = lambda s:set(["".join(random.sample(list(s), len(s))) for _ in range(700*math.factorial(len(s)))])

seed = lambda inp:pwordalt.simple_hasher(pwordalt.SECRET_KEY) * pwordalt.simple_hasher(inp[0]) + pwordalt.easy_hasher(inp[0]) * inp[1]

for _ in range(BIGNUM):
    inpt = [eval(t) for t in input("Enter an input string and password size combination to test: ").split()]
    target = seed(inpt)

    characters = string.ascii_letters + string.digits
    tests = (''.join([random.choice(characters) for _ in range(len(inpt[0]))]) for _ in range(BIGNUM))

    for t in tests:
        if seed([t, inpt[1]]) == target and t not in anagrams(inpt[0]):
            print(f"The string {t} produces the same password as {inpt[0]}")
            break
        else:
            print(f"{t} produces {seed([t, inpt[1]])}, not a match!")
            moveUp(1)
            clear(100)

print("Has the apocalypse happened yet?")