var = input("Enter a Character :")
if( var.len(var)== 1):
 if (var.isalpha()):
    print("you have entered a alphabet")
 elif(var.isdigit()):
    print("you have enter a digit")
 elif(var.isspace()):
    print ("you have enter a white space")
 else: 
    print("invalid input or special characters")
else: 
    print("invalid input or special characters")