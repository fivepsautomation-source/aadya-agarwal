from PIL import Image

im = Image.open('assets/robotics/pic 1 - with robot.jpg')
w, h = im.size

# Simulate .gallery-card (310x430, aspect ratio 310/430)
# To cover: scale so width >= 310 and height >= 430
scale = max(310 / w, 430 / h) # max(0.43, 0.33) = 0.4305 (width fits, height is 560px)
new_w = int(w * scale)
new_h = int(h * scale)
resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)

# Top center crop: crop (0, 0, 310, 430)
top_crop = resized.crop((0, 0, 310, 430))
top_crop.save('gallery_card_top_crop.jpg')
print("Saved gallery_card_top_crop.jpg")

# Simulate .curated-visual-frame (540x520)
scale2 = max(540 / w, 520 / h) # 540/720 = 0.75 -> height is 975px
resized2 = im.resize((540, int(h * 0.75)), Image.Resampling.LANCZOS)
top_crop2 = resized2.crop((0, 0, 540, 520))
top_crop2.save('curated_frame_top_crop.jpg')
print("Saved curated_frame_top_crop.jpg")
