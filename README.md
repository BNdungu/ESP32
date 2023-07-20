# ESP32

## Thonny IDE Setup

Thonny IDE is a beginner-friendly Python Integrated Development Environment (IDE) that allows you to write and run Python code easily. Follow these steps to set up Thonny on your computer:

### Step 1: Download Thonny

1. Go to the Thonny website: https://thonny.org/
2. Click on the "Download" link in the navigation menu.

### Step 2: Choose the Appropriate Version

1. If you're using Windows, click on the "Windows installer" link to download the Windows version.
2. For macOS, click on the "macOS installer" link.
3. For Linux users, select the appropriate package for your distribution (e.g., Debian, Ubuntu, Fedora).

### Step 3: Install Thonny

1. Windows:
   - Double-click the downloaded installer (e.g., `thonny-3.3.7.exe`).
   - Follow the on-screen instructions to install Thonny.
   - Once the installation is complete, you should find Thonny in the Start menu.

2. macOS:
   - Open the downloaded `.dmg` file (e.g., `thonny-3.3.7.dmg`).
   - Drag the Thonny icon into the Applications folder.
   - Thonny is now installed and available in your Applications folder.

3. Linux:
   - Open a terminal window.
   - Navigate to the directory where you downloaded the Thonny installer.
   - Install Thonny using the package manager for your distribution (e.g., `apt`, `dnf`, `yum`, etc.).

## MicroPython Setup for ESP32

MicroPython is a lightweight implementation of the Python programming language optimized for microcontrollers like the ESP32. Here's how to flash MicroPython onto your ESP32 board:

### Step 1: Download MicroPython Firmware

1. Go to the MicroPython website: https://micropython.org/download/esp32/
2. Download the appropriate MicroPython firmware for your ESP32 board. Choose the stable version for better reliability.

### Step 2: Connect ESP32 to Your Computer

1. Plug the ESP32 board into your computer using a USB cable. Make sure it is properly connected.

### Step 3: Install esptool

1. Open a terminal or command prompt on your computer.
2. Install the `esptool` utility using pip (Python package manager):
    ``` python 
        pip install esptool

### Step 4: Erase Flash Memory (Optional but Recommended)

1. To ensure a clean flash, erase the ESP32's flash memory by running the following command:
    ``` python 
        esptool.py --chip esp32 erase_flash


### Step 5: Flash MicroPython Firmware

1. Change the path in the command below to the location where you downloaded the MicroPython firmware:
    ``` python 
        esptool.py --chip esp32 --port <port> write_flash -z 0x1000 <path_to_firmware>


- Replace `<port>` with the serial port of your ESP32 board (e.g., `COM1` on Windows, `/dev/ttyUSB0` on Linux).
- `<path_to_firmware>` should be the path to the MicroPython firmware you downloaded.

### Step 6: Access MicroPython REPL

1. After flashing, unplug and re-plug the ESP32 board to reset it.
2. Open Thonny IDE.
3. Click on the "View" menu, then select "Shell" to open the Python Shell.
4. In the Shell, select the correct serial port for the ESP32 board (e.g., `/dev/ttyUSB0`).
5. Click the "Connect" button to access the MicroPython REPL (Read-Eval-Print Loop).

You're now ready to start writing and running MicroPython code on your ESP32 using Thonny IDE!


