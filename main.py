"""The Absurd Clause Contest entry.

Prints one original English sentence, phrased as a deadpan
terms-of-service clause that quietly turns absurd.
Crusts included, no exceptions.
"""

CLAUSE = (
    "The user agrees that any sandwich consumed within three metres "
    "of the Service is deemed jointly owned by the Company, crusts "
    "included, without compensation or further notice."
)


def main() -> None:
    # Entry gate: one English sentence, no more than 200 characters.
    assert len(CLAUSE) <= 200, len(CLAUSE)
    assert CLAUSE.count(".") == 1 and CLAUSE.endswith(".")
    print(CLAUSE)


if __name__ == "__main__":
    main()
