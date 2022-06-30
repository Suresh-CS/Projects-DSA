from bs4 import BeautifulSoup
import requests
from csv import writer
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

window = tk.Tk()
window.title('Scrap Data')
window.geometry('420x200')
window.config(bg='black')

window.resizable(False, False)


def scrapping(web):
    page2 = requests.get(web)

    soup2 = BeautifulSoup(page2.text, 'lxml')
    AllLinks = soup2.find_all('a', 'bbc-puhg0e e1ibkbh73')
    countStories = 0

    flag = True
    linkList = []
    with open('file.csv', 'w', newline='', encoding='utf8') as filer:
        thewriter = writer(filer)
        header = ['Title', 'Stories', 'Category']
        thewriter.writerow(header)
        for z in AllLinks:
            counter = 1
            while(flag):
                page = requests.get(
                    'https://www.bbc.com'+z['href']+'?page='+str(counter))
                soup = BeautifulSoup(page.text, 'lxml')

                link_soup = soup.select('.bbc-uk8dsi.emimjbx0')

                for i in link_soup:
                    linkList.append(i['href'])
                for l in linkList:
                    req = requests.get(l)
                    soup1 = BeautifulSoup(req.text, 'lxml')
                    try:
                        blog = soup1.select(
                            '.e1j2237y4.bbc-1n11bte.essoxwk0')[0]
                        title = blog.select(
                            '.bbc-1pfktyq.essoxwk0')[0].text
                        body_soup = blog.select('.bbc-4wucq3.essoxwk0')
                    except Exception:
                        continue
                    All_text = []
                    for p in body_soup:
                        All_text.append(p.text)
                    All_text = ' '.join(All_text)
                    info = [title, All_text, z.text]
                    thewriter.writerow(info)
                    countStories += 1
                    if countStories == 100:
                        flag = False
                        break
                counter += 1
            flag = True
            countStories = 0


def longStory():
    max = 0
    story = ''
    for i in stories.tolist():
        if len(i) > max:
            max = len(i)
            story = i
    print(story)


def shortStory():
    min = len(stories.tolist()[0])
    story = ''
    for i in stories:
        if len(i) < min:
            min = len(i)
            story = i
    print(story)


def uniqueWords():
    words = []
    for i in dataset:
        if i not in words:
            words.append(i)
    print(words)


def top10words():
    dict = {}
    list = {}
    string = ''
    for i in dataset:
        if not i in dict:
            dict[i] = 1
        else:
            dict[i] = (dict.get(i)+1)
    counter = 0
    while counter < 10:
        max = 0
        word = ''
        for i in dict:
            if dict[i] > max:
                max = dict[i]
                word = i
        list[word] = dict[word]
        string += (word+' : '+str(dict[word])+'\n')
        dict[word] = -1
        counter += 1
    print(list)


def storyCounter():
    categories1 = {}
    str1 = ''
    for i in categories:
        if i not in categories1:
            categories1[i] = 1
        else:
            categories1[i] = (categories.get(i)+1)
    for j in categories1:
        str1 += j+" : "+str(categories1.get(j))+'\n'


def Graph():
    categories2 = {}
    for i in categories:
        if i not in categories2:
            categories2[i] = 1
        else:
            categories2[i] = (categories2.get(i) + 1)
    cat = []
    total = []
    for j in categories2:
        cat.append(j[::-1])
        total.append(categories2[j])
    f = plt.figure(figsize=(7, 5))
    positions = [1, 2, 3, 4, 5, 6, 7]
    plt.bar(positions, total, color='green', width=0.3)
    plt.xticks(positions, cat)
    plt.show()


myfile = pandas.read_excel('C:\\Users\\Suresh\\Documents\\Scraped.xlsx')
title = myfile['Title'].values
stories = myfile['Stories'].values
categories = myfile['Category'].values
dataset = []
for i in title:
    dataset.append(i)
for i in categories:
    dataset.append(i)
for i in stories:
    dataset.append(i)

uniqueWords()
shortStory()
longStory()
Graph()
top10words()
storyCounter()
text = tk.StringVar()
label = tk.Label(text='website link: ', font=(
    'Arial 16 bold'), bg='black', fg='white')
label.place(x=5, y=20)
text1 = tk.Entry(textvariable=text, font=('Arial 16 bold'))
text1.place(x=150, y=20)
button = tk.Button(text='scrap', bg='#27AE60', fg='white',
                   command=lambda: [scrapping(text.get())], font=('Arial 16 bold'))
button.place(x=230, y=75)
window.mainloop()
