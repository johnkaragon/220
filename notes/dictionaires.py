families = {"Smith": ["Susie, Sam"], "Jones": ["Elliot, Maggie"]}
print(families)


for family in families:
    print(family, end="\n\t")
    for name in families[family]:
        print(name, end=" ")
    print()


