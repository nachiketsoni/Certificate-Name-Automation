

# Certificate-Name-Automation

The Certificate-Name-Automation is a Python program that allows you to apply customized text to multiple certificate images. You can specify the text, font, font size, text color, and position for each certificate. The modified certificates are saved as separate files.

## Prerequisites

- Python 3.x
- Pillow (PIL) library
```bash
pip install pillow
```
- EasyGUI library
```bash
pip install easygui
```

## How to Use

1. **Clone or Download the Repository**

   Clone this repository to your local machine or download the ZIP file and extract it to a folder.

2. **Run the Program**

   Open a terminal or command prompt, navigate to the folder where you extracted the program files, and run the following command:

   ```bash
   python Certificate_Name_Maker.py
   ```

3. **Step 1: Select Certificate Images**

   - Click the "Select Certificate Images" button to choose one or more certificate images (PNG, JPG, JPEG, BMP, GIF).

4. **Step 2: Select Font File**

   - Click the "Select Font File" button to choose a TrueType Font (TTF) or OpenType Font (OTF) file.

5. **Step 3: Enter Certificate Details**

   - In the dialog box that appears, enter the following details for the certificates:
     - Name: The text you want to apply to the certificates.
     - Font Size: The size of the font.
     - Text Color: The color of the text (e.g., 'black', 'red', '#FF0000').
     - X Position: The horizontal position of the text.
     - Y Position: The vertical position of the text.

6. **Step 4: Apply Changes**

   - Click the "OK" button in the dialog box to apply the specified changes to the selected certificate images.

7. **Step 5: View Modified Certificates**

   - The modified certificates are saved in the same folder as the originals with "_Modified" added to their filenames.

8. **Step 6: Repeat for More Certificates**

   - You can repeat the process for more certificate images by clicking "Select Certificate Images" again and specifying the details.

9. **Step 7: Exit the Program**

   - Click the "Cancel" button in the dialog box to exit the program.

## Sample Usage

- You can use this program to quickly add names or other text to certificates for various events, such as awards, recognition, or completion certificates.

## License

This program is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This program uses the Pillow (PIL) and EasyGUI libraries to process images and create the user interface.
```

You can save this content as a README.md file in your project directory for users to refer to when using your program.
