
import time
import os
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from datetime import datetime



os.chdir(r"working directory")  # Update this path
names = """Aiman Muhammed Rabi al-Zawahiri  
Abu Bakr al-Baghdadi  
Saif al-Adel  
Abdullah Ahmed Abdullah  
Abu Musab al-Zarqawi  
Abdul Mohsen Abdallah Ibrahim al-Tuwaijri  
Abu Muhammad al-Julani  
Abu Sayyaf  
Mokhtar Belmokhtar  
Abdelmalek Droukdel  
Sami al-Sa’id al-Shihri  
Ibrahim Awwad Ibrahim Ali al-Badri  
Khalid Sheikh Mohammed  
Abu Anas al-Libi  
Abu Hamza al-Masri  
Abu Qatada al-Filistini  
Abu Dujana al-Khorasani  
Abu Omar al-Shishani  
Abd al-Rahman al-Dakhil  
Abu Hafs al-Mauritani"""

names = names.split('\n')
names = names[:2]
for name in names:
        
    # Path to Edge WebDriver
    edgedriver_path = r"C:\Program Files (x86)\Microsoft\msedgedriver.exe"  # Update this path
    
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(executable_path=edgedriver_path)
    driver = webdriver.Edge(service=service, options=options)
    
    # Load page and perform search
    driver.get("https://duckduckgo.com/")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(f"{name}")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    
    page_text = driver.find_element(By.TAG_NAME, "body").text


    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


    text_filename = f"search_text_{name}_{timestamp}.txt"
    with open(text_filename, "w", encoding="utf-8") as f:
        f.write(f"Search results for: {name}\nTimestamp: {timestamp}\n\n")
        f.write(page_text)


    # Get dimensions
    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")
    driver.set_window_size(1920, viewport_height)
    time.sleep(1)
    
    # Scroll and capture
    screenshots = []
    scroll_position = 0
    index = 0
    
    while scroll_position < total_height:
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(1)
        filename = f"screenshot_{index}.png"
        driver.save_screenshot(filename)
        screenshots.append(filename)
        scroll_position += viewport_height
        index += 1
    
    driver.quit()
    
    # Stitch screenshots
    images = [Image.open(img) for img in screenshots]
    width = max(img.width for img in images)
    total_height = sum(img.height for img in images)
    
    stitched_image = Image.new('RGB', (width, total_height))
    y_offset = 0
    for img in images:
        stitched_image.paste(img, (0, y_offset))
        y_offset += img.height
    
    stitched_image.save(f"fullpage_stitched {name}.png")
    print("Full-page screenshot saved as fullpage_stitched.png")
    
    # Cleanup
    for img in screenshots:
        os.remove(img)
        
        
# image_path = "fullpage_stitched.png"  # Replace with your image filename
# image = Image.open(image_path)

# # Convert to RGB (PDF doesn't support alpha channel)
# if image.mode == "RGBA":
#     image = image.convert("RGB")

# # Save as PDF
# pdf_path = "fullpage_output.pdf"
# image.save(pdf_path, "PDF", resolution=100.0)

# print(f"Saved PDF as {pdf_path}")
