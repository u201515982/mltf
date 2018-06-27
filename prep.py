from random import shuffle

if __name__ == "__main__":
    ######################
    filename = "test.csv"
    n = 270000
    ######################
    ds = open(filename).readlines()
    del ds[0]
    shuffle(ds)
    pr = open("dstest.csv","w+")
    for i in range(n):
    	pr.write(ds[i])
    pr.close()