from app.tasks.cele import celery
from PIL import Image
from pathlib import Path
from pydantic import EmailStr
from app.tasks.email_temp import create_booking_email
import smtplib
from app.config import settings


@celery.task
def process_picture(
        path: str,
):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized1 = im.resize((256, 256))
    im_resized2 = im.resize((100, 200))
    im_resized1 .save(f"app/static/images/resized_1{im_path.name}")
    im_resized2.save(f"app/static/images/resized_2{im_path.name}")


@celery.task
def send_booking_email(
        booking: dict,
        email_to: EmailStr

):

    msg = create_booking_email(booking, email_to)
    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.send_message(msg)
