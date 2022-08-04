import subprocess
from tkinter import *
import tkinter as tk
from subprocess import call
import numpy
import os
from subprocess import Popen, PIPE
from os import path
from tkinter import messagebox
##Make sure that above modules are installed
    
def but1():
    messagebox.showinfo("Instruction","Wait Until it changes from 'Non-responding to responding'")
    subprocess.call('git clone https://github.com/googlecodelabs/tensorflow-for-poets-2',shell=True)
    subprocess.call('cd tensorflow-for-poets-2 && cd tf_files && mkdir flower_photos',shell=True)
    
def but2():
    messagebox.showinfo("Instructions","1. Please copy the folder containing pictures you wanna classify in the popup window.\n2. Make Sure that the name of the folder is right.\n3.Then proceed to step 3.")
    subprocess.call('cd tensorflow-for-poets-2\\tf_files\\flower_photos && start.',shell=True)
    
def but3():
    messagebox.showinfo("Instruction","The following training takes Time")
    subprocess.call('Step_3.sh',shell=True)
    messagebox.showinfo("Progress","From Step_4 we are gonna train it for Android")
def but4():
    #os.startfile('C:\\Users\\LENOVO\\Desktop\\Gui_TF\\Step_4.sh')
    subprocess.call('Step_4.sh',shell=True)
    #messagebox.showinfo("Progress","And")
def but5():
    #messagebox.showinfo("Instruction","1.Make the following change in the popup\n2.  private static final String INPUT_NAME ="+'"'+"input"+'"'+"\n private static final String OUTPUT_NAME ="+'"'+"final_result"+'"'+"\n i.e., MobilenetV1/Predictions/Softmax to final_result" )
    #subprocess.call('cd tensorflow-for-poets-2/android/tfmobile/src/org/tensorflow/demo && ClassifierActivity.java',shell=True)
    subprocess.call('cd tensorflow-for-poets-2/android/tfmobile/src/org/tensorflow/demo && del ClassifierActivity.java ',shell=True)
    subprocess.call('copy ClassifierActivity.java "tensorflow-for-poets-2/android/tfmobile/src/org/tensorflow/demo"',shell=True)
    #os.startfile('C:\\Users\\LENOVO\\Desktop\\Gui_TF\\tensorflow-for-poets-2\\android\\tfmobile\\src\\org\\tensorflow\\demo\\ClassifierActivity.java')
def but6():
    k=subprocess.call('cd tensorflow-for-poets-2 && start.',shell=True)
    
def but7():
    g=subprocess.call('pip install tkinter',shell=True)
    print(g)
    
r = tk.Tk(className='Image Classification')
r.geometry("500x600")
button=tk.Button(r,text='Start(Step1)',width=50,height=5,command=but1,bg='blue')
button2=tk.Button(r,text='Step2',width=50,height=5,command=but2,bg='red')
button3=tk.Button(r,text='Step3',width=50,height=5,command=but3,bg='yellow')
button4=tk.Button(r,text='Step4',width=50,height=5,command=but4,bg='green')
button5=tk.Button(r,text='Step5',width=50,height=5,command=but5,bg='brown')
button6=tk.Button(r,text='Show_folder',width=50,height=5,command=but6,bg='orange')
#button7=tk.Button(r,text='Install_Modules',width=50,height=5,command=but7,bg='yellow')
button.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
#button7.pack()




