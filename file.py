from tkinter import*


root=Tk()
root.title("ADV-C147: ENCRYPTION WITH ASCII CODE")
root.geometry("400x400")
root.configure(background='green')
enter_word= Entry(root)
enter_word.place(relx=0.5,rely=0.4, anchor=CENTER)
Ascii = Label(root,text="Name in Ascii : ", bg="cyan" , fg ="black")
Encrypted = Label(root,text="Encrypted Name : ", bg="red" , fg ="white")

def asciiConverter():
    input_word = enter_word.get()
  
    for letter in input_word :
        Ascii["text"] += str(ord(letter)) + ","
        ascii1 = int(ord(letter))
        encrypted = ascii1 - 1
        Encrypted["text"] += str(chr(encrypted))
btn=Button(root,text="Show name in Ascii",command=asciiConverter, bg='gold', fg ='black')
btn.place(relx=0.5 , rely=0.5, anchor=CENTER) 
Ascii.place(relx=0.5,rely=0.6, anchor=CENTER)  
Encrypted.place(relx=0.5,rely=0.7, anchor=CENTER) 
root.mainloop()
