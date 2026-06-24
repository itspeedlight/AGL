from PIL import Image
import collections
import os

def get_dominant_green(image_path):
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return None
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = list(img.getdata())
    
    # Filter for green-ish colors
    greens = [p for p in pixels if p[1] > p[0] + 10 and p[1] > p[2] + 10 and p[1] > 30]
    
    if not greens:
        return None
        
    most_common = collections.Counter(greens).most_common(1)[0][0]
    return '#{:02x}{:02x}{:02x}'.format(*most_common)

logo_path = 'logo/WhatsApp_Image_2026-06-19_at_23.47.25-removebg-preview.png'
print(f"Logo Green: {get_dominant_green(logo_path)}")
