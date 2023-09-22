# Youtube Link: https://www.youtube.com/watch?v=PgLjwl6Br0k
import warnings
warnings.filterwarnings("ignore")
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import pandas as pd
import datetime as dt
from datetime import datetime, timedelta, timezone
# initalise the tkinter GUI
root = tk.Tk()
root.title('JAA - Job Assignment Advisor')
#root.geometry("900x600") # set the root dimensions
#root.attributes('-fullscreen',True)
#getting screen width and height of display
width= root.winfo_screenwidth()
height= root.winfo_screenheight() - 40
#setting tkinter window size
root.geometry("%dx%d" % (width, height))
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
root.resizable(0, 0) # makes the root window fixed in size.

# Frame for TreeView
frame1 = tk.LabelFrame(root, text="Workplan")
frame1.place(height=460, width=800)

# Frame for Tractor stat Treeview
file_frame = tk.LabelFrame(root, text="Tractor Option")
file_frame.place(height=290, width=1000, rely=0.60, relx=0.00)

# Frame for TreeView
frame2 = tk.LabelFrame(root, text="Tractor Stat")
frame2.place(height=290, width=250, rely=0.60, relx=0.68)
# Frame for TreeViewMedium
frame3 = tk.LabelFrame(root, text="Lock Flight")
frame3.place(height=460, width=200, rely=0.00, relx=0.52)

# Frame for TreeView
frame4 = tk.LabelFrame(root, text="Edit Tractor Recommended")
frame4.place(height=100, width=192, rely=0.60, relx=0.85)

# Frame for TreeView
frame5 = tk.LabelFrame(root, text="Edit Tractor NOT!! Recommended")
frame5.place(height=100, width=192, rely=0.73, relx=0.85)

# Frame for TreeView
frame6 = tk.LabelFrame(root, text="Requested Time")
frame6.place(height=150, width=470, rely=0.19, relx=0.68)

# Frame for TreeView
frame7 = tk.LabelFrame(root, text="Edit Bay")
frame7.place(height=150, width=470, rely=0.00, relx=0.68)

# Frame for TreeView
frame8 = tk.LabelFrame(root, text="Edit Bay")
frame8.place(height=165, width=470, rely=0.38, relx=0.68)


# Button Creation

button1 = tk.Button(root, text="First Cal", command=lambda: FirstCal())
button1.place(rely=0.88, relx=0.90)

button3 = tk.Button(root, text="Update Task", command=lambda: UpdateTask())
button3.place(rely=0.93, relx=0.89)

button4 = tk.Button(frame4, text="Edit Tractor", command=lambda: Editlockflt3())
button4.place(rely=0.60, relx=0.30)

button5 = tk.Button(frame5, text="Edit Tractor", command=lambda: Editlockflt4())
button5.place(rely=0.60, relx=0.30)

button6 = tk.Button(frame6, text="Edit Time", command=lambda: Edit_time())
button6.place(rely=0.81, relx=0.75)

button7 = tk.Button(frame7, text="Edit Bay", command=lambda:Edit_Bay())
button7.place(rely=0.81, relx=0.75)


def update_edit_flt(fllt):
    wp = pd.read_csv (r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Tractor_option.csv')
    xx = wp['Flight'].values.tolist()
    fllt['values'] = xx
    #return xx

def update_edit_flt_unused(fllt2):
    wp = pd.read_csv (r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Tractor_option2.csv')
    xx = wp['Flight'].values.tolist()
    fllt2['values'] = xx
    #return xx

def update_bay_name(fllt4):
    BB = pd.read_csv (r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Bay_Name.csv')
    xx = BB['Bay'].values.tolist()
    fllt4['values'] = xx
    #return xx

def sel_lstbox_lock_flight():
    #datalock = []
    dl = r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\datalock.txt'
    with open(dl, "r") as f:
        lines = f.readlines()

    for line in lines:
        for i in range(list1.size()):
            if list1.get(i) == line.strip():
                # select the item if it matches the target value
                list1.selection_set(i)
        #print('this is sel_lstbox_lock_flight')
        #print(line.strip())



def on_sel_lstbox_lock_flight(event):
    #datalock = []
    dl = r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\datalock.txt'
    with open(dl, "r") as f:
        lines = f.readlines()

    for line in lines:
        for i in range(list1.size()):
            if list1.get(i) == line.strip():
                # select the item if it matches the target value
                list1.selection_set(i)
        #print(line.strip())


def display_reqtime():
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\ReqTime.txt', "r") as f:
        file_contents = f.read()
        text_widget.insert("end", file_contents)

def display_fltpair():
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\fltpair.txt', "r") as f:
        file_contents = f.read()
        text_widget3.insert("end", file_contents)

def display_EditBay():
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Bay.txt', "r") as f:
        file_contents = f.read()
        text_widget2.insert("end", file_contents)

def Edit_time():
    text_widget.delete(1.0, END)
    Update_Edittime(flt3.get(),year_spinbox.get(),month_spinbox.get(),day_spinbox.get(),hour_spinbox.get(),minute_spinbox.get(),second_spinbox.get())
    display_reqtime()

def Edit_Bay():
    text_widget2.delete(1.0, END)
    Update_edit_bay(sel_flt4.get(), sel_bay.get())
    display_EditBay()

text_widget = tk.Text(frame6, width=35, height=7)
text_widget.place(relx=0.025, rely=0.025)
scrollbar = Scrollbar(frame6, command=text_widget.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_widget.config(yscrollcommand=scrollbar.set)

text_widget2 = tk.Text(frame7, width=35, height=7)
text_widget2.place(relx=0.025, rely=0.025)
scrollbar = Scrollbar(frame7, command=text_widget2.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_widget2.config(yscrollcommand=scrollbar.set)

text_widget3 = tk.Text(frame8, width=53, height=7.5)
text_widget3.place(relx=0.025, rely=0.025)
scrollbar = Scrollbar(frame8, command=text_widget3.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_widget3.config(yscrollcommand=scrollbar.set)

sel_flt = tk.StringVar()
flt = ttk.Combobox(frame4, textvariable=sel_flt)
flt['state'] = 'readonly'
flt.pack()

sel_flt2 = tk.StringVar()
flt2 = ttk.Combobox(frame5, textvariable=sel_flt2)
flt2['state'] = 'readonly'
flt2.pack()

sel_flt3 = tk.StringVar()
flt3 = ttk.Combobox(frame6, width=13, textvariable=sel_flt3)
flt3['state'] = 'readonly'
flt3.place(relx=0.70, rely=0.01)

sel_flt4 = tk.StringVar()
flt4 = ttk.Combobox(frame7, width=13, textvariable=sel_flt4)
flt4['state'] = 'readonly'
flt4.place(relx=0.70, rely=0.01)

sel_bay = tk.StringVar()
bay = ttk.Combobox(frame7, width=13, textvariable=sel_bay)
bay['state'] = 'readonly'
bay.place(relx=0.70, rely=0.21)

now = datetime.now(timezone.utc)
year_spinbox = tk.Spinbox(frame6, width=4, from_=2023, to=datetime.now().year,state=NORMAL, value=now.year)
month_spinbox = tk.Spinbox(frame6, width=2, from_=1, to=12)
day_spinbox = tk.Spinbox(frame6, width=2, from_=1, to=31)
hour_spinbox = tk.Spinbox(frame6, width=2, from_=0, to=23)
minute_spinbox = tk.Spinbox(frame6, width=2, from_=0, to=59)
second_spinbox = tk.Spinbox(frame6, width=2, from_=0, to=59)
#timezone_entry = tk.Entry(frame6)
year_spinbox.place(relx=0.65, rely=0.20)
month_spinbox.place(relx=0.73, rely=0.20)
day_spinbox.place(relx=0.78, rely=0.20)
hour_spinbox.place(relx=0.83, rely=0.20)
minute_spinbox.place(relx=0.88, rely=0.20)
second_spinbox.place(relx=0.93, rely=0.20)
year_spinbox.bind("<Tab>", on_sel_lstbox_lock_flight)
month_spinbox.bind("<Tab>", on_sel_lstbox_lock_flight)
day_spinbox.bind("<Tab>", on_sel_lstbox_lock_flight)
hour_spinbox.bind("<Tab>", on_sel_lstbox_lock_flight)
minute_spinbox.bind("<Tab>", on_sel_lstbox_lock_flight)
second_spinbox.bind("<Tab>", on_sel_lstbox_lock_flight)


# Bind the selection event of tv1


def edit_flt_changed(event):
    """ handle the flt changed event """
    xxx = []
    to = pd.read_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Tractor_option.csv')
    #print(sel_flt.get())
    aax = to.loc[to['Flight'] == sel_flt.get()].index
    xxx.append(str(to['Tractor1'][aax].values)[2:8])
    xxx.append(str(to['Tractor2'][aax].values)[2:8])
    xxx.append(str(to['Tractor3'][aax].values)[2:8])
    xxx.append(str(to['Tractor4'][aax].values)[2:8])
    xxx.append(str(to['Tractor5'][aax].values)[2:8])
    xxx.append(str(to['Tractor6'][aax].values)[2:8])
    xxx.append(str(to['Tractor7'][aax].values)[2:8])
    xxx.append(str(to['Tractor8'][aax].values)[2:8])
    xxx.append(str(to['Tractor9'][aax].values)[2:8])
    xxx.append(str(to['Tractor10'][aax].values)[2:8])
    xxx.append(str(to['Tractor11'][aax].values)[2:8])
    xxx.append(str(to['Tractor12'][aax].values)[2:8])
    xxx.append(str(to['Tractor13'][aax].values)[2:8])
    xxx.append(str(to['Tractor14'][aax].values)[2:8])
    xxx.append(str(to['Tractor15'][aax].values)[2:8])
    xxx.append(str(to['Tractor16'][aax].values)[2:8])
    xxx.append(str(to['Tractor17'][aax].values)[2:8])
    xxx.append(str(to['Tractor18'][aax].values)[2:8])
    xxx.append(str(to['Tractor19'][aax].values)[2:8])
    xxx.append(str(to['Tractor20'][aax].values)[2:8])
    trct['values'] = xxx
    trct['state'] = 'readonly'
    #print(xxx)
    sel_lstbox_lock_flight()

    return

def edit_flt_changed2(event):
    """ handle the flt changed event """
    xxx = []
    to = pd.read_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Tractor_option2.csv')
    #print(sel_flt2.get())
    aax = to.loc[to['Flight'] == sel_flt2.get()].index
    xxx.append(str(to['Tractor1'][aax].values)[2:8])
    xxx.append(str(to['Tractor2'][aax].values)[2:8])
    xxx.append(str(to['Tractor3'][aax].values)[2:8])
    xxx.append(str(to['Tractor4'][aax].values)[2:8])
    xxx.append(str(to['Tractor5'][aax].values)[2:8])
    xxx.append(str(to['Tractor6'][aax].values)[2:8])
    xxx.append(str(to['Tractor7'][aax].values)[2:8])
    xxx.append(str(to['Tractor8'][aax].values)[2:8])
    xxx.append(str(to['Tractor9'][aax].values)[2:8])
    xxx.append(str(to['Tractor10'][aax].values)[2:8])
    xxx.append(str(to['Tractor11'][aax].values)[2:8])
    xxx.append(str(to['Tractor12'][aax].values)[2:8])
    xxx.append(str(to['Tractor13'][aax].values)[2:8])
    xxx.append(str(to['Tractor14'][aax].values)[2:8])
    xxx.append(str(to['Tractor15'][aax].values)[2:8])
    xxx.append(str(to['Tractor16'][aax].values)[2:8])
    xxx.append(str(to['Tractor17'][aax].values)[2:8])
    xxx.append(str(to['Tractor18'][aax].values)[2:8])
    xxx.append(str(to['Tractor19'][aax].values)[2:8])
    xxx.append(str(to['Tractor20'][aax].values)[2:8])
    trct2['values'] = xxx
    trct2['state'] = 'readonly'
    #print(xxx)
    sel_lstbox_lock_flight()

    return


def tv3_selection_changed(event):
    selected_item = tv3.focus()  # Get the selected item in tv3
    selected_text = tv3.set(selected_item, 'Tractor')  # Get the value in column 1 of the selected item

    # Clear the current selection in tv1
    tv1.selection_remove(tv1.get_children())

    # Iterate over the items in tv1
    for item in tv1.get_children():
        item_text = tv1.set(item, 'Tractor')
        if selected_text in item_text:
            # Select the matching row in tv1
            tv1.selection_add(item)

flt.bind('<<ComboboxSelected>>', edit_flt_changed)
sel_trct = tk.StringVar()
trct = ttk.Combobox(frame4, textvariable=sel_trct)
#trct['values'] = edit_flt_changed
#trct['state'] = 'readonly'
trct.pack()

flt2.bind('<<ComboboxSelected>>', edit_flt_changed2)
sel_trct2 = tk.StringVar()
trct2 = ttk.Combobox(frame5, textvariable=sel_trct2)
#trct['values'] = edit_flt_changed
#trct['state'] = 'readonly'
trct2.pack()

flt3.bind('<<ComboboxSelected>>', on_sel_lstbox_lock_flight)
#sel_trct2 = tk.StringVar()
#trct2 = ttk.Combobox(frame5, textvariable=sel_trct2)
#trct['values'] = edit_flt_changed
#trct['state'] = 'readonly'
#trct2.pack()

trct.bind('<<ComboboxSelected>>',on_sel_lstbox_lock_flight)
trct2.bind('<<ComboboxSelected>>',on_sel_lstbox_lock_flight)

#listbox
yscrollbar = Scrollbar(frame3)
yscrollbar.pack(side = RIGHT, fill = Y)
list1 = Listbox(frame3, selectmode="multiple",
               yscrollcommand=yscrollbar.set)

# Widget expands horizontally and
# vertically by assigning both to
# fill option
list1.pack(padx=10, pady=10,
          expand=YES, fill="both")


yscrollbar.config(command = list1.yview)
## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

tv2 = ttk.Treeview(file_frame)
tv2.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(file_frame, orient="vertical", command=tv2.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(file_frame, orient="horizontal", command=tv2.xview) # command means update the xaxis view of the widget
tv2.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

tv3 = ttk.Treeview(frame2)
tv3.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).
treescrolly = tk.Scrollbar(frame2, orient="vertical", command=tv3.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame2, orient="horizontal", command=tv3.xview) # command means update the xaxis view of the widget
tv3.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget



tv3.bind('<<TreeviewSelect>>', tv3_selection_changed)


def FirstCal():
    #os.system(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Code\AutoAssign\iTAFM_V8_lock.py')
    os.system(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\iTAFM_V8_lock.py')
    #get_lock_flight()
    Load_stat_data()
    Load_wp_data()
    Load_Tractor_data()
    #Refresh_Flight_lst()
    Refresh_Flight_lst_1cal()
    update_edit_flt(flt)
    update_edit_flt_unused(flt2)
    update_edit_flt(flt3)
    update_edit_flt(flt4)
    update_bay_name(bay)
    Refresh_Edittime()
    Refresh_Editbay()
    Refresh_Editfltpair()
    text_widget.delete(1.0, END)
    text_widget2.delete(1.0, END)
    text_widget3.delete(1.0, END)
    display_reqtime()
    display_EditBay()
    display_fltpair()
    clear_lock_flight()


def UpdateTask():
    get_lock_flight()
    print('ZZZZZZZZZZZZZZZZZZZZZZ')
    os.system(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\iTAFM_V8_next.py')
    Load_stat_data()
    Load_wp_data()
    Load_Tractor_data()
    # Refresh_Flight_lst()
    Refresh_Flight_lst_1cal()
    update_edit_flt(flt)
    update_edit_flt_unused(flt2)
    update_edit_flt(flt3)
    update_edit_flt(flt4)
    update_bay_name(bay)
    sel_lstbox_lock_flight()
    text_widget3.delete(1.0, END)
    text_widget.delete(1.0, END)
    text_widget2.delete(1.0, END)
    display_reqtime()
    display_EditBay()
    display_fltpair()

def Editlockflt():
    Update_Sel_editlock(sel_flt.get(),sel_trct.get())
    Update_edit_bay(sel_flt4.get(), sel_bay.get())
    get_lock_flight()
    os.system(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\iTAFM_V8_next_editflt.py')
    Load_stat_data()
    Load_wp_data()
    Load_Tractor_data()
    #Refresh_Flight_lst()
    Refresh_Flight_lst_1cal()
    update_edit_flt(flt)
    update_edit_flt_unused(flt2)
    update_edit_flt(flt3)
    update_edit_flt(flt4)
    update_bay_name(bay)
    sel_lstbox_lock_flight()
    text_widget.delete(1.0, END)
    text_widget2.delete(1.0, END)
    display_reqtime()
    display_EditBay()

def Editlockflt2():
    Update_Sel_editlock(sel_flt2.get(),sel_trct2.get())
    Update_edit_bay(sel_flt4.get(), sel_bay.get())
    get_lock_flight()
    os.system(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\iTAFM_V8_next_editflt.py')
    Load_stat_data()
    Load_wp_data()
    Load_Tractor_data()
    #Refresh_Flight_lst()
    Refresh_Flight_lst_1cal()
    update_edit_flt(flt)
    update_edit_flt_unused(flt2)
    update_edit_flt(flt3)
    update_edit_flt(flt4)
    update_bay_name(bay)
    sel_lstbox_lock_flight()
    text_widget.delete(1.0, END)
    text_widget2.delete(1.0, END)
    display_reqtime()
    display_EditBay()

def Editlockflt3():
    text_widget3.delete(1.0, END)
    Update_fltpair(sel_flt.get(), sel_trct.get())
    display_fltpair()

def Editlockflt4():
    text_widget3.delete(1.0, END)
    Update_fltpair(sel_flt2.get(), sel_trct2.get())
    display_fltpair()

def Update_Sel_editlock(a,b):
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Edit_flt.txt', 'w') as f:
        f.write(a)
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Edit_trct.txt', 'w') as ff:
        ff.write(b)

def Update_Edittime(a,b,c,d,e,f,g):
    dt_et = dt.datetime(int(b),int(c),int(d),int(e),int(f),int(g))
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\ReqTime.txt', 'a') as ff:
        ff.write("%s;%s+00:00\n"%(a,dt_et))

def Update_edit_bay(a,b):
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Bay.txt', 'a') as f:
        f.write("%s;%s\n"%(a,b))

def Update_fltpair(a,b):
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\fltpair.txt', 'a') as f:
        f.write("%s;%s\n"%(a,b))




def Refresh_Edittime():
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\ReqTime.txt', 'w') as f:
        f.truncate(0)
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\ReqTime.txt', 'a') as ff:
        ff.write("flight;Time\n")

def Refresh_Editbay():
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Bay.txt', 'w') as f:
        f.truncate(0)
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Bay.txt', 'a') as ff:
        ff.write("flight;Bay\n")

def Refresh_Editfltpair():
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\fltpair.txt', 'w') as f:
        f.truncate(0)
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\fltpair.txt', 'a') as ff:
        ff.write("flight;Tractor\n")


def Refresh_Flight_lst():
    #list1.delete(0,END)
    L_wp = pd.read_json (r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\df_das.json')
    x = L_wp['flight_number'].values.tolist()

    for each_item in range(len(x)):
        list1.insert(END, x[each_item])
        list1.itemconfig(each_item)

def Refresh_Flight_lst_1cal():
    list1.delete(0,END)
    L_wp = pd.read_json (r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\df_das.json')
    x = L_wp['flight_number'].values.tolist()

    for each_item in range(len(x)):
        list1.insert(END, x[each_item])
        list1.itemconfig(each_item)

def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
    label_file["text"] = filename
    return None


def Load_wp_data():
    """If the file selected is valid this will load the file into the Treeview"""
    dfsss = pd.read_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\dfs.csv', delimiter=',')
    dfss = pd.DataFrame(dfsss)
    pair2 = dfss[['flight_number', 'Tractor']]

    pair2.rename(columns={'flight_number': 'flight'}, inplace=True)

    #file_path = label_file["text"]
    file_path = r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\df_show.csv'
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    tv1.column(0,minwidth=50,width=50)
    tv1.column(1, minwidth=100, width=100)
    tv1.column(2, minwidth=100, width=100)
    tv1.column(3, minwidth=100, width=100)
    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row)
    # Define the value to match
    match_values = pair2['flight']

    # Add a tag for the matching rows
    tv1.tag_configure('red', foreground='red')

    # Iterate over the Treeview items
    for item in tv1.get_children():
        # Get the values of the current item
        values = tv1.item(item)['values']
        # Check if the match value is present in the values
        if any(match_value in values for match_value in match_values):
            # Add the 'red' tag to the current item
            tv1.item(item, tags=('red',))

    return None

def Load_Tractor_data():
    """If the file selected is valid this will load the file into the Treeview"""
    #file_path = label_file["text"]
    file_path = r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Tractor_option.csv'
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear2_data()
    tv2["column"] = list(df.columns)
    tv2["show"] = "headings"
    for column in tv2["columns"]:
        tv2.heading(column, text=column) # let the column heading = column name

    tv2.column(0, minwidth=50, width=50)

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv2.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None
def clear2_data():
    tv2.delete(*tv2.get_children())
    return None

def Load_stat_data():
    """If the file selected is valid this will load the file into the Treeview"""
    #file_path = label_file["text"]
    file_path = r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\Tractor_stat_out.csv'
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear3_data()
    tv3["column"] = list(df.columns)
    tv3["show"] = "headings"
    for column in tv3["columns"]:
        tv3.heading(column, text=column) # let the column heading = column name

    tv3.column(0,minwidth=20,width=20)
    tv3.column(1, minwidth=50, width=50)
    tv3.column(2, minwidth=50, width=50)

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv3.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None
def clear3_data():
    tv3.delete(*tv3.get_children())
    return None
def clear_data():
    tv1.delete(*tv1.get_children())
    return None

def get_lock_flight():
    datalock = []
    dl = r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\datalock.txt'
    for i in list1.curselection():
        datalock.append(list1.get(i))
    efi = pd.read_csv(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\fltpair.txt', delimiter=';')
    efi = efi.drop_duplicates(subset=['flight'], keep='last')
    efi = efi.reset_index(drop=True)
    print(datalock)
    print(efi)
    a =0
    for j in efi['flight']:
        print(efi['flight'][a])
        datalock.append(efi['flight'][a])
        a=a+1
    print('ZZZZZZZZZZZZZZZZZZZZZZ')
    print(datalock)
    with open(dl, 'w') as fp:
        for item in datalock:
            # write each item on a new line
            fp.write("%s\n" % item)

def clear_lock_flight():
    with open(r'C:\Users\ZinZayin\Desktop\TG_JobAssignment\datalock.txt', 'w') as f:
        f.truncate(0)



root.mainloop()