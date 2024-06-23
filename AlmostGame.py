import random
map = [
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
    ]
def draw_map():
    #draw map
    for y in map:
        draw = ""
        for x in y:
            draw += x
        print(f"{draw}")

def main():
    x = 0
    y = 0
    z = 0
    player_x = 0
    player_y = 0
    old_player_x = 0
    old_player_y = 0
    map_player = list(map)
    player_position = [player_y][player_x]
    player = "P"
    map_player[player_y][player_x] = f"[{player}]"
    enemy_x = 0
    enemy_y = 4
    old_enemy_x = 0
    old_enemy_y = 0
    map_enemy = list(map)
    enemy_position = [enemy_y][enemy_x]
    enemy = "E"
    map_enemy[enemy_y][enemy_x] = f"[{enemy}]"
    #draw map
    #player movement and enemy movement
    draw_map()
    while z == 0:
        try:
            move = input(f"Please put in you movement: ")
            if move == "w":
                old_player_y = player_y
                player_y -=1
                map_player[player_y][player_x] = f"[{player}]"
                map_player[old_player_y][player_x] = f"[ ]"
                draw_map()
            if move == "a":
                old_player_x = player_x
                player_x -=1
                map_player[player_y][player_x] = f"[{player}]"
                map_player[player_y][old_player_x] = f"[ ]"
                draw_map()
            if move == "s":
                old_player_y = player_y
                player_y +=1
                map_player[player_y][player_x] = f"[{player}]"
                map_player[old_player_y][player_x] = f"[ ]"
                draw_map()
            if move == "d":
                old_player_x = player_x
                player_x +=1
                map_player[player_y][player_x] = f"[{player}]"
                map_player[player_y][old_player_x] = f"[ ]"
                draw_map()
        except:
            continue
    
main()