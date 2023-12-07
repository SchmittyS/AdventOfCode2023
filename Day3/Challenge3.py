def checkifTouching(row,col,spec_char_list):
    print(test)
    #Check Left Upper Diag row-1,col-1
    
    #Check Left Side col-1
    
    #Check Left Lower Diag row+1,col-1
    
    #Check Right Upper Diag row-1,col+1
    
    #Check Right Side col+1
    
    #Check Right Lower Diag row+1,col+1
    
    #Check Top row-1
    
    #Check Bot row+1

def getSumOfDigitsThatTouch(file_list,spec_char_list):
    isLastCharDigit=False
    isTouchingSpecial=False
    
    digit_list=[]
    for col in range(len(file_list)):
        for row in range(len(file_list[col])):
            #Check if value is numeric
            if(file_list[col][row].isnumeric()):
                #Append to the digit list
                digit_list.append(int(file_list[col][row]))
                isLastCharDigit=True
                
                #Check if touching special character
                isTouchingSpecial=checkifTouching(row,col,spec_char_list)
            else:
                #Check if it touched a special char
                if(isLastCharDigit and isTouchingSpecial):
                    #Calculate Value
                    print()
                
                isTouchingSpecial=False
                isLastCharDigit=False
                

def combine_special_lists(special_char_row,special_char_col):
    new_list=[]
    for idx,val in enumerate(special_char_col):
        calcVal=int(val)+(10*int(special_char_row[idx]))
        new_list.append(calcVal)
        print(calcVal)
    

def getSolution(fileLocation):
    file_list=[]
    special_char_row=[]
    special_char_col=[]
    
    with open(fileLocation, 'r') as fileobj:
        row_index=0
        for row in fileobj:
            
            row=row.rstrip('\n')
            
            file_list.append(list(row))
            
            for idx, val in enumerate(row):
                if(val=='*' or val=='#' or val=='+' or val=='$'):
                    special_char_row.append(int(row_index))
                    special_char_col.append(str(idx))
        
            row_index=row_index+1

    spec_char_list=combine_special_lists(special_char_row,special_char_col)
    
    getSumOfDigitsThatTouch(file_list,spec_char_list)
            
            
            
   
    
if __name__ == '__main__':
    getSolution("example.txt")