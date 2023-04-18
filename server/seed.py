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

    i21=Item(condition=9, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231260M145012_1/paul-smith-gunmetal-dog-tag-necklace.jpg ", color="silver", name="Dog Tag Necklace", price = 150.00, for_sale=True, owner_id=2, type_id=5, subtype_id=12, size_id=1, brand_id=9)
    i22=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231260M145010_1/paul-smith-silver-rope-chain-necklace.jpg ", color="Silver", name="Rope Chain Necklace", price = 325.00, for_sale=True, owner_id=2, type_id=5, subtype_id=12, size_id=1, brand_id=9)
    i23=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231260M145000_1/paul-smith-gunmetal-zip-necklace.jpg ", color="Silver", name="Gun Metal Zip Necklace", price = 125.00, for_sale=True, owner_id=2, type_id=5, subtype_id=12, size_id=1, brand_id=9)
    i24=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231260M145002_1/paul-smith-gunmetal-gold-star-necklace.jpg ", color="Silver", name="Gun Metal Gold Star Necklace", price = 350.00, for_sale=True, owner_id=2, type_id=5, subtype_id=12, size_id=1, brand_id=9)
    i25=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231260M145003_1/paul-smith-black-logo-pendant-necklace.jpg ", color="Black", name="Black Logo Pendant Necklace", price = 125.00, for_sale=True, owner_id=2, type_id=5, subtype_id=12, size_id=1, brand_id=9)
    i26=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222451M134056_1/gucci-blue-oval-sunglasses.jpg ", color="Blue", name="Blue Oval Sunglasses", price = 565.00, for_sale=True, owner_id=2, type_id=5, subtype_id=13, size_id=1, brand_id=3)
    i27=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222451M134051_1/gucci-black-mask-sunglasses.jpg ", color="Black", name="Black Mask Sunglasses", price = 1175.00, for_sale=True, owner_id=2, type_id=5, subtype_id=13, size_id=1, brand_id=3)
    i28=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222451M134048_1/gucci-silver-shield-sunglasses.jpg ", color="Pink", name="Silver Shield Sunglasses", price = 1175.00, for_sale=True, owner_id=3, type_id=5, subtype_id=13, size_id=1, brand_id=3)
    i29=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231451M134072_1/gucci-gold-rectangular-sunglasses.jpg ", color="Black", name="Gold Rectangular Sunglasses", price = 565.00, for_sale=True, owner_id=1, type_id=5, subtype_id=13, size_id=1, brand_id=3)
    i30=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231451M134059_1/gucci-black-round-sunglasses.jpg ", color="Black", name="Black Round Sunglasses", price = 565.00, for_sale=True, owner_id=3, type_id=5, subtype_id=13, size_id=1, brand_id=3)
    i31=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222451M134059_1/gucci-silver-geometric-sunglasses.jpg", color="Black", name="Silver Geometric Sunglasses", price = 1175.00, for_sale=True, owner_id=1, type_id=5, subtype_id=13, size_id=1, brand_id=3)
    i32=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231129F049000_1/acne-studios-black-embossed-tote.jpg", color="Black", name="Black Embossed Tote", price = 650.00, for_sale=True, owner_id=2, type_id=5, subtype_id=14, size_id=1, brand_id=11)
    i32=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231129F046006_1/acne-studios-off-white-and-gray-distortion-bag.jpg", color="Grey", name="Off-White Distortion Bag", price = 1700.00, for_sale=True, owner_id=3, type_id=5, subtype_id=14, size_id=1, brand_id=11)
    i33=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231129F049002_1/acne-studios-white-and-green-printed-tote.jpg", color="Green", name="White and Green Printed Tote", price = 750.00, for_sale=True, owner_id=1, type_id=5, subtype_id=14, size_id=1, brand_id=11)
    i34=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/232451F048024_1/gucci-orange-gg-matelasse-shoulder-bag.jpg", color="Orange", name="Orange GG Matelasse Shoulder bag", price = 1980.00, for_sale=True, owner_id=3, type_id=5, subtype_id=14, size_id=1, brand_id=3)
    i35=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231404F048010_1/versace-pink-mini-virtus-bag.jpg", color="Pink", name="Pink Mini Virtus Bag", price = 1175.00, for_sale=True, owner_id=1, type_id=5, subtype_id=14, size_id=1, brand_id=14)
    i36=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222404F046028_1/versace-black-la-medusa-bag.jpg", color="Black", name="Black La Medusa Bag", price = 2325.00, for_sale=True, owner_id=2, type_id=5, subtype_id=14, size_id=1, brand_id=14)
    i37=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222404F048037_1/versace-black-la-medusa-round-crossbody-bag.jpg", color="Black", name="Black La Medusa Round Crossbody Bag", price = 2325.00, for_sale=True, owner_id=2, type_id=5, subtype_id=14, size_id=1, brand_id=14)
    i38=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222404F048057_1/versace-red-greca-goddess-bag.jpg", color="Red", name="Red Greca Goddess Bag", price = 2895.00, for_sale=True, owner_id=1, type_id=5, subtype_id=14, size_id=1, brand_id=14)
    i39=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222404F044000_1/versace-black-greca-goddess-clutch.jpg", color="Red", name="Black Greca Goddess Clutch", price = 2895.00, for_sale=True, owner_id=2, type_id=5, subtype_id=14, size_id=1, brand_id=14)
    i40=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222129F042003_1/acne-studios-orange-furry-fleece-backpack.jpg", color="Orange", name="Orange Furry Fleece Backoack", price = 470.00, for_sale=True, owner_id=1, type_id=5, subtype_id=14, size_id=1, brand_id=11)

    
    items=[i1,i2, i21, i22, i23, i24, i25, i26, i27, i28, i29, i30, i31, i32, i33, i34, i35, i36, i37, i38, i39, i40 ]
    i1=Item(condition=8, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231368M180014_1/acronym-khaki-and-black-j1wts-gt-jacket.jpg", color="Black", name="J1WTS-GT", price = 1100.99, for_sale=True, owner_id=1, type_id=1, subtype_id=1, size_id=3, brand_id=2)
    i2=Item(condition=3, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231368M180001_1/acronym-black-j111ts-ch-jacket.jpg", color="Black", name="J11TS-CH", price = 999.99, for_sale=True, owner_id=2, type_id=1, subtype_id=1, size_id=4, brand_id=2)
    i3=Item(condition=7, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231038M202007_1/doublet-gray-braids-hair-hoodie.jpg", color="Brown", name="Hair Hoodie", price = 650.55, for_sale=True, owner_id=2, type_id=2, subtype_id=2, size_id=1, brand_id=7)
    i4=Item(condition=8, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231038M213012_1/doublet-white-bread-t-shirt.jpg", color="White", name="Bread Tee", price = 98.99, for_sale=True, owner_id=3, type_id=2, subtype_id=3, size_id=3, brand_id=7)
    i5=Item(condition=6, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231038M186003_1/doublet-white-destroyed-jeans.jpg", color="White", name="Destroyed Jeans", price = 459.99, for_sale=True, owner_id=3, type_id=3, subtype_id=2, size_id=2, brand_id=7)
    i6=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231038M191005_1/doublet-khaki-mirage-trousers.jpg", color="Green", name="Mirage Trousers", price = 400.50, for_sale=True, owner_id=1, type_id=3, subtype_id=1, size_id=4, brand_id=7)
    i7=Item(condition=6, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222038M213010_1/doublet-pink-forever-my-friend-t-shirt.jpg", color="Pink", name="Pink Tee", price = 112.50, for_sale=True, owner_id=1, type_id=2, subtype_id=3, size_id=2, brand_id=7)
    i8=Item(condition=6, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222038M192002_1/doublet-blue-hand-embroidery-shirt.jpg", color="Blue", name="Hand Shirt", price = 667.50, for_sale=True, owner_id=2, type_id=2, subtype_id=5, size_id=3, brand_id=7)
    i9=Item(condition=6, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222038M192002_1/doublet-blue-hand-embroidery-shirt.jpg", color="Blue", name="Hand Shirt", price = 667.50, for_sale=True, owner_id=2, type_id=2, subtype_id=5, size_id=3, brand_id=7)
    i10=Item(condition=8, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231985M201004_1/kiko-kostadinov-beige-murad-sweater.jpg", color="Grey", name="Murad Sweater", price = 380.00, for_sale=False, owner_id=3, type_id=2, subtype_id=1, size_id=1, brand_id=5)
    i11=Item(condition=8, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231985M213002_1/kiko-kostadinov-navy-zlatyu-long-sleeve-t-shirt.jpg", color="Black", name="Zlatyu Sweater", price = 175.00, for_sale=True, owner_id=3, type_id=2, subtype_id=1, size_id=3, brand_id=5)
    i12=Item(condition=4, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231985M180000_1/kiko-kostadinov-blue-zlatyu-coat.jpg", color="Blue", name="Zlatyu Coat", price = 822.00, for_sale=True, owner_id=1, type_id=1, subtype_id=2, size_id=4, brand_id=5)
    i13=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231985M191011_1/kiko-kostadinov-black-tonkin-contrast-trousers.jpg", color="Black", name="Tonkin Trousers", price = 700.69, for_sale=True, owner_id=2, type_id=3, subtype_id=1, size_id=2, brand_id=5)
    i14=Item(condition=6, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231451M189001_1/gucci-black-shiny-leather-pants.jpg", color="Black", name="Shiny Leather Pants", price = 1200.11, for_sale=True, owner_id=2, type_id=3, subtype_id=4, size_id=3, brand_id=3)
    i15=Item(condition=9, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231232M189007_1/rick-owens-black-bela-leather-pants.jpg", color="Black", name="Bela Leather Pants", price = 1000.00, for_sale=True, owner_id=3, type_id=3, subtype_id=4, size_id=1, brand_id=6)
    i16=Item(condition=9, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231232M193023_1/rick-owens-black-cargo-pods-shorts.jpg", color="Black", name="Pod Shorts", price = 430.00, for_sale=True, owner_id=3, type_id=3, subtype_id=6, size_id=2, brand_id=6)
    i17=Item(condition=8, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231232M192031_1/rick-owens-black-larry-fogpocket-shirt.jpg", color="Black", name="Larry Shirt", price = 499.99, for_sale=False, owner_id=2, type_id=2, subtype_id=5, size_id=3, brand_id=6)
    i18=Item(condition=6, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231347M206000_1/comme-des-garcons-homme-plus-multicolor-jacquard-vest.jpg", color="Multicolor", name="Jacquard Vest", price = 315.99, for_sale=True, owner_id=3, type_id=2, subtype_id=1, size_id=5, brand_id=1)
    i19=Item(condition=9, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231347M191005_1/comme-des-garcons-homme-plus-black-stirrup-trousers.jpg", color="Black", name="Stirrup Trousers", price = 289.99, for_sale=True, owner_id=1, type_id=3, subtype_id=1, size_id=2, brand_id=1)
    i20=Item(condition=2, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/212347M213075_1/comme-des-garcons-homme-plus-faux-leather-croc-cut-out-shorts.jpg", color="Black", name="Cutout Shorts", price = 533.99, for_sale=True, owner_id=1, type_id=3, subtype_id=6, size_id=3, brand_id=1)
    i61=Item(condition=8, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231735M191002_1/craig-green-brown-packable-trousers.jpg", color="Brown", name="Packable Trousers", price = 69.99, for_sale=True, owner_id=2, type_id=3, subtype_id=1, size_id=2, brand_id=13)
    i62=Item(condition=7, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231735M201004_1/craig-green-ssense-exclusive-white-fluffy-vest.jpg", color="White", name="White Fluffy Vest", price = 269.99, for_sale=True, owner_id=1, type_id=2, subtype_id=1, size_id=3, brand_id=13)
    i63=Item(condition=6, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222735M191006_1/craig-green-ssense-exclusive-off-white-fluffy-reversible-trousers.jpg", color="White", name="White Trousers", price = 529.99, for_sale=True, owner_id=1, type_id=3, subtype_id=1, size_id=4, brand_id=13)
    i64=Item(condition=10, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231404M175004_1/versace-blue-and-orange-varsity-reversible-bomber-jacket.jpg", color="Blue", name="Varsity Jacket", price = 745.99, for_sale=True, owner_id=2, type_id=1, subtype_id=1, size_id=5, brand_id=14)
    i65=Item(condition=6, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/231368M191012_1/acronym-black-pleated-trousers.jpg", color="Black", name="Pleated Trousers", price = 800.99, for_sale=True, owner_id=3, type_id=3, subtype_id=1, size_id=3, brand_id=2)
    i66=Item(condition=7, image = "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/222368M202013_1/acronym-khaki-s31-px-hoodie.jpg", color="Green", name="S31-Px Hoodie", price = 500.99, for_sale=True, owner_id=3, type_id=2, subtype_id=2, size_id=3, brand_id=2)



 


    items=[i1,i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i19, i20, i61, i62, i63, i64, i65, i66]

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

    trousers = SubType(subtype = "Trousers", type_id = 3)
    jeans = SubType(subtype = "Jeans", type_id = 3)
    cargo = SubType(subtype = "Cargos", type_id = 3)
    leather = SubType(subtype = "Leather", type_id = 3)
    sweatpants = SubType(subtype = "Sweatpants", type_id = 3)
    shorts = SubType(subtype = "Shorts", type_id = 3)
    swimwear = SubType(subtype = "Swimwear", type_id = 3)


    subtypes = [jackets, coats, trenchcoats, tailoring, fur, down, knits, sweatshirts, tshirts, tanks, buttonups, trousers, jeans, cargo, leather, sweatpants, shorts, swimwear]

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
    rickowens = Brand(brand="Rick Owens")
    doublet = Brand(brand = "Doublet")
    kapital = Brand(brand = "Kapital")
    paulsmith = Brand(brand = "Paul Smith")
    prada = Brand(brand = "Prada")
    acne=Brand(brand = "Acne Studios")
    dries = Brand(brand = "Dries Van Noten")
    craiggreen = Brand(brand="Craig Green")
    versace=Brand(brand="Versace")

    brands = [cdg, acronym, gucci, hermes, kikokostadinov, rickowens, doublet, kapital, paulsmith, prada, acne, dries,craiggreen, versace]

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
   

    

    