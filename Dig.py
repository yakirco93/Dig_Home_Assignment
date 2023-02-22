import pandas as pd
from datetime import datetime

def credit_card (val):
    counter_1 = 0
    counter_2 = 0
    for i in val:
        if i.isdigit():
            counter_1 +=1
        if i == '-':
            counter_2 +=1
    if counter_1 == 16 and counter_2== 3:
        return True
    else:
        return False

def medicare_id(val):
    if not isinstance(val, str):
        return False
    if len(val) != 13:
        return False
    for i in range(13):
        if i in [0, 3, 7,11,12] and not val[i].isdigit():
            return False
        elif i in [1, 5 , 10] and not val[i].isalpha():
            return False
    return True
            
User_file = input(r'Please right the root of your file same like "C:\Users\Yakir\Downloads\financials.csv": ')
file = pd.read_csv(User_file)
new_data = []

for val in file.values.flatten():
    str_val = str(val)
    if credit_card(str_val):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_data.append(['credit card', current_time])
    elif medicare_id(str_val):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_data.append(['medicare id', current_time])

        
new_df = pd.DataFrame(new_data, columns=['Sensitive Values', 'Date'])

        
current_date = datetime.now().strftime('%Y-%m-%d')
output_file = r'C:\Users\Yakir\Downloads\output_{}.csv'.format(current_date)
new_df.to_csv(output_file, index=False)
print('The output file is ready in the same path you specified')