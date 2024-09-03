import sys
import csv

def add(i):
    with open('data.csv','a+',newline='')as file:
        writer = csv.writer(file)
        writer .writerow(i)



def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    print(data)
    return data
    
#view()    

def remove(i):

    def save(j):
        with open('data.csv','w',newline='')as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone = i

    with open('data.csv','r')as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)


            for elemet in row:
                if elemet == telephone:
                    new_list.remove(row)
        save(new_list)  

#remove('1234')                  
#view()


def update(i):


    def update_newlist(j):
        with open('data.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)


    new_list = []
    telephone = i[0]
    #['123','apurv','123','apk@gnail.com']


    with open('data.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    name = i[1]
                    telephone=i[2]
                    email=i[3]


                    data = [name,telephone,email]
                    index = new_list.index(row)
                    new_list[index] = data
    update_newlist(new_list) 

#sample['123','boy','apk@gmail.com']
#update(sample)

def search(i):
    data = []
    telephone = i

    with open('data.csv','r')as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == telephone:
                    data.append(row)
    print(data)                
    return data
search('123')                



