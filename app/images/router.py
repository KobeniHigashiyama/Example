from fastapi import APIRouter
from fastapi import UploadFile
import shutil
from app.tasks.task import process_picture
router = APIRouter(prefix="/images", tags=["images"])


@router.post("/hotels",)
async def add_image(name: int, file: UploadFile):
    im_path = f"app/static/images/{name}.webp"
    with open(im_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
        process_picture.delay(im_path)
