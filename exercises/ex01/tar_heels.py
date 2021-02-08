"""An exercise in remainders and boolean logic."""

__author__ = "730411124"

# Begin your solution here...
ask = input("Enter an int: ")
nummer = int(ask)

if nummer // 2 == nummer / 2 and nummer // 7 == nummer / 7:
        print("TAR HEELS") 
else:
       if nummer // 2 == nummer / 2:
            print("TAR")
       else:
            if nummer // 7 == nummer / 7:
                print("HEELS")
            else:
                print("CAROLINA")

