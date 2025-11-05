import cv2
import numpy as np
import random
import os

# Output folders
os.makedirs("multi_shapes/images", exist_ok=True)
os.makedirs("multi_shapes/labels", exist_ok=True)

# Our shape classes
classes = ["circle", "square", "triangle", "star"]

def random_color():
    return tuple(np.random.randint(0, 255, 3).tolist())

for i in range(500):  # number of new images to create
    img = np.ones((640, 640, 3), dtype=np.uint8) * 255  # white background
    label_lines = []
    
    # draw between 2 to 5 random shapes
    for j in range(random.randint(2, 5)):
        shape_type = random.choice(classes)
        cx, cy = random.randint(100, 540), random.randint(100, 540)
        size = random.randint(50, 120)
        color = random_color()
        
        if shape_type == "circle":
            cv2.circle(img, (cx, cy), size // 2, color, -1)
        elif shape_type == "square":
            cv2.rectangle(img, (cx - size//2, cy - size//2), (cx + size//2, cy + size//2), color, -1)
        elif shape_type == "triangle":
            pts = np.array([[cx, cy - size//2],
                            [cx - size//2, cy + size//2],
                            [cx + size//2, cy + size//2]], np.int32)
            cv2.fillPoly(img, [pts], color)
        elif shape_type == "star":
            pts = np.array([[cx, cy - size//2],
                            [cx + size//5, cy - size//10],
                            [cx + size//2, cy - size//10],
                            [cx + size//4, cy + size//10],
                            [cx + size//3, cy + size//2],
                            [cx, cy + size//4],
                            [cx - size//3, cy + size//2],
                            [cx - size//4, cy + size//10],
                            [cx - size//2, cy - size//10],
                            [cx - size//5, cy - size//10]], np.int32)
            cv2.fillPoly(img, [pts], color)

        # YOLO label format
        label_lines.append(f"{classes.index(shape_type)} {cx/640:.6f} {cy/640:.6f} {size/640:.6f} {size/640:.6f}\n")

    # Save image and label
    cv2.imwrite(f"multi_shapes/images/{i:04d}.jpg", img)
    with open(f"multi_shapes/labels/{i:04d}.txt", "w") as f:
        f.writelines(label_lines)

print("✅ Multi-shape dataset created successfully!")
