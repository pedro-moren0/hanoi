def switch(xs: list, p: str, q: str) -> list:
    return list(map(
        lambda pair: (q if pair[0] == p else p if pair[0] == q else pair[0],
                      q if pair[1] == p else p if pair[1] == q else pair[1]),
        xs
    ))


def gen_hanoi(n: int, start: str, aux: str, target: str) -> list:
    sol = [(start, target)]
    i = 1
    while i < n:
        fst_half = switch(sol, aux, target)
        snd_half = switch(sol, start, aux)
        sol = fst_half + [(start, target)] + snd_half
        i += 1
    return sol


def hanoi(n: int) -> list:
    return gen_hanoi(n, 'A', 'B', 'C')


def hanoi_len(n: int) -> int:
    return 2 ** n - 1
