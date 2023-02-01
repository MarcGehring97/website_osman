import os

images_folder = "images/arc_turkey"

with open("arc_turkey.html", "r") as f:
    html_file = f.read()

print(html_file)

images = ""

for filename in os.listdir(images_folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        image_path = os.path.join(images_folder, filename)
        images += f'''
          <div class="col-sm-6 col-md-4 col-lg-3 col-xl-3 item" data-aos="fade" data-src="{image_path}" data-sub-html="<h4></h4><p></p>">
            <a href="#"><img src="{image_path}" alt="IMage" class="img-fluid"></a>
          </div>
        '''

print(images)

html_file = html_file.replace("<!-- Placeholder for images -->", images)

with open("arc_turkey.html", "w") as f:
    f.write(html_file)






with open("arc_turkey_de.html", "r") as f:
    html_file = f.read()

print(html_file)

images = ""

for filename in os.listdir(images_folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        image_path = os.path.join(images_folder, filename)
        images += f'''
          <div class="col-sm-6 col-md-4 col-lg-3 col-xl-3 item" data-aos="fade" data-src="{image_path}" data-sub-html="<h4></h4><p></p>">
            <a href="#"><img src="{image_path}" alt="IMage" class="img-fluid"></a>
          </div>
        '''

print(images)

html_file = html_file.replace("<!-- Placeholder for images -->", images)

with open("arc_turkey_de.html", "w") as f:
    f.write(html_file)


