from tkinter import*
root = Tk()
root.geometry("500x400")

def getvals():
    print("accepted")

Label(root, text="CONTACT BOOK ", font="arial 15 bold").grid(row=0, column=4,)

name = Label(root, text="Name")
phoneNo = Label(root, text="PhoneNo")
email = Label(root, text="Email")
gender = Label(root, text="Gender")
age= Label(root, text="Age")
aadharNo = Label(root, text="AadharNo")
address = Label(root, text="Address")
city = Label(root, text="City")
state = Label(root, text="State")
pincode = Label(root, text="Pincode")

name.grid(row=1, column=2)
phoneNo.grid(row=2, column=2)
email.grid(row=3, column=2)
gender.grid(row=4, column=2)
age.grid(row=5, column=2)
aadharNo.grid(row=6, column=2)
address.grid(row=7, column=2)
city.grid(row=8, column=2)
state.grid(row=9, column=2)
pincode.grid(row=10, column=2)


nameVlaue = StringVar
phoneValue = StringVar
emailValue = StringVar
genderValue = StringVar
ageValue = StringVar
aadharNoValue = StringVar
addressValue = StringVar
cityValue = StringVar
stateValue = StringVar
pincodeValue = StringVar
checkValue = IntVar

nameentry = Entry(root, textvariable =nameVlaue)
phoneentry = Entry(root, textvariable =phoneValue)
emailentry = Entry(root, textvariable =emailValue)
genderentry = Entry(root, textvariable =genderValue)
ageentry = Entry(root, textvariable =ageValue)
aadharentry = Entry(root, textvariable =aadharNoValue)
addressentry = Entry(root, textvariable =addressValue)
cityentry = Entry(root, textvariable =cityValue)
stateentry = Entry(root, textvariable =stateValue)
pincodeentry = Entry(root, textvariable =pincodeValue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
emailentry.grid(row=3, column=3)
genderentry.grid(row=4, column=3)
ageentry.grid(row=5, column=3)
aadharentry.grid(row=6, column=3)
addressentry.grid(row=7, column=3)
cityentry.grid(row=8, column=3)
stateentry.grid(row=9, column=3)
pincodeentry.grid(row=10, column=3)

Button(text="submit", command=getvals).grid(row=15, column=4)

root.mainloop()














