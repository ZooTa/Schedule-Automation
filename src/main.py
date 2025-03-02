import json
from data_processing import load_data, preprocess_data
from image_creation import save_table_as_image
from messaging import send_whatsapp_schedule

def load_config(config_file):
    """Load configuration settings from a JSON file."""
    with open(config_file, 'r') as file:
        return json.load(file)

def main():
    # Load configuration
    config = load_config('../config/config.json')

    # Load data from the specified file
    df = load_data(config['file_path'])
    if df is None:
        return

    # Extract configuration settings
    alias_mapping = config['alias_mapping']
    desired_columns = config['desired_columns']

    # Preprocess the data
    schedule_df = preprocess_data(df, alias_mapping, desired_columns)
    if schedule_df is None:
        return

    # Extract additional configuration settings
    directory = config['output_directory']
    width_ratio = config['width_ratio']
    height_ratio = config['height_ratio']

    # Get unique emails from the DataFrame
    unique_emails = schedule_df['Email'].unique()

    # Loop through each unique email to process data
    for email in unique_emails:
        instructor_df = schedule_df.query('Email == @email')

        if not instructor_df.empty:
            # Save the table as an image
            instructor_name = instructor_df.Instructor_Name.iloc[0]
            img_path = save_table_as_image(instructor_df, instructor_name, email, directory, width_ratio, height_ratio)

            if img_path:
                # Send the image via WhatsApp
                phone_number = instructor_df.Phone_Number.iloc[0]
                message = config['message']
                send_whatsapp_schedule(phone_number, img_path, message)


if __name__ == "__main__":
    main()
