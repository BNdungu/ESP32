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

### Step 3: flash micropython

1. Start up thonny IDE.
2. Click on tools.
3. Options ...
4. Click on the Interprator tab.
5. On the section "Which interpreter or device should Thonny use for running the code" select "Micropython(ESP32)".
6. In the "Port or WebREPL" section, select the port connected to you mounted ESP32 board.
7. Click on "Install or update firmware".
8. Select the usb port you ESP32 board is mounted at in the PORT section.
9. In the firmware part click on browse to select the downloaded micropython file in your computer's Downloads folder.
10. Check the Erase flash before installing check box and finnaly click on install.
