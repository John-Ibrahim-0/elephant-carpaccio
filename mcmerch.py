import sys

def main():
    tax = {"ON": 0.13, "QC": 0.14975, "MB": 0.05, "NS": 0.15, "BC": 0.05}
    
    # extract the first argument as price
    price = float(sys.argv[1])

    # extract the second argument as quantity
    quantity = int(sys.argv[2])

    # extract the third argument as province
    province = sys.argv[3]

    pre_tax = price * quantity

    after_tax = pre_tax * (1 + tax[province])

    print(f"The total cost is: ${round(after_tax, 2)}")

if __name__ == "__main__":
    main()