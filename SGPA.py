from pack_1.test2 import S_credit,G_credit
T_S_credit=0
T_G_credit=0
flag = 0
Subjects= [
    'DIP',
    'ML',
    'ISS',
    'CAO',
    'AI',
    'CC',
    'DIP_L',
    'ML_L',
    'PYTHON_L',
    'MAD_L',
    'ERP',
    'DECA'
]
for subject in Subjects:
    T_S_credit+=S_credit.get(subject)
    Grade=input(f"{subject} --> " ).upper()
    if Grade=="F":
        flag = 1
    T_G_credit+=(G_credit.get(Grade)*S_credit.get(subject))
if flag==1:
    print("\t\t\t\t\t\t\t\t\t\t\t\t--> Fail....")
sgpa=T_G_credit/T_S_credit
print(f"\t\t\t\t\t\t\t\t\t\t\t\t--> SGPA = {sgpa}")