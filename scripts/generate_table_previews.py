"""
WSL Data Hub - Table Preview PNG Generator
Generates high-resolution PNG image previews of the first 35 rows for all CSV datasets.
"""

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
LCL_DIR = os.path.join(BASE_DIR, "data", "teams", "london_city_lionesses")
PREVIEWS_DIR = os.path.join(BASE_DIR, "assets", "images", "previews")

os.makedirs(PREVIEWS_DIR, exist_ok=True)

def render_dataframe_to_png(df: pd.DataFrame, title: str, output_path: str, max_rows: int =40):
    """
    Renders a DataFrame subset (up to max_rows) as a clean, styled PNG image card.
    """
    subset = df.head(max_rows).copy()
    
    # Format floating numbers cleanly
    float_cols = subset.select_dtypes(include=['float64', 'float32']).columns
    for c in float_cols:
        subset[c] = subset[c].round(2)

    num_rows, num_cols = subset.shape
    
    # Calculate figure dimensions dynamically
    fig_width = max(16, num_cols * 1.2)
    fig_height = max(8, num_rows * 0.35 + 1.5)
    
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=150)
    ax.axis('off')
    
    # Title header
    plt.title(f"Dataset Preview: {title} (First {min(max_rows, num_rows)} rows)", 
              fontsize=16, fontweight='bold', pad=20, color='#00e676')

    # Draw table
    table_data = [subset.columns.tolist()] + subset.values.tolist()
    tbl = ax.table(cellText=table_data, loc='center', cellLoc='center')
    
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    tbl.scale(1.0, 1.4)
    
    # Style table cells (Dark theme)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            # Header styling
            cell.set_facecolor('#1a2633')
            cell.set_text_props(weight='bold', color='#ffffff')
        else:
            # Alternating row colors
            bg_color = '#0f172a' if r % 2 == 0 else '#1e293b'
            cell.set_facecolor(bg_color)
            cell.set_text_props(color='#cbd5e1')
            
        cell.set_edgecolor('#334155')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', facecolor='#0b1329')
    plt.close(fig)
    print(f"Generated Table Preview PNG: {os.path.basename(output_path)}")

def main():
    print("=== Generating High-Res Table Previews (35 Rows) ===")
    
    csv_files = glob.glob(os.path.join(RAW_DIR, "*.csv")) + glob.glob(os.path.join(LCL_DIR, "*.csv"))
    print(f"Found {len(csv_files)} CSV datasets to render.")
    
    for filepath in csv_files:
        try:
            filename = os.path.basename(filepath)
            title = filename.replace(".csv", "")
            out_png = os.path.join(PREVIEWS_DIR, f"{title}_preview.png")
            
            df = pd.read_csv(filepath)
            render_dataframe_to_png(df, title, out_png, max_rows=35)
            
        except Exception as e:
            print(f"❌ Error rendering {filepath}: {e}")

    print("\n=== Table Previews Generation Complete! ===")

if __name__ == "__main__":
    main()
