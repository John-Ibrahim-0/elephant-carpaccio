import sys

def main():
    tax = {"ON": 0.13}
    
    price = float(sys.argv[1])

    quantity = int(sys.argv[2])

    pre_tax = price * quantity

    after_tax = pre_tax * (1 + tax["ON"])

    print(f"The total cost is: ${round(after_tax, 2)}")

if __name__ == "__main__":
    main()