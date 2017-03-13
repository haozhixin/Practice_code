### 员工信息表查询
程序介绍:
  bin  # 程序运行入口
  dbfile #存放数据文件
  core   #主逻辑
  数据文件为json格式
    [
  {"staff_id": 1, "name": "Alex Li", "age": "22", "phone": 129237284, "dept": "IT", "enroll_date": "2013-01-01"}
  ]

  程序如何使用？
  进入到bin目录，使用python3 执行 
  python3 search_content.py
  dbfile 目录
  - 支持 增，删，改，查 功能
  - 增 (语法)
  > add name age phone dept 
  > 例如： add xiaoli 22 1321231213 IT
  - 删 
  > del id
  > 例如： del 1
  - 改
  > update db SET dept="Market" where dept=IT
  - 查
  > select * from db 
  > select * from db where dept=IT
  > select name form db
  >
