from PIL import Image

def create_alpha_image(input_image_path, output_path='alpha_image.png'):
    input_image = Image.open(input_image_path).convert('RGBA')
    alpha_channel = input_image.split()[3]
    alpha_image = Image.new('L', input_image.size, 0)
    alpha_image.paste(alpha_channel, (0, 0, input_image.width, input_image.height))
    alpha_image.save(output_path)

input_image_path = "input_map_alpha.png"

output_path = "alpha_map.png"

create_alpha_image(input_image_path, output_path)

