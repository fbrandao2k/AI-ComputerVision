from pathlib import Path
import pandas as pd
import cv2

# Tile function
def tile_image_and_save(image, base_name, output_dir, tile_size=1024):
    count = 0
    for y in range(0, image.shape[0], tile_size):
        for x in range(0, image.shape[1], tile_size):
            tile = image[y:y+tile_size, x:x+tile_size]
            if tile.shape[0] == tile_size and tile.shape[1] == tile_size:
                tile_filename = output_dir / f"{base_name}_tile_{count:03}.png"
                cv2.imwrite(str(tile_filename), tile)
                count += 1

# Process the uploaded image: resize to 2080x1248 and tile into 416x416

# Define paths
#uploaded_image_path = "D:/AI-ComputerVision/Damages/Crack/PonteJacunda/Drones/01_Zenmuse/DJI_202311301117_002_UgCS-JacundaT60/DJI_20231130112414_0100.JPG"
uploaded_image_folder = "D:/AI-ComputerVision/Damages/Crack/PonteJacunda/Drones/01_Zenmuse/DJI_202312011513_013_original"
#resized_output_path = "D:/AI-ComputerVision/Damages/Crack/PonteJacunda/Drones/01_Zenmuse/DJI_202311301117_002_UgCS-JacundaT60_resized/DJI_20231130112414_0100_resized.JPG"
tiled_output_folder = Path("D:/AI-ComputerVision/Damages/Crack/PonteJacunda/Drones/01_Zenmuse/DJI_202312011513_013_FPs")
tiled_output_folder.mkdir(parents=True, exist_ok=True)

# Get all image files in the uploaded_image_folder
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff')
image_files = [f for f in Path(uploaded_image_folder).iterdir() if f.suffix.lower() in image_extensions]

i = 0
while i < len(image_files):
    uploaded_image_path = str(image_files[i])
    base_name = Path(uploaded_image_path).stem

    # Read and resize
    original_image = cv2.imread(uploaded_image_path)
    # Optionally resize here if needed
    # resized_image = cv2.resize(original_image, (2080, 1248), interpolation=cv2.INTER_AREA)
    # cv2.imwrite(uploaded_image_path, resized_image)

    # Tile and save
    tile_image_and_save(original_image, base_name, tiled_output_folder)
    i += 1



cv2.imwrite(uploaded_image_path, original_image)




# Tile and save
#tile_image_and_save(original_image, "DJI_20231130112414_0100", tiled_output_folder)
# List created tiles
#tile_files = sorted(tiled_output_folder.glob("*.jpg"))
#tools.display_dataframe_to_user(name="Tiled Images", dataframe=pd.DataFrame({
#    "Tile Filename": [tile.name for tile in tile_files]

#df = pd.DataFrame({
#    "Tile Filename": [tile.name for tile in tile_files]
#})
#print("Tiled Images:")
#print(df)