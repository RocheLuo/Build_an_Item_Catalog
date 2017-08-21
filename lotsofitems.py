from database_setup import Base,Item,Shop
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

# Create session and connect to DB
engine = create_engine('sqlite:///item.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Shops for db

shop1 = Shop(name="Tmall")
session.add(shop1)
session.commit()

shop2 = Shop(name="Walmart")
session.add(shop2)
session.commit()

shop3 = Shop(name="Amazon")
session.add(shop3)
session.commit()

shop4 = Shop(name="Shopbop")
session.add(shop4)
session.commit()

shop5 = Shop(name="Gilt")
session.add(shop5)
session.commit()


# items for shop1

item1 = Item(title="Uniqlo T-shirt",price=19.9,discount_price=15.9,shop=shop1,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="UNIQLO")

session.add(item1)
session.commit()

item2 = Item(title="COS Dress",price=49.9,discount_price=25.9,shop=shop1,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="COS")

session.add(item2)
session.commit()

item3 = Item(title="Theory Coat",price=49.9,discount_price=25.9,shop=shop1,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Theory")

session.add(item3)
session.commit()

item4 = Item(title="GAP ",price=49.9,discount_price=25.9,shop=shop1,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="GAP")

session.add(item4)
session.commit()

item5 = Item(title="GU shoes",price=9.9,discount_price=5.9,brand="GU",shop=shop1,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg")

session.add(item5)
session.commit()

item6 = Item(title="UGG boots",price=129.9,discount_price=65.9,brand="UGG",shop=shop1,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg")

session.add(item6)
session.commit()

# items for shop2

item2_1 = Item(title="White wine Walmart",price=19.9,discount_price=15.9,shop=shop2,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="UNIQLO")

session.add(item2_1)
session.commit()

item2_2 = Item(title="Coke Cola Light",price=49.9,discount_price=25.9,shop=shop2,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Coke Cola")

session.add(item2_2)
session.commit()

item2_3 = Item(title="Dr. Pepper Strawberry",price=49.9,discount_price=25.9,shop=shop2,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Dr.Pepper")

session.add(item2_3)
session.commit()

item2_4 = Item(title="Olay 7 days Cream",price=49.9,discount_price=25.9,shop=shop2,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Olay")

session.add(item2_4)
session.commit()

item2_5 = Item(title="Head & Shoulders Shampoo ",price=9.9,discount_price=5.9,brand="P&G",shop=shop2,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg")

session.add(item2_5)
session.commit()

item2_6 = Item(title="Lays Potao Chips",price=129.9,discount_price=65.9,brand="Lays",shop=shop2,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg")

session.add(item2_6)
session.commit()


# items for shop3

item3_1 = Item(title="India",price=19.9,discount_price=15.9,shop=shop3,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Lonely Planet")

session.add(item3_1)
session.commit()

item3_2 = Item(title="Mapping Experiences",price=49.9,discount_price=25.9,shop=shop3,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="O'REILLY")

session.add(item3_2)
session.commit()

item3_3 = Item(title="Big Money Thinks Small",price=49.9,discount_price=25.9,shop=shop3,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Joel Tillinghast")

session.add(item3_3)
session.commit()

item3_4 = Item(title="The Best Investment Writing",price=49.9,discount_price=25.9,shop=shop3,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Meb Fabe")

session.add(item3_4)
session.commit()

item3_5 = Item(title="Change by Design",price=9.9,discount_price=5.9,brand="Tim Brown",shop=shop3,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg")

session.add(item3_5)
session.commit()

item3_6 = Item(title="The Service Innovation Handbook",price=129.9,discount_price=65.9,brand="Lucy Kimbell",shop=shop3,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg")

session.add(item3_6)
session.commit()

# items for shop4

item4_1 = Item(title="Star Pumps",price=19.9,discount_price=15.9,shop=shop4,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Jimmy Choo")

session.add(item4_1)
session.commit()

item4_2 = Item(title="Red handbags",price=49.9,discount_price=25.9,shop=shop4,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Kate Spade")

session.add(item4_2)
session.commit()

item4_3 = Item(title="Black high-heeled shoes",price=49.9,discount_price=25.9,shop=shop4,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Sam Edelman")

session.add(item4_3)
session.commit()

item4_4 = Item(title="Work day tote",price=49.9,discount_price=25.9,shop=shop4,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Marc Jobs")

session.add(item4_4)
session.commit()

item4_5 = Item(title="Back Bags for work",price=9.9,discount_price=5.9,brand="Jason Wu",shop=shop4,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg")

session.add(item4_5)
session.commit()

item4_6 = Item(title="Silk slippers",price=129.9,discount_price=65.9,brand="Equipment",shop=shop4,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg")

session.add(item4_6)
session.commit()


# items for shop5

item5_1 = Item(title="Never Full",price=19.9,discount_price=15.9,shop=shop5,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="LV")

session.add(item5_1)
session.commit()

item5_2 = Item(title="Wallet on Chain",price=49.9,discount_price=25.9,shop=shop5,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Kate Spade")

session.add(item5_2)
session.commit()

item5_3 = Item(title="Speedy",price=49.9,discount_price=25.9,shop=shop5,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="LV")

session.add(item5_3)
session.commit()

item5_4 = Item(title="Bayswater",price=49.9,discount_price=25.9,shop=shop5,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg",brand="Mulberry")

session.add(item5_4)
session.commit()

item5_5 = Item(title="Dew",price=9.9,discount_price=5.9,brand="Chloe",shop=shop5,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg")

session.add(item5_5)
session.commit()

item5_6 = Item(title="Belt",price=129.9,discount_price=65.9,brand="Celine",shop=shop5,pic="https://img.alicdn.com/bao/uploaded/i3/TB1jygwQXXXXXclXpXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg")

session.add(item5_6)
session.commit()
