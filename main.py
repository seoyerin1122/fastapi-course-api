from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


# 요청 데이터 형식 정의
class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str


# GET /courses
@app.get("/courses")
def get_courses():
    with open("courses.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


# POST /courses
@app.post("/courses")
def add_course(course: Course):

    # 기존 데이터 읽기
    with open("courses.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 새 데이터 추가
    data.append(course.dict())

    # 파일 다시 저장
    with open("courses.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return {
        "message": "과목 추가 완료",
        "new_course": course
    }