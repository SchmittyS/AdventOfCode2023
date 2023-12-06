def check_if_valid_game(row):
    row=row.rstrip('\n')
    line_split=row.split(": ")
    #Gets the Game Number
    game_number=int(line_split[0].split(" ")[1])
    #Game Values
    game_values=line_split[1].split("; ")
    valid_game=True
    #Itterate through all variables in the round
    for x in game_values:
        round=x.split(", ")
        red_cubes=12
        green_cubes=13
        blue_cubes=14
        #Loop through all the cubes
        for value in round:  
            color_value=value.split(" ")
            
            #Check the cube color and subtract from # of cubes
            if(color_value[1]=="blue"):
                blue_cubes=blue_cubes-int(color_value[0])
            elif(color_value[1]=="green"):
                green_cubes=green_cubes-int(color_value[0])
            else:
                red_cubes=red_cubes-int(color_value[0])
             
        #If any are less than the original number of cubes, the game is not valid   
        if(red_cubes<0 or green_cubes <0 or blue_cubes <0):
            valid_game=False
            break
       
    #Return the game number if valid, otherwise return 0
    if(valid_game):
        return game_number
    else:
        return 0


def get_lowest_cubes_count(row):
    row=row.rstrip('\n')
    line_split=row.split(": ")
    
    #Game Values
    game_values=line_split[1].split("; ")
    
    #Itterate through all variables in the round
    red_cubes=0
    green_cubes=0
    blue_cubes=0
    
    #Loop through all round values
    for x in game_values:
        round=x.split(", ")
        
        #Loop through all the cubes
        for value in round:  
            color_value=value.split(" ")
            
            #Get the color and check if greater than the last highest cube count
            #Change if greater than the highest
            if(color_value[1]=="blue" and int(color_value[0])>blue_cubes):
                blue_cubes=int(color_value[0])
            elif(color_value[1]=="green"and int(color_value[0])>green_cubes):
                green_cubes=int(color_value[0])
            elif(color_value[1]=="red"and int(color_value[0])>red_cubes):
                red_cubes=int(color_value[0])
        
    return red_cubes*green_cubes*blue_cubes
    
def readFile(fileLocation):
    game_counter=0
    game2_counter=0
    with open(fileLocation, 'r') as fileobj:
        for row in fileobj:
            game_counter=game_counter+check_if_valid_game(row)
            game2_counter=game2_counter+get_lowest_cubes_count(row)
    
    print("Part 1: "+str(game_counter))
    print("Part 2: "+str(game2_counter))

if __name__ == '__main__':
    readFile("input1.txt")
    