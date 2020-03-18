import random
import time


from tkinter import *

root= Tk()

canvas1 = Canvas(root, width = 400, height = 300)
canvas1.pack()



def init():

    labelQuestion = Label(root, text= 'Somme de départ ?',font=('helvetica', 10))
    labelQuestion = canvas1.create_window(200, 100, window=labelQuestion)

    entry = Entry (root) 
    entry.focus()
    entry2 = canvas1.create_window(200, 140, window=entry)

    button = Button(text='Valider', command= lambda: start(entry))
    button =canvas1.create_window(200, 180, window=button)



def displayPot(pot):
    labelPot = Label(root, text= 'Pot: ' + str(pot) + ' €',font=('helvetica', 10))
    canvas1.create_window(200, 230, window=labelPot)    

def start(entry):  
    pot2 = entry.get()
    try:
        assert int(pot2) > 0 and int(pot2) < 10000
    except AssertionError:
        labelInfo = Label(root, "Veuillez rentrer un nombre supérieur à 0 et inférieur à 10000")
        labelInfo = canvas1.create_window(200, 100, window=labelInfo)        
    except ValueError:
        labelInfo = Label(root, text= 'Veuillez rentrer un nombre')
        labelInfo = canvas1.create_window(200, 100, window=labelInfo)

    if int(pot2) > 0 and int(pot2) < 10000 :
        pot = int(pot2)
        entry.delete(0, 'end')
        canvas1.delete("all")
        displayPot(pot)
        askNumber(pot)


def askNumber(pot):
    labelQuestion = Label(root, text= 'Misez sur un nombre entre 1 et 50:',font=('helvetica', 10))
    labelQuestion = canvas1.create_window(200, 100, window=labelQuestion)

    entry = Entry (root) 
    entry.focus()
    entry2 = canvas1.create_window(200, 140, window=entry)

    button = Button(text='Valider', command= lambda: setNumber(entry, pot))
    button =canvas1.create_window(200, 180, window=button)



def setNumber(entry, pot):
    number = entry.get()

    try:
        assert int(number) > 0 and int(number) < 50
    except AssertionError:
        labelInfo = Label(root, "Veuillez rentrer un nombre supérieur à 0 et inférieur à 50")
        labelInfo = canvas1.create_window(200, 100, window=labelInfo)        
    except ValueError:
        labelInfo = Label(root, text= 'Veuillez rentrer un nombre')
        labelInfo = canvas1.create_window(200, 100, window=labelInfo)


    if int(number) > 0 and int(number) < 50 :
        number=int(number)
        entry.delete(0, 'end')
        canvas1.delete("all")
        displayPot(pot)
        askMise(pot, number)



def askMise(pot, number):
    labelQuestion = Label(root, text= 'Misez sur une somme de votre pot:',font=('helvetica', 10))
    labelQuestion = canvas1.create_window(200, 100, window=labelQuestion)

    entry = Entry (root) 
    entry.focus()
    entry2 = canvas1.create_window(200, 140, window=entry)

    button = Button(text='Valider', command= lambda: setMise(entry, pot, number))
    button = canvas1.create_window(200, 180, window=button)







def setMise(entry, pot, number):
    mise = entry.get()
    try:
        assert int(mise) > 0 and int(mise) <= pot
    except AssertionError:
        labelInfo = Label(root, "Veuillez rentrer un nombre supérieur à 0 et inférieur à votre pot")
        labelInfo = canvas1.create_window(200, 100, window=labelInfo)        
    except ValueError:
        labelInfo = Label(root, text= 'Veuillez rentrer un nombre')
        labelInfo = canvas1.create_window(200, 100, window=labelInfo)

    if int(mise) > 0 and int(mise) <= pot :
        mise=int(mise)
        entry.delete(0, 'end')
        canvas1.delete("all")
        
        displayPot(pot)

        roll(pot, number, mise)

def roll(pot, number, mise):

    labelInfo = Label(root, text= "Vous avez misé " + str(mise) + "€ sur le chiffre " + str(number) +" !",font=('helvetica', 10))
    canvas1.create_window(200, 175, window=labelInfo)

    root.after(5000, labelInfo.destroy)

    # labelInfo2 = Label(root, text= 'ça tourne..',font=('helvetica', 10))
    # canvas1.create_window(200, 100, window=labelInfo2)
    # root.after(3000, labelInfo2.destroy)
    res = random.randint(1, 50)



    if res == number:
        pot += mise * 2
        labelInfo3 = Label(root, text= str(res) + " - GG tu gagnes "+ str(mise * 2))
        canvas1.create_window(200, 200, window=labelInfo3)
        root.after(5000, labelInfo3.destroy)


    elif number % 2 == res % 2:
        labelInfo3 = Label(root, text= str(res) + " - tu es remboursé")
        canvas1.create_window(200, 200, window=labelInfo3)
        root.after(5000, labelInfo3.destroy)

    else:
        pot -= mise
        labelInfo3 = Label(root, text= str(res) + " - raté")
        canvas1.create_window(200, 200, window=labelInfo3)  
        root.after(5000, labelInfo3.destroy)
     
    if pot <=0:
        labelInfo5 = Label(root, text= "plus d'argent")
        canvas1.create_window(200, 230, window=labelInfo5)
    else:
        labelPot = Label(root, text= 'Pot: ' + str(pot) + ' €',font=('helvetica', 10))
        canvas1.create_window(200, 230, window=labelPot)           
        root.after(5000, lambda : askNumber(pot)) 
    


init()


root.mainloop()





