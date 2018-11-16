#card_list=[]
card_list=[{'name': 'xm', 'phone': '1', 'qq': '2', 'email': '3'}]

def show_menu():
    """显示菜单"""
    print("*"*50)
    print("欢迎显示【名片管理系统】")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*"*50)

def new_card():
    """新增名片"""
    print("*"*50)
#     print("新增名片")
    
    # 1. add user card info
    name=input("name: ")
    phone=input("phone: ")
    qq=input("qq: ")
    email=input("email: ")
    
    # 2. make user card dict
    card_dict={"name":name,"phone":phone,"qq":qq,"email":email}
    # 3. add dict to list
    card_list.append(card_dict)
    print(card_list)
    # 4. print success
    print("add user card info success!")

def show_all():
    """显示全部"""
    print("*"*50)
    
    if len(card_list) ==0:
        print("no info!")
        return
        #return
    
    for table_head in card_list:
        for k in table_head.keys():
            print("{0}".format(k),end="\t\t")
        print("")
        print("."*50)
        print("")
        break
    
    for card_dict in card_list:
        for v in card_dict.values():
            print("{0}\t\t".format(v),end="")
        print("")
#     print("显示全部")
    
def search_card():
    """搜索名片"""
    print("*"*50)
    
    find_name=input("please enter name: ")
    for card_dict in card_list:
        if card_dict["name"] ==find_name:
            print(card_dict)
            break
    else:
        print("can not find [{0}]".format(find_name))
#     print("搜索名片")