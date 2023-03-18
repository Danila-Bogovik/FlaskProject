import pandas as pd
# Load the xlsx file
excel_data = pd.read_excel('P.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data)
# Print the content
lst = []

dickt = {'ь':'', 'ъ':'', 'а':'a', 'б':'b','в':'v',
       'г':'g', 'д':'d', 'е':'e', 'ё':'yo','ж':'zh',
       'з':'z', 'и':'i', 'й':'y', 'к':'k', 'л':'l',
       'м':'m', 'н':'n', 'о':'o', 'п':'p', 'р':'r', 
       'с':'s', 'т':'t', 'у':'u', 'ф':'f', 'х':'h',
       'ц':'ts', 'ч':'ch', 'ш':'sh', 'щ':'sch', 'ы':'yi',
       'э':'e', 'ю':'yu', 'я':'ya'}

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

    if "".join(res) == "Дата_согласования_времени_выезда_инсталлятора_первая":
        res = list("Дата_cогл_врем_выезд_инстал_перв")

    if "".join(res) == "Дата_начала_действия_договора_КУРС":
        res = list("Дата_начала_действ_договора_КУРС")
        
    if "".join(res) == "Дата_регистрации_наряда_на_назначение_ТД":
        res = list("Дата_регистр_наряда_на_назнач_ТД")

    if "".join(res) == "Номер_заявки_из_внешнего_источника":
        res = list("Нмр_заявк_из_внеш_источника")

        
    t = ''
    for i in res:
        t+=dickt.get(i.lower(), i.lower()).upper() if i.isupper() else dickt.get(i, i)
    
    res = list(t)
        
    lst.append(f"{''.join(res)} = db.Column(db.String(255))" + "\n")




    

print(*lst)
