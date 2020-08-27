# 集成ORM类操纵数据库
from sqlalchemy import create_engine, ForeignKey, Table
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker, relationship  # 代替conn，执行数据库操作语句
from sqlalchemy.ext.declarative import declarative_base  # 用于创建数据库表基类
from sqlalchemy import or_,and_

engine = create_engine(
    "mysql+pymysql://root:s814466057@127.0.0.1:3306/test",  # 连接地址
    max_overflow=5,  # 最大连接数
    pool_size=5,  # 连接池大小
    echo=True  # 回显
)
Base = declarative_base()
User2Language = Table('user2_2_language2',Base.metadata,
                      Column('user2_id',ForeignKey('user2.id'),primary_key=True),
                      Column('language2_id',ForeignKey('language2.id'))
                      )
class User2(Base):
    __tablename__ = 'user2'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(125), nullable=True)
    gender = Column(String(10), nullable=True, default="保密")
    town = Column(String(125))
    # secondary使用第三张表
    language = relationship('Language2', backref='user2',cascade='all,delete',secondary=User2Language)


class Language2(Base):
    __tablename__ = 'language2'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(125), nullable=True)
    advantage = Column(String(125), nullable=True)
    disadvantage = Column(String(125), nullable=True)
    user_id = Column(Integer(), ForeignKey('user2.id'))

# Base.metadata.create_all(engine)
if __name__ == '__main__':
    Session = sessionmaker(engine)
    session = Session()
    # 添加用户
    # u1 = User2(name='张三',gender='男',town='北京')
    # u2 = User2(name='李四', gender='女', town='北京')
    # session.add_all([u1,u2])
    # session.commit()
    # # 添加语言
    # ll = Language2(name='python',
    #                advantage='Hello',
    #                disadvantage='World'
    #                )
    # ll.user2.append(u1)
    # session.add(ll)
    # session.commit()

    # 同时添加
    # u3 = User2(name='王五', gender='女', town='天津')
    # u3.language = [
    #     Language2(
    #         name='Java',
    #         advantage='Hello',
    #         disadvantage='World'
    #     ),
    #     Language2(
    #         name='C#',
    #         advantage='Hello',
    #         disadvantage='World'
    #     ),
    # ]
    # session.add(u3)
    # session.commit()

    # 查找数据
    # 查询有多少ID大于0的数据
    count = session.query(User2).filter(User2.id > 0).count()
    print(count)
    # 查询所有的user，以userID降序排列， - 代表降序
    li = session.query(User2).order_by(-User2.id).all()[:2]
    o = session.query(User2).filter(or_(User2.id==1,User2.id==2)).all()
    print(o)
    a = session.query(User2).filter(and_(User2.id==1,User2.id==2)).all()
    print(a)
    l = session.query(User2).filter(User2.name.like('_三')).all()
    print(l)