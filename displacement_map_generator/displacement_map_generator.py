from PIL import Image, ImageFilter
import numpy as np

def generate_displacement_map(image_path, scale=10):
    input_image = Image.open(image_path).convert("L") 
    input_image = input_image.filter(ImageFilter.GaussianBlur(radius=2))
    image_array = np.array(input_image)
    normalized_array = image_array / 255.0
    displacement_map = normalized_array * scale
    displacement_map_image = Image.fromarray((displacement_map * 255).astype('uint8'), mode='L')

    return displacement_map_image

def main():
    input_image_path = "input_map_displacement.png"
    scale = 10

    displacement_map = generate_displacement_map(input_image_path, scale)

    displacement_map.save("displacement_map.png")

if __name__ == "__main__":
    main()
