import time
class color:
        default = "\033[0m"
        red =  "\033[91m"
        yellow = "\033[93m"
        green = "\033[32m"
        blue = "\033[94m"
        cyan = "\033[96m"
        purple = "\033[95m"

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

map3 = [
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
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

def draw_map3():
    #draw map
    for y in map3:
        draw = ""
        for x in y:
            draw += x
        print(f"{draw}")

def blocking():
    #block player
    print("Blocked")
    draw_map1()

def blocking2():
    #block player
    print("Blocked")
    draw_map2()

def blocking3():
    #block player
    print("Blocked")
    draw_map3()

def main():
    #define variables and their positions
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
    map1_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
    map2_player = list(map2)
    map2_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
    map3_player = list(map3)
    map3_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
    goal_x = 4
    goal_y = 4
    goal = "G"
    map1_goal = list(map1)
    map1_goal[goal_y][goal_x] = f"[{color.green}{goal}{color.default}]"
    gravity = 0
    block_x = 0
    block_y = 3
    block = "B"
    map1_block = list(map1)
    map1_block[block_y][block_x] = f"[{color.purple}{block}{color.default}]"
    #gravity toggle
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
                        if player_y+1 == block_y and player_x == block_x:
                            blocking()
                            break
                        old_player_y = player_y
                        player_y += 1
                        map1_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
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
                    if player_y-1 == block_y and player_x == block_x:
                        blocking()
                        continue
                    else:
                        old_player_y = player_y
                        player_y -=1
                        if player_y < 0:
                            player_y = 4
                        map1_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                        map1_player[old_player_y][player_x] = f"[ ]"
                        draw_map1()
                if move == "a":
                    if player_y == block_y and player_x-1 == block_x:
                        blocking()
                        continue
                    else:
                        old_player_x = player_x
                        player_x -=1
                        if player_x < 0:
                            player_x = 4
                        map1_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                        map1_player[player_y][old_player_x] = f"[ ]"
                        draw_map1()
                if move == "s":
                    if player_y+1 == block_y and player_x == block_x:
                        blocking()
                        continue
                    else:
                        old_player_y = player_y
                        player_y +=1
                        if player_y > 4:
                            player_y = 0
                        map1_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                        map1_player[old_player_y][player_x] = f"[ ]"
                        draw_map1()
                if move == "d":
                    if player_y == block_y and player_x+1 == block_x:
                        blocking()
                        continue
                    else:
                        old_player_x = player_x
                        player_x +=1
                        if player_x > 4:
                            player_x = 0
                        map1_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                        map1_player[player_y][old_player_x] = f"[ ]"
                        draw_map1()
            except:
                continue
    if success == 1:
        block_x = 2
        block_y = 2
        map2_block = list(map2)
        map2_block[block_y][block_x] = f"[{color.purple}{block}{color.default}]"
        goal_x = 2
        goal_y = 1
        map2_goal = list(map2)
        map2_goal[goal_y][goal_x] = f"[{color.green}{goal}{color.default}]"
        draw_map2()
        player_x = 0
        player_y = 0
        old_player_x = 0
        old_player_y = 0
        while z == 0:
            try:
                if gravity == 1:
                    while player_y != 4:
                        if player_y+1 == block_y and player_x == block_x:
                            blocking2()
                            break
                        old_player_y = player_y
                        player_y += 1
                        map2_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                        map2_player[old_player_y][player_x] = f"[ ]"
                        print(f"Fall")
                        time.sleep(0.5)
                        draw_map2()
                if goal_x == player_x and goal_y == player_y:
                    success += 1
                    print()
                    break
                move = input(f"Please put in you movement: ")
                if move == "w":
                    if player_y-1 == block_y and player_x == block_x:
                        blocking2()
                        continue
                    old_player_y = player_y
                    player_y -=1
                    if player_y < 0:
                        player_y = 4
                    map2_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                    map2_player[old_player_y][player_x] = f"[ ]"
                    draw_map2()
                if move == "a":
                    if player_y == block_y and player_x-1 == block_x:
                        blocking2()
                        continue
                    old_player_x = player_x
                    player_x -=1
                    if player_x < 0:
                        player_x = 4
                    map2_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                    map2_player[player_y][old_player_x] = f"[ ]"
                    draw_map2()
                if move == "s":
                    if player_y+1 == block_y and player_x == block_x:
                        blocking2()
                        continue
                    old_player_y = player_y
                    player_y +=1
                    if player_y > 4:
                        player_y = 0
                    map2_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                    map2_player[old_player_y][player_x] = f"[ ]"
                    draw_map2()
                if move == "d":
                    if player_y == block_y and player_x+1 == block_x:
                        blocking2()
                        continue
                    old_player_x = player_x
                    player_x +=1
                    if player_x > 4:
                        player_x = 0
                    map2_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                    map2_player[player_y][old_player_x] = f"[ ]"
                    draw_map2()
            except:
                continue
    if success == 2:
        block_x = 5
        block_y = 1
        map3_block = list(map3)
        map3_block[block_y][block_x] = f"[{color.purple}{block}{color.default}]"
        goal_x = 5
        goal_y = 0
        map3_goal = list(map3)
        map3_goal[goal_y][goal_x] = f"[{color.green}{goal}{color.default}]"
        draw_map3()
        player_x = 0
        player_y = 0
        old_player_x = 0
        old_player_y = 0
        while z == 0:
            try:
                if gravity == 1:
                    while player_y != 5:
                        if player_y+1 == block_y and player_x == block_x:
                            blocking3()
                            break
                        old_player_y = player_y
                        player_y += 1
                        map3_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                        map3_player[old_player_y][player_x] = f"[ ]"
                        print(f"Fall")
                        time.sleep(0.5)
                        draw_map3()
                move = input(f"Please put in you movement: ")
                if move == "w":
                    if player_y-1 == block_y and player_x == block_x:
                        blocking3()
                        continue
                    old_player_y = player_y
                    player_y -=1
                    if player_y < 0:
                        player_y = 5
                    map3_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                    map3_player[old_player_y][player_x] = f"[ ]"
                    draw_map3()
                if move == "a":
                    if player_y == block_y and player_x-1 == block_x:
                        blocking3()
                        continue
                    old_player_x = player_x
                    player_x -=1
                    if player_x < 0:
                        player_x = 5
                    map3_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                    map3_player[player_y][old_player_x] = f"[ ]"
                    draw_map3()
                if move == "s":
                    if player_y+1 == block_y and player_x == block_x:
                        blocking3()
                        continue
                    old_player_y = player_y
                    player_y +=1
                    if player_y > 5:
                        player_y = 0
                    map3_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                    map3_player[old_player_y][player_x] = f"[ ]"
                    draw_map3()
                if move == "d":
                    if player_y == block_y and player_x+1 == block_x:
                        blocking3()
                        continue
                    old_player_x = player_x
                    player_x +=1
                    if player_x > 5:
                        player_x = 0
                    map3_player[player_y][player_x] = f"[{color.red}{player}{color.default}]"
                    map3_player[player_y][old_player_x] = f"[ ]"
                    draw_map3()
            except:
                continue
main()