def main():
    map = [
        ["[] ", "[] ", "[] "],
        ["[] ", "[] ", "[] "],
        ["[] ", "[] ", "[] "]
    ]
    x = 2
    y = 1
    print(map[y][x])
    for row in map:
        for column in row:
            print(map[y][x])
main()

"[] [] [] "