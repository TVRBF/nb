class Texteditor:
    def __init__ (self):
        self.document =""
        self.undo=[]
        self.redo=[]
        
    def makechanges(self,change):
        self.undo.append(self.document)
        self.document=change
        self.redo.clear()
        print("changes applied succesfully")
    
    def undo_action(self):
        if self.undo:
            self.redo.append(self.document)
            self.document = self.undo.pop()
            print("undo succesfull")
        else:
            print("nothing to undo")
        
    def redo_action(self):
        if self.redo:
            self.undo.append(self.document)
            self.document=self.redo.pop()
        else:
            print("nothing to redo")
            
    def show(self):
        print("the cunect contend is: ",self.document)
        
t1=Texteditor()

while True:
    print("menu")
    print("1. Make A Change")
    print("2. Undo Last Change")
    print("3. Redo Last Undone Change")
    print("4. Print entire Document")
    print("5. Exit")
    
    choice = int(input("Enter Your Choice:"))
    if choice ==1:
        change=input("Enter The Change To Be Made: ")
        t1.makechanges(change)
    elif choice ==2:
        t1.undo_action()
    elif choice == 3:
        t1.redo_action()
    elif choice == 4:
        t1.show()
    elif choice==5:
        print("Exting")
        break
    else:
        print("Invalid Choice")