#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cards_tool import *
from re import search

while True:
    # TODO 显示功能菜单
    show_menu()
    
    action_str=input("请选择希望执行的操作：")
    print("您选择的操作是: 【{0}】".format(action_str))
    
    # 1,2,3 名片操作
    if action_str in ["1","2","3"]:
        # 1  新增名片
            if action_str=="1":
                new_card()
        # 2  显示全部
            elif action_str=="2":
                show_all()
        # 3  查询名片
            elif action_str=="3":
                search_card( )
    
    # 0 exit
    elif action_str=="0":
        print("欢迎再次使用！")
        break
    # other error
    else:
        print("输入错误，请重新输入！")