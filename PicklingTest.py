import pickle

def store ():
    book=['science','maths','history']
    bank=['icici','hdfc','citi']

    db={}
    db['bk']=book
    db['bnk']=bank

    dbfile=open('pickle.pkl','wb')
    pickle.dump(db,dbfile)
    dbfile.close()

def read():
    dbfile=open('pickle.pkl','rb')
    db=pickle.load(dbfile)
    for i in db:
        print(db[i])

store()
read()