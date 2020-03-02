def main():
    n = int(input("Please enter a whole number"))
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
    print("The factor of", n, "is", fact)

main()