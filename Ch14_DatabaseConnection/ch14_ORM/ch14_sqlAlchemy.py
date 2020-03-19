from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 建立與product表格對應的Product物件
Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'
    pid = Column(Integer, primary_key=True)
    name = Column(String(60))
    price = Column(Integer)


# 建立與資料庫的連線(session)
engine = create_engine('mysql://dbuser:aabb1234@localhost/my_demo_db', echo=False)

# sessionmaker建立一個DBsession類別
DBSession = sessionmaker(bind=engine)

# 將DBSession類別實體化為session物件
session = DBSession()

print('列出全部產品:')
for p in session.query(Product):
    print(p.pid, p.name, p.price)

print('列出價格大於6000的產品')
# filter -> where
for p in session.query(Product).filter(Product.price > 6000):
    print(p.pid, p.name, p.price)

session.close()