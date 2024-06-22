from PIL import Image
image_path_list = ["Nishant1.jpeg","Nishant2.jpeg","Nishant3.jpeg","Nishant4.jpeg"]
image_list = [Image.open(file)for file in image_path_list]
image_list[0].save(
    'animation.gif',
    save_all = True,
    append_images = image_list[1:],
    duration = 1000,
    loop = 0,
    
    
)
                   