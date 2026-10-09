age = int(input("enter your age:"))
can_swim = input("can you swim? (yes/no)")
adult_there = input("is there an adult eith you? (yes/no)")

if age < 5:
    print(" Age group: toddler - splash pool! but ALWAYS with an adult")
    
elif age < 12:
    print("Age group: child - main pool only with an adult")

elif age < 18:
    print("Age group: teenager - main pool alone if uk swimming")

else:
    print("age group: adult! - all the pools are open to you")

if can_swim != "yes" and can_swim != "no":
    print("input error, pls answer the questin with a yes or no")
    swim_known = False

else: swim_known = True  

if can_swim == "yes" and adult_there == "no":
    print("deep pool: allowed- you can swim and an adult is present there")

if age<12 or can_swim == "no":
    print("shallow only : stay in shallow end")

if adult_there == True and not (adult_there == "yes"):
    print("remninder: no adult with u - the lifeguard must be told ")







