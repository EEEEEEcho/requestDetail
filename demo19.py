# 集成ORM类操纵数据库
from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker                     # 代替conn，执行数据库操作语句
from sqlalchemy.ext.declarative import declarative_base     # 用于创建数据库表基类
engine = create_engine(
    "mysql+pymysql://root:s814466057@127.0.0.1:3306/test",  #连接地址
    max_overflow = 5,   #最大连接数
    pool_size=5,        #连接池大小
    echo=True           #回显
)
Base = declarative_base()
class Host(Base):
    # 表名
    __tablename__ = 'hosts',
    # 字段
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=8080) # default 默认值
# 创建表
Base.metadata.create_all(engine)

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    sess = Session()
    h = Host(hostname='test1',ip_addr='127.0.0.1')
    h2 = Host(hostname='test2', ip_addr='127.0.0.2',port=9001)
    h3 = Host(hostname='test3', ip_addr='127.0.0.3', port=9003)
    sess.add(h)     # 添加一条数据
    sess.add_all([h2,h3])   # 添加多条数据

    # 查询Host表中id大于1的值，并删除
    sess.query(Host).filter(Host.id >1).delete()

    # 查询Host表中id=1的值，并修改
    sess.query(Host).filter(Host.id == 1).update({'port':9000})

    # 查询
    res = sess.query(Host).filter_by(id=1).all()
    for i in res:
        print(i.hostname,i.port)
    sess.commit()           # 提交