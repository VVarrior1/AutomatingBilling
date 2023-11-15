import pyautogui as pa
import time
import pandas as pd
import flights
import tkinter as tkk
from tkinter import messagebox
from tkinter import filedialog


go_away = (1001, 317)
date_position = (161, 451)  # company laptop
add_billing_entry = (557, 327)  # company laptop
# sky_cafe_billing_entries = (555, 417)  # personal laptop
sky_cafe_billing_entries = (372, 327)  # work laptop
# AD_HOC_CHARGES = (575, 540)  # personal laptop
AD_HOC_CHARGES = (390, 429)  # work laptop
# AD_HOC_DATE_CLICK = (303, 561)  # personal laptop
AD_HOC_DATE_CLICK = (165, 447)  # work laptop
file_name = "Your file path will show here"

#
window = tkk.Tk()
window.title('Billing Automation for skycafe')
window.minsize(width=500, height=500)
days_back_label = tkk.Label(text='days back')
days_back_label.grid(row=0, column=0)
date_back = tkk.Entry()
date_back.insert(tkk.END, '0')
date_back.grid(row=0, column=1)
file_name_label = tkk.Label(text=file_name)
file_name_label.grid(row=0, column=2, columnspan=3)
window.config(padx=50, pady=50)


def open_file():
    file_path = filedialog.askopenfilename()
    global file_name
    file_name = file_path
    file_name_label.config(text=file_name)


open_file_button = tkk.Button(text="open file", command=open_file)
open_file_button.grid(row=20, column=1)
execute_button = tkk.Button(text='execute', command=window.quit)
execute_button.grid(row=20, column=4)

saab_label = tkk.Label(text='saab')
saab_label.grid(row=1, column=0)
saab_ans = tkk.Entry()
saab_ans.insert(tkk.END, '0')
saab_ans.grid(row=1, column=1)

q1_label = tkk.Label(text='q1')
q1_label.grid(row=2, column=0)
q1_ans = tkk.Entry()
q1_ans.insert(tkk.END, '0')
q1_ans.grid(row=2, column=1)

q2_label = tkk.Label(text='q2')
q2_label.grid(row=3, column=0)
q2_ans = tkk.Entry()
q2_ans.insert(tkk.END, '0')
q2_ans.grid(row=3, column=1)

jettsl1sc_label = tkk.Label(text='jettsl1')
jettsl1sc_label.grid(row=4, column=0)
jettsl1sc_ans = tkk.Entry()
jettsl1sc_ans.insert(tkk.END, '0')
jettsl1sc_ans.grid(row=4, column=1)

jettsl2sc_label = tkk.Label(text='jettsl2sc')
jettsl2sc_label.grid(row=5, column=0)
jettsl2sc_ans = tkk.Entry()
jettsl2sc_ans.insert(tkk.END, '0')
jettsl2sc_ans.grid(row=5, column=1)

jettsl3sc_label = tkk.Label(text='jettsl3sc')
jettsl3sc_label.grid(row=6, column=0)
jettsl3sc_ans = tkk.Entry()
jettsl3sc_ans.insert(tkk.END, '0')
jettsl3sc_ans.grid(row=6, column=1)

jettsl5sc_label = tkk.Label(text='jettsl5sc')
jettsl5sc_label.grid(row=7, column=0)
jettsl5sc_ans = tkk.Entry()
jettsl5sc_ans.insert(tkk.END, '0')
jettsl5sc_ans.grid(row=7, column=1)

jettsl2dc_label = tkk.Label(text='jettsl2dc')
jettsl2dc_label.grid(row=8, column=0)
jettsl2dc_ans = tkk.Entry()
jettsl2dc_ans.insert(tkk.END, '0')
jettsl2dc_ans.grid(row=8, column=1)

jettsl3dc_label = tkk.Label(text='jettsl3dc')
jettsl3dc_label.grid(row=9, column=0)
jettsl3dc_ans = tkk.Entry()
jettsl3dc_ans.insert(tkk.END, '0')
jettsl3dc_ans.grid(row=9, column=1)

jettsl4dc_label = tkk.Label(text='jettsl4dc')
jettsl4dc_label.grid(row=10, column=0)
jettsl4dc_ans = tkk.Entry()
jettsl4dc_ans.insert(tkk.END, '0')
jettsl4dc_ans.grid(row=10, column=1)

jettsl5dc_label = tkk.Label(text='jettsl5dc')
jettsl5dc_label.grid(row=11, column=0)
jettsl5dc_ans = tkk.Entry()
jettsl5dc_ans.insert(tkk.END, '0')
jettsl5dc_ans.grid(row=11, column=1)

jettslcdc_label = tkk.Label(text='jettslcdc')
jettslcdc_label.grid(row=12, column=0)
jettslcdc_ans = tkk.Entry()
jettslcdc_ans.insert(tkk.END, '0')
jettslcdc_ans.grid(row=12, column=1)

mxpptloa_label = tkk.Label(text="password")
mxpptloa_label.grid(row=13, column=0)

mxpptloa_entry = tkk.Entry(show="*")
mxpptloa_entry.grid(row=13, column=1)


def start():
    mxpptloa = mxpptloa_entry.get()
    make_sure = messagebox.askokcancel(title="Double check", message=f"You're file is {file_name}")
    if make_sure and mxpptloa == "A5599B":
        back_date = int(date_back.get())
        print(back_date)
        # sky_cafe_billing_entries = (555,417) # personal laptop
        # AD_HOC_CHARGES = (575,540) # personal laptop
        # AD_HOC_DATE_CLICK = (303,561) # personal laptop
        saab = int(saab_ans.get())
        q1 = int(q1_ans.get())
        q2 = int(q2_ans.get())
        jettsl1sc = int(jettsl1sc_ans.get())
        jettsl2sc = int(jettsl2sc_ans.get())
        jettsl3sc = int(jettsl3sc_ans.get())
        jettsl5sc = int(jettsl5sc_ans.get())
        jettsl2dc = int(jettsl2dc_ans.get())
        jettsl3dc = int(jettsl3dc_ans.get())
        jettsl4dc = int(jettsl4dc_ans.get())
        jettsl5dc = int(jettsl5dc_ans.get())
        jettslcdc = int(jettslcdc_ans.get())
        globals().update(locals())
    else:
        pass


start_button = tkk.Button(text='start', command=start)
start_button.grid(row=20, column=3)
window.mainloop()

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv(file_name)
df = df.iloc[11:]

new_header = df.iloc[0]
df = df[1:]
df.columns = ['Driver', 'Flight #', 'Origin', 'ETA Date/Time', 'PAX', 'Gate', 'Tail #', 'Flight ##', 'Destination',
              'ETD Date/Time', 'PAX', 'SL', 'SC/DC', 'Comments', 'On Tail', 'Off Tail', 'DONE Y/N']
df.drop(df.tail(1).index, inplace=True)
df.drop(df.loc[df['DONE Y/N'] == 'No'].index, inplace=True)
df["Tail #"] = df['Tail #'].astype('Int64', errors='ignore')
df["Flight ##"] = df["Flight ##"].astype('Int64', errors='ignore')
df['SL'] = df['SL'].astype('Int64', errors='ignore').astype('str')
print(df["Tail #"])
# SAAB DATA--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
saab_df = df[df['Tail #'].between(500, 600)]
saab_tail_numbers = []  # list of all saab tails
for i in range(len(saab_df)):
    saab_tail_numbers.append(int(saab_df.iloc[i, 6]))

saab_flight_numbers = []  # list of all saab flight numbers

for i in range(len(saab_df)):
    saab_flight_numbers.append(saab_df.iloc[i, 7])

# Q1 DATA--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
q1_tail_numbers = []  # list of all QSl1 tails
q1_flight_numbers = []

q1_df = df[(df['SL'] == '0') | (df['SL'] == '1')][df['Tail #'].between(400, 500)]

for i in range(len(q1_df)):
    q1_tail_numbers.append(int(q1_df.iloc[i, 6]))

for i in range(len(q1_df)):
    q1_flight_numbers.append(q1_df.iloc[i, 7])

# Q2 DATA--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
q2_tail_numbers = []  # list of all QSl1 tails
q2_flight_numbers = []

q2_df = df[(df['SL'] == '2') | (df['SL'] == '3') | (df['SL'] == 'C')][df['Tail #'].between(400, 500)]

for i in range(len(q2_df)):
    q2_tail_numbers.append(int(q2_df.iloc[i, 6]))

for i in range(len(q2_df)):
    q2_flight_numbers.append(q2_df.iloc[i, 7])

# JETTSL1SC--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

jettsl1sc_tail_numbers = []  # list of all jettsl1sc tails
jettsl1sc_flight_numbers = []

jettsl1sc_df = df[(df['SL'] == '1')][df['SC/DC'] == 'SC'][~df['Tail #'].between(400, 500)][
    ~df['Tail #'].between(500, 600)]

for i in range(len(jettsl1sc_df)):
    jettsl1sc_tail_numbers.append(int(jettsl1sc_df.iloc[i, 6]))

for i in range(len(jettsl1sc_df)):
    jettsl1sc_flight_numbers.append(jettsl1sc_df.iloc[i, 7])

# JETTSL2SC---------------------------------------------------------------------------------------------------------------------

jettsl2sc_tail_numbers = []  # list of all jettsl1sc tails
jettsl2sc_flight_numbers = []

jettsl2sc_df = df[(df['SL'] == '2')][df['SC/DC'] == 'SC'][~df['Tail #'].between(400, 500)][
    ~df['Tail #'].between(500, 600)]

for i in range(len(jettsl2sc_df)):
    jettsl2sc_tail_numbers.append(int(jettsl2sc_df.iloc[i, 6]))

for i in range(len(jettsl2sc_df)):
    jettsl2sc_flight_numbers.append(jettsl2sc_df.iloc[i, 7])

# JETTSL3SC--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
jettsl3sc_tail_numbers = []  # list of all jettsl1sc tails
jettsl3sc_flight_numbers = []

jettsl3sc_df = df[(df['SL'] == '3')][df['SC/DC'] == 'SC'][~df['Tail #'].between(400, 500)][
    ~df['Tail #'].between(500, 600)]

for i in range(len(jettsl3sc_df)):
    tail_int = int(jettsl3sc_df.iloc[i, 6])
    jettsl3sc_tail_numbers.append(tail_int)

for i in range(len(jettsl3sc_df)):
    jettsl3sc_flight_numbers.append(jettsl3sc_df.iloc[i, 7])
# JETTSL5SC--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

jettsl5sc_tail_numbers = []  # list of all jettsl1sc tails
jettsl5sc_flight_numbers = []

jettsl5sc_df = df[(df['SL'] == '5')][df['SC/DC'] == 'SC'][~df['Tail #'].between(400, 500)][
    ~df['Tail #'].between(500, 600)]

for i in range(len(jettsl5sc_df)):
    jettsl5sc_tail_numbers.append(int(jettsl5sc_df.iloc[i, 6]))

for i in range(len(jettsl5sc_df)):
    jettsl5sc_flight_numbers.append(jettsl5sc_df.iloc[i, 7])

# JETTSL2DC--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
jettsl2dc_tail_numbers = []  # list of all jettsl1sc tails
jettsl2dc_flight_numbers = []

jettsl2dc_df = df[(df['SL'] == '2')][df['SC/DC'] == 'DC'][~df['Tail #'].between(400, 500)][
    ~df['Tail #'].between(500, 600)]

for i in range(len(jettsl2dc_df)):
    jettsl2dc_tail_numbers.append(int(jettsl2dc_df.iloc[i, 6]))

for i in range(len(jettsl2dc_df)):
    jettsl2dc_flight_numbers.append(jettsl2dc_df.iloc[i, 7])
# JETTSL3DC--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

jettsl3dc_tail_numbers = []  # list of all jettsl1sc tails
jettsl3dc_flight_numbers = []

jettsl3dc_df = df[(df['SL'] == '3')][df['SC/DC'] == 'DC'][~df['Tail #'].between(400, 500)][
    ~df['Tail #'].between(500, 600)]

for i in range(len(jettsl3dc_df)):
    jettsl3dc_tail_numbers.append(int(jettsl3dc_df.iloc[i, 6]))

for i in range(len(jettsl3dc_df)):
    jettsl3dc_flight_numbers.append(jettsl3dc_df.iloc[i, 7])

# JETTSL4DC--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
jettsl4dc_tail_numbers = []  # list of all jettsl1sc tails
jettsl4dc_flight_numbers = []

jettsl4dc_df = df[(df['SL'] == '4')][df['SC/DC'] == 'DC'][~df['Tail #'].between(400, 500)][
    ~df['Tail #'].between(500, 600)]

for i in range(len(jettsl4dc_df)):
    jettsl4dc_tail_numbers.append(int(jettsl4dc_df.iloc[i, 6]))

for i in range(len(jettsl4dc_df)):
    jettsl4dc_flight_numbers.append(jettsl4dc_df.iloc[i, 7])
# JETTSL5DC
jettsl5dc_tail_numbers = []  # list of all jettsl1sc tails
jettsl5dc_flight_numbers = []

jettsl5dc_df = df[(df['SL'] == '5')][df['SC/DC'] == 'DC'][~df['Tail #'].between(400, 500)][
    ~df['Tail #'].between(500, 600)]

for i in range(len(jettsl5dc_df)):
    jettsl5dc_tail_numbers.append(int(jettsl5dc_df.iloc[i, 6]))

for i in range(len(jettsl5dc_df)):
    jettsl5dc_flight_numbers.append(jettsl5dc_df.iloc[i, 7])

adhocs_dryice_quantity = (len(jettsl5dc_flight_numbers) + len(jettsl4dc_flight_numbers)) * 4 + (
            len(jettsl5sc_flight_numbers) * 2)

print(adhocs_dryice_quantity)
# JETTSLCDC------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

jettslcdc_tail_numbers = []  # list of all jettsl1sc tails
jettslcdc_flight_numbers = []

jettslcdc_df = df[(df['SL'] == 'C')][df['SC/DC'] == 'DC'][~df['Tail #'].between(400, 500)][
    ~df['Tail #'].between(500, 600)]

for i in range(len(jettslcdc_df)):
    jettslcdc_tail_numbers.append(int(jettslcdc_df.iloc[i, 6]))

for i in range(len(jettslcdc_df)):
    jettslcdc_flight_numbers.append(jettslcdc_df.iloc[i, 7])


# Automation process ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def setup():
    time.sleep(2)
    keep_search_2 = True
    while keep_search_2:
        time.sleep(1)
        if pa.pixel(38, 423) == (54,54,54):
            pa.click(date_position)
            time.sleep(0.25)
            with pa.hold('ctrl'):
                pa.press('left', back_date)
            keep_search_2 = False

    pa.press('enter')
    keep_search_for_station_select = True
    while keep_search_for_station_select:
        time.sleep(1)
        if pa.pixel(79,533) == (54,54,54):
            keep_search_for_station_select = False
            time.sleep(1)
    pa.press('tab')
    time.sleep(0.25)
    pa.press('down', 25)
    pa.press(['up', 'up'])
    pa.press('enter')
    pa.press('tab')
    pa.press('down')
    time.sleep(1)
    keep_search_3 = True
    while keep_search_3:
        time.sleep(1)
        if pa.pixel(288, 680) != (153,153,153):
            pa.press('down', 8)
            pa.press('enter')
            pa.press('tab')
            pa.move(go_away)
            keep_search_3 = False




def after_submition():
    time.sleep(2)
    keep_search_1 = True
    while keep_search_1:
        time.sleep(1)
        if pa.pixel(463, 332) == (0, 57, 109):
            time.sleep(1)
            pa.click(add_billing_entry)  # company laptop
            keep_search_1 = False


def adhoc_dryice():
    time.sleep(10)
    pa.click(sky_cafe_billing_entries)
    time.sleep(10)
    pa.click(AD_HOC_CHARGES)
    time.sleep(10)
    pa.click(AD_HOC_DATE_CLICK)
    with pa.hold('ctrl'):
        pa.press('left', back_date)
    pa.press('enter')
    pa.press('tab')
    time.sleep(2)
    pa.press('down', 19)
    pa.press('enter')
    pa.press('tab')
    time.sleep(5)
    pa.write('west')
    time.sleep(1)
    pa.press('enter')
    pa.press('tab')
    pa.write(str(adhocs_dryice_quantity))
    pa.press('tab')
    time.sleep(1)
    pa.press('down', 6)
    pa.press('tab')
    time.sleep(1)
    pa.write('ws')
    pa.press('enter')
    pa.press('tab')
    pa.write('Multiple')
    time.sleep(0.5)
    pa.press('enter')


def auto_saab(i):
    f_n = i
    t_n = i
    for i in range(len(saab_flight_numbers)):
        if t_n >= len(saab_tail_numbers):
            return
        setup()
        flights.saab()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = saab_tail_numbers[t_n]
        flight_number = saab_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1
        after_submition()
        time.sleep(1)


def auto_q1(i):
    f_n = i
    t_n = i

    for i in range(len(q1_flight_numbers)):
        if t_n >= len(q1_tail_numbers):
            return
        setup()
        flights.q1()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = q1_tail_numbers[t_n]
        flight_number = q1_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1

        after_submition()
        time.sleep(1)


def auto_q2(i):
    f_n = i
    t_n = i
    for i in range(len(q2_flight_numbers)):
        if t_n >= len(q2_tail_numbers):
            return
        setup()
        flights.q2()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = q2_tail_numbers[t_n]
        flight_number = q2_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1

        after_submition()
        time.sleep(1)


def auto_jett1sc(i):
    f_n = i
    t_n = i
    for i in range(len(jettsl1sc_flight_numbers)):
        if t_n >= len(jettsl1sc_tail_numbers):
            return
        setup()
        flights.jet1sc()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = jettsl1sc_tail_numbers[t_n]
        flight_number = jettsl1sc_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1

        after_submition()
        time.sleep(1)


def auto_jett2sc(i):
    f_n = i
    t_n = i
    for i in range(len(jettsl2sc_flight_numbers)):
        if t_n >= len(jettsl2sc_tail_numbers):
            return
        setup()
        flights.jet2sc()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = jettsl2sc_tail_numbers[t_n]
        flight_number = jettsl2sc_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1

        after_submition()
        time.sleep(1)


def auto_jett3sc(i):
    f_n = i
    t_n = i
    for i in range(len(jettsl3sc_flight_numbers)):
        if t_n >= len(jettsl3sc_tail_numbers):
            return
        setup()
        flights.jet3sc()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = jettsl3sc_tail_numbers[t_n]
        flight_number = jettsl3sc_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1

        after_submition()
        time.sleep(1)


def auto_jett5sc(i):
    f_n = i
    t_n = i
    for i in range(len(jettsl5sc_flight_numbers)):
        if t_n >= len(jettsl5sc_tail_numbers):
            return
        setup()
        flights.jet5sc()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = jettsl5sc_tail_numbers[t_n]
        flight_number = jettsl5sc_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1

        after_submition()
        time.sleep(1)


def auto_jett2dc(i):
    f_n = i
    t_n = i
    for i in range(len(jettsl2dc_flight_numbers)):
        if t_n >= len(jettsl2dc_tail_numbers):
            return
        setup()
        flights.jet2dc()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = jettsl2dc_tail_numbers[t_n]
        flight_number = jettsl2dc_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1

        after_submition()
        time.sleep(1)


def auto_jett3dc(i):
    f_n = i
    t_n = i
    for i in range(len(jettsl3dc_flight_numbers)):
        if t_n >= len(jettsl3dc_tail_numbers):
            return
        setup()
        flights.jet3dc()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = jettsl3dc_tail_numbers[t_n]
        flight_number = jettsl3dc_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1

        after_submition()
        time.sleep(1)


def auto_jett4dc(i):
    f_n = i
    t_n = i
    for i in range(len(jettsl4dc_flight_numbers)):
        if t_n >= len(jettsl4dc_tail_numbers):
            return
        setup()
        flights.jet4dc()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = jettsl4dc_tail_numbers[t_n]
        flight_number = jettsl4dc_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1

        after_submition()
        time.sleep(1)


def auto_jett5dc(i):
    f_n = i
    t_n = i
    for i in range(len(jettsl5dc_flight_numbers)):
        if t_n >= len(jettsl5dc_tail_numbers):
            return
        setup()
        flights.jet5dc()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = jettsl5dc_tail_numbers[t_n]
        flight_number = jettsl5dc_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1

        after_submition()
        time.sleep(1)


def auto_jettcdc(i):
    f_n = i
    t_n = i
    for i in range(len(jettslcdc_flight_numbers)):
        if t_n >= len(jettslcdc_tail_numbers):
            return
        setup()
        flights.jetcdc()  # place the flight bill here
        pa.press('tab')
        pa.press('tab')
        pa.press('down')
        pa.press('tab')
        pa.press('tab')

        tail_number = jettslcdc_tail_numbers[t_n]
        flight_number = jettslcdc_flight_numbers[t_n]

        pa.write(str(flight_number))
        pa.press('tab')
        pa.write(str(tail_number))
        pa.press('enter')
        time.sleep(0.3)
        pa.press('enter')

        f_n += 1
        t_n += 1

        after_submition()
        time.sleep(1)

time.sleep(5)
auto_saab(saab)
auto_q1(q1)
auto_q2(q2)
auto_jett1sc(jettsl1sc)
auto_jett2sc(jettsl2sc)
auto_jett3sc(jettsl3sc)
auto_jett5sc(jettsl5sc)
auto_jett2dc(jettsl2dc)
auto_jett3dc(jettsl3dc)
auto_jett4dc(jettsl4dc)
auto_jett5dc(jettsl5dc)
auto_jettcdc(jettslcdc)
adhoc_dryice()

window.mainloop()
