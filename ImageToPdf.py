from PIL import Image
file = "images\\screenshot.png"
image = Image.open(file)
if image.mode == "RGBA":
    image = image.convert("RGB")
output = "documents\\ImageToPdf.pdf"
image.save(output, "PDF", resolution=100.0)