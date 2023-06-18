import configparser
from PIL import Image

def resize_image(image_path, output_size, background_color):
    img = Image.open(image_path)
    img.thumbnail(output_size, Image.ANTIALIAS)
    
    new_img = Image.new("RGB", output_size, background_color)
    new_img.paste(img, ((output_size[0] - img.size[0]) // 2,
                        (output_size[1] - img.size[1]) // 2))

    output_path = f"{output_size[0]}x{output_size[1]}_{image_path}"
    new_img.save(output_path)

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    image_path = config.get('DEFAULT', 'Image')
    aspect_ratios = config.get('DEFAULT', 'AspectRatios').split(',')
    background_color = config.get('DEFAULT', 'BackgroundColor')

    for ratio in aspect_ratios:
        width, height = map(int, ratio.split('x'))
        resize_image(image_path, (width, height), background_color)

if __name__ == "__main__":
    main()