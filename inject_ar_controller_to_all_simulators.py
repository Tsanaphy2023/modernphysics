#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Injects ar_mediapipe_controller.js into all 40 simulator HTML files in simulators/
Ensures every single simulation has the touchless AR MediaPipe hand control bar!
"""

import os
import glob

SIM_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/simulators"
files = glob.glob(os.path.join(SIM_DIR, "sim_*.html"))

injected_count = 0
for fpath in sorted(files):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if "ar_mediapipe_controller.js" not in content:
        # Inject right before </body>
        new_content = content.replace("</body>", "  <script src=\"ar_mediapipe_controller.js\"></script>\n</body>")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        injected_count += 1
        print(f"✅ Injected AR controller into {os.path.basename(fpath)}")
    else:
        print(f"ℹ️ Already present in {os.path.basename(fpath)}")

print(f"🎉 Successfully injected AR MediaPipe controller into {injected_count} simulator files (Total: {len(files)})!")
