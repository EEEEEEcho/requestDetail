# SQLAlchemy 是python编程语言下的一款ORM框架，该框架建立在
# 数据库API之上，使用关系对象映射进行数据库操作，简而言之：将对象
# 转换为SQL，然后使用数据API执行SQL并获取执行结果

# SQLALchemy中的数据类型与python的对应信息
# Text -> Long str
# Boolean -> bool
# BigInteger -> int
# Date -> Datetime.data
# DateTime -> Datatime.datetime
# Float -> float
# String -> str
from sqlalchemy import create_engine,MetaData,Table     # 创建引擎
from sqlalchemy import Column,String,Integer,select
engine = create_engine(
    "mysql+pymysql://root:s814466057@127.0.0.1:3306/test",  #连接地址
    max_overflow = 5,   #最大连接数
    pool_size=5,        #连接池大小
    echo=True           #回显
)
metadata = MetaData()
#
user = Table(
    'user',metadata,    # 表名和元数据
    Column('id',Integer,primary_key=True,autoincrement=True),   # ID字段
    Column('name',String(20))                                   # name字段
)
metadata.create_all(engine)         # 创建表

# 原生语句的操作
# 插入数据
engine.execute("insert into user (name) values ('Echo')")
# # 更新数据
engine.execute("update user set id=5 where name='Echo'")
# 查询数据
result = engine.execute("select * from user")
for item in result:
    print(item)
# # 删除数据
engine.execute("delete from user where id = 5")


# 表结构的操作
conn = engine.connect() #获取连接
# 执行插入
conn.execute(user.insert(),{'name':"python"})
# 修改数据
conn.execute(user.update().where(user.c.id==2).values(name='c++'))
# 查询数据，需要导入select函数
res = conn.execute((select([user.c.id,user.c.name])))
print(res.fetchall())
# 删除数据
conn.execute(user.delete().where(user.c.id==2))

conn.close()