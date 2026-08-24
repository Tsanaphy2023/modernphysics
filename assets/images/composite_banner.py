#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Composite Exact Portrait of Asst. Prof. Dr. Chewa Thassana onto Modern Physics Futuristic Banner.
Applies:
- Clean Alpha Masking
- Cyber Cyan Rim Glow / Volumetric Aura
- Seamless Bottom Gradient Blending
- High-grade Typography Overlay (PIL)
- Versioning Management (v1, v2, v3)
"""

import os
import shutil
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance

BASE_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics"
IMG_DIR = os.path.join(BASE_DIR, "assets/images")
BOOK_DIR = os.path.join(BASE_DIR, "หนังสือ-เล่ม1-ฟิสิกส์ยุคใหม่")
os.makedirs(IMG_DIR, exist_ok=True)

# File Paths
bg_path = "/Users/chewathassana/.gemini/antigravity-ide/brain/679e2469-a84d-4997-9cf3-ebd6c6dd88fe/modern_physics_banner_1787544473378.jpg"
v2_path = "/Users/chewathassana/.gemini/antigravity-ide/brain/679e2469-a84d-4997-9cf3-ebd6c6dd88fe/chewa_modern_physics_banner_1787545400156.jpg"
cutout_path = os.path.join(IMG_DIR, "chewa_portrait_cutout.png")

# 1. Archive Version 1 & Version 2
shutil.copyfile(bg_path, os.path.join(IMG_DIR, "modern_physics_banner_v1_pure_scifi.jpg"))
shutil.copyfile(v2_path, os.path.join(IMG_DIR, "modern_physics_banner_v2_ai_synth.jpg"))
shutil.copyfile(bg_path, os.path.join(BOOK_DIR, "modern_physics_banner_v1_pure_scifi.jpg"))
shutil.copyfile(v2_path, os.path.join(BOOK_DIR, "modern_physics_banner_v2_ai_synth.jpg"))

print("Archived Version 1 and Version 2.")

# 2. Load Background & Cutout
bg = Image.open(bg_path).convert("RGBA")
bg_w, bg_h = bg.size

portrait = Image.open(cutout_path).convert("RGBA")
p_w, p_h = portrait.size

# Target height for portrait in banner (~86% of banner height)
target_h = int(bg_h * 0.88)
aspect = p_w / p_h
target_w = int(target_h * aspect)

portrait_resized = portrait.resize((target_w, target_h), Image.Resampling.LANCZOS)

# Position: Right side of banner
pos_x = bg_w - target_w - int(bg_w * 0.03)
pos_y = bg_h - target_h  # bottom aligned

# 3. Create Cyber Rim Light Glow (Multi-Layer Neon Cyan Glow)
# Extract alpha channel
alpha = portrait_resized.split()[3]

# Create cyan silhouette for glow
glow_color = Image.new("RGBA", (target_w, target_h), (0, 240, 255, 255))
glow_mask = alpha.point(lambda p: 255 if p > 30 else 0)

# Layer 1: Wide soft aura
glow_wide = Image.new("RGBA", (target_w + 120, target_h + 120), (0, 0, 0, 0))
glow_wide.paste((0, 210, 255, 140), (60, 60), mask=alpha)
glow_wide = glow_wide.filter(ImageFilter.GaussianBlur(radius=28))

# Layer 2: Tight bright neon rim
glow_tight = Image.new("RGBA", (target_w + 40, target_h + 40), (0, 0, 0, 0))
glow_tight.paste((0, 255, 255, 220), (20, 20), mask=alpha)
glow_tight = glow_tight.filter(ImageFilter.GaussianBlur(radius=10))

# 4. Color Grading on Portrait (Add subtle cyan ambient to match sci-fi lighting)
r, g, b, a = portrait_resized.split()
# Slight cool tone boost on highlights
enhancer = ImageEnhance.Color(portrait_resized)
portrait_graded = enhancer.enhance(1.08)

# Smooth vertical gradient alpha fade at the bottom (bottom 18% fades to 0)
np_a = np.array(a).astype(float)
fade_start = int(target_h * 0.82)
for y in range(fade_start, target_h):
    factor = 1.0 - ((y - fade_start) / (target_h - fade_start))
    np_a[y, :] *= factor

a_faded = Image.fromarray(np_a.astype(np.uint8))
portrait_graded.putalpha(a_faded)

# 5. Composite onto Background
canvas = bg.copy()

# Paste Wide Glow
canvas.paste(glow_wide, (pos_x - 60, pos_y - 60), glow_wide)
# Paste Tight Rim Glow
canvas.paste(glow_tight, (pos_x - 20, pos_y - 20), glow_tight)
# Paste Exact Portrait
canvas.paste(portrait_graded, (pos_x, pos_y), portrait_graded)

# 6. Add High-Tech Typography & Professor Title Badge
draw = ImageDraw.Draw(canvas)

# Try loading standard system fonts
font_title = None
font_sub = None
font_sm = None
font_paths = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/SFNS.ttf",
    "/System/Library/Fonts/Supplemental/Futura.ttc"
]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, int(bg_h * 0.052))
            font_sub = ImageFont.truetype(fp, int(bg_h * 0.032))
            font_sm = ImageFont.truetype(fp, int(bg_h * 0.024))
            break
        except Exception:
            continue

if not font_title:
    font_title = font_sub = font_sm = ImageFont.load_default()

# Overlay Name Tag on Professor Box (Cyber Holographic Badge below/near the portrait)
badge_x = pos_x - 10
badge_y = bg_h - int(bg_h * 0.12)
badge_w = target_w + 20
badge_h = int(bg_h * 0.09)

# Draw semi-transparent glass panel under name
glass_overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
glass_draw = ImageDraw.Draw(glass_overlay)
glass_draw.rounded_rectangle(
    [badge_x, badge_y, badge_x + badge_w, badge_y + badge_h],
    radius=12,
    fill=(11, 17, 32, 220),
    outline=(0, 240, 255, 180),
    width=2
)
canvas = Image.alpha_composite(canvas, glass_overlay)
draw = ImageDraw.Draw(canvas)

# Text inside badge
draw.text((badge_x + 16, badge_y + 8), "ASST. PROF. DR. CHEWA THASSANA", fill=(0, 240, 255, 255), font=font_sub)
draw.text((badge_x + 16, badge_y + 8 + int(bg_h * 0.038)), "COURSE DIRECTOR • RBRU PHYSICS", fill=(148, 163, 184, 255), font=font_sm)

# Convert to RGB and Save
final_v3 = canvas.convert("RGB")

v3_path = os.path.join(IMG_DIR, "modern_physics_banner_v3_exact_portrait.jpg")
main_banner_assets = os.path.join(IMG_DIR, "modern_physics_banner.jpg")
main_banner_book = os.path.join(BOOK_DIR, "modern_physics_banner.jpg")
v3_book = os.path.join(BOOK_DIR, "modern_physics_banner_v3_exact_portrait.jpg")

final_v3.save(v3_path, "JPEG", quality=96)
final_v3.save(main_banner_assets, "JPEG", quality=96)
final_v3.save(main_banner_book, "JPEG", quality=96)
final_v3.save(v3_book, "JPEG", quality=96)

print("Successfully generated and saved Version 3 Exact Portrait Banner!")
