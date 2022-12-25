import datetime



x = input("enter number to test")
          
while(x != "stop"):
      x = int(x)
      print(x)
      if(x%2 == 0):
          print("even")
      else:
          print("odd")
      x = input("enter number to test")


 