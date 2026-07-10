import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_dct(image_path):
    # 1. Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Could not load image.")
        return

    # 2. Ensure image dimensions are divisible by 8
    h, w = img.shape
    h_new, w_new = (h // 8) * 8, (w // 8) * 8
    img = img[:h_new, :w_new]

    # 3. Apply DCT in 8x8 blocks
    dct_blocks = []
    for i in range(0, h_new, 8):
        for j in range(0, w_new, 8):
            block = img[i:i+8, j:j+8].astype(np.float32)
            dct_block = cv2.dct(block)
            dct_blocks.append(dct_block)

    # 4. Average the DCT coefficients to find global anomalies
    dct_avg = np.mean(dct_blocks, axis=0)
    
    # 5. Calculate log-magnitude for visualization
    # Adding 1e-6 to avoid log(0)
    magnitude_spectrum = np.log(np.abs(dct_avg) + 1e-6)
  
    print(f"Log-Magnitude Spectrum:\n{magnitude_spectrum}")
    # 6. Plotting
    plt.figure(figsize=(10, 5))
    plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Input Image')
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='inferno'), plt.title('DCT Frequency Spectrum')
    plt.show()

# Run the analysis
analyze_dct('path of image')