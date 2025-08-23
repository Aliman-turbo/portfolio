from PIL import Image, ImageDraw
import random

# Настройки изображения
width = 800
height = 600

# Создание нового изображения
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Генерация случайных фигур
for _ in range(100):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)

    shape_type = random.choice(["rectangle", "ellipse", "line"])
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if shape_type == "rectangle":
        draw.rectangle([x1, y1, x2, y2], fill=color)
    elif shape_type == "ellipse":
        draw.ellipse([x1, y1, x2, y2], fill=color)
    elif shape_type == "line":
        draw.line([x1, y1, x2, y2], fill=color, width=3)

# Сохранение изображения
image.save("generated_image.png")

print("Изображение сгенерировано и сохранено как 'generated_image.png'.")
