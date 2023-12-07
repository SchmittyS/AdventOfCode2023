




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
                    special_char_row.append(row_index)
                    special_char_col.append(str(idx))
        
            row_index=row_index+1
            
            
            
   
    
if __name__ == '__main__':
    getSolution("example.txt")