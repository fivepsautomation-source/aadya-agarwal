import os
import shutil

src_dir = r"c:\Users\hp\Desktop\addhay agarwal"
dst_dir = r"C:\Users\hp\Desktop\Aadya-New-Portfolio"

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# Copy html, css, js
for f in os.listdir(src_dir):
    if f.endswith('.html') or f.endswith('.css') or f.endswith('.js') or f.endswith('.json'):
        src_file = os.path.join(src_dir, f)
        dst_file = os.path.join(dst_dir, f)
        shutil.copy2(src_file, dst_file)
        print(f"Copied {f}")

# Copy assets folder recursively
src_assets = os.path.join(src_dir, 'assets')
dst_assets = os.path.join(dst_dir, 'assets')
if os.path.exists(src_assets):
    if os.path.exists(dst_assets):
        # copy over tree
        for root, dirs, files in os.walk(src_assets):
            rel_dir = os.path.relpath(root, src_assets)
            target_sub = os.path.join(dst_assets, rel_dir)
            if not os.path.exists(target_sub):
                os.makedirs(target_sub)
            for file in files:
                shutil.copy2(os.path.join(root, file), os.path.join(target_sub, file))
    else:
        shutil.copytree(src_assets, dst_assets)
    print("Assets synchronized successfully!")

# Copy projects folder recursively (including videos)
src_projects = os.path.join(src_dir, 'projects')
dst_projects = os.path.join(dst_dir, 'projects')
if os.path.exists(src_projects):
    if os.path.exists(dst_projects):
        for root, dirs, files in os.walk(src_projects):
            rel_dir = os.path.relpath(root, src_projects)
            target_sub = os.path.join(dst_projects, rel_dir)
            if not os.path.exists(target_sub):
                os.makedirs(target_sub)
            for file in files:
                shutil.copy2(os.path.join(root, file), os.path.join(target_sub, file))
    else:
        shutil.copytree(src_projects, dst_projects)
    print("Projects synchronized successfully!")

# Copy slider folder recursively
src_slider = os.path.join(src_dir, 'slider')
dst_slider = os.path.join(dst_dir, 'slider')
if os.path.exists(src_slider):
    if os.path.exists(dst_slider):
        for root, dirs, files in os.walk(src_slider):
            rel_dir = os.path.relpath(root, src_slider)
            target_sub = os.path.join(dst_slider, rel_dir)
            if not os.path.exists(target_sub):
                os.makedirs(target_sub)
            for file in files:
                shutil.copy2(os.path.join(root, file), os.path.join(target_sub, file))
    else:
        shutil.copytree(src_slider, dst_slider)
    print("Slider synchronized successfully!")

print("All synchronized to C:\\Users\\hp\\Desktop\\Aadya-New-Portfolio successfully!")
