def process_strings():
    N = int(input("Введіть кількість рядків N: "))
    lines = []

    for i in range(N):
        line = input(f"Введіть рядок {i + 1}: ")
        if len(line) % 2 == 0: 
            mid_index = len(line) // 2
            line = line[:mid_index-1] + line[mid_index-1:mid_index+1].upper() + line[mid_index+1:]
        lines.append(line)

    print("\nОброблені рядки:")
    for line in lines:
        print(line)

process_strings()
