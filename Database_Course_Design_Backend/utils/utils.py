def make_res(select_res, res_type):
    array_res = []
    if res_type == "student":
        for i in select_res:
            array_res.append({
                "id": i.id,
                "name": i.name,
                "sex": i.sex,
                "studentId": i.student_id,
                "department": i.department,
                "className": i.class_name,
                "telephone": i.telephone
            })
    elif res_type == "teacher":
        for i in select_res:
            array_res.append({
                "id": i.id,
                "name": i.name,
                "teacherId": i.teacher_id,
                "courseId": i.course_id
            })
    elif res_type == "course":
        for i in select_res:
            array_res.append({
                "id": i.id,
                "courseName": i.course_name,
                "maxSelectNum": i.max_select_num,
                "selectedNum": i.selected_num
            })
    elif res_type == "hard_resource":
        for i in select_res:
            array_res.append({
                "id": i.id,
                "resourceName": i.resource_name,
                "resourceNum": i.resource_num
            })
    elif res_type == "sc":
        for i in select_res:
            array_res.append({
                "id": i.id,
                "studentId": i.student_id,
                "courseId": i.course_id
            })
    elif res_type == "rc":
        for i in select_res:
            array_res.append({
                "id": i.id,
                "courseId": i.course_id,
                "resourceId": i.resource_id
            })
    return array_res
