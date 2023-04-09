# Write a function called excel_to_column_number that will take a positive integer, N. Return the equivalent column number in Excel. 
#For simplicity, we’ll skip over the “AA” column behavior and simply convert to a base-25 number, using alpha characters as digits.
# For Example:
# A=0
# B=1
# C=2
# Z=25
# BA=26
# BB=27
# BC=28

# def  excel_to_column_number(Number):
#     column = 0
#     if Number // 26 == 1:
#         column = int(Number / 26) * 26
#         print(column)
#     if Number < 26:
#         column = Number
#     if Number > 26:
#         column = int(Number / 26) * 26 



# print(excel_to_column_number(26))
# print(excel_to_column_number(4))
# print(excel_to_column_number(284))


print(2560 % 26) # 12 = M
print(2560 // 26) # 98
print(98// 26) # d = 3
print(98 % 26) # v = 20

#DVM
(3 * 26 * 26) + (20 * 26) + 12

# floor divide N
# if N > 26:
# floor divide result of that
# modulo divide result


