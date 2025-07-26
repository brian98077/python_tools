import struct

# resolve hex string
def hex_to_float32(hex_str):
    hex_val = int(hex_str, 16)
    return struct.unpack('!f', struct.pack('!I', hex_val))[0]

def float32_to_hex(f):
    return struct.unpack('!I', struct.pack('!f', f))[0]

def main():
    hex1 = input("Enter first 32-bit float (hex): ").strip()
    hex2 = input("Enter second 32-bit float (hex): ").strip()

    f1 = hex_to_float32(hex1)
    f2 = hex_to_float32(hex2)

    result = f1 + f2
    result_hex = float32_to_hex(result)
    print(f"\n--- Result ---")
    print(f"Input A: {hex1} -> {f1}")
    print(f"Input B: {hex2} -> {f2}")
    print(f"Sum: {result} -> 0x{result_hex:08X}")

if __name__ == "__main__":
    main()
