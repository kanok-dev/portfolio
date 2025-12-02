#!/usr/bin/env python3
"""
Image Resizer Script for Portfolio Images
Resizes all images to 1080px width while maintaining aspect ratio.
Supports: PNG, JPG, JPEG, WEBP
"""

import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Installing...")
    os.system("pip3 install Pillow")
    from PIL import Image

# Configuration
TARGET_WIDTH = 1080
SUPPORTED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.webp'}
BASE_DIR = Path(__file__).parent

# Folders to process
FOLDERS = [
    'content-ai',
    'eorder-mobile',
    'kanoks-me-nextjs',
    'kugarden-reactjs',
    'lotto-nextjs',
    'lucky-number-magic-reactjs',
    'merchandiser-mobile-app',
    'n8n',
    'smartsales-csharp-jquery',
    'sport-games-nextjs',
    'stack-nextjs',
    'stock-portfolio-manager-reactjs',
]

def resize_image(image_path: Path, target_width: int = TARGET_WIDTH) -> bool:
    """
    Resize an image to target width while maintaining aspect ratio.
    Returns True if image was resized, False if skipped.
    """
    try:
        with Image.open(image_path) as img:
            original_width, original_height = img.size
            
            # Skip if already smaller than or equal to target width
            if original_width <= target_width:
                print(f"  ⏭️  Skipped (already {original_width}px): {image_path.name}")
                return False
            
            # Calculate new height maintaining aspect ratio
            ratio = target_width / original_width
            new_height = int(original_height * ratio)
            
            # Resize image with high-quality resampling
            resized_img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
            
            # Preserve image format and save
            resized_img.save(image_path, quality=90, optimize=True)
            
            print(f"  ✅ Resized: {image_path.name} ({original_width}x{original_height} → {target_width}x{new_height})")
            return True
            
    except Exception as e:
        print(f"  ❌ Error processing {image_path.name}: {e}")
        return False

def process_folder(folder_path: Path) -> tuple[int, int]:
    """
    Process all images in a folder and its subfolders.
    Returns tuple of (resized_count, skipped_count).
    """
    resized = 0
    skipped = 0
    
    if not folder_path.exists():
        print(f"⚠️  Folder not found: {folder_path}")
        return 0, 0
    
    # Process all files in folder and subfolders
    for file_path in folder_path.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
            if resize_image(file_path):
                resized += 1
            else:
                skipped += 1
    
    return resized, skipped

def main():
    print("=" * 60)
    print("🖼️  Portfolio Image Resizer")
    print(f"   Target width: {TARGET_WIDTH}px")
    print("=" * 60)
    print()
    
    total_resized = 0
    total_skipped = 0
    
    for folder_name in FOLDERS:
        folder_path = BASE_DIR / folder_name
        print(f"📁 Processing: {folder_name}/")
        
        resized, skipped = process_folder(folder_path)
        total_resized += resized
        total_skipped += skipped
        
        if resized == 0 and skipped == 0:
            print("   (no images found)")
        print()
    
    # Also process root level images
    print("📁 Processing: root folder")
    for file_path in BASE_DIR.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
            if resize_image(file_path):
                total_resized += 1
            else:
                total_skipped += 1
    
    print()
    print("=" * 60)
    print(f"✨ Complete!")
    print(f"   Resized: {total_resized} images")
    print(f"   Skipped: {total_skipped} images (already ≤{TARGET_WIDTH}px)")
    print("=" * 60)

if __name__ == "__main__":
    main()
