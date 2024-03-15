from PIL import Image
import pytesseract
#Necessario instalar a biblioteca PIL

# Load the image
image_path = "inputs\imagemciclista_texto.jpg"
image = Image.open(image_path)

# Extract text using pytesseract
extracted_text = pytesseract.image_to_string(image, lang="por")

# Print the extracted text
print(extracted_text)

