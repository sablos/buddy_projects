# Mini Project

import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect( " dbFile.txt ")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS book_info(id PRIMARYKEY text, fName text, lName text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, fName, lName):
        self.dbCursor.execute("INSERT INTO book_info VALUES(?, ?, ?, ?, ?)", (id, fName, lName))
        self.dbConnection.commit()

    def Update(self, fName, lName):
        self.dbCursor.execute( "UPDATE book_info SET fName = ?, lName = ?, WHERE id = ? ", (fName, lName, id))
        self.dbConnection.commit()

    def Search(self, id):
        self.dbCursor.execute( " SELECT * FROM book_info WHERE id = ? ", (id,))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute( " DELETE FROM book_info WHERE id = ? ", (id,))

        self.dbConnection.commit()

    def Display(self):
        self.dbCursor.execute( " SELECT * FROM book_info ")
        records = self.dbCursor.fetchall()
        return records

class Values:

    def Validate(self, id, fName, lName):
        if not (id.isdigit() and (len(id) == 3)):
            return " id "
        elif not (fName.isalpha()):
            return " fName "

    column = 1, row = 3)



    # Set previous values

    self.database = Database()
    self.searchResults = self.database.Search(id)
    tkinter.Label(self.window, text=self.searchResults[0][1], width=25).grid(pady=5, column=2, row=2)
    tkinter.Label(self.window, text=self.searchResults[0][2], width=25).grid(pady=5, column=2, row=3)
    tkinter.Label(self.window, text=self.searchResults[0][3], width=25).grid(pady=5, column=2, row=4)
    # Fields
    # Entry widgets
    self.fNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.fName)
    self.lNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lName)
    self.fNameEntry.grid(pady=5, column=3, row=2)
    self.lNameEntry.grid(pady=5, column=3, row=3)
    # Combobox widgets
    # Button widgets
    tkinter.Button(self.window, width=20, text= " Update ", command = self.Update).grid(pady=15, padx=5, column=1,
                                                                                        row=14)
    tkinter.Button(self.window, width=20, text= " Reset ", command = self.Reset).grid(pady=15, padx=5, column=2, row=14)
    tkinter.Button(self.window, width=20, text= " Close ", command = self.window.destroy).grid(pady=15, padx=5,
                                                                                              column=3, row=14)
    self.window.mainloop()

    def Update(self):
        self.database = Database()
        self.database.Update(self.fNameEntry.get(), self.lNameEntry.get(), self.id)
        tkinter.messagebox.showinfo( " Updated data ", " Successfully updated the above data in the database ")

    def Reset(self):
        self.fNameEntry.delete(0, tkinter.END)
        self.lNameEntry.delete(0, tkinter.END)