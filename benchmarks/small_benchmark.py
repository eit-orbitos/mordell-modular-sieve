from time import perf_counter

from mordell_sieve import find_integer_points


def main() -> None:
    cases = [2, -2, 17, -17, 30]
    primes = [5, 7, 11, 13, 17, 19, 23]

    start = perf_counter()
    for k in cases:
        points, stats = find_integer_points(
            k=k,
            x_min=-1000,
            x_max=1000,
            primes=primes,
            return_stats=True,
        )
        print(
            f"k={k:>4} | x={stats.total_x_values:>5} | "
            f"after_sieve={stats.candidates_after_sieve:>5} | points={len(points):>3}"
        )
    elapsed = perf_counter() - start
    print(f"Elapsed seconds: {elapsed:.4f}")


if __name__ == "__main__":
    main()
