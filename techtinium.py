


import json

capacity1 ='''
{
     "L": 10,
    "XL": 20,
    "2XL": 40,
    "4XL": 80,
    "8XL": 160,
    "10XL": 320

}

'''
data1 = '''
{
"newyork" :

    {
        "L": 120,
        "XL": 230,
        "2XL": 450,
        "4XL": 774,
        "8XL": 1400,
        "10XL": 2820
    },
"india" :

    {
        "L": 140,
        "XL": "na",
        "2XL": 413,
        "4XL": 890,
        "8XL": 1300,
        "10XL": 2970
    },

"china" :

    {
        "L": 110,
        "XL": 200,
        "2XL": "na",
        "4XL": 670,
        "8XL": 1180,
        "10XL": "na"
    }

}


'''

# utilities


def fetch_plan(units):
    for i in capacity:
        if units ==capacity[i]:
            plan=i
            return plan

def fetch_cost(country,units):
    for i in capacity:
        if units ==capacity[i]:
            plan=i
            break
    for i in data:
        if country ==i:
            return data[country][plan]

    

def sort_by_values(key_value):
    s=sorted(key_value.items(), key = lambda kv:[kv[1], kv[0]])
    return s

def rev_dict_keys(test_dict):
    res=[]
    for ele in test_dict.keys(): 
        res.append(ele) 

    res.reverse()
    return res


def cal_priority_queue():
    seen={}
    for i in data:
        keys=rev_dict_keys(data[i])
        for key in keys:
            if type(data[i][key]) != str:
                pole_plan=key
                pole_factor=key[:-2] if key !="L" else 1
                pole_amount=data[i][key]
                break
        seen[i]={}
        pole_factor=int(pole_factor)
        # print(i)
        for key in keys:
            if type(data[i][key]) != str:
                key_factor=key[:-2] if key !="L" else 0.5
                key_factor= 1 if key_factor =="" else key_factor
                key_factor=float(key_factor)
                mul=pole_factor//key_factor

                amount=int(mul*data[i][key])

                seen[i][key]=amount
        seen[i]=sort_by_values(seen[i])
    return seen
    
def modify_priority_queue(seen):
    seen2={}
    for country in seen:
        seen2[country] = [list(ele) for ele in seen[country]]
    for country in seen2:
        for plan in seen2[country]:
            for model in capacity:
                if plan[0] == model:
                    plan[0]=capacity[model]
        
    return seen2




def get_output(p1,seen2):
    answer={}
    answer["output"]=[]
    for country in seen2:
        p=p1
        total_cost=0
        mac_count=[]
        for plan in seen2[country]:
            if p>0:
                if p<plan[0]:
                    continue
                t=p//plan[0]
                total_cost += t*fetch_cost(country,plan[0])
                # print(total_cost)
                # print(country)
                # print(fetch_cost(country,plan[0]))
                
                mac_id=(fetch_plan(plan[0]),t)
                mac_count.append(mac_id)
                p=p-(t*plan[0])
        dict_1={}
        dict_1["region"]=country
        dict_1["total_cost"]=total_cost
        dict_1["machines"]=mac_count
        answer["output"].append(dict_1)
    return(answer)



def update_capacity(capacity):
    for plan in capacity:
        if plan =="10XL":
                capacity["16XL"]=capacity[plan]
                del capacity[plan]
        

def update_data(data):
    for i in data:
        for plan in data[i]:
            if plan =="10XL":
                data[i]["16XL"]=data[i][plan]
                del data[i][plan]

data = json.loads(data1)
capacity = json.loads(capacity1)


update_data(data)
update_capacity(capacity)


def get_run(p1):
    seen = cal_priority_queue()
    seen2 =modify_priority_queue(seen)
    return get_output(p1,seen2)


p1=int(input('Enter Units Required ::'))
h=int(input('Enter hours Required ::'))

print(get_run(p1))



