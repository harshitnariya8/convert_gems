import pandas as pd


df = pd.DataFrame(data)

my_data = []

for i in df.index:
    s = df['data'][i].replace(' ','_').replace('-','_').replace('.','').lower()
    
    
    listStr = list(df['data'][i])

    for i,val in enumerate(listStr):
        if val == ' ':
            cap = listStr[i + 1].upper()
            listStr[i + 1] = cap

    listStr[0] = listStr[0].upper()
    finalStr = ''.join(listStr)
    
    my_data.append({'value': s, 'label': finalStr})
    
print(my_data)
f = open('output.txt', 'w')
f.write(str(my_data))  # python will convert \n to os.linesep
f.close()



