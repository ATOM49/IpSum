import os

def SHOP_CATEGORY_CHOICES():
    try:
        fp = open(os.path.dirname(os.path.realpath(__file__)) + os.sep + "modelFieldChoices" + os.sep + "Shop_Category_Choices.txt", 'r')
        choices = [(line.split(" ")[0], line.split(" ")[1]) for line in fp]
        return choices
    except Exception as e:
        print str(e)
        return None

def PRODUCT_CATEGORY_CHOICES():
    try:
        fp = open(os.path.dirname(os.path.realpath(__file__)) + os.sep + "modelFieldChoices" + os.sep + "Product_Category_Choices.txt", 'r')
        choices = [(line.split(" ")[0], line.split(" ")[1]) for line in fp]
        return choices
    except Exception as e:
        print str(e)
        return None

def STATE_CATEGORY_CHOICES():
    try:
        fp = open(os.path.dirname(os.path.realpath(__file__)) + os.sep + "modelFieldChoices" + os.sep + "State_Category_Choices.txt", 'r')
        choices = [(line.split(" ")[0], line.split(" ")[1]) for line in fp]
        return choices
    except Exception as e:
        print str(e)
        return None