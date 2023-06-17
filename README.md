# Database_Course_Design_Backend

## 简介

Database_Course_Design_Backend 是电信学院数据库及应用实践课程大作业的后端部分。

前端部分：https://github.com/TomSawyer2/Database_Course_Design_FE

## 技术栈

- Python 
- Django

## 实现的功能

- 学生信息
  - 学生信息查询
  - 学生信息修改
  - 学生信息删除
  - 学生信息添加
  - 帮助学生选课
- 教师信息
  - 教师信息查询
  - 教师信息修改
  - 教师信息删除
  - 教师信息添加
- 课程信息
  - 课程信息查询
  - 课程信息修改
  - 课程信息删除
  - 课程信息添加
- 硬件资源信息
  - 硬件资源信息查询
  - 硬件资源信息修改
  - 硬件资源信息删除
  - 硬件资源信息添加

## 数据库迁移

```bash
# 修改setting.py中数据库的设置
python manage.py makemigrations
python manage.py migrate
```

## 启动项目

```bash
python manage.py runserver
```

## Contributor

- [TomSawyer2](https://github.com/TomSawyer2)
- [guofuwei](https://github.com/guofuwei)
