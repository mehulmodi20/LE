def make_change_1(coin_denoms, change):
    if change in coin_denoms:
        return 1
    min_coins = float("inf")
    for i in [c for c in coin_denoms if c <= change]:
        print(f"change {change-i}")
        num_coins = 1 + make_change_1(
            coin_denoms, change - i
        )
        print(f"-------------------------{num_coins}")

        min_coins = min(num_coins, min_coins)
    return min_coins


print(make_change_1([1, 5, 10, 25], 26))


# make_change(coin_denoms, 25)
# make_change(coin_denoms, 24)
#
