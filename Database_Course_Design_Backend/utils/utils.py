def make_res(select_res):
    array_res = []
    for i in select_res:
        array_res.append({
            "id": i.id,
            "name": i.name,
            "sex": i.sex,
            "student_id": i.student_id,
            "department": i.department,
            "class_name": i.class_name,
            "telephone": i.telephone
        }
        )
    return array_res