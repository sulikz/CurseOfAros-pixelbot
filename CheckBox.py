from PIL import ImageGrab, Image, ImageChops


def check_box(image_path, box_coords, error=10, debug=False):
    use_box = ImageGrab.grab(box_coords)
    image_path = Image.open(image_path)
    out = ImageChops.difference(use_box, image_path)
    if type(out.getcolors()) is list:
        if debug:
            print(len(out.getcolors()))
        if len(out.getcolors()) < error:
            return True
        else:
            # print("Not found")
            return False
    else:
        # print("Not found")
        return False
