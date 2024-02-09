# MED-Punctual

Brief description of what the project does and its purpose.

## Description

More detailed information about your project. You can discuss the project's functionality, its use case, how it leverages Azure Custom Vision, the significance of the 3D models, and the role of the ESP32 module with RTC.

## Getting Started

### Dependencies

- Python 3.8 (for `azure_custom_vision.py`)
- ESP32 Development Board
- Arduino IDE for ESP32 programming (`time_module_esp32.ino`)
- Any necessary libraries for 3D printing software to handle the models in the `3D Models` folder
- An Azure account with Custom Vision Service set up for the Python script

### Installing

#### Software

1. **Clone the Project:**
   - First, clone the repository to your local machine:
     ```shell
     git clone https://github.com/nihalbaig0/MED-Punctual.git
     cd MED-Punctual
     ```

2. **Python Environment Setup:**
   - Ensure Python is installed on your system.
   - Create a virtual environment in the project directory:
     ```shell
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```shell
       .\venv\Scripts\activate
       ```
     - On Unix or MacOS:
       ```shell
       source venv/bin/activate
       ```
   - Install required Python libraries using the `requirements.txt` file:
     ```shell
     pip install -r requirements.txt
     ```
    
3. **Arduino Environment Setup:**
   - Install the [Arduino IDE](https://www.arduino.cc/en/software) compatible with your system.
   - Follow the instructions to install the ESP32 board into your Arduino IDE: [ESP32 Board Installation Guide](https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/)
   - Install the [RTC](https://github.com/Makuna/Rtc/wiki) library via the Arduino Library Manager.

#### Hardware

- Prepare your ESP32 development board and any necessary connections to the RTC module as required by `time_module_esp32.ino`.

![diagram](diagram.png)

### Running the Project

1. **Azure Custom Vision Python Script:**
   - Before running `azure_custom_vision.py`, ensure you have set up your Azure Custom Vision project and have your endpoint and keys ready.

   ```
   ENDPOINT = ""      
   PREDICTION_KEY = ""
   PROJECT_ID = ""
   MODEL_NAME = ""

   ```
   - Update `azure_custom_vision.py` with your specific Azure Custom Vision project details.
   - Run the script:
     ```shell
     streamlit run azure_custom_vision.py
     ```

2. **ESP32 Time Module:**
   - Open `time_module_esp32.ino` in the Arduino IDE.
   - Select the correct port and board (ESP32) under Tools.
   - Upload the code to your ESP32.

3. **3D Models:**
   - The `3D Models` folder contains all models necessary for this project. Use compatible 3D printing software to open and print these models.

## Contributing

If you'd like to contribute to the project, please fork the repository and create a pull request with your changes. You're also welcome to submit issues for any bugs found or features suggested.

## License

This project is licensed under the [INSERT LICENSE HERE] License - see the LICENSE.md file for details.

## Acknowledgments

- Mention any inspirations, code snippets, etc.
- Any collaborators or contributors
- External resources or communities that helped

