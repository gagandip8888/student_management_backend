from fastapi import APIRouter, HTTPException
from Model.studentmodel import StudentStruct
from Model.updatestudent import updateStruct
from Database.connection import collectionName

router = APIRouter()


@router.post("/student")
def CreateStudent(student: StudentStruct):
    try:
        # Check if roll number already exists
        if collectionName.find_one({"roll": student.roll}):
            raise HTTPException(
                status_code=400,
                detail=f"Student with roll number {student.roll} already exists"
            )

        sinfo = {
            "roll": student.roll,
            "name": student.name,
            "age": student.age,
            "email": student.email
        }

        collectionName.insert_one(sinfo)

        return {"message": "new student created"}

    except HTTPException:
        raise
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/studentslist")
def Getallstudents():
    try:
        alldata = list(collectionName.find({}, {"_id": 0}))
        return alldata
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Unable to fetch students")


@router.put("/edit/{roll}")
def UpdateStudent(roll: int, studentinfo: updateStruct):
    try:
        student = collectionName.find_one({"roll": roll})
        if not student:
            raise HTTPException(
                status_code=404,
                detail=f"Student with roll number {roll} not found"
            )

        updatedinfo = {}

        if studentinfo.name is not None and studentinfo.name.strip() != "":
            updatedinfo["name"] = studentinfo.name

        if studentinfo.age is not None:
            updatedinfo["age"] = studentinfo.age

        if studentinfo.email is not None and str(studentinfo.email).strip() != "":
            updatedinfo["email"] = studentinfo.email

        if not updatedinfo:
            raise HTTPException(
                status_code=400,
                detail="Please enter at least one field to update"
            )

        collectionName.update_one(
            {"roll": roll},
            {"$set": updatedinfo}
        )

        return {"message": "Student updated successfully"}

    except HTTPException:
        raise
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete/{roll}")
@router.delete("/delet/{roll}")
def Deletstudent(roll: int):
    try:
        result = collectionName.delete_one({"roll": roll})
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail=f"Student with roll number {roll} not found"
            )

        return {"message": "Student deleted successfully"}

    except HTTPException:
        raise
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))