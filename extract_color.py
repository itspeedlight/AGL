from PIL import Image
import collections

def get_dominant_green(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = list(img.getdata())
    
    # Filter for green-ish colors
    # Green-ish: G > R and G > B and G is reasonably high
    greens = [p for p in pixels if p[1] > p[0] + 20 and p[1] > p[2] + 20 and p[1] > 50]
    
    if not greens:
        return None
        
    most_common = collections.Counter(greens).most_common(1)[0][0]
    return '#{:02x}{:02x}{:02x}'.format(*most_common)

print(f"Logo 1 Green: {get_dominant_green('c:/Users/2025/Desktop/logistics pro/logo/3e1f46a7-1098-487f-858b-33ffe1bc921f.png')}")
print(f"Logo 2 Green: {get_dominant_green('c:/Users/2025/Desktop/logistics pro/logo/WhatsApp Image 2026-06-19 at 23.47.25.jpeg')}")
