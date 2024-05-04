from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def effacer():
    ff.ls.clear()
def conv10_b(n,b):
    ch=""
    while n != 0:
        r=n%b
        if 0<=r<=9:
            ch=chr(r+48)+ ch
        else:
            ch=chr(r+55)+ ch
        n = n // b
    if ch=="":
        ch="0"
    return(ch)
def conv():
    
    if  not ff.len.text().isdecimal():
        msg="Donner un nombre décimal"
    elif not ff.leb.text().isdecimal():
        msg="La base doit être numérique "
    elif not(2<=int(ff.leb.text())<=16):
        msg="La base doit êtrecomprise entre 2 et 16 "
    else:
        n=int(ff.len.text())
        b=int(ff.leb.text())
        msg=conv10_b(n,b)
        s="("+str(n)+")10 ="+"("+msg+")"+str(b)
        ff.ls.addItem(s)
    ff.lres.setText(msg)
    
        










app=QApplication([])
ff=loadUi("Interface.ui")
ff.show()
ff.bconv.clicked.connect(conv)
ff.beff.clicked.connect(effacer)
app.exec_()