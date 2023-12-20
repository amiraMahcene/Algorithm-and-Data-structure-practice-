# with the use of the verity table ti understand how things works together .. r= 4 == 100, w = 2 == 010 ,ex = 1 == 001
# the and & operator work : x1 =1 and x2 = 1 x1 & x2 = 1
 
read_permession = 4
write_premession = 2
execute_permession = 1

user_permession = 6

# to give the user the permession to read 

if user_permession & read_permession == read_permession:   # 110 & 100 == 100, in other word  6 and 4 == 4 using the wise_operator
    print("read")
else:
    print("you don't  have permission")

print(user_permession & read_permession)

# or | at least one of the operators == 1  so the result is 1
# 5|6 = 101 | 110 == 111 so 5|6 ==7


# to get a user persmession you have to have write permession or read permession

if user_permession == write_premession | read_permession :   # 010 | 100 == 110 
    print ("permession")
else:
    print("you don't have permession as a user")

# the exclusif operator xor , to get a 1 as result you have to be each operator is the opesit than the first
# 1 ^ 0 == 1

# we can use xor to remove a given permission

user_permession ^= write_premession
print (user_permession)
print(bin(user_permession))

# the not ~ operator, take a operator and give you the oposit for each bits
# at the end we have left and right shift operators, >>,<<