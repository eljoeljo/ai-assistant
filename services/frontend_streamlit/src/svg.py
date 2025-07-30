from pathlib import Path
def svg_paths():
    # -Avatars- 
    HERE = Path(__file__).resolve().parent
    ROOT = HERE.parent
    SVG_DIR = ROOT / "svg_files"
    robot_svg = SVG_DIR / "robot-svgrepo-com.svg"  # Relative Path for AI SVG
    user_svg = SVG_DIR / "user-svgrepo-com.svg"  # Relative Path for User SVG
    
    paths = [robot_svg,user_svg]
    return paths