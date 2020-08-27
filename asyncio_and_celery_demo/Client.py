from server import get_html
from celery.result import AsyncResult

tasks = []

for i in range(10):
    task = get_html.delay() # 这是celery获取结果的ID
    tasks.append(task)      # 将这些ID存储起来，为了以后能找到相应结果

for t in tasks:
    print(AsyncResult(t.get()))