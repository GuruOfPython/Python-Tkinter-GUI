# from binary_tree import *
#
# root = Node(8)
#
# root.insert(3)
# root.insert(10)
# root.insert(1)
# root.insert(6)
# root.insert(4)
# root.insert(7)
# root.insert(14)
# root.insert(13)
# node, parent = root.lookup(6)
# print(node, parent)
# root.print_tree()
#
# root.delete(10)
#
# root.print_tree()


import tkinter as tk
from tkinter import *
# import tkMessageBox as messagesbox
import tkinter.messagebox as messagebox
import ttk
from tkinter import simpledialog

from treeview import TreeView
from random import shuffle
from naive import NaiveBST, perfect_inserter
from random import *
import random

class main_GUI(Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.resizable(0, 0)

        self.geometry("1200x800")

        self.setting_frame = LabelFrame(self, text="Setting")

        create_btn = Button(self.setting_frame, text="Create", height=1, width=10, command=self.create)
        create_btn.grid(row=0, padx=5, pady=5)
        insert_btn = Button(self.setting_frame, text="Insert", height=1, width=10, command=self.insert)
        insert_btn.grid(row=2, padx=5, pady=5)
        # self.insert_e = Entry(self.setting_frame, height=1, width=10)
        self.insert_e = Entry(self.setting_frame)
        self.insert_e.grid(row=2, column=1, padx=5, pady=5)

        delete_btn = Button(self.setting_frame, text="Delete", height=1, width=10, command=self.delete)
        delete_btn.grid(row=4, padx=5, pady=5)
        # self.delete_e = Entry(self.setting_frame, height=1, width=10)
        self.delete_e = Entry(self.setting_frame)
        self.delete_e.grid(row=4, column=1, padx=5, pady=5)

        search_btn = Button(self.setting_frame, text="Search", height=1, width=10, command=self.search)
        search_btn.grid(row=6, padx=5, pady=5)
        # self.search_e = Entry(self.setting_frame, height=1, width=10)
        self.search_e = Entry(self.setting_frame)
        self.search_e.grid(row=6, column=1, padx=5, pady=5)

        # self.setting_frame.grid(row=1, padx=5, pady=5, sticky=N+S)
        self.setting_frame.pack(padx=5, pady=5, side=LEFT)
        self.drawing_frame = tk.LabelFrame(self, text="Drawing")
        # self.drawing_frame.grid(row=1, column=2, padx=5, pady=5, sticky=N+S)
        self.drawing_frame.pack(padx=5, pady=5, fill=BOTH, expand=1)

        self.tree = NaiveBST()
        self.treeview = TreeView(self.drawing_frame, tree=self.tree)

        def callback():
            if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
                self.destroy()
                self.treeview.end_pause = True
        self.protocol("WM_DELETE_WINDOW", callback)

    def create(self):

        # keys = list(range(20))

        # shuffle(keys)
        # print(keys)

        # keys = [randint(1,30) for i in range(20)]
        keys = random.sample(range(1, 30), 20)
        self.tree.root = None
        print(keys)
        for i in keys:
            self.tree.insert(i)
        # perfect_inserter(self.tree, sorted(keys))
        self.tree.view()

    def insert(self):
        if self.tree.root is None:
            messagebox.showerror("No Tree", "There is no tree. Please create a tree")
            return

        if not self.insert_e.get():
            messagebox.showerror("No Value", "Please enter a node key")
            return
        elif not self.insert_e.get().isdigit():
            messagebox.showerror("Invalid Value", "Please enter an integer value")
            return

        node_key = int(self.insert_e.get())
        [flag, p] = self.tree.search(node_key)
        if not flag:
            self.tree.insert(node_key)
            self.tree.view()
        else:
            messagebox.showerror("Invalid Value", "The key already exists. Please enter another value")
            return

    def delete(self):
        if self.tree.root is None:
            messagebox.showerror("No Tree", "There is no tree. Please create a tree")
            return

        if not self.delete_e.get():
            messagebox.showerror("No Value", "Please enter a node key")
            return
        elif not self.delete_e.get().isdigit():
            messagebox.showerror("Invalid Value", "Please enter an integer value")
            return

        node_key = int(self.delete_e.get())
        [flag, p] = self.tree.search(node_key)
        if flag:
            self.tree.delete(node_key)
            self.tree.view()
        else:
            messagebox.showerror("Invalid Value", "The key doesn't exists. Please enter another value")
            return

    def search(self):
        if self.tree.root is None:
            messagebox.showerror("No Tree", "There is no tree. Please create a tree")
            return

        if not self.search_e.get():
            messagebox.showerror("No Value", "Please enter a node key")
            return
        elif not self.search_e.get().isdigit():
            messagebox.showerror("Invalid Value", "Please enter an integer value")
            return



        node_key = int(self.search_e.get())
        [flag, p] = self.tree.search(node_key)
        if flag and p:
            self.tree.view(highlight_nodes=[p])
        else:
            messagebox.showerror("Invalid Value", "The key can't be found")


if __name__ == '__main__':
    app = main_GUI(None)
    app.title("Binary Search Tree")
    app.mainloop()
