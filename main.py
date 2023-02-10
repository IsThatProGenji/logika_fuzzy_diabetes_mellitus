#! /usr/bin/env python
import csv
import sys


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = 0
except ImportError:
    import tkinter.ttk as ttk

    py3 = 1



import threading


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    top = New_Toplevel_1(root)

    root.mainloop()


w = None
age_low = None
age_medium = None
age_high = None

glucose_low = None
glucose_medium = None
glucose_high = None

Bmi_low = None
Bmi_medium = None
Bsmi_high = None


def create_New_Toplevel_1(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel_1(w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
        top is the toplevel containing window."""
        _bgcolor = "#d9d9d9"  # X11 color: 'gray85'
        _fgcolor = "#000000"  # X11 color: 'black'
        _compcolor = "#d9d9d9"  # X11 color: 'gray85'
        _ana1color = "#d9d9d9"  # X11 color: 'gray85'
        _ana2color = "#d9d9d9"  # X11 color: 'gray85'
        font11 = (
            "-family Arial -size 19 -weight normal -slant roman "
            "-underline 0 -overstrike 0"
        )
        font12 = (
            "-family Arial -size 12 -weight normal -slant roman "
            "-underline 0 -overstrike 0"
        )
        font14 = (
            "-family Arial -size 15 -weight normal -slant roman "
            "-underline 0 -overstrike 0"
        )
        font15 = (
            "-family Arial -size 12 -weight bold -slant roman "
            "-underline 0 -overstrike 0"
        )
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use("winnative")
        self.style.configure(".", background=_bgcolor)
        self.style.configure(".", foreground=_fgcolor)
        self.style.configure(".", font="TkDefaultFont")
        self.style.map(
            ".", background=[("selected", _compcolor), ("active", _ana2color)]
        )

        top.geometry("968x493+919+245")
        top.title("Diabetes Detection Fuzzy System")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#b9b9b9")
        top.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.01, rely=0.02, relheight=0.94, relwidth=0.48)
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief=GROOVE)
        self.TFrame1.configure(width=465)

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.3, rely=0.04, height=32, width=350)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=font11)
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text="""Enter Patient's data """)

        # ----------------------------AGE----------------------------------
        self.TLabel2 = ttk.Label(self.TFrame1)
        self.TLabel2.place(relx=0.02, rely=0.15, height=39, width=120)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font=font12)
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text="""Age""")

        self.TEntry_Age = ttk.Entry(self.TFrame1)
        self.TEntry_Age.place(relx=0.24, rely=0.17, relheight=0.05, relwidth=0.53)
        self.TEntry_Age.configure(width=246)
        self.TEntry_Age.configure(takefocus="")
        self.TEntry_Age.configure(cursor="ibeam")

        # -----------------------------------Glucose----------------------------------------
        self.TLabel3 = ttk.Label(self.TFrame1)
        self.TLabel3.place(relx=0.02, rely=0.24, height=39, width=120)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font=font12)
        self.TLabel3.configure(relief=FLAT)
        self.TLabel3.configure(text="""Glucose Level""")

        self.TEntry_Glucose = ttk.Entry(self.TFrame1)
        self.TEntry_Glucose.place(relx=0.24, rely=0.26, relheight=0.05, relwidth=0.53)
        self.TEntry_Glucose.configure(width=246)
        self.TEntry_Glucose.configure(takefocus="")
        self.TEntry_Glucose.configure(cursor="ibeam")

        # ---------------------------------BMI-------------------------------

        self.TLabel4 = ttk.Label(self.TFrame1)
        self.TLabel4.place(relx=0.02, rely=0.33, height=39, width=120)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font=font12)
        self.TLabel4.configure(relief=FLAT)
        self.TLabel4.configure(text="""BMI""")

        self.TEntry_Bmi = ttk.Entry(self.TFrame1)
        self.TEntry_Bmi.place(relx=0.24, rely=0.35, relheight=0.05, relwidth=0.53)
        self.TEntry_Bmi.configure(width=246)
        self.TEntry_Bmi.configure(takefocus="")
        self.TEntry_Bmi.configure(cursor="ibeam")

        self.TButton_eval = ttk.Button(self.TFrame1)
        self.TButton_eval.place(relx=0.35, rely=0.42, height=35, width=126)
        self.TButton_eval.configure(takefocus="")
        self.TButton_eval.configure(text="""Evaluate""")
        self.TButton_eval.bind(
            "<Button-1>", lambda e: main_support.TButton_eval_onClick(e)
        )
      
        
        self.TLabel_Indicator = ttk.Label(self.TFrame1)
        self.TLabel_Indicator.place(relx=0.29, rely=0.88, height=19, width=184)
        self.TLabel_Indicator.configure(background="#d9d9d9")
        self.TLabel_Indicator.configure(foreground="#000000")
        self.TLabel_Indicator.configure(relief=FLAT)
        self.TLabel_Indicator.configure(anchor=CENTER)

        self.TLabel_Fuzzifikasi = ttk.Label(self.TFrame1)
        self.TLabel_Fuzzifikasi.place(relx=0.02, rely=0.44, height=35, width=100)
        self.TLabel_Fuzzifikasi.configure(background="#d9d9d9",foreground="#000000",relief=FLAT)
    

        self.TLabel_AgeLow = ttk.Label(self.TFrame1)
        self.TLabel_AgeLow.place(relx=0.02, rely=0.50, height=35, width=200)
        self.TLabel_AgeLow.configure(background="#d9d9d9")
        self.TLabel_AgeLow.configure(foreground="#000000")
        self.TLabel_AgeLow.configure(relief=FLAT)

        self.TLabel_AgeMedium = ttk.Label(self.TFrame1)
        self.TLabel_AgeMedium.place(relx=0.02, rely=0.56, height=35, width=200)
        self.TLabel_AgeMedium.configure(background="#d9d9d9")
        self.TLabel_AgeMedium.configure(foreground="#000000")
        self.TLabel_AgeMedium.configure(relief=FLAT)
        
        self.TLabel_AgeHigh= ttk.Label(self.TFrame1)
        self.TLabel_AgeHigh.place(relx=0.02, rely=0.62, height=35, width=200)
        self.TLabel_AgeHigh.configure(background="#d9d9d9")
        self.TLabel_AgeHigh.configure(foreground="#000000")
        self.TLabel_AgeHigh.configure(relief=FLAT)
        
        self.TLabel_GlucoseLow= ttk.Label(self.TFrame1)
        self.TLabel_GlucoseLow.place(relx=0.02, rely=0.68, height=35, width=200)
        self.TLabel_GlucoseLow.configure(background="#d9d9d9")
        self.TLabel_GlucoseLow.configure(foreground="#000000")
        self.TLabel_GlucoseLow.configure(relief=FLAT)
        
        self.TLabel_GlucoseMedium= ttk.Label(self.TFrame1)
        self.TLabel_GlucoseMedium.place(relx=0.02, rely=0.74, height=35, width=200)
        self.TLabel_GlucoseMedium.configure(background="#d9d9d9")
        self.TLabel_GlucoseMedium.configure(foreground="#000000")
        self.TLabel_GlucoseMedium.configure(relief=FLAT)

        self.TLabel_GlucoseHigh= ttk.Label(self.TFrame1)
        self.TLabel_GlucoseHigh.place(relx=0.02, rely=0.80, height=35, width=200)
        self.TLabel_GlucoseHigh.configure(background="#d9d9d9")
        self.TLabel_GlucoseHigh.configure(foreground="#000000")
        self.TLabel_GlucoseHigh.configure(relief=FLAT)
        
        self.TLabel_BmiLow= ttk.Label(self.TFrame1)
        self.TLabel_BmiLow.place(relx=0.50, rely=0.50, height=35, width=200)
        self.TLabel_BmiLow.configure(background="#d9d9d9")
        self.TLabel_BmiLow.configure(foreground="#000000")
        self.TLabel_BmiLow.configure(relief=FLAT)
        
        self.TLabel_BmiMedium= ttk.Label(self.TFrame1)
        self.TLabel_BmiMedium.place(relx=0.50, rely=0.56, height=35, width=200)
        self.TLabel_BmiMedium.configure(background="#d9d9d9")
        self.TLabel_BmiMedium.configure(foreground="#000000")
        self.TLabel_BmiMedium.configure(relief=FLAT)

        self.TLabel_BmiHigh= ttk.Label(self.TFrame1)
        self.TLabel_BmiHigh.place(relx=0.50, rely=0.62, height=35, width=200)
        self.TLabel_BmiHigh.configure(background="#d9d9d9")
        self.TLabel_BmiHigh.configure(foreground="#000000")
        self.TLabel_BmiHigh.configure(relief=FLAT)

        


        self.TLabel7 = ttk.Label(self.TFrame1)
        self.TLabel7.place(relx=0.8, rely=0.18, height=19, width=36)
        self.TLabel7.configure(background="#d9d9d9")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(font=font15)
        self.TLabel7.configure(relief=FLAT)
        self.TLabel7.configure(anchor=W)
        self.TLabel7.configure(text="""0-81""")
        self.TLabel7.configure(width=36)

        self.TLabel8 = ttk.Label(self.TFrame1)
        self.TLabel8.place(relx=0.8, rely=0.26, height=19, width=46)
        self.TLabel8.configure(background="#d9d9d9")
        self.TLabel8.configure(foreground="#000000")
        self.TLabel8.configure(font=font15)
        self.TLabel8.configure(relief=FLAT)
        self.TLabel8.configure(anchor=W)
        self.TLabel8.configure(text="""0-199""")
        self.TLabel8.configure(width=46)

        self.TLabel9 = ttk.Label(self.TFrame1)
        self.TLabel9.place(relx=0.8, rely=0.35, height=19, width=66)
        self.TLabel9.configure(background="#d9d9d9")
        self.TLabel9.configure(foreground="#000000")
        self.TLabel9.configure(font=font15)
        self.TLabel9.configure(relief=FLAT)
        self.TLabel9.configure(anchor=W)
        self.TLabel9.configure(text="""0-67.1""")
        self.TLabel9.configure(width=66)

        self.TLabel_Output = ttk.Label(top)
        self.TLabel_Output.place(relx=0.52, rely=0.06, height=19, width=200)
        self.TLabel_Output.configure(background="#d9d9d9",foreground="#000000",relief=FLAT)
       
        self.TLabel_Output.configure(text="""Inferensi :""")

        self.TLabel_OutputText = ttk.Label(top)
        self.TLabel_OutputText.place(relx=0.52, rely=0.66, height=50, width=500)
        self.TLabel_OutputText.configure(background="#d9d9d9")
        self.TLabel_OutputText.configure(foreground="#000000")
        
        self.TLabel_OutputText.configure(relief=FLAT)
       
        self.TLabel_OutputText.configure(width=500)

        self.TLabel_OutputText2 = ttk.Label(top)
        self.TLabel_OutputText2.place(relx=0.52, rely=0.72, height=29, width=500)
        self.TLabel_OutputText2.configure(background="#d9d9d9")
        self.TLabel_OutputText2.configure(foreground="#000000")
       
        self.TLabel_OutputText2.configure(relief=FLAT)
      
        self.TLabel_OutputText2.configure(width=500)

        self.TLabel_OutputText3 = ttk.Label(top)
        self.TLabel_OutputText3.place(relx=0.52, rely=0.78, height=29, width=500)
        self.TLabel_OutputText3.configure(background="#d9d9d9")
        self.TLabel_OutputText3.configure(foreground="#000000")
        self.TLabel_OutputText3.configure(relief=FLAT)
      
        self.TLabel_OutputText3.configure(width=500)
        
        self.TLabel_OutputText4 = ttk.Label(top)
        self.TLabel_OutputText4.place(relx=0.52, rely=0.84, height=29, width=500)
        self.TLabel_OutputText4.configure(background="#d9d9d9")
        self.TLabel_OutputText4.configure(foreground="#000000")
        self.TLabel_OutputText4.configure(relief=FLAT)
        self.TLabel_OutputText4.configure(width=500)
        
        self.TLabel_OutputText5 = ttk.Label(top)
        self.TLabel_OutputText5.place(relx=0.52, rely=0.90, height=29, width=500)
        self.TLabel_OutputText5.configure(background="#d9d9d9")
        self.TLabel_OutputText5.configure(foreground="#000000")
        self.TLabel_OutputText5.configure(relief=FLAT)
        self.TLabel_OutputText5.configure(width=500)
        self.TLabely= ttk.Label(self.TFrame1)
        widgets = [
            self.TEntry_Age,
            self.TEntry_Glucose,
            self.TEntry_Bmi,
        ]
        self.TButton_eval.bind(
            "<Button-1>", lambda e: self.TButton_eval_onClick(e, widgets,top=top)
        )

        self.TEntry_Age.insert(END, "50")
        self.TEntry_Glucose.insert(END, "148")
        self.TEntry_Bmi.insert(END, "33.6")

    def TButton_eval_onClick(self, p1, widgets,top =None):

    
       
        predikat = []
        z = []
        # run in multithread so our UI won't freeze
        args = [float(x.get()) for x in widgets]
        if args[0] >= 45:
            age_low = 0
        if args[0] >= 21.48 and args[0] <= 45:
            age_low = (45 - args[0]) / (45 - 21.8)
        if args[0] <= 21.48:
            age_low = 1
        if args[0] <= 21.48 or args[0] >= 63:
            age_medium = 0
        if args[0] >= 21.48 and args[0] <= 45:
            age_medium = (args[0] - 21.48) / (45 - 21.8)
        if args[0] >= 45 and args[0] <= 63:
            age_medium = (63 - args[0]) / (63 - 45)
        if args[0] <= 45:
            age_high = 0
        if args[0] >= 45 and args[0] <= 63:
            age_high = (args[0] - 45) / (63 - 45)
        if args[0] >= 63:
            age_high = 1

        if args[1] >= 152.6:
            glucose_low = 0
        if args[1] >= 88.4 and args[1] <= 152.6:
            glucose_low = (152.6 - args[1]) / (152.6 - 88.4)
        if args[1] <= 88.4:
            glucose_low = 1
        if args[1] <= 88.4 or args[1] >= 175.8:
            glucose_medium = 0
        if args[1] >= 88.4 and args[1] <= 152.6:
            glucose_medium = (args[1] - 88.4) / (152.6 - 88.4)
        if args[1] >= 152.6 and args[1] <= 175.8:
            glucose_medium = (175.8 - args[1]) / (175.8 - 152.6)
        if args[1] <= 152.6:
            glucose_high = 0
        if args[1] >= 152.6 and args[1] <= 175.8:
            glucose_high = (args[1] - 152.6) / (175.8 - 152.6)
        if args[1] >= 175.8:
            glucose_high = 1

        if args[2] >= 39.87:
            Bmi_low = 0
        if args[2] >= 24.1 and args[2] <= 39.87:
            Bmi_low = (39.87 - args[2]) / (39.87 - 24.11)
        if args[2] <= 24.11:
            Bmi_low = 1
        if args[2] <= 24.11 or args[2] >= 53.49:
            Bmi_medium = 0
        if args[2] >= 24.11 and args[2] <= 39.87:
            Bmi_medium = (args[2] - 24.11) / (39.87 - 24.11)
        if args[2] >= 39.87 and args[2] <= 53.49:
            Bmi_medium = (53.49 - args[2]) / (53.49 - 39.87)
        if args[2] <= 39.87:
            Bmi_high = 0
        if args[2] >= 39.87 and args[2] <= 53.49:
            Bmi_high = (args[2] - 39.87) / (53.49 - 39.87)
        if args[2] >= 53.49:
            Bmi_high = 1

        print(age_low)
        print(age_medium)
        print(age_high)
        print(glucose_low)
        print(glucose_medium)
        print(glucose_high)
        print(Bmi_low)
        print(Bmi_medium)
        print(Bmi_high)
        ruleSet= []
        # 1
        if age_low != 0 and glucose_low != 0 and Bmi_low != 0:
            predikat.append(min(age_low, glucose_low, Bmi_low))
            z.append(1)
            ruleSet.append("if age is low and glucose is low and bmi is low then diabetic is 1")
        # 2
        if age_low != 0 and glucose_low != 0 and Bmi_medium != 0:
            predikat.append(min(age_low, glucose_low, Bmi_medium))
            z.append(1)
            ruleSet.append("if age is low and glucose is low and bmi is medium then diabetic is 1")
        # 3
        if age_low != 0 and glucose_low != 0 and Bmi_high != 0:
            predikat.append(min(age_low, glucose_low, Bmi_high))
            z.append(1)
            ruleSet.append("if age is low and glucose is low and bmi is high then diabetic is 1")
        # 4
        if age_low != 0 and glucose_medium != 0 and Bmi_low != 0:
            predikat.append(min(age_low, glucose_medium, Bmi_low))
            z.append(1)
            ruleSet.append("if age is low and glucose is medium and bmi is low then diabetic is 1")
        # 5
        if age_low != 0 and glucose_medium != 0 and Bmi_medium != 0:
            predikat.append(min(age_low, glucose_medium, Bmi_medium))
            z.append(1)
            ruleSet.append("if age is low and glucose is medium and bmi is medium then diabetic is 1")
        # 6
        if age_low != 0 and glucose_medium != 0 and Bmi_high != 0:
            predikat.append(min(age_low, glucose_medium, Bmi_high))
            z.append(0)
            ruleSet.append("if age is low and glucose is medium and bmi is high then diabetic is 0")
        # 7
        if age_low != 0 and glucose_high != 0 and Bmi_low != 0:
            predikat.append(min(age_low, glucose_high, Bmi_low))
            z.append(1)
            ruleSet.append("if age is low and glucose is high and bmi is low then diabetic is 1")
        # 8
        if age_low != 0 and glucose_high != 0 and Bmi_medium != 0:
            predikat.append(min(age_low, glucose_high, Bmi_medium))
            z.append(0)
            ruleSet.append("if age is low and glucose is high and bmi is medium then diabetic is 0")
        # 9
        if age_low != 0 and glucose_high != 0 and Bmi_high != 0:
            predikat.append(min(age_low, glucose_high, Bmi_high))
            z.append(1)
            ruleSet.append("if age is low and glucose is high and bmi is high  then diabetic is 1")
        # 10
        if age_medium != 0 and glucose_low != 0 and Bmi_low != 0:
            predikat.append(min(age_medium, glucose_low, Bmi_low))
            z.append(1)
            ruleSet.append("if age is medium and glucose is low and bmi is low then diabetic is 1")
        # 11
        if age_medium != 0 and glucose_low != 0 and Bmi_medium != 0:
            predikat.append(min(age_medium, glucose_low, Bmi_medium))
            z.append(1)
            ruleSet.append("if age is medium and glucose is low and bmi is medium then diabetic is 1")
        # 12
        if age_medium != 0 and glucose_low != 0 and Bmi_high != 0:
            predikat.append(min(age_medium, glucose_low, Bmi_high))
            z.append(0)
            ruleSet.append("if age is medium and glucose is low and bmi is high then diabetic is 0")
        # 13
        if age_medium != 0 and glucose_medium != 0 and Bmi_low != 0:
            predikat.append(min(age_medium, glucose_medium, Bmi_low))
            z.append(1)
            ruleSet.append("if age is medium and glucose is medium and bmi is low then diabetic is 1")
        # 14
        if age_medium != 0 and glucose_medium != 0 and Bmi_medium != 0:
            predikat.append(min(age_medium, glucose_medium, Bmi_medium))
            z.append(0)
            ruleSet.append("if age is medium and glucose is medium and bmi is medium then diabetic is 1")
        # 15
        if age_medium != 0 and glucose_medium != 0 and Bmi_high != 0:
            predikat.append(min(age_medium, glucose_medium, Bmi_high))
            z.append(0)
            ruleSet.append("if age is medium and glucose is medium and bmi is medium then diabetic is 0")
        # 16
        if age_medium != 0 and glucose_high != 0 and Bmi_low != 0:
            predikat.append(min(age_medium, glucose_high, Bmi_low))
            z.append(0)
            ruleSet.append("if age is medium and glucose is high and bmi is low then diabetic is 0")
        # 17
        if age_medium != 0 and glucose_high != 0 and Bmi_medium != 0:
            predikat.append(min(age_medium, glucose_high, Bmi_medium))
            z.append(0)
            ruleSet.append("if age is medium and glucose is high and bmi is medium then diabetic is 0")
        # 18
        if age_medium != 0 and glucose_high != 0 and Bmi_high != 0:
            predikat.append(min(age_medium, glucose_high, Bmi_high))
            z.append(0)
            ruleSet.append("if age is medium and glucose is high and bmi is high then diabetic is 0")
        # 19
        if age_high != 0 and glucose_low != 0 and Bmi_low != 0:
            predikat.append(min(age_high, glucose_low, Bmi_low))
            z.append(1)
            ruleSet.append("if age is high and glucose is low and bmi is low then diabetic is 1")
        # 20
        if age_high != 0 and glucose_low != 0 and Bmi_medium != 0:
            predikat.append(min(age_high, glucose_low, Bmi_medium))
            z.append(0)
            ruleSet.append("if age is high and glucose is low and bmi is medium then diabetic is 0")
        # 21
        if age_high != 0 and glucose_low != 0 and Bmi_high != 0:
            predikat.append(min(age_high, glucose_low, Bmi_high))
            z.append(0)
            ruleSet.append("if age is high and glucose is low and bmi is high then diabetic is 0")
        # 22
        if age_high != 0 and glucose_medium != 0 and Bmi_low != 0:
            predikat.append(min(age_high, glucose_medium, Bmi_low))
            z.append(0)
            ruleSet.append("if age is high and glucose is medium and bmi is low then diabetic is 0")
        # 23
        if age_high != 0 and glucose_medium != 0 and Bmi_medium != 0:
            predikat.append(min(age_high, glucose_medium, Bmi_medium))
            z.append(0)
            ruleSet.append("if age is high and glucose is medium and bmi is medium then diabetic is 0")
        # 24
        if age_high != 0 and glucose_medium != 0 and Bmi_high != 0:
            predikat.append(min(age_high, glucose_medium, Bmi_high))
            z.append(0)
            ruleSet.append("if age is high and glucose is medium and bmi is high then diabetic is 0")
        # 25
        if age_high != 0 and glucose_high != 0 and Bmi_low != 0:
            predikat.append(min(age_high, glucose_high, Bmi_low))
            z.append(0)
            ruleSet.append("if age is high and glucose is high and bmi is low then diabetic is 0")
        # 26
        if age_high != 0 and glucose_high != 0 and Bmi_medium != 0:
            predikat.append(min(age_high, glucose_high, Bmi_medium))
            z.append(0)
            ruleSet.append("if age is high and glucose is high and bmi is medium then diabetic is 0")
        # 27
        if age_high != 0 and glucose_high != 0 and Bmi_high != 0:
            predikat.append(min(age_high, glucose_high, Bmi_high))
            z.append(0)
            ruleSet.append("if age is high and glucose is high and bmi is high then diabetic is 0")
        predikat_v = 0

        for i, num in enumerate(predikat):
            predikat_v += predikat[i] * z[i]
        hasil = None
        positive = None
        negative = None

        hasil = (predikat_v / sum(predikat)) 

        if hasil >= 0.7:
            negative = 0
        if hasil >= 0.3 and hasil <= 0.7:
            negative = (0.7 - hasil) / (0.7 - 0.3)
        if hasil <= 0.3:
            negative = 1
        if hasil <= 0.3:
            positive = 0
        if hasil >= 0.3 and hasil <= 0.7:
            positive = (hasil - 0.3) / (0.7 - 0.3)
        if hasil >= 0.7:
            positive = 1
        
        print(ruleSet)
        print(z)
        print(predikat)
        print(predikat_v)
        print((predikat_v / sum(predikat)) * 2)
        print("positive", positive)
        print("negatif", negative)
        self.TLabel_Fuzzifikasi["text"] = "Fuzifikasi"
        self.TLabel_AgeLow["text"] = f"Age Low = {age_low}"
        self.TLabel_AgeMedium["text"] = f"Age Medium = {age_medium}"
        self.TLabel_AgeHigh["text"] = f"Age High= {age_high}"
        self.TLabel_GlucoseLow["text"] = f"Glucose Low = {glucose_low}"
        self.TLabel_GlucoseMedium["text"] = f"Glucose Medium = {glucose_medium}"
        self.TLabel_GlucoseHigh["text"] = f"Glucose High = {glucose_high}"
        self.TLabel_BmiLow["text"] = f"BMI Low = {Bmi_low}"
        self.TLabel_BmiMedium["text"] = f"BMI Medium = {Bmi_medium}"
        self.TLabel_BmiHigh["text"] = f"BMI High = {Bmi_high}"
        label= []
        a =[1,2,3,4,5,6,7,8]
        for i in a:
            self.TLabely= ttk.Label(top)
            self.TLabely.place(relx=0.52, rely=(0.12 + 0.06 *i) , height=35, width=500)
            self.TLabely.configure(background='#d9d9d9',foreground='#000000',relief=FLAT,text="" )
        for i, num in enumerate(ruleSet):
            
            self.TLabely= ttk.Label(top)
            self.TLabely.place(relx=0.52, rely=(0.12 + 0.06 *i) , height=35, width=500)
            self.TLabely.configure(background='#d9d9d9',foreground='#000000',relief=FLAT,text=ruleSet[i] )
        defu=''
        defu2=''
        my_formatted_list = [ '%.2f' % elem for elem in predikat ]
        for i, num in enumerate(my_formatted_list):
           
            defu += f'({my_formatted_list[i]} * {z[i]})+'
        for i, num in enumerate(my_formatted_list):
           
            defu2 += f'{my_formatted_list[i]} +'
        self.TLabel_OutputText["text"] = f"Defuzifikasi "
        self.TLabel_OutputText2["text"] = f"{defu[:-1]}"
        self.TLabel_OutputText3["text"] = f"/"
        self.TLabel_OutputText4["text"] = f"{defu2[:-1]}"
        self.TLabel_OutputText5["text"] = f"Hasil =  {round(hasil,2)},    Positive = {round(negative,2)},     Negative = {round(positive,2)}"
       

   


if __name__ == "__main__":
    vp_start_gui()
