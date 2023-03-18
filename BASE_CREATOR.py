import pandas as pd
# Load the xlsx file
excel_data = pd.read_excel('P.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data)
# Print the content
lst = []
for i in data:
    res = []
    for k in i:
        if k == " " or k == "-":
            res.append("_")   
        elif k in "*.!?,:;#/\//\\+=()'" or k == '"':
            res.append("")  
        else:
            res.append(k)
    if "подкл" in ''.join(res).lower() and len(res) >32:
        res[5:16] = "подкл"
    if "превышение" in ''.join(res).lower() and len(res) >32:
        res[0:10] = "превыш"    
    if res[-1] == "_":
        del res[-1]
    
        
    lst.append(f"{''.join(res)} VARCHAR," + "\n")

print(*lst)
