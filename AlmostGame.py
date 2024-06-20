def main():
    map = [
        ["[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]"]
    ]
    x = 0
    y = 0
    player_x = 0
    player_y = 0
    move = str(input())
    if move == "w":
        player_y -= 1
    if move == "a":
        player_x -= 1
    if move == "s":
        player_y += 1
    if move == "d":
        player_x += 1
    player_position = [player_y][player_x]
    player = "P"
    map_player = list(map)
    map_player[player_y][player_x] = f"[{player}]"

    #draw map
    for y in map:
        draw = ""
        for x in y:
            draw += x
        print(f"{draw}")
    
main()