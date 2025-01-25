#!/usr/bin/env python3.9


def move_tower(n, fro, to, aux):
    if n < 1:
        return
    move_tower(n-1, fro, aux, to)
    print(f"moving {fro} to {to}")
    move_tower(n-1, aux, to, fro)


move_tower(3, "A", "B", "C")
