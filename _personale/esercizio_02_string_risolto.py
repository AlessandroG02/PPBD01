ricetta_orig = "oliva\t, pepe,cappero ,\n detersivo,\t \n cappero, peperone, acciuga ,oliva , pepe\t,\t cappero , \noliva,pasta\n"
ricetta_dict = {}                            

ricetta_orig_list = ricetta_orig.split(',')  
for ing_one in ricetta_orig_list:      
    ing_two = ing_one.strip()    

    if ing_two in ricetta_dict:        
        ricetta_dict[ing_two] += 1     
    else:                                    
        ricetta_dict[ing_two] = 1      

print(ricetta_dict)
print('Devo comprare:', )                          

for key in ricetta_dict:                     
    if ricetta_dict[key] > 1:                
        print('\t', ricetta_dict[key], key)  