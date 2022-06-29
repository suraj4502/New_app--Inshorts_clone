import io
from tkinter import *
import requests
from urllib.request import Request, urlopen
from PIL import ImageTk,Image
import webbrowser

class App:
    def __init__(self):

        url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=303c61a7a6bf475bbe6db86160ab1408')
        #getting the data from Api
        self.data = requests.get(url).json()
        # GUI
        self.load_gui()
        #laoding news items
        self.load_news_item(0)




    def load_gui(self):
        self.root = Tk()
        self.root.geometry('400x675')
        self.root.resizable(0,0)
        self.root.title('News App')
        self.root.configure(background='#06113C')

    def clear(self):  # to clear the screen
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):
        self.clear()
        try:
            #getting image
            req= Request(self.data['articles'][index]['urlToImage'],headers = {'User-Agent': 'Mozilla/5.0'})
            img_data=urlopen(req).read()
            im=Image.open(io.BytesIO(img_data)).resize((400,250))
            final_photo=ImageTk.PhotoImage(im)
            label = Label(self.root,image = final_photo)
            label.pack()
        except :
            req= Request('https://fisnikde.com/wp-content/uploads/2019/01/broken-image.png',headers = {'User-Agent': 'Mozilla/5.0'})
            img_data = urlopen(req).read()
            im = Image.open(io.BytesIO(img_data)).resize((400, 250))
            final_photo = ImageTk.PhotoImage(im)
            label = Label(self.root, image=final_photo)
            label.pack()


        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='#06113C',
                        fg='white',wraplength=400,justify='left')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',17))

        description = Label(self.root,text=self.data['articles'][index]['description'],bg='#06113C',
                        fg='white',wraplength=400,justify='left')
        description.pack(pady=(10, 20))
        description.config(font=('verdana', 12))

        frame = Frame(self.root,bg='#06113C')
        frame.pack(expand=True,fill=BOTH)

        if index !=0:
            prev = Button(frame,text= 'prev',width=19,height=4,
                          command= lambda :self.load_news_item(index -1))
            prev.pack(side=LEFT)

        more = Button(frame, text='Read More', width=19, height=4,
                      command= lambda :self.open_link(self.data['articles'][index]['url']))
        more.pack(side=LEFT)
        if index != len(self.data['articles']) -1:
            next = Button(frame, text='next', width=19, height=4,
                          command= lambda :self.load_news_item(index +1))
            next.pack(side=LEFT)

        self.root.mainloop()
        
    def open_link(self,url):
        webbrowser.open(url)




newsapp = App()

