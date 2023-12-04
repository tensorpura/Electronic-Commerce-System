# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:15:59 2021

@author: Acer
"""

import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',password='password',db='onlineshopping')#链接数据库
cur=conn.cursor()#游标，暂存数据库中提取的数据
#查询函数
def table_find(cur, tab_name, col_name = '*', num_line = None):
    sql='SELECT %s FROM %s' % (col_name, tab_name)#sql选择语句
    try:
        cur.execute(sql)#执行sql语句
        Li = cur.fetchall()#返回数据到Li中
        return Li[:num_line]#返回Li的结果
    except:
         messagebox.showerror('错误','出现错误，请重新操作')
#删除函数
def table_delete(cur, tab_name,cols_list, values):
    global tmp
    try:
        list_value=[]
        for i in range(0,len(cols_list)):
            tmp = cols_list[i] + "=" + values[i]#用等于号连接
            list_value.append(str(tmp))#将连接成的字符串增加到list_value中
        delete_value=' and '.join(list_value)#用逗号间隔    
        sql='DELETE FROM {} WHERE {} ' .format(tab_name,delete_value) #sql删除语句
        cur.execute(sql)#执行sql语句
        conn.commit()#提交到数据库中执行，要增加这步，在python中的改变才能同步到数据库中
        messagebox.showinfo('提示','操作成功！')
    except:
         messagebox.showerror('错误','删除数据时出现错误，请检查操作')
#更改函数
def table_update0(cur, tab_name, cols_list, values_list):
    try:
        list_value=[]
        for i in range(1,len(cols_list)):
            tmp = cols_list[i] + "=" + values_list[i]#用等于号连接
            list_value.append(tmp)#将连接成的字符串增加到list_value中
        update_value=','.join(list_value)#用逗号间隔   
        b='UPDATE %s SET %s WHERE %s = %s' % (tab_name, update_value,cols_list[0],values_list[0])#sql更改语句
        cur.execute(b)#执行sql语句
        conn.commit()#提交到数据库中执行，要增加这步，在python中的改变才能同步到数据库中
        messagebox.showinfo('提示','{}操作成功！'.format(update_value))
    except:
        messagebox.showerror('错误','更新数据时出现错误，请重新操作')
        
def table_update(cur, tab_name, cols_list, values_list):
    try:
        list_value=[]
        for i in range(1,len(cols_list)):
            tmp = cols_list[i] + "='" + values_list[i]+"'"#用等于号连接
            
            list_value.append(tmp)#将连接成的字符串增加到list_value中
        update_value=','.join(list_value)#用逗号间隔   
        b='UPDATE %s SET %s WHERE %s = %s' % (tab_name, update_value,cols_list[0],values_list[0])#sql更改语句
        cur.execute(b)#执行sql语句
        conn.commit()#提交到数据库中执行，要增加这步，在python中的改变才能同步到数据库中
        messagebox.showinfo('提示','{}操作成功！'.format(update_value))
    except:
        messagebox.showerror('错误','更新数据时出现错误，请重新操作')
#增加函数
def table_insert0(cur, tab_name, values_list):
    try:
        list_value=[]
        for i in range(0,len(values_list)):#注意，是从0开始
            tmp = values_list[i]
            list_value.append(tmp)#将values_list一个个接到list_value中
            insert_values=','.join(values_list)#根据sql格式，用逗号间隔
        print('INSERT INTO {} VALUES({})' .format(tab_name, insert_values))
        cur.execute('INSERT INTO {} VALUES({})' .format(tab_name, insert_values))#sql增加函数
        conn.commit()#提交到数据库中执行，要增加这步，在python中的改变才能同步到数据库中
        messagebox.showinfo('提示','操作成功！')
    except:
        messagebox.showerror('错误','出现错误，请重新操作')
def table_insert(cur, tab_name, values_list):
    try:
        list_value=[]
        for i in range(0,len(values_list)):#注意，是从0开始
            tmp = '\'{}\''.format(values_list[i])
            list_value.append(tmp)#将values_list一个个接到list_value中
        insert_values=','.join(list_value)#根据sql格式，用逗号间隔
        print('INSERT INTO {} VALUES({})' .format(tab_name, insert_values))
        cur.execute('INSERT INTO {} VALUES({})' .format(tab_name, insert_values))#sql增加函数
        conn.commit()#提交到数据库中执行，要增加这步，在python中的改变才能同步到数据库中
        messagebox.showinfo('提示','操作成功！')
    except:
        messagebox.showerror('错误','插入数据库出现错误，请重新操作')
#计数统计函数，统计数组的元素总数
def table_count(cur,tab_name,col_name):
    sql='SELECT %s FROM %s' % (col_name, tab_name)#sql选择语句
    cur.execute(sql)#执行sql语句
    Li = cur.fetchall()#返回数据到Li中
    global n
    n=len(Li)
    return n
#排序函数
def table_rank(cur,tab_name,col_name = '*', num_line = None):
    cur.execute('SELECT %s FROM %s' % (col_name, tab_name))#选择数组
    L = cur.fetchall()#存放数组
    for i in range(1,len(cols_list)):#冒泡排序
        for j in range(1,len(cols_list)-1):
            if L[i]>=L[j]:
                k=L[i]
                L[i]=L[j]
                L[j]=k
    return L[:num_line]#返回排序结果

# cur.close() # 关闭游标
# conn.close() # 关闭连接




from tkinter import *
import time
import tkinter
from tkinter import ttk
#函数池 （所有预定义函数要在每一个界面前定义好）
def get_time():  # 屏幕刷新时间
    time_str = time.strftime("%H:%M:%S", time.localtime())  # 获得系统现在时间
    label_4.configure(text=time_str)  # 重新设置文本标签
    my_windows.after(1000, get_time)
def run(x):  # 确定账号
    a=x
    tmp=0
    pyusers=table_find(cur,'users')
    global admno
    for i in range(0,len(pyusers)):
        if inp1.get() == pyusers[i][0] and inp2.get() == pyusers[i][1]:
            tmp=pyusers[i][2]
    if tmp=='管理员':  # 判断用户类别
         pyadmin=table_find(cur,'administrator')
         for i in range(0,len(pyadmin)):
            if inp1.get()== pyadmin[i][1]:
                admno=pyadmin[i][0]
                break
            else:
                continue
         s = "尊敬的管理员:{}登录成功！\n".format(a)
         txt.insert('end', s)  # 追加显示运算结果
         inp1.delete(0, 'end')  # 清空输入
         inp2.delete(0, 'end')  # 清空输入
         new_windows_admin(my_windows)  # 进去新界面
         my_windows.withdraw()
    elif tmp=='顾客':
         global cno
         pycustom=table_find(cur,'customer')
         for i in range(0,len(pycustom)):
            if inp1.get()== pycustom[i][1]:
                cno=pycustom[i][0]
                break
            else:
                continue
         s = "尊敬的顾客:{}登录成功！\n".format(a)
         txt.insert('end', s)
         inp1.delete(0, 'end')  # 清空输入
         inp2.delete(0, 'end')  # 清空输入
         new_windows_customer(my_windows)  # 进去新界面
         my_windows.withdraw()
    elif tmp=='商家':  # 判断用户类别
         global sno
         pyseller=table_find(cur,'seller')
         for i in range(0,len(pyseller)):
            if inp1.get()== pyseller[i][1]:
                sno=pyseller[i][0]
                admno=pyseller[i][2]
                break
            else:
                continue
         s = "尊敬的商家:{}登录成功！\n".format(a)
         txt.insert('end', s)  # 追加显示运算结果
         inp1.delete(0, 'end')  # 清空输入
         inp2.delete(0, 'end')  # 清空输入
         new_windows_merchant(my_windows)# 进去新界面
         my_windows.withdraw()
    else:
         s = "信息输入错误！请重新输入！\n"
         txt.insert('end', s)  # 追加显示运算结果
         inp1.delete(0, 'end')  # 清空输入
         inp2.delete(0, 'end')  # 清空输入
         
         
        
        
        
def sign(): # 定义一个注册函数
    def sign_up():
        np=entry_usr_pwd.get()
        npf=entry_usr_pwd_confirm.get()
        nn=entry_new_name.get()
        if len(nn)>12 or len(nn)<6:
            messagebox.showerror('错误','账号长度应在6-12位间')
        elif np!=npf:
            messagebox.showerror('错误','两次密码输入不一致')
        elif len(np)>12 or len(np)<6:
            messagebox.showerror('错误','密码长度应在6-12位间')
        for i in range(0,len(pyusers)):
            if nn == pyusers[i][0]:
                messagebox.showerror('错误','该账号已被注册')
                return()
        table_insert(cur,'users',[nn,np,'顾客'])
         
    window_sign=Toplevel(my_windows)
    window_sign.geometry(align_str)
    window_sign.resizable(width=True,height=True)
    window_sign.title('注册界面(测试阶段，仅提供顾客注册！)')
    
    new_name=StringVar()
    Label(window_sign, text='账号: ').place(relx=0.3, rely=0.2)
    entry_new_name = Entry(window_sign, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(relx=0.4, rely=0.2) 
 
    new_password=StringVar()
    Label(window_sign, text='密码: ').place(relx=0.3, rely=0.3)
    entry_usr_pwd = Entry(window_sign, textvariable=new_password, show='*')
    entry_usr_pwd.place(relx=0.4, rely=0.3)
 
    new_password_confirm=StringVar()
    Label(window_sign, text='确认密码: ').place(relx=0.3, rely=0.4)
    entry_usr_pwd_confirm = Entry(window_sign, textvariable=new_password_confirm, show='*')
    entry_usr_pwd_confirm.place(relx=0.4, rely=0.4)
    
    btn_comfirm_sign_up = Button(window_sign, text='顾客注册', command=lambda:sign_up())
    btn_comfirm_sign_up.place(relx=0.4, rely=0.6)
    

def back(windows):
    windows.withdraw()
    
def new_windows_admin(windows):  # 创建管理员窗口函数
    
    def admincheck():
        def delButton(tree):
            x=tree.get_children()
            for item in x:
                tree.delete(item)
        def get_selection():
            try:
                tmp=sell_tree.item(sell_tree.focus())
                a=tmp['values'][0]
                return a
            except:
                messagebox.showerror('错误','获取选中项出现错误，请重新操作')
                return
        def goods_drop():
          tmp=str(get_selection())
          cols_list=('gno','state')
          values_list=(tmp,'下架')
          table_update(cur, 'goods', cols_list, values_list)
          sell_tree_show('gno')
        def good_addselect():
          tmp=str(get_selection())
          cols_list=('gno','state')
          values_list=(tmp,'在售')
          table_update(cur, 'goods', cols_list, values_list)
          sell_tree_show('gno')        
        def sell_tree_show(a):
          delButton(sell_tree)
          pygoods=table_find(cur,'goods'+str(a))
          for i in range(0,len(pygoods)):
              if pygoods[i][1]!= 0:
                    sell_tree.insert('', END, values=(pygoods[i][0],)+pygoods[i][1:8])
                    
                    
        window_admincheck=Toplevel()
        window_admincheck.title('查看商品')
        window_admincheck.geometry(align_str)
        cols = ['商品编号','商家编号', '商品种类编号', '商品名', '库存量', '商品介绍', '商品价格','商品状态']
        sell_tree=ttk.Treeview(window_admincheck,height=8,columns=cols,show='headings')
        sell_tree.heading(column='商品编号', text='商品编号', anchor='w',command=lambda:sell_tree_show('gno'))  # 定义表头
        sell_tree.heading('商家编号', text='商家编号',command=lambda:sell_tree_show('sno') )  # 定义表头
        sell_tree.heading('商品种类编号', text='商品种类编号',command=lambda:sell_tree_show('gcno') )  # 定义表头
        sell_tree.heading('商品名', text='商品名', )  # 定义表头
        sell_tree.heading('库存量', text='库存量', )  # 定义表头
        sell_tree.heading('商品介绍', text='商品介绍', )  # 定义表头
        sell_tree.heading('商品价格', text='商品价格', )  # 定义表头
        sell_tree.heading('商品状态', text='商品状态', )  # 定义表头
        sell_tree.column('商品编号', width=45, minwidth=45, anchor=S)  # 定义列
        sell_tree.column('商家编号', width=45, minwidth=45, anchor=S)  # 定义列
        sell_tree.column('商品种类编号', width=90, minwidth=80, anchor=S)  # 定义列
        sell_tree.column('商品名', width=100, minwidth=100, anchor=S)  # 定义列
        sell_tree.column('库存量', width=60, minwidth=60, anchor=S)  # 定义列
        sell_tree.column('商品介绍', width=200, minwidth=100, anchor=S)  # 定义列
        sell_tree.column('商品价格', width=60, minwidth=60, anchor=S)  # 定义列
        sell_tree.column('商品状态', width=60, minwidth=60, anchor=S)  # 定义列 
        sell_tree_show('gno')
        sell_tree.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.5)
        Button(window_admincheck,text='上架选中商品',command=lambda:good_addselect()).place(relx=0.5,rely=0.6,relwidth=0.15,relheight=0.1)       
        Button(window_admincheck,text='下架选中商品',command=lambda:goods_drop()).place(relx=0.3,rely=0.6,relwidth=0.15,relheight=0.1)
        lab1=Label(window_admincheck,text='点击前三列表头进行排序')
        lab1.place(relx=0.4,rely=0.8)
        btn_back=Button(window_admincheck,text='back',command=lambda:[back(window_admincheck),winNew1.deiconify()])
        btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)
    def cuscheck():
        def delButton(tree):
            x=tree.get_children()
            for item in x:
                tree.delete(item)
        def tree_show():
          delButton(collect_tree)
          pycustom=table_find(cur,'customer')
          for i in range(0,len(pycustom)):
              if pycustom[i][1]!= 0:
                    collect_tree.insert('', END, values=(pycustom[i][0],)+pycustom[i][1:7])
        cols = ['顾客编号','顾客账号', '顾客名称', '顾客电话','顾客地址','银行','银行账户']
        window_cuscheck=Toplevel()
        window_cuscheck.title('查看顾客')
        window_cuscheck.geometry(align_str)
        collect_tree=ttk.Treeview(window_cuscheck,height=8,columns=cols,show='headings')
        collect_tree.heading(column='顾客编号', text='顾客编号', anchor='w')  # 定义表头
        collect_tree.heading('顾客账号', text='顾客账号', )  # 定义表头
        collect_tree.heading('顾客名称', text='顾客名称', )  # 定义表头
        collect_tree.heading('顾客电话', text='顾客电话', )  # 定义表头
        collect_tree.heading('顾客地址', text='顾客地址', )  # 定义表头
        collect_tree.heading('银行', text='银行', )  # 定义表头
        collect_tree.heading('银行账户', text='银行账户', )  # 定义表头
        collect_tree.column('顾客编号', width=45, minwidth=45, anchor=S)  # 定义列
        collect_tree.column('顾客账号', width=45, minwidth=45, anchor=S)  # 定义列
        collect_tree.column('顾客名称', width=90, minwidth=80, anchor=S)  # 定义列
        collect_tree.column('顾客电话', width=100, minwidth=100, anchor=S)  # 定义列
        collect_tree.column('顾客地址', width=45, minwidth=45, anchor=S)  # 定义列
        collect_tree.column('银行', width=45, minwidth=45, anchor=S)  # 定义列
        collect_tree.column('银行账户', width=90, minwidth=80, anchor=S)  # 定义列
        tree_show()
        collect_tree.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.5)
        btn_back=Button(window_cuscheck,text='back',command=lambda:[back(window_cuscheck),winNew1.deiconify()])
        btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)
    def show_after():
        def delButton(tree):
            x=tree.get_children()
            for item in x:
                tree.delete(item)
        def get_selection():
            try:
                tmp=after_tree.item(after_tree.focus())
                a=tmp['values'][0]
                return a
            except:
                messagebox.showerror('错误','获取选中项出现错误，请重新操作')
                return
        def after_tree_show():
            delButton(after_tree)
            pyafter=table_find(cur,'aftersales')
            for i in range(0,len(pyafter)):
              if pyafter[i][1]!= 0:
                    after_tree.insert('', END, values=(pyafter[i][0],)+pyafter[i][1:4])
        def mess_delete():
            tmp=str(get_selection())
            a=tkinter.messagebox.askyesno('提示', '要执行此操作吗')
            if a:
                 table_delete(cur, 'aftersales',('aftno',),(tmp,))
                 after_tree_show()
                 return()
       
        def mess_cho():
            try:
                tmp=after_tree.item(after_tree.focus())
                a=tmp['values'][1]
                delButton(after_tree)
                pyafter=table_find(cur,'aftersales')
                for i in range(0,len(pyafter)):
                    if pyafter[i][1]== a:
                        after_tree.insert('', END, values=(pyafter[i][0],)+pyafter[i][1:4])
            except:
                messagebox.showerror('错误','请重试!')
          
                
                
        
        window_admafter=Toplevel()
        window_admafter.title('管理员售后查询')
        window_admafter.geometry(align_str)
        cols = ['消息编号','订单编号','发送人', '消息内容']
        after_tree=ttk.Treeview(window_admafter,height=8,columns=cols,show='headings')
        after_tree.heading(column='消息编号', text='消息编号', anchor='w')  # 定义表头
        after_tree.heading('订单编号', text='订单编号', )  # 定义表头
        after_tree.heading('发送人', text='发送人', )  # 定义表头
        after_tree.heading('消息内容', text='消息内容', )  # 定义表头
        after_tree.column('消息编号', width=45, minwidth=45, anchor=S)  # 定义列
        after_tree.column('订单编号', width=45, minwidth=45, anchor=S)  # 定义列
        after_tree.column('发送人', width=70, minwidth=70, anchor=S)
        after_tree.column('消息内容', width=100, minwidth=100, anchor=S)
        after_tree.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.5)# 定义列
        after_tree_show()
        
        btn_delete=Button(window_admafter,text='删除',command=lambda:mess_delete())
        btn_delete.place(relx=0.6,rely=0.7,relwidth=0.1,relheight=0.1)
        
        btn_delete=Button(window_admafter,text='只展示选中订单号的消息',command=lambda:mess_cho())
        btn_delete.place(relx=0.3,rely=0.7,relwidth=0.2,relheight=0.1)
        
        btn_delete=Button(window_admafter,text='展示全部订单',command=lambda:after_tree_show())
        btn_delete.place(relx=0.1,rely=0.7,relwidth=0.15,relheight=0.1)
        
        btn_back=Button(window_admafter,text='back',command=lambda:[back(window_admafter),winNew1.deiconify()])
        btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)
        
        
        
    def show_gc():
        def delButton(tree):
            x=tree.get_children()
            for item in x:
                tree.delete(item)
        def tree_show():
          delButton(gc_tree)
          pygc=table_find(cur,'goodscategory')
          for i in range(0,len(pygc)):
              gc_tree.insert('', END, values=pygc[i])
        def get_selection():
            try:
                tmp=gc_tree.item(gc_tree.focus())
                a=tmp['values'][0]
                return a
            except:
                messagebox.showerror('错误','获取选中项出现错误，请重新操作')
                return
            
        
             
      
        
        def gc_ins():
            if entry.get()!='':
               values_list=['default',"'"+str(entry.get())+"'"]
               table_insert0(cur, 'goodscategory', values_list) 
               tree_show()
            else:
               messagebox.showerror('错误','无输入') 
            
            
        def gc_del():
            if get_selection()!='':
                tmp=str(get_selection())
                a=tkinter.messagebox.askyesno('提示', '要执行此操作吗')
                if a:
                      table_delete(cur, 'goodscategory',('gcno',),(tmp,))
                      tree_show()
                      return()
            
        def gc_cha():
            if entry.get()=='':
                messagebox.showerror('错误','无输入')
                return
            if get_selection()=='':
                messagebox.showerror('错误','无选中')
                return
            
            tmp=str(get_selection())
            cols_list=('gcno','categoryname')
            values_list=(tmp,str(entry.get()))
            table_update(cur, 'goodscategory', cols_list, values_list)
            tree_show()
        
        window_gc=Toplevel()
        window_gc.title('商品类别信息')
        window_gc.geometry(align_str)
        
        cols = ['商品类别编号','商品类别名']
        gc_tree=ttk.Treeview(window_gc,height=8,columns=cols,show='headings')
        gc_tree.heading(column='商品类别编号', text='商品类别编号', anchor='w')  # 定义表头
        gc_tree.heading('商品类别名', text='商品类别名', )  # 定义表头

        gc_tree.column('商品类别编号', width=45, minwidth=45, anchor=S)  # 定义列
        gc_tree.column('商品类别名', width=45, minwidth=45, anchor=S)  # 定义列

        tree_show()
        gc_tree.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.5)
        
        
        lab1=Label(window_gc,text='如果有属于该类别的商品，则该类别不可删除')
        lab1.place(relx=0.2,rely=0.9)
        entry= Entry(window_gc)
        entry.place(relx=0.1, rely=0.6,relwidth=0.2,relheight=0.1)
        
        btn1=Button(window_gc,text='插入',command=lambda:gc_ins())
        btn1.place(relx=0.1,rely=0.75,relwidth=0.2,relheight=0.1)
        
        btn2=Button(window_gc,text='选中行删除',command=lambda:gc_del())
        btn2.place(relx=0.5,rely=0.6,relwidth=0.2,relheight=0.1)
        
        btn3=Button(window_gc,text='选中行更改',command=lambda:gc_cha())
        btn3.place(relx=0.5,rely=0.75,relwidth=0.2,relheight=0.1)
        
        btn_back=Button(window_gc,text='back',command=lambda:[back(window_gc),winNew1.deiconify()])
        btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)
        
        
        
        
    winNew1 = Toplevel()
    winNew1.geometry(align_str)  # 设置窗口大小保持和主窗口相同
    winNew1.resizable(width=True, height=True)
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    winNew1.title('管理员界面')
    label_a1 = Label(winNew1, text="尊敬的管理员您好", fg="red", font=("宋体", 26), relief=GROOVE).pack()
    label_b1 = Label(winNew1, text="管理员功能", font=("宋体", 20)).pack()
    
    btn_cuscheck=Button(winNew1,text='查看顾客信息',command=lambda:[cuscheck(),winNew1.withdraw()])
    btn_cuscheck.place(relx=0.2,rely=0.3,relwidth=0.2,relheight=0.12)
    
    btn_admincheck=Button(winNew1,text='查看商品信息',command=lambda:[admincheck(),winNew1.withdraw()])
    btn_admincheck.place(relx=0.2,rely=0.5,relwidth=0.2,relheight=0.12)
    
    btn_after=Button(winNew1,text='售后查询',command=lambda:[show_after(),winNew1.withdraw()])
    btn_after.place(relx=0.6,rely=0.3,relwidth=0.2,relheight=0.12)
    
    btn_after=Button(winNew1,text='商品分类信息',command=lambda:[show_gc(),winNew1.withdraw()])
    btn_after.place(relx=0.6,rely=0.5,relwidth=0.2,relheight=0.12)
    
    
    
    btn_back=Button(winNew1,text='back',command=lambda:[back(winNew1),my_windows.deiconify()])
    btn_back.place(relx=0.7,rely=0.7,relwidth=0.1,relheight=0.05)
    

    
def new_windows_customer(windows):  # 创建顾客窗口函数

    def info(): #个人信息界面
        
        def alter():
            pycustomer=table_find(cur,'customer')
            for i in range(0,len(pycustomer)):
                if pycustomer[i][0]==cno:
                    me=pycustomer[i]
            tmp=str(cno)
            name=entry_name.get()
            telnum=entry_telnum.get()
            address=entry_address.get()
            bank=entry_bank.get()
            bcnum=entry_bcnum.get()
            
            if str(name)==me[2] and str(telnum)==me[3] and str(bank)==me[5] and str(bcnum)==me[6] and str(address)==me[4]:
                messagebox.showinfo('提示','未修改！') 
                return
     
            a=tkinter.messagebox.askyesno('提示', '要执行此操作吗')
            if a:
                if name!=me[2]:
                    cols_list=['cno','name']
                    values_list=[tmp,str(name)]
                    
                    table_update(cur, 'customer', cols_list, values_list)
                if telnum!=me[3]:
                    cols_list=['cno','telnum']
                    values_list=[tmp,str(telnum)]
                    table_update(cur, 'customer', cols_list, values_list)
                if bank!=me[5]:
                    cols_list=['cno','bank']
                    values_list=[tmp,str(bank)]
                    table_update(cur, 'customer', cols_list, values_list)
                if bcnum!=me[6]:
                    cols_list=['cno','bcnum']
                    values_list=[tmp,str(bcnum)]
                    table_update(cur, 'customer', cols_list, values_list)
                if address!=me[4]:
                    cols_list=['cno','address']
                    values_list=[tmp,str(address)]
                    table_update(cur, 'customer', cols_list, values_list)
                messagebox.showinfo('提示','设置成功！') 
            
            
            
        
        window_info=Toplevel()
        window_info.title('个人信息')
        window_info.geometry(align_str)
        
        pycustomer=table_find(cur,'customer')
        for i in range(0,len(pycustomer)):
            if pycustomer[i][0]==cno:
                me=pycustomer[i]
                # print(me)
        
        Label(window_info,text='账号').place(relx=0.15,rely=0.2)
        account=StringVar(master=window_info)
        account.set(me[1])
        entry_account=Entry(window_info,textvariable=account,state='readonly')
        entry_account.place(relx=0.2,rely=0.2,relwidth=0.15,relheight=0.05)
        
        Label(window_info,text='昵称').place(relx=0.45,rely=0.2)
        name=StringVar(master=window_info)
        name.set(me[2])
        entry_name=Entry(window_info,textvariable=name)
        entry_name.place(relx=0.5,rely=0.2,relwidth=0.15,relheight=0.05)
        
        Label(window_info,text='联系方式').place(relx=0.7,rely=0.2)
        telnum=StringVar(master=window_info)
        telnum.set(me[3])
        entry_telnum=Entry(window_info,textvariable=telnum)
        entry_telnum.place(relx=0.8,rely=0.2,relwidth=0.15,relheight=0.05)
        
        Label(window_info,text='地址').place(relx=0.15,rely=0.5)
        address=StringVar(master=window_info)
        address.set(me[4])
        entry_address=Entry(window_info,textvariable=address)
        entry_address.place(relx=0.2,rely=0.5,relwidth=0.15,relheight=0.05)
     
        Label(window_info,text='付款银行').place(relx=0.42,rely=0.5)
        bank=StringVar(master=window_info)
        bank.set(me[5])
        entry_bank=Entry(window_info,textvariable=bank)
        entry_bank.place(relx=0.5,rely=0.5,relwidth=0.1,relheight=0.05)
        
        Label(window_info,text='银行卡号').place(relx=0.72,rely=0.5)
        bcnum=StringVar(master=window_info)
        bcnum.set(me[6])
        entry_bcnum=Entry(window_info,textvariable=bcnum)
        entry_bcnum.place(relx=0.8,rely=0.5,relwidth=0.15,relheight=0.05)
        
        
        btn_back=Button(window_info,text='保存更改',command=lambda:alter())
        btn_back.place(relx=0.6,rely=0.7,relwidth=0.1,relheight=0.05) 
        
        btn_back=Button(window_info,text='back',command=lambda:[back(window_info),winNew2.deiconify()])
        btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)    
        
    def check():#查看商品
        #判断函数，用于判断是否存在单号以及是否数量满足，a是商品编号，b是数量        
        def delButton(tree):
            x=tree.get_children()
            for item in x:
                tree.delete(item)
                
        def newdan(a,b): 
            pycustomer=table_find(cur,'customer')
            for i in range(0,len(pycustomer)):
                if pycustomer[i][0]==cno:
                    me=pycustomer[i]
            for i in range(3,7):
                if str(me[i])=='None':
                    messagebox.showinfo('提醒','请完善个人信息')
                    return
                    
                    
            pynewdan=table_find(cur,'goods')
            danhao=a.get()
            number=b.get()
            for i in range(0,len(pynewdan)):
                if danhao == pynewdan[i][0] and number <=pynewdan[i][4] and number >0 and pynewdan[i][7]=='在售':
                    q=i
                    break
                else:
                    q=-1
                    continue #判断是否存在这样的单号
            if q ==-1:
                messagebox.showerror('错误','请核对您的单号、数量以及商品状态')
            else:# 否则将订单插入到订单表中
                gno=pynewdan[q][0]
                now = time.strftime("%H:%M:%S", time.localtime())
                add_newdan=['default',str(cno),str(gno),str(number),"'"+'待发货'+"'","'"+now+"'",'default']
                try:
                    table_insert0(cur,'orders',add_newdan)
                    sell_tree_show()
                    messagebox.showinfo('您好','您已成功下单')
                except:
                    messagebox.showerror('您好','wrong')
                 
        def sell_tree_show():
          delButton(sell_tree)
          pygoods=table_find(cur,'extragoods')
          for i in range(0,len(pygoods)):
              if pygoods[i][2]== '在售':
                    sell_tree.insert('', END, values=pygoods[i][0:2]+(pygoods[i][6],)+pygoods[i][3:6]+pygoods[i][7:9])
                    
        window_check=Toplevel()
        window_check.title('查看商品')
        window_check.geometry(align_str)
        cols = ['商品编号','商品名','商品价格', '库存量', '商品介绍','商家编号', '商家名称','商品种类']
        sell_tree=ttk.Treeview(window_check,height=8,columns=cols,show='headings')
        sell_tree.heading(column='商品编号', text='商品编号', anchor='w')  # 定义表头
        sell_tree.heading('商品名', text='商品名', )  # 定义表头
        sell_tree.heading('商品价格', text='商品价格', )  # 定义表头
        sell_tree.heading('库存量', text='库存量', )  # 定义表头
        sell_tree.heading('商品介绍', text='商品介绍', )  # 定义表头
        sell_tree.heading('商家编号', text='商家编号', )  # 定义表头
        sell_tree.heading('商家名称', text='商家名称', )  # 定义表头
        sell_tree.heading('商品种类', text='商品种类', )  # 定义表头
        
        sell_tree.column('商品编号', width=80, minwidth=45, anchor=S)  # 定义列
        sell_tree.column('商品名', width=110, minwidth=100, anchor=S)  # 定义列
        sell_tree.column('商品价格', width=80, minwidth=60, anchor=S)  # 定义列
        sell_tree.column('库存量', width=60, minwidth=60, anchor=S)  # 定义列
        sell_tree.column('商品介绍', width=200, minwidth=100, anchor=S)  # 定义列
        sell_tree.column('商家编号', width=80, minwidth=45, anchor=S)  # 定义列
        sell_tree.column('商家名称', width=80, minwidth=45, anchor=S)  # 定义列
        sell_tree.column('商品种类', width=110, minwidth=80, anchor=S)  # 定义列 
        
        sell_tree_show()
        
        sell_tree.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.5)
        
        new_danhao=IntVar(master=window_check)
        Label(window_check,text='商品编号').place(relx=0.15,rely=0.65)
        entry_new_danhao=Entry(window_check,textvariable=new_danhao)
        entry_new_danhao.place(relx=0.25,rely=0.65)
        
        new_number=IntVar(master=window_check)
        Label(window_check,text='数量').place(relx=0.15,rely=0.75)
        entry_new_number=Entry(window_check,textvariable=new_number)
        entry_new_number.place(relx=0.25,rely=0.75)
        
        
        button_ok=Button(window_check,text='下单',command=lambda:newdan(new_danhao, new_number))
        button_ok.place(relx=0.6,rely=0.68,relwidth=0.1,relheight=0.07)
        
        
        btn_back=Button(window_check,text='back',command=lambda:[back(window_check),winNew2.deiconify()])
        btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)
        
    
    def show_collect():
        
        def delButton(tree):
            x=tree.get_children()
            for item in x:
                tree.delete(item)
                
        def collect_add(a):
           pynewdan=table_find(cur,'goods')
           add_num=a.get()
           for i in range(0,len(pynewdan)):
              if add_num == pynewdan[i][0]:
                  if pynewdan[i][7]=='下架':
                      messagebox.showinfo('提示','该商品已经下架')
                      return
            
           for i in range(0,len(pynewdan)):
            if add_num == pynewdan[i][0]:
              messagebox.showinfo('您好','您的收藏已添加')
              q=i
              break
            else:
              q=-1
              continue #判断是否存在这样的单号
           if q ==-1:
              messagebox.showerror('错误','收藏列表内没有找到此商品')
           else: # 否则将收藏插入到收藏表中
             gno=pynewdan[q][0]
             add_collect=[str(cno),str(gno)]
             table_insert(cur, 'collection', add_collect)
             collect_tree_show()
        def collect_delete(a):
            pycollect=table_find(cur,'collection')
            delete_num=a.get()
            for i in range(0,len(pycollect)):
             if cno==pycollect[i][0] and delete_num == pycollect[i][1]:
                table_delete(cur, 'collection', ['cno','gno'], [str(cno),str(delete_num)]) 
                messagebox.showinfo('您好','您的收藏已删除')
                collect_tree_show()
                q=i
                break
             else:
                q=-1
                continue
            if q ==-1:
              messagebox.showerror('错误','没有找到此商品')
        
        def collect_tree_show():
            delButton(collect_tree)
            pygoods=table_find(cur,'extragoods')
            pycollect=table_find(cur,'collection')
            for i in range(0,len(pycollect)):
                if pycollect[i][0]== cno:# 查找到此顾客的收藏列表 并打印
                    his_collect=pycollect[i][1]
                    for t in range(0,len(pygoods)):
                        if pygoods[t][0]==his_collect:
                          collect_tree.insert('', END, values=pygoods[t][0:2]+(pygoods[t][5],)+pygoods[t][7:9])        
        
        window_collect=Toplevel()
        window_collect.title('我的收藏')
        window_collect.geometry(align_str)
        
        cols = ['商品编号','商品名','商家编号','商家名', '商品种类' ]
        collect_tree=ttk.Treeview(window_collect,height=8,columns=cols,show='headings')
        collect_tree.heading(column='商品编号', text='商品编号', anchor='w')  # 定义表头
        collect_tree.heading('商品名', text='商品名', )  # 定义表头
        collect_tree.heading('商家编号', text='商家编号', )  # 定义表头
        collect_tree.heading('商家名', text='商家名', )  # 定义表头
        collect_tree.heading('商品种类', text='商品种类', )  # 定义表头
        
        
        collect_tree.column('商品编号', width=45, minwidth=45, anchor=S)  # 定义列
        collect_tree.column('商品名', width=100, minwidth=100, anchor=S)  # 定义列
        collect_tree.column('商家编号', width=45, minwidth=45, anchor=S)  # 定义列
        collect_tree.column('商家名', width=45, minwidth=45, anchor=S)  # 定义列
        collect_tree.column('商品种类', width=90, minwidth=80, anchor=S)  # 定义列
        
        
        collect_tree_show()
        collect_tree.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.5)
        
        collect_num=IntVar(master=window_collect)
        collect_entry=Entry(window_collect,textvariable=collect_num)
        collect_entry.place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.1)
        
        Button(window_collect,text='添加',command=lambda:collect_add(collect_num)).place(relx=0.4,rely=0.75,relwidth=0.1,relheight=0.07)#点击添加按钮添加收藏商品
        Button(window_collect,text='删除',command=lambda:collect_delete(collect_num)).place(relx=0.52,rely=0.75,relwidth=0.1,relheight=0.07)
        
        btn_back=Button(window_collect,text='back',command=lambda:[back(window_collect),winNew2.deiconify()])
        btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)
        
    def show_order():
        
        def get_selection():
            try:
                tmp=orders_tree.item(orders_tree.focus())
                a=tmp['values'][0]
                return a
            except:
                messagebox.showerror('错误','获取选中项出现错误，请重新操作')
                return
        # def test():
        #     tmp=orders_tree.item(orders_tree.focus())
        #     a=tmp['values'][0]
        #     b=tmp['values'][9]
        #     print(a,b)
        
        def orders_alter():
            tmp=orders_tree.item(orders_tree.focus())
            if tmp['values'][6]!='待收货':
                messagebox.showerror('错误','请检查订单状态')
                return  
            tmp=str(get_selection())
            cols_list=('ono','state')
            values_list=(tmp,'已收货')
            table_update(cur, 'orders', cols_list, values_list)
            orders_tree_show()
            
        def orders_review():
            a=entry_review.get()
            tmp=orders_tree.item(orders_tree.focus())
            if tmp['values'][6]!='已收货':
                messagebox.showerror('错误','订单未收货')
                return  
            tmp=str(get_selection())
            cols_list=('ono','remark')
            values_list=(tmp,a)
            table_update(cur, 'orders', cols_list, values_list)
            orders_tree_show()
            
        
        def delButton(tree):
            x=tree.get_children()
            for item in x:
                tree.delete(item)
                
        def orders_tree_show():
            delButton(orders_tree)
            pyorders=table_find(cur,'extraorder2')
            for i in range(0,len(pyorders)):
                if pyorders[i][0]==cno:
                    orders_tree.insert('', END, values=pyorders[i][1:15])
                    
        

        # pysellers=table_find(cur,'seller')
        
        window_dancheck1=Toplevel()
        window_dancheck1.title('我的订单')
        window_dancheck1.geometry('1500x600+200+120')
        
        pyorders=table_find(cur,'extraorder')
        
        cols = ['订单编号', '商品名称','商品编号','商品单价','商品数量','订单总价', 
                '订单状态','下单时间','收货地址','评价', 
                '商家编号', '商家名','商家电话','管理员电话'
                ]
        orders_tree=ttk.Treeview(window_dancheck1,height=8,columns=cols,show='headings')
        
        orders_tree.heading(column='订单编号', text='订单编号', anchor='w')  # 定义表头
        orders_tree.heading('商品名称', text='商品名称', )  # 定义表头
        orders_tree.heading('商品编号', text='商品编号', )  # 定义表头
        orders_tree.heading('商品单价', text='商品单价', )  # 定义表头
        orders_tree.heading('商品数量', text='商品数量', )  # 定义表头
        
        orders_tree.heading('订单总价', text='订单总价', )  # 定义表头
        orders_tree.heading('订单状态', text='订单状态', )  # 定义表头
        orders_tree.heading(column='下单时间', text='下单时间', anchor='w')  # 定义表头
        orders_tree.heading('收货地址', text='收货地址', )  # 定义表头
        orders_tree.heading('评价', text='评价', )  # 定义表头
        
        orders_tree.heading('商家编号', text='商家编号', )  # 定义表头
        orders_tree.heading('商家名', text='商家名', )  # 定义表头
        orders_tree.heading('商家电话', text='商家电话', )  # 定义表头
        orders_tree.heading('管理员电话', text='管理员电话', )  # 定义表头
        
        
        orders_tree.column('订单编号', width=80, minwidth=60, anchor=S)  # 定义列
        orders_tree.column('商品名称', width=80, minwidth=80, anchor=S)  # 定义列
        orders_tree.column('商品编号', width=80, minwidth=80, anchor=S)  # 定义列
        orders_tree.column('商品单价', width=110, minwidth=60, anchor=S)  # 定义列
        orders_tree.column('商品数量', width=100, minwidth=100, anchor=S)  # 定义列
        
        orders_tree.column('订单总价', width=80, minwidth=60, anchor=S)  # 定义列
        orders_tree.column('订单状态', width=80, minwidth=60, anchor=S)  # 定义列
        orders_tree.column('下单时间', width=80, minwidth=60, anchor=S)  # 定义列
        orders_tree.column('收货地址', width=80, minwidth=80, anchor=S)  # 定义列
        orders_tree.column('评价', width=80, minwidth=80, anchor=S)  # 定义列
        
        orders_tree.column('商家编号', width=80, minwidth=80, anchor=S)  # 定义列
        orders_tree.column('商家名', width=100, minwidth=100, anchor=S)  # 定义列
        orders_tree.column('商家电话', width=80, minwidth=80, anchor=S)  # 定义列
        orders_tree.column('管理员电话', width=100, minwidth=100, anchor=S)  # 定义列
        
        orders_tree.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.5)
        
        orders_tree_show()
        
        Button(window_dancheck1,text='将选中订单确认收货',command=lambda:orders_alter()).place(relx=0.15,rely=0.65,relwidth=0.15,relheight=0.1)
        Button(window_dancheck1,text='评价选中订单',command=lambda:orders_review()).place(relx=0.4,rely=0.65,relwidth=0.15,relheight=0.1)
        
        Label(window_dancheck1,text='举报请联系管理员电话').place(relx=0.72,rely=0.7)
        
        review=StringVar(master=window_dancheck1)
        entry_review=Entry(window_dancheck1,textvariable=review)
        entry_review.place(relx=0.4,rely=0.8,relwidth=0.15,relheight=0.1)
        
        btn_back=Button(window_dancheck1,text='back',command=lambda:[back(window_dancheck1),winNew2.deiconify()])
        btn_back.place(relx=0.8,rely=0.85,relwidth=0.1,relheight=0.05)
        
    def xiaoxi():
        def send_after(a,b):
            num=a.get()
            mess=b.get()
            pyafter=table_find(cur, 'aftersales')
            pycustom=table_find(cur,'customer')
            pyorder=table_find(cur,'orders')
            for i in range(0,len(pyorder)): #先判断该顾客是否有此订单
                if pyorder[i][1]==cno and pyorder[i][0]==num:
                    q=1
                    break
                else: 
                    q=-1
                    continue
            if q==1: #若有订单，则记录此顾客的id然后将对应信息发送
                for i in range(0,len(pycustom)):
                    if pycustom[i][0]== cno:
                        custom_name=pycustom[i][1]
                        break
                    else:
                        continue
                maxq=0
                total=0
                for i in range(0,len(pyafter)):
                    if pyafter[i][1]==num:
                        total=total+1
                        maxq=max(maxq,pyafter[i][0])
                    
                aftno=max(maxq,total)+1
                
                table_insert(cur,'aftersales',[str(aftno),str(num),custom_name,mess])
                messagebox.showinfo('您好','您的消息已发送')
                window_xiaoxi.destroy()
                xiaoxi()
            else:
                messagebox.showerror('错误','您没有此订单')
        def xiaoxi_tree_show():
            pyafter=table_find(cur, 'extraaftersales')
            
            for t in range(0,len(pyafter)):
                if pyafter[t][4]==cno:
                    xiaoxi_tree.insert('', END, values=pyafter[t][0:4])
                    
        window_xiaoxi=Toplevel()
        window_xiaoxi.title('我的消息')
        window_xiaoxi.geometry(align_str)
        cols = ['消息编号','订单编号','发送者账号','消息内容']
        xiaoxi_tree=ttk.Treeview(window_xiaoxi,height=8,columns=cols,show='headings')
        xiaoxi_tree.heading(column='消息编号', text='消息编号', anchor='w')  # 定义表头
        xiaoxi_tree.heading('订单编号', text='订单编号', )  # 定义表头
        xiaoxi_tree.heading('发送者账号', text='发送者账号', )  # 定义表头
        xiaoxi_tree.heading('消息内容', text='消息内容', )  # 定义表头
        xiaoxi_tree.column('消息编号', width=45, minwidth=45, anchor=S)  # 定义列
        xiaoxi_tree.column('订单编号', width=45, minwidth=45, anchor=S)  # 定义列
        xiaoxi_tree.column('发送者账号', width=45, minwidth=45, anchor=S)  # 定义列
        xiaoxi_tree.column('消息内容', width=100, minwidth=100, anchor=S)
        xiaoxi_tree.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.5)# 定义列
        xiaoxi_tree_show()
        Label(window_xiaoxi,text='订单编号').place(relx=0.19,rely=0.65)
        send_num=IntVar()
        entry_num=Entry(window_xiaoxi,textvariable=send_num)
        entry_num.place(relx=0.25,rely=0.65,relwidth=0.1,relheight=0.05)
        Label(window_xiaoxi,text='消息内容').place(relx=0.36,rely=0.65)
        send=StringVar()
        entry_send=Entry(window_xiaoxi,textvariable=send)
        entry_send.place(relx=0.45,rely=0.65,relwidth=0.22,relheight=0.05)
        send_btn=Button(window_xiaoxi,text='发送',command=lambda:send_after(send_num,send))
        send_btn.place(relx=0.7,rely=0.65,relwidth=0.1,relheight=0.05)
        btn_back=Button(window_xiaoxi,text='back',command=lambda:[back(window_xiaoxi),winNew2.deiconify()])
        btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)
    
    winNew2 = Toplevel()
    winNew2.geometry(align_str)  # 设置窗口大小保持和主窗口相同
    winNew2.resizable(width=True, height=True)
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    winNew2.title('顾客界面')
    label_a2 = Label(winNew2, text="尊敬的顾客您好", fg="red", font=("宋体", 26), relief=GROOVE).pack()
    label_b2 = Label(winNew2, text="顾客功能", font=("宋体", 20)).pack()
    
    btn_xiadan=Button(winNew2,text='我的信息',command=lambda:[info(),winNew2.withdraw()])
    btn_xiadan.place(relx=0.1,rely=0.25,relwidth=0.2,relheight=0.12)
    
    btn_check=Button(winNew2,text='查看商品',command=lambda:[check(),winNew2.withdraw()])
    btn_check.place(relx=0.1,rely=0.4,relwidth=0.2,relheight=0.12)
    
    btn_collect=Button(winNew2,text='我的收藏',command=lambda:[show_collect(),winNew2.withdraw()])
    btn_collect.place(relx=0.1,rely=0.55,relwidth=0.2,relheight=0.12)
    
    btn_report=Button(winNew2,text='我的订单',command=lambda:[show_order()])
    btn_report.place(relx=0.1,rely=0.70,relwidth=0.2,relheight=0.12)
    
    btn_xiaoxi=Button(winNew2,text='我的消息',command=lambda:[xiaoxi(),winNew2.withdraw()])
    btn_xiaoxi.place(relx=0.6,rely=0.25,relwidth=0.2,relheight=0.12)
    
    btn_back=Button(winNew2,text='back',command=lambda:[back(winNew2),my_windows.deiconify()])
    btn_back.place(relx=0.7,rely=0.7,relwidth=0.1,relheight=0.05)
    
    
def new_windows_merchant(windows):  # 创建商家seller窗口函数
    def scheck():  
        def get_selection():
            try:
                tmp=goods_tree.item(goods_tree.focus())
                a=tmp['values'][0]
                return a
            except:
                messagebox.showerror('错误','获取选中项出现错误，请重新操作')
                return
        # def test():
        #     tmp=goods_tree.item(goods_tree.focus())
        #     a=tmp['values'][0]
        #     print(a)
            
            
            
            
        def goods_add():
            name=entry_name.get()
            type=entry_type.get()
            amount=entry_amount.get()
            intro=entry_intro.get()
            price=entry_price.get()
            
            values_list=['default',"'"+str(sno)+"'","'"+str(type)+"'","'"+str(name)+"'",
                         "'"+str(amount)+"'","'"+str(intro)+"'","'"+str(price)+"'",'default']
            table_insert0(cur, 'goods', values_list)
            goods_tree_show()
            
            entry_name.delete(0, 'end')
            entry_type.delete(0, 'end')
            entry_amount.delete(0, 'end')
            entry_intro.delete(0, 'end')
            entry_price.delete(0, 'end')
                
        def goods_alter():
            tmp=str(get_selection())
            name=entry_name.get()
            type=entry_type.get()
            amount=entry_amount.get()
            intro=entry_intro.get()
            price=entry_price.get()
            
            if name!='':
                cols_list=['gno','name']
                values_list=[tmp,str(name)]
                table_update(cur, 'goods', cols_list, values_list)
            
            if type!='':
                cols_list=['gno','gcno']
                values_list=[tmp,str(type)]
                table_update(cur, 'goods', cols_list, values_list)
            
            if amount!='':
                cols_list=['gno','amount']
                values_list=[tmp,str(amount)]
                table_update(cur, 'goods', cols_list, values_list)
            
            if intro!='':
                cols_list=['gno','introduction']
                values_list=[tmp,str(intro)]
                table_update(cur, 'goods', cols_list, values_list)
            
            if price!='':
                cols_list=['gno','price']
                values_list=[tmp,str(price)]
                table_update(cur, 'goods', cols_list, values_list)
            
            goods_tree_show()
            
            
        def goods_drop():
            tmp=str(get_selection())
            cols_list=('gno','state')
            values_list=(tmp,'下架')
            table_update(cur, 'goods', cols_list, values_list)
            goods_tree_show()
             
        def goods_del():
            tmp=str(get_selection())
            a=tkinter.messagebox.askyesno('提示', '要执行此操作吗')
            if a:
                 table_delete(cur, 'goods',('gno',),(tmp,))
                 goods_tree_show()
                 return()
            
                
           
        
        def delButton(tree):
            x=tree.get_children()
            for item in x:
                tree.delete(item)
                
        def goods_tree_show():
            delButton(goods_tree)
            pygoods=table_find(cur,'goods')
            for i in range(0,len(pygoods)):
                if pygoods[i][1]==sno:
                    goods_tree.insert('', END, values=(pygoods[i][0],)+pygoods[i][2:8])
                    
        def show_gc():
            def delButton(tree):
                x=tree.get_children()
                for item in x:
                    tree.delete(item)
            def tree_show():
              delButton(gc_tree)
              pygc=table_find(cur,'goodscategory')
              for i in range(0,len(pygc)):
                  gc_tree.insert('', END, values=pygc[i])
                    
        
            window_gc=Toplevel()
            window_gc.title('商品类别信息')
            window_gc.geometry(align_str)
        
            cols = ['商品类别编号','商品类别名']
            gc_tree=ttk.Treeview(window_gc,height=8,columns=cols,show='headings')
            gc_tree.heading(column='商品类别编号', text='商品类别编号', anchor='w')  # 定义表头
            gc_tree.heading('商品类别名', text='商品类别名', )  # 定义表头

            gc_tree.column('商品类别编号', width=45, minwidth=45, anchor=S)  # 定义列
            gc_tree.column('商品类别名', width=45, minwidth=45, anchor=S)  # 定义列

            tree_show()
            gc_tree.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.5)
            btn_back=Button(window_gc,text='back',command=lambda:[back(window_gc),window_scheck.deiconify()])
            btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)            
        
        

        # pysellers=table_find(cur,'seller')
        
        window_scheck=Toplevel()
        window_scheck.title('查看商品')
        window_scheck.geometry(align_str)
        
        pygoods=table_find(cur,'goods')
        
        cols = ['商品编号', '商品种类编号', '商品名', '库存量', '商品介绍', '商品价格','商品状态']
        goods_tree=ttk.Treeview(window_scheck,height=8,columns=cols,show='headings')
        goods_tree.heading(column='商品编号', text='商品编号', anchor='w')  # 定义表头
        goods_tree.heading('商品种类编号', text='商品种类编号', )  # 定义表头
        goods_tree.heading('商品名', text='商品名', )  # 定义表头
        goods_tree.heading('库存量', text='库存量', )  # 定义表头
        goods_tree.heading('商品介绍', text='商品介绍', )  # 定义表头
        goods_tree.heading('商品价格', text='商品价格', )  # 定义表头
        goods_tree.heading('商品状态', text='商品状态', )  # 定义表头
        goods_tree.column('商品编号', width=60, minwidth=60, anchor=S)  # 定义列
        goods_tree.column('商品种类编号', width=90, minwidth=80, anchor=S)  # 定义列
        goods_tree.column('商品名', width=100, minwidth=100, anchor=S)  # 定义列
        goods_tree.column('库存量', width=60, minwidth=60, anchor=S)  # 定义列
        goods_tree.column('商品介绍', width=200, minwidth=100, anchor=S)  # 定义列
        goods_tree.column('商品价格', width=60, minwidth=60, anchor=S)  # 定义列
        goods_tree.column('商品状态', width=60, minwidth=60, anchor=S)  # 定义列
        
        goods_tree_show()
        
        
        goods_tree.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.4)
        
        
        # Label(window_scheck,text='商品编号').place(relx=0.07,rely=0.65)
        # scheck_num=StringVar(master=window_scheck)
        # entry_num=Entry(window_scheck,textvariable=scheck_num)
        # entry_num.place(relx=0.15,rely=0.65,relwidth=0.07,relheight=0.05)
        
        Label(window_scheck,text='商品类别编号').place(relx=0.14,rely=0.75)
        scheck_type=StringVar(master=window_scheck)
        entry_type=Entry(window_scheck,textvariable=scheck_type)
        entry_type.place(relx=0.25,rely=0.75,relwidth=0.07,relheight=0.05)
        
        
        Label(window_scheck,text='商品名称').place(relx=0.37,rely=0.75)
        scheck_name=StringVar(master=window_scheck)
        entry_name=Entry(window_scheck,textvariable=scheck_name)
        entry_name.place(relx=0.45,rely=0.75,relwidth=0.1,relheight=0.05)
        
        Label(window_scheck,text='数量').place(relx=0.1,rely=0.85)
        scheck_amount=StringVar(master=window_scheck)
        entry_amount=Entry(window_scheck,textvariable=scheck_amount)
        entry_amount.place(relx=0.15,rely=0.85,relwidth=0.07,relheight=0.05)
        
        Label(window_scheck,text='介绍').place(relx=0.5,rely=0.85)
        scheck_intro=StringVar(master=window_scheck)
        entry_intro=Entry(window_scheck,textvariable=scheck_intro)
        entry_intro.place(relx=0.55,rely=0.85,relwidth=0.2,relheight=0.1)
        
        Label(window_scheck,text='价格').place(relx=0.3,rely=0.85)
        scheck_price=StringVar(master=window_scheck)
        entry_price=Entry(window_scheck,textvariable=scheck_price)
        entry_price.place(relx=0.35,rely=0.85,relwidth=0.07,relheight=0.05)
        
        Label(window_scheck,text='上架必须写全所有属性').place(relx=0.6,rely=0.65)
        Label(window_scheck,text='输入数据处').place(relx=0.3,rely=0.65)
        
        Button(window_scheck,text='上架新商品',command=lambda:goods_add()).place(relx=0.05,rely=0.5,relwidth=0.12,relheight=0.1)
        Button(window_scheck,text='下架选中商品',command=lambda:goods_drop()).place(relx=0.22,rely=0.5,relwidth=0.12,relheight=0.1)
        Button(window_scheck,text='更改选中商品信息',command=lambda:goods_alter()).place(relx=0.4,rely=0.5,relwidth=0.16,relheight=0.1)
        Button(window_scheck,text='删除选中商品',command=lambda:goods_del()).place(relx=0.63,rely=0.5,relwidth=0.12,relheight=0.1)
        Button(window_scheck,text='查看商品类别信息',command=lambda:show_gc()).place(relx=0.8,rely=0.5,relwidth=0.16,relheight=0.1)
        
        btn_back=Button(window_scheck,text='back',command=lambda:[back(window_scheck),winNew3.deiconify()])
        btn_back.place(relx=0.8,rely=0.85,relwidth=0.1,relheight=0.05)
        
        # btn_test=Button(window_scheck,text='test',command=lambda:test())
        # btn_test.place(relx=0.9,rely=0.9,relwidth=0.1,relheight=0.05)



# 商家查看自己订单        
    def dancheck():
        def get_selection():
            try:
                tmp=orders_tree.item(orders_tree.focus())
                a=tmp['values'][0]
                return a
            except:
                messagebox.showerror('错误','获取选中项出现错误，请重新操作')
                return
        # def test():
        #     tmp=orders_tree.item(orders_tree.focus())
        #     a=tmp['values'][0]
        #     b=tmp['values'][9]
        #     print(a,b)
        
        def orders_alter():
            tmp=orders_tree.item(orders_tree.focus())
            if tmp['values'][9]!='待发货':
                messagebox.showerror('错误','请检查订单状态')
                return  
            tmp=str(get_selection())
            cols_list=('ono','state')
            values_list=(tmp,'待收货')
            table_update(cur, 'orders', cols_list, values_list)
            orders_tree_show()
            
            
            
        
        def delButton(tree):
            x=tree.get_children()
            for item in x:
                tree.delete(item)
                
        def orders_tree_show():
            delButton(orders_tree)
            pyorders=table_find(cur,'extraorder')
            for i in range(0,len(pyorders)):
                if pyorders[i][0]==sno:
                    orders_tree.insert('', END, values=pyorders[i][1:13])
                    
        

        # pysellers=table_find(cur,'seller')
        
        window_dancheck=Toplevel()
        window_dancheck.title('我的订单')
        window_dancheck.geometry('1200x600+510+240')
        
        pyorders=table_find(cur,'extraorder')
        
        cols = ['订单编号', '顾客编号', '顾客姓名', '顾客联系方式', '收货地址', '商品编号','商品名称','购买数量'
                ,'订单总价','订单状态','下单时间','评价']
        orders_tree=ttk.Treeview(window_dancheck,height=8,columns=cols,show='headings')
        
        orders_tree.heading(column='订单编号', text='订单编号', anchor='w')  # 定义表头
        orders_tree.heading('顾客编号', text='顾客编号', )  # 定义表头
        orders_tree.heading('顾客姓名', text='顾客姓名', )  # 定义表头
        orders_tree.heading('顾客联系方式', text='顾客联系方式', )  # 定义表头
        orders_tree.heading('收货地址', text='收货地址', )  # 定义表头
        orders_tree.heading('商品编号', text='商品编号', )  # 定义表头
        orders_tree.heading('商品名称', text='商品名称', )  # 定义表头
        orders_tree.heading(column='购买数量', text='购买数量', anchor='w')  # 定义表头
        orders_tree.heading('订单总价', text='订单总价', )  # 定义表头
        orders_tree.heading('订单状态', text='订单状态', )  # 定义表头
        orders_tree.heading('下单时间', text='下单时间', )  # 定义表头
        orders_tree.heading('评价', text='评价', )  # 定义表头
        
        orders_tree.column('订单编号', width=80, minwidth=60, anchor=S)  # 定义列
        orders_tree.column('顾客编号', width=80, minwidth=80, anchor=S)  # 定义列
        orders_tree.column('顾客姓名', width=80, minwidth=80, anchor=S)  # 定义列
        orders_tree.column('顾客联系方式', width=110, minwidth=60, anchor=S)  # 定义列
        orders_tree.column('收货地址', width=100, minwidth=100, anchor=S)  # 定义列
        orders_tree.column('商品编号', width=80, minwidth=60, anchor=S)  # 定义列
        orders_tree.column('商品名称', width=80, minwidth=60, anchor=S)  # 定义列
        orders_tree.column('购买数量', width=80, minwidth=60, anchor=S)  # 定义列
        orders_tree.column('订单总价', width=80, minwidth=80, anchor=S)  # 定义列
        orders_tree.column('订单状态', width=80, minwidth=80, anchor=S)  # 定义列
        orders_tree.column('下单时间', width=80, minwidth=80, anchor=S)  # 定义列
        orders_tree.column('评价', width=100, minwidth=100, anchor=S)  # 定义列
        
        orders_tree.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.5)
        
        orders_tree_show()
        
        Button(window_dancheck,text='将选中订单发货',command=lambda:orders_alter()).place(relx=0.25,rely=0.75,relwidth=0.15,relheight=0.1)
       
        btn_back=Button(window_dancheck,text='back',command=lambda:[back(window_dancheck),winNew3.deiconify()])
        btn_back.place(relx=0.8,rely=0.85,relwidth=0.1,relheight=0.05)
        
        # btn_test=Button(window_dancheck,text='test',command=lambda:test())
        # btn_test.place(relx=0.9,rely=0.9,relwidth=0.1,relheight=0.05)
        
    def aftcheck():
        
        def delButton(tree):
            x=tree.get_children()
            for item in x:
                tree.delete(item)
                
        def send_after(a,b):
            num=a.get()#订单号
            mess=b.get()#信息
            pyafter=table_find(cur, 'extraaftersales')
            pyorder=table_find(cur,'extraorder')
            tmp=0
            tmp1=0
            #先判断该商家是否有此订单
            for i in range(0,len(pyorder)):
                if pyorder[i][0]==sno and pyorder[i][1]==num:
                    tmp=1
            if tmp==0:
                messagebox.showerror('错误','您没有此订单')
                return
            
            if tmp==1:
                #获取自己的账号
                pyseller=table_find(cur,'seller')
                for i in range(0,len(pyseller)):
                    if pyseller[i][0]==sno:
                        me=pyseller[i]
                #得到aftno
                maxq=0
                total=0
                for i in range(0,len(pyafter)):
                    if pyafter[i][1]==num:
                        total=total+1
                        maxq=max(maxq,pyafter[i][0])
                    
                aftno=max(maxq,total)+1
                
                table_insert0(cur,'aftersales',[str(aftno),str(num),"'"+str(me[1])+"'","'"+mess+"'"])
                messagebox.showinfo('您好','您的消息已发送')
                xiaoxi_tree_show()
                
            
            
            
                
        def xiaoxi_tree_show():
            delButton(xiaoxi_tree)
            pyafter=table_find(cur, 'extraaftersales')
            for i in range(0,len(pyafter)):
                if pyafter[i][5]==sno:
                    xiaoxi_tree.insert('', END, values=pyafter[i][0:4])
                    
                    
        window_xiaoxi=Toplevel()
        window_xiaoxi.title('我的消息')
        window_xiaoxi.geometry(align_str)
        
        cols = ['消息编号','订单编号', '发送人','消息内容']
        xiaoxi_tree=ttk.Treeview(window_xiaoxi,height=8,columns=cols,show='headings')
        
        xiaoxi_tree.heading(column='消息编号', text='消息编号', anchor='w')  # 定义表头
        xiaoxi_tree.heading('订单编号', text='订单编号', )  # 定义表头
        xiaoxi_tree.heading('发送人', text='发送人', )  # 定义表头
        xiaoxi_tree.heading('消息内容', text='消息内容', )
        
        xiaoxi_tree.column('消息编号', width=45, minwidth=45, anchor=S)  # 定义列
        xiaoxi_tree.column('订单编号', width=45, minwidth=45, anchor=S)  # 定义列
        xiaoxi_tree.column('发送人', width=70, minwidth=70, anchor=S)
        xiaoxi_tree.column('消息内容', width=100, minwidth=100, anchor=S)
        
        xiaoxi_tree.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.5)# 定义列
        xiaoxi_tree_show()
        
        Label(window_xiaoxi,text='订单编号').place(relx=0.15,rely=0.65)
        send_num=IntVar()
        entry_num=Entry(window_xiaoxi,textvariable=send_num)
        entry_num.place(relx=0.25,rely=0.65,relwidth=0.1,relheight=0.05)
        Label(window_xiaoxi,text='消息内容').place(relx=0.36,rely=0.65)
        send=StringVar()
        entry_send=Entry(window_xiaoxi,textvariable=send)
        entry_send.place(relx=0.45,rely=0.65,relwidth=0.22,relheight=0.05)
        send_btn=Button(window_xiaoxi,text='发送',command=lambda:send_after(send_num,send))
        send_btn.place(relx=0.7,rely=0.65,relwidth=0.1,relheight=0.05)
        btn_back=Button(window_xiaoxi,text='back',command=lambda:[back(window_xiaoxi),winNew3.deiconify()])
        btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)
    def infcheck():
        
        
        def alter():
            tmp=str(sno)
            
            name=entry_name.get()
            telnum=entry_telnum.get()
            bank=entry_bank.get()
            intro=entry_intro.get()
            bcnum=entry_bcnum.get()
            if name==me[3] and telnum==me[5] and bank==me[6] and bcnum==me[7] and intro==me[4]:
                messagebox.showinfo('提示','未修改！') 
                return
     
            a=tkinter.messagebox.askyesno('提示', '要执行此操作吗')
            if a:
                if name!=me[3]:
                    cols_list=['sno','name']
                    values_list=[tmp,str(name)]
                    print([tmp,str(name)])
                    table_update(cur, 'seller', cols_list, values_list)
                if telnum!=me[5]:
                    cols_list=['sno','telnum']
                    values_list=[tmp,str(telnum)]
                    table_update(cur, 'seller', cols_list, values_list)
                if bank!=me[6]:
                    cols_list=['sno','bank']
                    values_list=[tmp,str(bank)]
                    table_update(cur, 'seller', cols_list, values_list)
                if bcnum!=me[7]:
                    cols_list=['sno','bcnum']
                    values_list=[tmp,str(bcnum)]
                    table_update(cur, 'seller', cols_list, values_list)
                if intro!=me[4]:
                    cols_list=['sno','introduction']
                    values_list=[tmp,str(intro)]
                    table_update(cur, 'seller', cols_list, values_list)
                messagebox.showinfo('提示','设置成功！') 
            
            
            
        
        
        
        
        
        
        window_infcheck=Toplevel()
        window_infcheck.title('查看本店信息')
        window_infcheck.geometry(align_str)
        
        pyseller=table_find(cur,'seller')
        for i in range(0,len(pyseller)):
            if pyseller[i][0]==sno:
                me=pyseller[i]
                print(me)
        
        Label(window_infcheck,text='账号').place(relx=0.15,rely=0.2)
        account=StringVar(master=window_infcheck)
        account.set(me[1])
        entry_account=Entry(window_infcheck,textvariable=account,state='readonly')
        entry_account.place(relx=0.2,rely=0.2,relwidth=0.15,relheight=0.05)
        
        
        Label(window_infcheck,text='负责人编号').place(relx=0.40,rely=0.2)
        admno=StringVar(master=window_infcheck)
        admno.set(me[2])
        entry_admno=Entry(window_infcheck,textvariable=admno, state='readonly')
        entry_admno.place(relx=0.5,rely=0.2,relwidth=0.1,relheight=0.05)
        
        Label(window_infcheck,text='商家姓名').place(relx=0.72,rely=0.2)
        name=StringVar(master=window_infcheck)
        name.set(me[3])
        entry_name=Entry(window_infcheck,textvariable=name)
        entry_name.place(relx=0.8,rely=0.2,relwidth=0.15,relheight=0.05)
        
        Label(window_infcheck,text='联系方式').place(relx=0.12,rely=0.5)
        telnum=StringVar(master=window_infcheck)
        telnum.set(me[5])
        entry_telnum=Entry(window_infcheck,textvariable=telnum)
        entry_telnum.place(relx=0.2,rely=0.5,relwidth=0.15,relheight=0.05)
     
        Label(window_infcheck,text='收款银行').place(relx=0.42,rely=0.5)
        bank=StringVar(master=window_infcheck)
        bank.set(me[6])
        entry_bank=Entry(window_infcheck,textvariable=bank)
        entry_bank.place(relx=0.5,rely=0.5,relwidth=0.1,relheight=0.05)
        
        Label(window_infcheck,text='银行卡号').place(relx=0.72,rely=0.5)
        bcnum=StringVar(master=window_infcheck)
        bcnum.set(me[7])
        entry_bcnum=Entry(window_infcheck,textvariable=bcnum)
        entry_bcnum.place(relx=0.8,rely=0.5,relwidth=0.15,relheight=0.05)
        
        Label(window_infcheck,text='简介').place(relx=0.15,rely=0.8)
        intro=StringVar(master=window_infcheck)
        intro.set(me[4])
        entry_intro=Entry(window_infcheck,textvariable=intro)
        entry_intro.place(relx=0.2,rely=0.8,relwidth=0.2,relheight=0.1)
        
        btn_back=Button(window_infcheck,text='保存更改',command=lambda:alter())
        btn_back.place(relx=0.7,rely=0.8,relwidth=0.1,relheight=0.05) 
        
        btn_back=Button(window_infcheck,text='back',command=lambda:[back(window_infcheck),winNew3.deiconify()])
        btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)    
    
    winNew3 = Toplevel()
    winNew3.geometry(align_str)  # 设置窗口大小保持和主窗口相同
    winNew3.resizable(width=True, height=True)
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    winNew3.title('商家界面')
    label_a3 = Label(winNew3, text="尊敬的商家您好", fg="red", font=("宋体", 26), relief=GROOVE).pack()
    label_b3 = Label(winNew3, text="商家功能", font=("宋体", 20)).pack()
    
    btn_scheck=Button(winNew3,text='查看商品',command=lambda:[scheck(),winNew3.withdraw()])
    btn_scheck.place(relx=0.2,rely=0.3,relwidth=0.2,relheight=0.12)
    
    btn_dancheck=Button(winNew3,text='查看订单',command=lambda:[dancheck(),winNew3.withdraw()])
    btn_dancheck.place(relx=0.2,rely=0.5,relwidth=0.2,relheight=0.12)
    
    btn_dancheck=Button(winNew3,text='查看售后消息',command=lambda:[aftcheck(),winNew3.withdraw()])
    btn_dancheck.place(relx=0.6,rely=0.3,relwidth=0.2,relheight=0.12)
    
    btn_dancheck=Button(winNew3,text='基础信息',command=lambda:[infcheck(),winNew3.withdraw()])
    btn_dancheck.place(relx=0.6,rely=0.5,relwidth=0.2,relheight=0.12)
    
    btn_back=Button(winNew3,text='back',command=lambda: [back(winNew3),my_windows.deiconify()])
    btn_back.place(relx=0.85,rely=0.85,relwidth=0.1,relheight=0.05)
    
    
    
    
    
    
my_windows=Tk()# 初始化TK
my_windows.title('远泽航购物平台')# 设置标题
width=900
height=600
screenwidth=my_windows.winfo_screenwidth()
screenheight=my_windows.winfo_screenheight()
align_str='%dx%d+%d+%d'%(width,height,(screenwidth-width)/2,(screenheight-height)/2)
my_windows.geometry(align_str)#设置窗口大小
my_windows.resizable(width=True,height=True)
label_0=Label(my_windows,text='电子商务平台',fg='red',font=('宋体',30))
label_0.pack()
label_1=Label(my_windows,text='请输入账号密码',font=('宋体',20))
label_1.place(relx=0.4,rely=0.2)
# 可视化标题设计
inp1=Entry(my_windows)# 定义输入框，统一用inp表示输入框
inp1.place(relx=0.35,rely=0.3,relwidth=0.3,relheight=0.1)
inp2=Entry(my_windows,show='*')# 定义第二个框 密码部分用*隐藏
inp2.place(relx=0.35,rely=0.45,relwidth=0.3,relheight=0.1)
inp_label1 = Label(my_windows, text="账号:", font=("宋体", 15))  # 定义账号
inp_label1.place(relx=0.25, rely=0.31)
inp_label2 = Label(my_windows, text="密码:", font=("宋体", 15))  # 定义密码
inp_label2.place(relx=0.25, rely=0.46)
btn1=Button(my_windows, text='登录', command=lambda: run(inp1.get()))  # 登入系统的按钮
btn1.place(relx=0.36, rely=0.57, relwidth=0.12, relheight=0.07)
btn2=Button(my_windows, text='注册', command=lambda: sign())  # 注册的按钮
btn2.place(relx=0.52, rely=0.57, relwidth=0.12, relheight=0.07)
label_4 = Label(my_windows, text=" ", fg="blue", font=("宋体", 20))
label_4.place(relx=0.45, rely=0.65)
pyusers=table_find(cur,'users')
get_time()
txt = Text(my_windows, bg="#d3fbfb")  # 定义文本框

txt.place(relx=0.1,rely=0.72,relwidth=0.8, relheight=0.4)

def callbackClose():


    messagebox.showwarning(title='警告', message='可爱的你点击了 [关闭] 按钮')


    os._exit(0)



my_windows.mainloop()

cur.close() # 关闭游标
conn.close() # 关闭连接




















