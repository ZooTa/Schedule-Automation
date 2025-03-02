import pywhatkit
import logging

def send_whatsapp_schedule(phone_number, img_path, message, wait_time=30, close_time=5):
    """Send an image with a caption via WhatsApp."""
    try:
        logging.info(f"Sending image to {phone_number}")
        pywhatkit.sendwhats_image(
            receiver="+" + phone_number,
            img_path=img_path,
            caption=message,
            wait_time=wait_time,
            tab_close=True,
            close_time=close_time
        )
    except Exception as e:
        logging.error(f"An error occurred while sending the image: {e}")
