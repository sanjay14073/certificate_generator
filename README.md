# Certificate Generator

This Python project generates personalized certificates from a template image using participant names from an Excel file.

## Features
- Reads participant names from an Excel file.
- Creates personalized certificates using a template image.
- Automatically saves certificates in an output directory.

## Prerequisites
- Python 3.x installed on your system.
- Necessary Python libraries installed (see below).

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the following files in the project folder:
   - **`participants.xlsx`**: An Excel file containing participant names in a column named `name`.
   - **`certificate.png`**: The certificate template image with a blank area for the participant name.
   - **`arial.ttf`**: The font file used to render participant names.

## Usage

1. Run the script:
   ```bash
   python generate_certificates.py
   ```

2. The personalized certificates will be saved in the `certificates/` directory.

## File Structure

```
.
├── participants.xlsx         # Excel file with participant names
├── certificate.png           # Certificate template image
├── generate_certificates.py  # Main script
├── certificates/             # Directory where output certificates are saved
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## Customization

- **Template Positioning**: Adjust the `x` and `y` values in the script for correct placement of the name on the certificate.
- **Font**: Replace `arial.ttf` with any desired font file.
- **Font Size & Color**: Modify `font_size` and `font_color` variables in the script.

## Dependencies

The project requires the following Python libraries:
- pandas
- Pillow

These are listed in the requirements.txt file.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project.

Happy coding! 😊
