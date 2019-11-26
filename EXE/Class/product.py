'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-22 10:02:13
@LastEditTime: 2019-11-26 17:51:18
@Description:
'''
import os
import json

def writeProductIndex(productIndex):
    with open(
            './Data/Index/ProductIndex.json', 'w',
            encoding='utf-8') as outfile:
        json.dump(productIndex, outfile)

def readProductIndex():
    with open(
            './Data/Index/ProductIndex.json', 'r', encoding='utf-8') as infile:
        return json.load(infile)

def getNewProductNum():
    productIndex = readProductIndex()

    numList = [-1]
    for productNum in productIndex.keys():
        numList.append(int(productNum))
    return max(numList) + 1


class Product():
    def __init__(self,
                 productName='',
                 productNum=getNewProductNum(),
                 productCost=0,
                 productDescription=''):
        self.productName = productName
        self.productNum = productNum
        self.productCost = productCost
        self.productDescription = productDescription


def readProducts():
    #try:
    result = {}
    for root, dirs, files in os.walk('./Data/Product'):
        for f in files:
            if (f.startswith('Product') and f.endswith('.json')):
                with open(
                        './Data/Product/' + str(f), 'r') as infile:
                    product = json.load(infile)
                    result[product.get('productNum')] = Product(
                        productName=product.get('productName'),
                        productNum=product.get('productNum'),
                        productCost=product.get('productCost'),
                        productDescription=product.get(
                            'productDescription'))
    return result
    #except:
    #    return None


def readProduct(productNum):
    try:
        with open('./Data/Product/Product' + str(productNum) + '.json',
                  'r') as infile:
            product = json.load(infile)
            return Product(
                productName=product.get('productName'),
                productNum=product.get('productNum'),
                productCost=product.get('productCost'),
                productDescription=product.get('productDescription'))
    except:
        print(Exception)


def product2Dict(product):
    return ({
        'productName': product.productName,
        'productNum': product.productNum,
        'productCost': product.productCost,
        'productDescription': product.productDescription,
    })


def writeProducts(products):
    for product in products.values():
        with open(
                './Data/Product/Product' + str(products.productNum) + '.json',
                'w') as outfile:
            json.dump(product2Dict(product), outfile)


def writeProduct(product):
    with open('./Data/Product/Product' + str(product.productNum) + '.json',
              'w') as outfile:
        json.dump(product2Dict(product), outfile)


def main():
    ps = readProducts()


if __name__ == '__main__':
    main()
