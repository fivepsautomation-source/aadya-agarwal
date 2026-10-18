from PIL import Image

im = Image.open('assets/robotics/pic 1 - with robot.jpg')
w, h = im.size
print(f"Image size: {w}x{h}")

# Let's save slices to see where face and robot are located:
# Top 45% (0 to 0.45*h)
top_half = im.crop((0, 0, w, int(h * 0.55)))
top_half.save('scratch_top.jpg')
print("Saved scratch_top.jpg")

# 0 to 65% of h
top_65 = im.crop((0, 0, w, int(h * 0.65)))
top_65.save('scratch_top_65.jpg')
print("Saved scratch_top_65.jpg")
