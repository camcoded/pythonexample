def inputfile():
   
    print("1.Show data")
    print("2.Enter new data")
    print("3.End program")
    menu_option = int(input("Enter your choice: "))
        

    if menu_option == 1:
        x = open ("record.txt")
        for data1 in x:
            print(data1)
            

    elif menu_option == 2:
            reg = input("Enter registration no: ")
            name = input("Enter name: ")
            mark = input("Enter marks: ")
            save = input("save file Y /N? ")
            if save == "y":
                r = open("record.txt","a")
                r.write("\n")
                r.write(reg + "," + name + "," + mark)
                r.close()
                inputfile()
            

                
                    
            
                
    elif menu_option == 3:
            print("End program")

    else:
        print("invaild no.")

inputfile()

        

    




    
                
        
    


