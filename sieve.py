from mordell_sieve import find_integer_points


def main() -> None:
    examples = [2, -2, 1, -1, 17]
    primes = [5, 7, 11, 13, 17, 19]

    for k in examples:
        points, stats = find_integer_points(
            k=k,
            x_min=-100,
            x_max=100,
            primes=primes,
            return_stats=True,
        )
        print(f"Curve: y^2 = x^3 + ({k})")
        print(f"Primes used: {stats.primes}")
        print(f"Checked x-values: {stats.total_x_values}")
        print(f"Candidates after sieve: {stats.candidates_after_sieve}")
        print(f"Integer points found: {points}")
        print("-" * 60)


if __name__ == "__main__":
    main()
