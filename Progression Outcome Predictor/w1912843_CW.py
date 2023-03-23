# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210180 / w1912843
# Date: 17 / 04 / 2022 

#Part1(Horizontal Histogram)
#Creating a function to output the horizontal histogram.
def horizontal_histogram(progress_counter,trailer_counter,retriever_counter,excluded_counter):
    print("-" * 80)
    print("Horizontal Histogram\n")
    print("Progress", progress_counter, "   :", (progress_counter * "*") )
    print("Trailer", trailer_counter,"    :", (trailer_counter * "*") )
    print("Retriever", retriever_counter, "  :", (retriever_counter * "*") )
    print("Excluded", excluded_counter, "   :", (excluded_counter * "*") )
    print()
    print((progress_counter + trailer_counter + retriever_counter + excluded_counter), "outcome(s) in total.")
    print("-" * 80)
 
#Part2
#Creating a function to output the vertical histogram.
#https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
def vertical_histogram(progress_counter,trailer_counter,retriever_counter,excluded_counter):
    print("-" * 80)
    print("Vertical Histogram\n")
    header = ['Progress', 'Trailer', 'Retriever', 'Excluded']
    print(' '.join(header))
    for x in range(max(progress_counter, trailer_counter, retriever_counter, excluded_counter)):
        print("  {0}         {1}         {2}         {3}".format("*" if x < progress_counter else ' ',
                                                                 "*" if x < trailer_counter else ' ',
                                                                 "*" if x < retriever_counter else ' ',
                                                                 "*" if x < excluded_counter else ' '))
     
    print((progress_counter + trailer_counter + retriever_counter + excluded_counter), "outcome(s) in total.")              
    print("-" * 80)
     
#Part 3
#Creating a function to output the lists.
def lists(list_progress, list_trailer, list_retriever, list_excluded):
    print("-" * 80)
    print("List\n")
    for i in list_progress:
        print("Progress - ", str(i)[1:-1])

    for j in list_trailer:
        print("Trailer - ", str(j)[1:-1])

    for k in list_retriever:
        print("Retriever - ", str(k)[1:-1])

    for l in list_excluded:
        print("Excluded - ", str(l)[1:-1])
    print("-" * 80)
     

#Part 4
#Creating a function to write the progression data in a text file and also to read it.
def text_file_write(list_progress, list_trailer, list_retriever, list_excluded):
    data_file = open("Student_Progression_Data.txt", "w")

    for i in list_progress:
        data_file.write("Progress - ")
        data_file.write(str(i)[1:-1])
        data_file.write("\n")

    for j in list_trailer:
        data_file.write("Trailer - ")
        data_file.write(str(j)[1:-1])
        data_file.write("\n")

    for k in list_retriever:
        data_file.write("Retriever - ")
        data_file.write(str(k)[1:-1])
        data_file.write("\n")

    for l in list_excluded:
        data_file.write("Excluded - ")
        data_file.write(str(l)[1:-1])
        data_file.write("\n")

    data_file.close()
    print("-" * 80)
    print("Reading from Text File:\n")
    data_file = open("Student_Progression_Data.txt", "r")
    for d in data_file:
        print(d)
    print("Done!")
    print("-" * 80)

#Creaing a main function to get inputs , menus and to process.
def main():
    #Create Variables.
    credit_pass = 0  
    credit_defer = 0  
    credit_fail = 0
    total_credits = 0
    option = ""
    choice = ""
    choose = ""
    progress_counter = 0
    trailer_counter = 0
    retriever_counter = 0
    excluded_counter = 0

    #Create Lists.
    list_progress = []
    list_trailer = []
    list_retriever = []
    list_excluded = []
    inputs = []
    range_of_values = [0, 20, 40, 60, 80, 100, 120]
     
    while True:
        print("\nEnter 1 if you are Student")
        print("Enter 2 if you are a Staff Member")
        print("Enter 3 to Exit")
        choose = input("\nEnter your choice: ")
  
        if choose == "1":
             
            while credit_pass != 0 or credit_pass != 20 or credit_pass != 40 or credit_pass != 60 or credit_pass != 80 or credit_pass != 100 or credit_pass != 120:
                try:
                    credit_pass = int(input("\nPlease enter your credits at pass: "))
                    if credit_pass in range_of_values:
                        break
                    else:
                        print("Out of range")
                except ValueError:#Show error when a any other data type(other than int) is used.
                    print("Integer required")#Printing Integer required.
        
        
        
            while credit_defer != 0 or credit_defer != 20 or credit_defer != 40 or credit_defer != 60 or credit_defer != 80 or credit_defer != 100 or credit_defer != 120:   
                try:
                    credit_defer = int(input("Please enter your credits at defer:  "))
                    if credit_defer in range_of_values:
                        break
                    else:
                        print("Out of range")
                except ValueError:#Show error when a any other data type(other than int) is used.
                    print("Integer required")#Printing Integer required.
            
        
            while credit_fail != 0 or credit_fail != 20 or credit_fail != 40 or credit_fail != 60 or credit_fail != 80 or credit_fail != 100 or credit_fail != 120:   
                try:
                    credit_fail = int(input("Please enter your credits at fail:  "))
                    if credit_fail in range_of_values:
                        break
                    else:
                        print("Out of range")
                except ValueError:#Show error when a any other data type(other than int) is used.
                    print("Integer required")#Printing Integer required.


            if credit_pass in range_of_values and credit_defer in range_of_values and credit_fail in range_of_values:
                total_credits = credit_pass + credit_defer + credit_fail#Getting the total credits.
                 
                if total_credits == 120:
                    if credit_pass == 120:
                        print("Progress")
                        
                     
                    elif credit_pass == 100:
                        print("Progress (module trailer)")
                         

                    elif credit_fail >= 80:
                        print("Exclude")
                         

                    else:
                        print("Module retriever")
                        
                else:
                    print("Total Incorrect")
                     
     
        elif choose == "2":
            while True:
                while credit_pass != 0 or credit_pass != 20 or credit_pass != 40 or credit_pass != 60 or credit_pass != 80 or credit_pass != 100 or credit_pass != 120:
                    try:
                        credit_pass = int(input("Please enter your credits at pass: "))
                        if credit_pass in range_of_values:
                            break
                        else:
                            print("Out of range")
                    except ValueError:#Show error when a any other data type(other than int) is used.
                        print("Integer required")#Printing Integer required.
            
            
            
                while credit_defer != 0 or credit_defer != 20 or credit_defer != 40 or credit_defer != 60 or credit_defer != 80 or credit_defer != 100 or credit_defer != 120:   
                    try:
                        credit_defer = int(input("Please enter your credits at defer:  "))
                        if credit_defer in range_of_values:
                            break
                        else:
                            print("Out of range")
                    except ValueError:#Show error when a any other data type(other than int) is used.
                        print("Integer required")#Printing Integer required.
                
            
                while credit_fail != 0 or credit_fail != 20 or credit_fail != 40 or credit_fail != 60 or credit_fail != 80 or credit_fail != 100 or credit_fail != 120:   
                    try:
                        credit_fail = int(input("Please enter your credits at fail:  "))
                        if credit_fail in range_of_values:
                            break
                        else:
                            print("Out of range")
                    except ValueError:#Show error when a any other data type(other than int) is used.
                        print("Integer required")#Printing Integer required.


                if credit_pass in range_of_values and credit_defer in range_of_values and credit_fail in range_of_values:
                    total_credits = credit_pass + credit_defer + credit_fail#Getting the total credits.
                     
                    if total_credits == 120:
                        if credit_pass == 120:
                            print("Progress")
                            progress_counter += 1
                            inputs = [credit_pass,credit_defer,credit_fail]
                            list_progress.append(inputs)
                         
                        elif credit_pass == 100:
                            print("Progress (module trailer)")
                            trailer_counter += 1
                            inputs = [credit_pass,credit_defer,credit_fail]
                            list_trailer.append(inputs)

                        elif credit_fail >= 80:
                            print("Exclude")
                            excluded_counter += 1
                            inputs = [credit_pass,credit_defer,credit_fail]
                            list_excluded.append(inputs)

                        else:
                            print("Module retriever")
                            retriever_counter += 1
                            inputs = [credit_pass,credit_defer,credit_fail]
                            list_retriever.append(inputs)
                    else:
                        print("Total Incorrect")#Printing error message in total not equal to 120.
    
                while True:
                    breaks = "" #Creating variable.
                    option = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
                    if option.lower() == 'y':
                        break
                          
                    elif option.lower() == 'q':
                        print("\n    1. Horizontal Histogram\n    2. Vertical Histogram\n    3. Lists\n    4. Text File")
                        choice = input("\nEnter which option in Staff Version you need to print: ")
                        if choice == "1":
                            horizontal_histogram(progress_counter,trailer_counter,retriever_counter,excluded_counter)#Calling horizontal_histogram function.
                            breaks = True
                            break
                        elif choice == "2":
                            vertical_histogram(progress_counter,trailer_counter,retriever_counter,excluded_counter)#Calling vertical_histogram function.
                            breaks = True
                            break
                    
                        elif choice == "3":
                            lists(list_progress, list_trailer, list_retriever, list_excluded)#Calling lists function.
                            breaks = True
                            break
                        
                        elif choice == "4":
                            text_file_write(list_progress, list_trailer, list_retriever, list_excluded)#Calling text_file_write function.
                            breaks = True
                            break
                         
                        else:
                            print("Invalid Input!")
                            continue
                        
                    else:
                        print("Invalid Input! Re-enter...")
                        continue     
                if breaks == True:
                    break
    
 
        elif choose == "3":
            print("Thank You")
            break
            
        else:
            print("Invalid Input! Renter...")
        
 
main()#Calling main function.
     
    
 
         
 
 
