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


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(125), nullable=True)
    gender = Column(String(10), nullable=True, default="保密")
    town = Column(String(125))
    # 用于构建一对多的关系，一个用户会多种语言
    # 关联的是Language类的名字，注意不能写成表的名字
    # backref指通过什么名字来关联另一张表
    language = relationship('Language', backref='user')


class Language(Base):
    __tablename__ = 'language'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(125), nullable=True)
    advantage = Column(String(125), nullable=True)
    disadvantage = Column(String(125), nullable=True)
    # 构造外键
    user_id = Column(Integer(), ForeignKey('user.id'))

# Base.metadata.create_all(engine)
if __name__ == '__main__':
    Session = sessionmaker(engine)
    session = Session()

    # # 添加
    # u1 = User(name='张三',gender='男',town='北京')
    # u2 = User(name='李四',gender='女',town='河南')
    # session.add_all([u1,u2])
    # session.commit()
    #
    # l1 = Language(name='python',advantage='开发快',disadvantage='运行慢')
    # # 建立关联,这里.user就是在backref中的user
    # l1.user = u1
    # session.add(l1)
    # session.commit()

    # u3 = User(name='王五',gender='女',town='天津')
    # # 创建一对多关系
    # u3.language = [
    #     Language(
    #         name='python3',
    #         advantage='开发快',
    #         disadvantage='运行慢'
    #     ),
    #     Language(
    #         name='C',
    #         advantage='运行极快',
    #         disadvantage='不好学'
    #     )
    # ]
    # session.add(u3)
    # session.commit()

    # 查询id为6的用户
    u = session.query(User).filter_by(id=6).first()
    print("用户:" + u.name + u.gender)
    # 查询id为6的用户所关联的语言
    lang = session.query(Language).filter_by(user_id=u.id)
    for i in lang:
        print("language:" + i.name)

    # 删除用户
    # u4 = User(name='马六',gender='男',town='云南')
    # u4.language = [
    #     Language(
    #         name='python3.8',
    #         advantage='开发快',
    #         disadvantage='运行慢'
    #     ),
    #     Language(
    #         name='C#',
    #         advantage='运行极快',
    #         disadvantage='不好学'
    #     )
    # ]
    # session.add(u4)
    # session.commit()
    #u = session.query(User).filter(User.id == 8).first()
    # 这里删除的只是用户，与之关联的语言并不会删除，关联数据空下的字段会变成null
    # 在这里就是语言字段的ID会变成null，浪费空间
    # 如果想要实现 级联删除数据。需要在user表中的relationship字段加上cascade
    # language = relationship('Language', backref='user',cascade='all,delete')
    # session.delete(u)
    # session.commit()

    # 更新
    u = session.query(User).filter(User.id == 4).first()
    u.name = '张便便'
    session.commit()