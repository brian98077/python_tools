def binary_multiply(bin1, bin2):

    if not bin1 or not bin2:
        return "0"
    
    bin1 = bin1.replace('0b', '')
    bin2 = bin2.replace('0b', '')
    
    if not all(c in '01' for c in bin1) or not all(c in '01' for c in bin2):
        raise ValueError("input should contains only 0 and 1")
    
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)

    result = num1 * num2
    
    return bin(result)[2:]


def main():
    print("=" * 50)
    print("binary multiplication")
    print("=" * 50)
    
    try:
        bin1 = input("\nfirst  binary number : ").strip().replace(" ", "").replace("_", "")
        bin2 = input("second binary number : ").strip().replace(" ", "").replace("_", "")

        result = binary_multiply(bin1, bin2)
        
        print("=" * 50)
        print(f"binary : {bin1}")
        print(f"    ×")
        print(f"binary : {bin2}")
        print(f"    =")
        print(f"binary : {result}")
        print("=" * 50)
        
        dec1 = int(bin1.replace('0b', ''), 2)
        dec2 = int(bin2.replace('0b', ''), 2)
        dec_result = int(result, 2)
        print(f"decimal : {dec1} × {dec2} = {dec_result}")
        
    except ValueError as e:
        print(f"\nError : {e}")
    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()