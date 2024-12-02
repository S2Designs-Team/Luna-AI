# image_encoder.py
import base64

def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def generate_encoded_image_url(base64_image: str) -> str:
    return f"data:image/jpeg;base64,{base64_image}"


if __name__ == "__main__":
    image_path = "/percorso/che/porta/alla/vostra/immagine.png"
    encoded_image = encode_image(image_path=image_path)
    print(encoded_image)