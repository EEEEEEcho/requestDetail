# 集成ORM类操纵数据库
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker, relationship  # 代替conn，执行数据库操作语句
from sqlalchemy.ext.declarative import declarative_base  # 用于创建数据库表基类

engine = create_engine(
    "mysql+pymysql://root:s814466057@127.0.0.1:3306/test",  # 连接地址
    max_overflow=5,  # 最大连接数
    pool_size=5,  # 连接池大小
    echo=True  # 回显
)
Base = declarative_base()


# 多对多建表

class User2(Base):
    __tablename__ = 'user2'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(125), nullable=True)
    gender = Column(String(10), nullable=True, default="保密")
    town = Column(String(125))
    language = relationship('Language2', back_populates='user2')


class Language2(Base):
    __tablename__ = 'language2'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(125), nullable=True)
    advantage = Column(String(125), nullable=True)
    disadvantage = Column(String(125), nullable=True)
    user = relationship('User2', back_populates='language2')

# relationship函数是sqlalchemy对关系之间提供的一种便利的调用方式
# backref参数则对关系提供反向引用的声明
# 最新版本的sqlalchemy中对relationship引进了back_populate参数，和
# backref一样，不过需要两边定义，一般不常用，一般常用第三张表来保存关系