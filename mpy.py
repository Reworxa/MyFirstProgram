from cgitb import text
from fileinput import close
from tkinter import *
import webbrowser

class MessageTypes:
    def okCancel(textOKC, func):
        app = Tk()
        app.title("Message")

        okcanceln_message = Label(app, text=textOKC)
        okcanceln_message.pack()

        def getClicked():
            func()
            app.destroy()

        okButton = Button(app, text="OK", command=getClicked, width=100)
        okButton.pack()

        def getCancelClicked():
            app.destroy()

        cancelButton = Button(app, text="Cancel", command=getCancelClicked, width=100)
        cancelButton.pack()
        
        app.mainloop()


    def Normal(textLabel):
        app = Tk()
        app.title("Message")

        textn_message = Label(app, text=str(textLabel))
        textn_message.pack()
        app.mainloop()

    def yesNo(textOKC, func):
        app = Tk()
        app.title("Message")

        okcanceln_message = Label(app, text=textOKC)
        okcanceln_message.pack()

        def getClicked():
            func()
            app.destroy()

        okButton = Button(app, text="YES", command=getClicked, width=100)
        okButton.pack()

        def getCancelClicked():
            app.destroy()

        cancelButton = Button(app, text="NO", command=getCancelClicked, width=100)
        cancelButton.pack()

        app.mainloop()

    def okhelp(TextOKC, func, helpLink):
        app = Tk()
        app.title("Message")

        textMessage = Label(app, text=TextOKC)
        textMessage.pack()

        def OkClicked():
            func()
            app.destroy()

        okButton = Button(app, text="OK", command=OkClicked)
        okButton.pack()

        def help():
            webbrowser.open(str(helpLink), new=2)
            app.destroy()

        HelpButton = Button(app, text="HELP", command=help)
        HelpButton.pack()

        app.mainloop()

