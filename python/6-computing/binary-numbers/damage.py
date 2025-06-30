def main():
    calculate_dps(8e6, 45)
    calculate_dps(1e7, 49)


# Don't edit below this line


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


main()
