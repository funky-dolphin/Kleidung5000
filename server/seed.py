from random import choice as rc
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from models import db, User, Item, Type, SubType, Size, Brand, Transaction, Message

with app.app_context():

# This will delete any existing rows
# so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    User.query.delete()
    Item.query.delete()
    Type.query.delete()
    SubType.query.delete()
    Size.query.delete()
    Brand.query.delete()
    Transaction.query.delete()
    Message.query.delete()

    print("Creating users...")
    nick=User(name="Nick", username="BDNick69", _password_hash = "123", email_address ="nick@kleidung5000.com", paypal_address = "nick@kleidung5000.com", zipcode = 10003)
    finn=User(name="Finn", username="finnychinny", _password_hash = "abc", email_address ="finn@kleidung5000.com", paypal_address = "finn@kleidung5000.com", zipcode = 10004)
    brett=User(name="Brett", username="frkshw", _password_hash = "123password", email_address ="brett@kleidung5000.com", paypal_address = "brett@kleidung5000.com", zipcode = 11237)
    users = [nick, finn, brett]

    print("Creating items...")
    i1=Item(condition=8, image = " ", color="black", name="myshirtttt", price = 100.99, for_sale=True, owner_id=1, type_id=1, subtype_id=1, size_id=3, brand_id=2)
    i2=Item(condition=3, image = " ", color="grey", name="thong", price = 444.99, for_sale=True, owner_id=2, type_id=1, subtype_id=2, size_id=4, brand_id=3)
    items=[i1,i2]

    i41=Item(condition=10, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231358M195019_1/dries-van-noten-khaki-paneled-blazer.jpg", color="Khaki", name="Paneled Blazer", price=1425.00, for_sale=True, owner_id=2, type_id=1, subtype_id=4, brand_id=12)
    i42=Item(condition=7, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231232M175011_1/rick-owens-black-fog-leather-bomber-jacket.jpg", color="Black", name="Fog Leather Bomber Jacket", price=2815.00, for_sale=True, owner_id=1, type_id=1, subtype_id=1, brand_id=6)
    i43=Item(condition=5, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231735M180001_1/craig-green-black-tab-jacket.jpg", color="Black", name="Tab Jacket", price=1665.00, for_sale=False, owner_id=3, type_id=1, subtype_id=1, brand_id=13 )
    i44=Item(condition=8, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222129M181003_1/acne-studios-brown-patchwork-leather-jacket.jpg", color="Brown", name="Patchwork Leather Jacket", price=2885.00, for_sale=True, owner_id=3, type_id=1, subtype_id=1, brand_id=11)
    i45=Item(condition=9, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231358M180018_1/dries-van-noten-black-spread-collar-jacket.jpg", color="Black", name="Spread Collar Jacket", price=965.00, for_sale=True, owner_id=1, type_id=1, subtype_id=4, brand_id=12)
    i46=Item(condition=6, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231057M191006_1/comme-des-garcons-homme-khaki-pleated-trousers.jpg", color="Khaki", name="Pleated Trousers", price=510.00, for_sale=True, owner_id=2, type_id=3, subtype_id=1, brand_id=1)
    i47=Item(condition=7, image="https://www.prada.com/content/dam/pradabkg_products/U/UPS/UPS600/12NFF0002/UPS600_12NF_F0002_S_231_MDF.jpg/_jcr_content/renditions/cq5dam.web.hebebed.1000.1000.jpg", color="black", name="Leather Coat", price=10100.00, for_sale=False, owner_id=3, type_id=1, subtype_id=3, brand_id=10)
    i48=Item(condition=10, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231985M191006_1/kiko-kostadinov-beige-danh-trousers.jpg", color="Beige", name="Danh Trousers", price=935.00, for_sale=True, owner_id=1, type_id=3, subtype_id=1, brand_id=5)
    i49=Item(condition=1, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231735M195001_1/craig-green-brown-packable-blazer.jpg", color="Brown", name="Packable Blazer", price=1435.00, for_sale=True, owner_id=2, type_id=1, subtype_id=4, brand_id=13)
    i50=Item(condition=7, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222347M192011_1/comme-des-garcons-homme-plus-brown-colorblock-shirt.jpg", color="Brown", name="Colorblock Shirt", price=310.00, for_sale=True, owner_id=3, type_id=2, subtype_id=5, brand_id=1)
    i51=Item(condition=9, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231260M181003_1/paul-smith-green-flap-pocket-leather-jacket.jpg", color="Green", name="Flap Pocket Jacket", price=2175.00, for_sale=True, owner_id=1, type_id=1, subtype_id=1, brand_id=9)
    i52=Item(condition=7, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231358M214000_1/dries-van-noten-multicolor-paneled-tank-top.jpg", color="Multicolor", name="Paneled Tank Top", price=295.00, for_sale=True, owner_id=3, type_id=2, subtype_id=4, brand_id=12)
    i53=Item(condition=10, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222451M180003_1/gucci-tan-nylon-jacket.jpg", color="Tan", name="Nylon Jacket", price=1950.00, for_sale=False, owner_id=2, type_id=1, subtype_id=1, brand_id=3)
    i54=Item(condition=4, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231451M180009_1/gucci-navy-quilted-gg-jacket.jpg", color="Navy", name="Quilted GG Jacket", price=2600.00, for_sale=True, owner_id=3, type_id=1, subtype_id=1, brand_id=3)
    i55=Item(condition=1, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231232M214034_1/rick-owens-khaki-rib-tank-top.jpg", color="Khaki", name="Rib Tank Top", price=435.00, for_sale=True, owner_id=3, type_id=2, subtype_id=4, brand_id=6 )
    i56=Item(condition=10, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231232M181010_1/rick-owens-pink-fogpocket-leather-jacket.jpg", color="Pink", name="FogPocket Leather Jacket", price=3470.00, for_sale=True, owner_id=2, type_id=1, subtype_id=1, brand_id=6)
    i57=Item(condition=5, image="https://www.mrporter.com/variants/images/1647597309323357/in/w1200_q60.jpg", color="Purple", name="Sweater Vest", price=375.00, for_sale=True, owner_id=3, type_id=2, subtype_id=1, brand_id=8)
    i58=Item(condition=9, image="https://www.mrporter.com/variants/images/1647597283516462/ou/w2000_q60.jpg", color="Gray", name="Intarsia Wool Sweater", price=680.00, for_sale=True, owner_id=2, type_id=2, subtype_id=2, brand_id=8)
    i59=Item(condition=10, image="https://www.mrporter.com/variants/images/1647597283516508/in/w1200_q60.jpg", color="Turqoise", name="Velvet Satin Bomber", price=1510.00, for_sale=True, owner_id=3, type_id=1, subtype_id=1, brand_id=8)
    i60=Item(condition=9, image="https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222232M179030_1/rick-owens-black-cropped-shearling-jacket.jpg", color="Black", name="Cropped Shearling Jacket", price=4755.00, for_sale=True, owner_id=2, type_id=1, subtype_id=5, brand_id=6)



    print("Creating types...")
    outerwear = Type(type = "Outerwear")
    tops = Type(type = "Tops")
    bottoms = Type(type = "Bottoms")
    footwear = Type(type = "Footwear")
    accessories = Type(type="Accessories")
    types = [outerwear, tops, bottoms, footwear, accessories]

    print("Creating subtypes...")
    jackets = SubType(subtype = "Jackets", type_id=1)
    coats = SubType(subtype = "Coats", type_id = 1)
    trenchcoats = SubType(subtype = "Trench Coats", type_id = 1)
    tailoring = SubType(subtype = "Tailoring", type_id=1)
    fur =  SubType(subtype = "Fur", type_id=1)
    down = SubType(subtype = "Down", type_id=1)

    knits = SubType(subtype = "Knits", type_id = 2)
    sweatshirts = SubType(subtype = "Sweatshirts", type_id = 2)
    tshirts = SubType(subtype = "T-Shirts", type_id = 2)
    tanks = SubType(subtype = "Tanks", type_id = 2)
    buttonups = SubType(subtype = "Button Ups", type_id = 2)

    subtypes = [jackets, coats, trenchcoats, tailoring, fur, down, knits, sweatshirts, tshirts, tanks, buttonups]

    print("Creating sizes...")
    xs = Size(size = "XS")
    s = Size(size = "S")
    m = Size(size = "M")
    l = Size(size = "L")
    xl = Size(size = "XL")
    xxl = Size(size = "XXL")
    sizes = [xs, s, m, l, xl, xxl]

    print("Creating brands...")
    cdg = Brand(brand = "Comme des Garcons")
    acronym = Brand(brand = "Acronym")
    gucci = Brand(brand = "Gucci")
    hermes = Brand(brand = "Hermes")
    kikokostadinov = Brand(brand = "Kiko Kostadinov")
    prada = Brand(brand = "Prada")
    brands = [cdg, acronym, gucci, hermes, kikokostadinov, prada]

    print("Creating transactions...")
    t1=Transaction(buyer_id = 1, seller_id=2, price=200, item_id=2)
    t2=Transaction(buyer_id = 2, seller_id=1, price =100, item_id = 1)
    t3=Transaction(buyer_id = 2, seller_id=3, price=400, item_id=4)
    transactions = [t1, t2, t3]

    print("Creating messages...")
    m1=Message(user_1=1, user_2=2, message="yo")
    m2=Message(user_1=2, user_2=1, message="wassup")
    m3=Message(user_1=1, user_2=3, message="brett is a dick")
    messages=[m1,m2,m3]

    db.session.add_all(users)
    db.session.add_all(items)
    db.session.add_all(types)
    db.session.add_all(subtypes)
    db.session.add_all(sizes)
    db.session.add_all(brands)
    db.session.add_all(transactions)
    db.session.add_all(messages)
    db.session.commit()

    print("Seeding done!")
    print(i1)
   


 

    