import easygui as eg
from PIL import Image, ImageDraw, ImageFont
import os

def browse_images():
    file_paths = eg.fileopenbox(msg="Select Certificate Images", filetypes=["*.png;*.jpg;*.jpeg;*.bmp;*.gif"], multiple=True)
    return file_paths

def browse_font():
    font_path = eg.fileopenbox(msg="Select Font File", filetypes=["*.ttf", "*.otf"])
    return font_path

def modify_certificates(image_paths, name, font_path, font_size, color, x_pos, y_pos):
    try:
        for image_path in image_paths:
            certificate_image = Image.open(image_path)
            selected_font = ImageFont.truetype(font_path, font_size)
            draw = ImageDraw.Draw(certificate_image)
            draw.text((x_pos, y_pos), name, fill=color, font=selected_font)

            base_name, extension = os.path.splitext(os.path.basename(image_path))
            output_path = f"{base_name}_Modified{extension}"
            certificate_image.save(output_path)
        
        eg.msgbox(f"{len(image_paths)} certificates modified and saved.", "Success")
    except Exception as e:
        eg.exceptionbox(e)

def main():
    image_paths = browse_images()
    if image_paths:
        font_path = browse_font()
        if font_path:
            msg = "Enter Certificate Details"
            title = "Certificate Modifier"
            field_names = ["Name:", "Font Size:", "Text Color (e.g., 'black'):", "X Position:", "Y Position:"]
            field_values = ["", "56", "black", "500", "700"]

            field_values = eg.multenterbox(msg, title, field_names, field_values)
            if field_values:
                name, font_size, color, x_pos, y_pos = field_values
                modify_certificates(image_paths, name, font_path, int(font_size), color, int(x_pos), int(y_pos))

if __name__ == "__main__":
    main()
