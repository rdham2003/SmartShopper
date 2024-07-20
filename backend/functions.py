import random

def highestRated():
    with(open('datasets/products.csv', 'r')) as products:
        prodList = products.readlines()[1:]
        # print(len(prodList))
        for i in range(len(prodList)):
            prod = prodList[i].split(',')
            prod[-1] = prod[-1][:-1]
            prodList[i] = prod
        prodList = sorted(prodList, key=lambda x: x[2])[::-1][:10]
        newProdList = []
        for prod in prodList:
            newProdList.append(prod[:3])
        return newProdList
    
def hotDeals():
    with(open('datasets/products.csv', 'r')) as products:
        prodList = products.readlines()[1:]
        # print(len(prodList))
        for i in range(len(prodList)):
            prod = prodList[i].split(',')
            prod[-1] = prod[-1][:-1]
            prodList[i] = prod
    newProdList = []
    for i in range(10):
        newProdList.append(prodList[random.randint(0,199)][:3])
    return newProdList
        
        
        
        
if __name__ == '__main__':
    print(highestRated())
    print(hotDeals())