"""One star, five stars for the food.

Entry for the make.fun bounty
u-po-pu-one-star-five-stars-for-the-food-f9166ee7.

The review: an alien tourist gives planet Earth a one-star
review, and still slips in a real compliment about the food.
The locals spend all day shouting at small glowing rectangles
— a grievance worth one star — but the noodles almost made
the 400-light-year trip worth it. The turn is the joke: the
complaint is petty and alien, and the compliment is the only
thing that nearly redeems the whole planet.

The program writes the single review sentence to
/output/entry.txt.
"""

import os

ENTRY = (
    "One star: the locals shout at small glowing rectangles "
    "all day, but the noodles — the noodles almost made the "
    "400-light-year trip worth it."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
