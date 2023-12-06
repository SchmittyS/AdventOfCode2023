
def check_if_valid_game(row):
    row=row.rstrip('\n')
    line_split=row.split(": ")
    #Gets the Game Number
    game_number=int(line_split[0].split(" ")[1])
    #Game Values
    game_values=line_split[1].split("; ")
    valid_game=True
    for x in game_values:
        round=x.split(", ")
        red_cubes=12
        green_cubes=13
        blue_cubes=14
        for value in round:  
            color_value=value.split(" ")
            if(color_value[1]=="blue"):
                blue_cubes=blue_cubes-int(color_value[0])
            elif(color_value[1]=="green"):
                green_cubes=green_cubes-int(color_value[0])
            else:
                red_cubes=red_cubes-int(color_value[0])
                
                
         
        
        if(red_cubes<0 or green_cubes <0 or blue_cubes <0):
            valid_game=False
            break
       

    if(valid_game):
        return game_number
    else:
        return 0


def get_lowest_cubes_count(row):
    row=row.rstrip('\n')

    
def readFile(fileLocation):
    game_counter=0
    with open(fileLocation, 'r') as fileobj:
        for row in fileobj:
            game_counter=game_counter+check_if_valid_game(row)
            
    print("Part 1: "+str(game_counter))




if __name__ == '__main__':
    
    readFile("input1.txt")
    