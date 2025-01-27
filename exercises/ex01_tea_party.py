"""Planning the price of a tea party"""

__author__: str = "730649282"


def main_planner(guests: int) -> None:
    """Brings togehter all subsequent functions and produces a printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People" + "!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Computes the number of tea bags needed based on number of guests"""
    return 2 * people


def treats(people: int) -> int:
    """Computes the number of treats needed based on how many guests expect to drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of the tea bags and the treats combined"""
    return 0.5 * tea_count + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
