# UUID学习
import uuid
from uuid import UUID
# 基于时间戳
print(uuid.uuid1())
# 基于名字的MD5散列
print(uuid.uuid3(UUID(int=1),"MS"))
# 基于随机数
print(uuid.uuid4())
# 基于名字的SHA-1散列
print(uuid.uuid5(UUID(int=2),"ECHO"))