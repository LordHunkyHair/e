import time
map1 = [
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    ]
map2 = [
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    ]

def draw_map1():
    #draw map
    for y in map1:
        draw = ""
        for x in y:
            draw += x
        print(f"{draw}")

def draw_map2():
    #draw map
    for y in map2:
        draw = ""
        for x in y:
            draw += x
        print(f"{draw}")

def main():
    x = 0
    y = 0
    z = 0
    success = 0
    player_x = 0
    player_y = 0
    old_player_x = 0
    old_player_y = 0
    player = "P"
    map1_player = list(map1)
    map1_player[player_y][player_x] = f"[{player}]"
    map2_player = list(map2)
    map2_player[player_y][player_x] = f"[{player}]"
    goal_x = 4
    goal_y = 4
    goal = "G"
    map1_goal = list(map1)
    map1_goal[goal_y][goal_x] = f"[{goal}]"
    gravity = 0
    while(True):
        type = input(f"Do you want gravity, y/n?: ")
        if type == "y":
            gravity = 1
            break
        elif type == "n":
            break
        else:
            print("Error: Please type the letter y for yes or n for no")
            continue
    #draw map
    #player movement and goal location
    if success == 0:
        draw_map1()
        while z == 0:
            try:
                if gravity == 1:
                    while player_y != 4:
                        old_player_y = player_y
                        player_y += 1
                        map1_player[player_y][player_x] = f"[{player}]"
                        map1_player[old_player_y][player_x] = f"[ ]"
                        print(f"Fall")
                        time.sleep(0.5)
                        draw_map1()
                if goal_x == player_x and goal_y == player_y:
                    success += 1
                    print()
                    break
                move = input(f"Please put in you movement: ")
                if move == "w":
                    old_player_y = player_y
                    player_y -=1
                    if player_y < 0:
                        player_y = 4
                    map1_player[player_y][player_x] = f"[{player}]"
                    map1_player[old_player_y][player_x] = f"[ ]"
                    draw_map1()
                if move == "a":
                    old_player_x = player_x
                    player_x -=1
                    if player_x < 0:
                        player_x = 4
                    map1_player[player_y][player_x] = f"[{player}]"
                    map1_player[player_y][old_player_x] = f"[ ]"
                    draw_map1()
                if move == "s":
                    old_player_y = player_y
                    player_y +=1
                    if player_y > 4:
                        player_y = 0
                    map1_player[player_y][player_x] = f"[{player}]"
                    map1_player[old_player_y][player_x] = f"[ ]"
                    draw_map1()
                if move == "d":
                    old_player_x = player_x
                    player_x +=1
                    if player_x > 4:
                        player_x = 0
                    map1_player[player_y][player_x] = f"[{player}]"
                    map1_player[player_y][old_player_x] = f"[ ]"
                    draw_map1()
            except:
                continue
    if success == 1:
        draw_map2()
        player_x = 0
        player_y = 0
        old_player_x = 0
        old_player_y = 0
        while z == 0:
            try:
                if gravity == 1:
                    while player_y != 4:
                        old_player_y = player_y
                        player_y += 1
                        map2_player[player_y][player_x] = f"[{player}]"
                        map2_player[old_player_y][player_x] = f"[ ]"
                        print(f"Fall")
                        time.sleep(0.5)
                        draw_map2()
                move = input(f"Please put in you movement: ")
                if move == "w":
                    old_player_y = player_y
                    player_y -=1
                    if player_y < 0:
                        player_y = 4
                    map2_player[player_y][player_x] = f"[{player}]"
                    map2_player[old_player_y][player_x] = f"[ ]"
                    draw_map2()
                if move == "a":
                    old_player_x = player_x
                    player_x -=1
                    if player_x < 0:
                        player_x = 4
                    map2_player[player_y][player_x] = f"[{player}]"
                    map2_player[player_y][old_player_x] = f"[ ]"
                    draw_map2()
                if move == "s":
                    old_player_y = player_y
                    player_y +=1
                    if player_y > 4:
                        player_y = 0
                    map2_player[player_y][player_x] = f"[{player}]"
                    map2_player[old_player_y][player_x] = f"[ ]"
                    draw_map2()
                if move == "d":
                    old_player_x = player_x
                    player_x +=1
                    if player_x > 4:
                        player_x = 0
                    map2_player[player_y][player_x] = f"[{player}]"
                    map2_player[player_y][old_player_x] = f"[ ]"
                    draw_map2()
            except:
                continue
main()