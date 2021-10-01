from PIL import Image, ImageDraw
import numpy
import base64
from io import BytesIO

#
# filename = input("File name?") or "/static/FlyingPigeon.jpg"
# img = Image.open(filename)
# img.show()
#
# for x in range(img.size[0]):
#     for y in range(img.size[1]):
#         r, g, b = img.getpixel((x, y))
#         img.putpixel((x, y), (b, g, r))
#
# img.show()
# image (PNG, JPG) to base64 conversion (string), learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)


# color_data prepares a series of images for data analysis
def image_data(path="static/RiceTypes/", img_list=None):  # path of static images is defaulted
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "jessicagavin.com", 'label': "Forbidden Rice", 'file': "Forbidden.PNG"},
            {'source': "jessicagavin.com", 'label': "Parboiled Rice", 'file': "Parboiled Rice.JPG"},
            {'source': "jessicagavin.com", 'label': "Sticky Rice", 'file': "Sticky Rice.JPG"},
            {'source': "jessicagavin.com", 'label': "Basmati Rice", 'file': "BasmatiRice.PNG"},
            {'source': "jessicagavin.com", 'label': "Brown Rice", 'file': "Brown Rice.JPG"},
            {'source': "jessicagavin.com", 'label': "Jasmine Rice", 'file': "Jasmine Rice.JPG"},
        ]

    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_ref = Image.open(file)  # PIL
        img_reference = ImageDraw.Draw(img_ref)
        img_reference.text((0, 0), "Yash sucks", (255,255,255))
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        img_dict['gray_data'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
            # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
        img_dict['hex_array_GRAY'] = []
        img_dict['binary_array_GRAY'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['gray_data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array_GRAY'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array_GRAY'].append(bin_value)
    return img_list  # list is returned with all the attributes for each image dictionary


# run this as standalone tester to see data printed in terminal
if __name__ == "__main__":
     local_path = "../static/RiceTypes/"
     img_test = [
         {'source': "idk who this is lol", 'label': "Forbidden-Rice", 'file': "Forbidden.png"}
     ]
     items = image_data(local_path, img_test)  # path of local run
     for row in items:
         # print some details about the image so you can validate that it looks like it is working
         # meta data
         print("---- meta data -----")
         print(row['label'])
         print(row['format'])
         print(row['mode'])
         print(row['size'])
         # data
         print("----  data  -----")
         print(row['data'])
         print("----  gray data  -----")
         print(row['gray_data'])
         print("----  hex of data  -----")
         print(row['hex_array'])
         print("----  bin of data  -----")
         print(row['binary_array'])
         # base65
         print("----  base64  -----")
         print(row['base64'])
         # display image
         print("----  render and write in image  -----")
         filename = local_path + row['file']
         image_ref = Image.open(filename)
         draw = ImageDraw.Draw(image_ref)
         draw.text((0, 0), "Size is {0} X {1}".format(*row['size']))  # draw in image
         image_ref.show()
print()