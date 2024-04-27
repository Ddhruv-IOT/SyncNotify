# SyncNotify

![Automation](https://img.shields.io/badge/Automation-Yes-blue.svg) ![Python Version](https://img.shields.io/badge/Python-3.9.1-blue.svg) ![Maintained](https://img.shields.io/badge/Maintained-Yes-green.svg) ![Stars](https://img.shields.io/github/stars/ddhruv-iot/SyncNotify.svg?style=social)

## Overview

SyncNotify is an instant laptop notification system designed to keep you connected to your device's activities in real-time. With just a simple Python script, SyncNotify sends instant notifications to your smartwatch the moment your laptop springs to life.

## Features

- Instant notification to your smartwatch upon laptop power-up
- Seamless integration with Telegram API and Bluetooth connectivity

## Tools and Technologies Used

- Python
- Telegram API
- Bluetooth connectivity

## Working

SyncNotify's Python script activates upon laptop power-up, waits for an active internet connection, and then utilizes the Telegram API to send a notification to your smartphone. The notification is then flashed on your smartwatch via Bluetooth.

## Getting Started

To get started with SyncNotify, follow the steps:

1. **Clone the Repository:**
   
   ```bash
   git clone https://github.com/Ddhruv-IOT/SyncNotify
   cd SyncNotify
   ```

2. **Install the dependencies**
   
   ```bash
   pip install -r requirements.py
   ```

3. **Move to Startup Folder**
   
   Copy all the python files with `.py` extension to the start-up apps location, generally found on this address:
   > C:\Users\<user-name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup



## How to Contribute

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## LinkedIn Post Link and Demo Video

[LinkedIn Post](https://www.linkedin.com/posts/ddhruv-arora_syncnotify-innovation-ddhruvarora-activity-7189643019401183235-pTft?utm_source=share&utm_medium=member_desktop)

[Demo Video](https://www.instagram.com/reel/C6O8cesvba0/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)


## Upcoming Features

- Reduced dependency on smartphones for standalone functionality.
- Capture and send photos of laptop activity to your smartphone

## Thank You

Thank you for checking out SyncNotify! We hope it enhances your productivity and keeps you connected to your device's activities seamlessly.
