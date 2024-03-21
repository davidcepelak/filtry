import urllib.request 
from PIL import Image, ImageEnhance, ImageFilter, ImageColor, ImageDraw

urllib.request.urlretrieve('https://cdn.myshoptet.com/usr/www.chlupaci.cz/user/documents/upload/clanky-psi-plemena/Finsky-laponsky-pes/Plemeno-Finsky-laponsky-pes%20(15).jpg', "pes.png") 

def elipsa():
    obrazek = Image.open("pes.png")
    draw = ImageDraw.Draw(obrazek)
    draw.ellipse((200, 125, 1200, 1000), fill=(255, 105, 180), outline=(0, 0, 0))
    return(obrazek)

def contrast():
  obrazek = Image.open("pes.png")
  enhancer = ImageEnhance.Contrast(obrazek)
  obrazek = enhancer.enhance(5)
  return(obrazek)

def blur():
  obrazek = Image.open("pes.png")
  return obrazek.filter(ImageFilter.BLUR)

def greyscale():
    obrazek = Image.open("pes.png")
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x, y))
            grayscale = int((r + g + b) / 3)
            obrazek.putpixel((x, y), (grayscale, grayscale, grayscale))
            y += 1
        x += 1
    return(obrazek)

while True:
    print("\n----- editors Database -----")
    print("1. filtr - elipsa")
    print("2. filtr - greyscale")
    print("3. filtr - contrast")
    print("4. filtr - blur")
    choice = input("Select an option: ")
    if choice == "1":
        modified_image = elipsa()
    elif choice == "2":
        modified_image = greyscale()
    elif choice == "3":
        modified_image = contrast()
    elif choice == "4":
        modified_image = blur()
    else:
        print("Wrong number! Select one of these numbers: 1, 2, 3, 4.")
    
    modified_image.show()




