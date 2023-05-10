import sys

file = open('bank_transactions.txt', 'r')

header = file.readline()
savings_total = 0
checkings_total = 0
investments_total = 0
total = 0

# transaction index variables
acct_idx = 1
ttype_idx = 2
amt_idx = 3
frm_acct_idx = 4

# define out account names
SAVINGS_ACCT = 'savings'
CHECKING_ACCT = 'checking'
INVESTMENT_ACCT = 'investment'

record_num = 0;
captured_record = ""
for eachline in file:
    trans = eachline.split (',')
    trans_type = trans[ttype_idx]
    account = trans[acct_idx]
    amount = int(trans[amt_idx])
    frm_acct = trans[frm_acct_idx]

    if (record_num == 5):
        print("Capture record")
        captured_record = trans
        if (captured_record[-1] == "\n"):
            captured_record.pop(-1)

    record_num += 1
  
    if trans_type == 'deposit':
        total += amount
       
        if account == SAVINGS_ACCT:
            savings_total += amount
          
        elif account == INVESTMENT_ACCT:
            investments_total += amount
        else:
            checkings_total += amount
           
    elif trans_type == 'withdrawal':
        total -= amount
        if account == SAVINGS_ACCT:
            savings_total -= amount
        else:
            checkings_total -= amount
           
    elif trans_type == 'transfer':
        if account == SAVINGS_ACCT:
            # add to savings
            savings_total += amount
           
            # subtract from the from account
            if frm_acct == CHECKING_ACCT:
                checkings_total -= amount
            else:
                investments_total -= amount
               
        elif account == CHECKING_ACCT:
            # add to the checking account
            checkings_total += amount
           
            # subtract from the from account
            # [ADD CODE HERE]
       
        else:
            # ADD CODE HERE TO HANDLE transfer to investment
            pass
          
    

# The report is below. No changes needed
print(f'My total across all accounts is {total}\n')    
print(f'My savings account total is {savings_total}\n')
print(f'My checking account total is {checkings_total}\n')
print(f'My investment account total is {investments_total}\n')

file.close()

print(captured_record)

file = open('bank_transactions.txt', 'a')

has_new_record = len(captured_record) > 0
if (has_new_record):
  file.write("\n")

  # write out the new  captured_record
  for field in captured_record:
    file.write(field + ",")

file.close()