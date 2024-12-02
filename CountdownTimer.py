import time
from colorama import Fore

input("Press Enter To Begin---") 
print("-"*40)

while True:
    time_limit = input(Fore.BLUE + "Enter your time in Seconds: ")
    if time_limit.isdigit():
        time_limit = int(time_limit)
        break
    else:
        print(Fore.RED + "Invalid input.Please try again.")
        continue

for i in range(time_limit,0,-1):
    seconds = i % 60
    minute = int(i/60) % 60
    hours = int(i/3600)
    
    print(Fore.GREEN + f"{hours:02}:{minute:02}:{seconds:02}")
    time.sleep(1)

print(Fore.RED + "TIME'S UP.")
print(Fore.LIGHTWHITE_EX + "-"*40)