#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ASSIGNMENT:
#Grade calculating program

p = int(input("Enter your percentage here="))
print("")
print("")
input("Press Enter to get your grade ! ")
print("")
print("")

if p >= 80 and p < 100:
    print("Progress:\nCongratulations your Grade is A+ !")
elif p >= 70 and p < 80:
    print("Progress:\nGRADE = A")
elif p >= 60 and p < 70:
    print("Progress:\nGRADE = B")
elif p >= 50 and p < 60:
    print("Progress:\nGRADE = C")
elif p >= 40 and p < 50:
    print("Progress:\nGRADE = D")
elif p >= 33 and p < 40:
    print("FAIL ! \n Better luck next time.")
elif p < 33 or p > 100:
    print("SORRY ! Inappropriate percentage.")
print("")
print("")
input("press enter to exit !")

