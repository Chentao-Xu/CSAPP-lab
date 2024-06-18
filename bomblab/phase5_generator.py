spell = [9, 15, 14, 5, 6, 7]

for offset in range(8):
    result = "".join(chr(num + 16 * offset) for num in spell)
    print(f"Offset {offset * 16} : {result}")
