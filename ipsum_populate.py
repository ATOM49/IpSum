import os

def populate():
    print('Populating Groups...')
    consumer_group = add_group('consumer')
    shop_admin_group = add_group('shopadmin')

    print('Populating Users...')

    user_am = add_user(first_name='Abhilash',
                       last_name='Mirji',
                       username='Abhilash_Mirji',
                       email='abhilashmirji@live.com',
                       password='123')

    user_rb = add_user(first_name='Rohit',
                       last_name='Biswas',
                       username='Rohit_Biswas',
                       email='rhino2rhonda@gmail.com',
                       password='123')

    consumer_group.user_set.add(user_am)
    consumer_group.user_set.add(user_rb)

    user_fresh = add_user(first_name='Mukesh',
                          last_name='Ambani',
                          username='Mr_Fresh',
                          email='boss@fresh.com',
                          password='123')

    user_malabar = add_user(first_name='Mallu',
                            last_name='Name',
                            username='Mr_Malabar',
                            email='owner@malabar.com',
                            password='123')

    shop_admin_group.user_set.add(user_fresh)
    shop_admin_group.user_set.add(user_malabar)


    print('Populating Shops...')

    shop_fresh_1 = add_shop(shop_name='Reliance Fresh',
                            shop_category='GR',
                            shop_latitude=13.066226,
                            shop_longitude=77.597035,
                            shop_contact_no=+918041608281,
                            plot_num=136,
                            street='Yelahanka',
                            city='Bengaluru',
                            state='KA',
                            zipcode=560064,
                            shop_info_text='Leading Grocery Retail Store',
                            shop_facebookpage='www.facebook.com/page1',
                            shop_email='fresh_ykh@reliance.com',
                            user_likes=84,
                            users_visits=105,
                            shop_admin=user_fresh)

    shop_fresh_2 = add_shop(shop_name='Reliance Fresh',
                            shop_category='GR',
                            shop_latitude=13.031630,
                            shop_longitude=77.635718,
                            shop_contact_no=+918041608281,
                            plot_num=475,
                            street='Hennur Bellary Rd',
                            city='Bengaluru',
                            state='KA',
                            zipcode=560043,
                            shop_info_text='Leading Grocery Retail Store',
                            shop_facebookpage='www.facebook.com/page2',
                            shop_email='fresh_hbr@reliance.com',
                            user_likes=95,
                            users_visits=135,
                            shop_admin=user_fresh)

    rest_malabar = add_shop(shop_name='Malabar Restaurant',
                            shop_category='GS',
                            shop_latitude=12.967833,
                            shop_longitude=77.654431,
                            shop_contact_no=+918041608281,
                            plot_num=40,
                            street='Jeevan Bhima Nagar',
                            city='Bengaluru',
                            state='KA',
                            zipcode=560075,
                            shop_info_text='Keralan Cuisine Restaurant',
                            shop_facebookpage='www.facebook.com/page3',
                            shop_email='help@malabar.com',
                            user_likes=214,
                            users_visits=450,
                            shop_admin=user_malabar)


    prod_1 = add_product(product_name='Real Fruit Juice',
                         product_category='GR',
                         product_type='Food/Drink',
                         manufacturer='PepsiCo',
                         mrp='80')
    prod_2 = add_product(product_name='Apples 1 dozen',
                         product_category='GR',
                         product_type='Fresh Fruits',
                         manufacturer='Kashmiri',
                         mrp='180')
    prod_3 = add_product(product_name='Garam Masala',
                         product_category='GS',
                         product_type='Spices',
                         manufacturer='MDH',
                         mrp='60')
    prod_4 = add_product(product_name='Parota',
                         product_category='GR',
                         product_type='Menu Item',
                         manufacturer='Kerala',
                         mrp='20')

    cat_1 = add_catalog(shop_fresh_1, prod_1, 75)
    cat_2 = add_catalog(shop_fresh_1, prod_2, 175)
    cat_3 = add_catalog(shop_fresh_1, prod_3, 75)
    cat_4 = add_catalog(shop_fresh_1, prod_1, 175)
    cat_5 = add_catalog(shop_fresh_1, prod_2, 55)
    cat_6 = add_catalog(rest_malabar, prod_3, 18)



def add_group(name):
    g = Group.objects.get_or_create(name=name)[0]
    return g


def add_user(first_name, last_name, username, email, password):
    u = User.objects.get_or_create(first_name=first_name, last_name=last_name, username=username, email=email, password=password)[0]
    return u


def add_shop(shop_name, shop_category, shop_latitude, shop_longitude, shop_contact_no, plot_num, street, city, state, zipcode, shop_info_text, shop_facebookpage, shop_email, user_likes, users_visits, shop_admin):
    s = Shop.objects.get_or_create(shop_name=shop_name, shop_category=shop_category, shop_latitude=shop_latitude, shop_longitude=shop_longitude, shop_contact_no=shop_contact_no, plot_num=plot_num, street=street, city=city, state=state, zipcode=zipcode, shop_info_text=shop_info_text, shop_facebookpage=shop_facebookpage, shop_email=shop_email, user_likes=user_likes, users_visits=users_visits, shop_admin=shop_admin)
    return s


def add_shop_offer(offer_Name,offer_Info,points_Needed,offer_Category,offer_Shop,is_eligible,offer_added,offer_From,offer_To):
    s_o = ShopOffer.objects.get_or_create(offer_Name=offer_Name, offer_Info=offer_Info, points_Needed=points_Needed, offer_Category=offer_Category, offer_Shop=offer_Shop, is_eligible=False, offer_added=offer_added, offer_From=offer_From, offer_To=offer_To)
    return s_o

def add_product(product_name, model_number, product_category, product_type, manufacturer, mrp ):
    p = Product.objects.get_or_create(product_name=product_name, model_number=model_number,product_category=product_category,product_type=product_type,manufacturer=manufacturer,mrp=mrp)
    return p


def add_catalog(shop,product,price):
    c = Catalog.objects.get_or_create(shop=shop, product=product, price=price)
    return c


# Start execution here!
if __name__ == '__main__':
    print "Starting IpSum population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IpSum.settings')
    from django.contrib.auth.models import Group, User
    from shops.models import Shop, ShopOffer, Catalog
    from products.models import Product
    populate()