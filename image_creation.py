import os
import matplotlib.pyplot as plt
import logging

def save_table_as_image(df, instructor_name, instructor_email, directory, width_ratio, height_ratio):
    """Save the DataFrame as an image in a specified directory."""
    try:
        logging.info(f"Saving table for {instructor_name} to image")

        # Calculate dimensions for the image
        num_rows, num_columns = df.shape
        width = num_columns * width_ratio
        height = num_rows * height_ratio

        # Create a matplotlib figure and axis
        fig, ax = plt.subplots(figsize=(width, height))
        ax.axis('tight')  # Remove extra space around the table
        ax.axis('off')    # Hide the axis

        # Create a table from the DataFrame
        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
        table.auto_set_font_size(False)  # Disable automatic font size adjustment
        table.set_fontsize(10)           # Set font size
        table.scale(1, 2)                # Scale the table

        # Apply alternating row colors
        colors = ['#f2f2f2', '#e6e6e6']
        for i, key in enumerate(table.get_celld().keys()):
            cell = table.get_celld()[key]
            if key[0] == 0:  # Header row
                cell.set_fontsize(12)
                cell.set_text_props(weight='bold')
                cell.set_facecolor('#4CAF50')  # Header background color
                cell.set_text_props(color='white')  # Header text color
            else:
                cell.set_facecolor(colors[i % 2])  # Alternating row colors

        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Save the table as an image
        img_path = os.path.join(directory, f"{instructor_name}_{instructor_email}_table.png")
        plt.savefig(img_path, bbox_inches='tight', dpi=300)

        return img_path  # Return the image path

    except Exception as e:
        logging.error(f"An error occurred while saving the image: {e}")
