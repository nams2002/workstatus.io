Overview
The WorkStatus Python Agent is a desktop application designed to track user activity, capture screenshots, and upload the relevant data to Amazon S3 or a similar cloud storage service. The application is highly configurable and features secure file handling, time zone management, and error resilience.

Features
Activity Tracking: Monitors user input, differentiating between genuine activity and emulated scripts.
Configurable Screenshot Capture: Allows users to configure intervals for screenshot captures and whether they should be blurred or clear.
Data Upload: Automatically uploads activity logs and screenshots to cloud storage (e.g., Amazon S3).
Error Handling & Resilience: Handles network failures, firewall issues, and unexpected disconnections gracefully.
Time Zone Management: Detects and logs system time zone changes.
Memory Optimization: Compresses screenshots before uploading and deletes old files to save space.
Instance Management: Ensures only one instance of the application is running.
Optional Features
Auto-Update Mechanism: Automatically checks for and applies updates.
Low Battery Detection: Detects low battery on laptops and pauses activity tracking to save power.
Advanced Security: Multi-factor authentication for configuration changes.
Setup and Installation
Prerequisites
Ensure you have the following installed:

Python 3.x: Download Python
Virtualenv (optional but recommended for managing dependencies).
Libraries/Dependencies
You can install the necessary dependencies with the following:

pip install -r requirements.txt
Here is a list of the key libraries used:

Flask: A lightweight WSGI web application framework.
Boto3: Amazon Web Services SDK for Python (used to interact with S3).
Pillow: Python Imaging Library (PIL) to process images.
Cryptography: Library to handle encryption.
LiveKit, OpenAI, Silero: For advanced AI functionalities.
Running the Application
Clone the Repository:

git clone https://github.com/your-repo/workstatus-python-agent.git
cd workstatus-python-agent
Create a Virtual Environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:


pip install -r requirements.txt
Set Up Environment Variables: Create a .env file in the root directory to store your AWS credentials and other sensitive information. Example:


AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
S3_BUCKET_NAME=your-s3-bucket
Running the Flask Application:

python agent.py
Testing with Postman:

Open Postman, create a new HTTP request (POST), and target the appropriate routes for uploading files or interacting with the agent.
Use http://127.0.0.1:5000/upload as the URL (or your respective URL).
Configuration
The application allows configuration changes to be polled from a web application, including:

Screenshot Interval: Customize the time interval (in minutes) for capturing screenshots.
Screenshot Type: Choose between blurred and clear screenshots.
Upload Settings: Configure cloud upload options for data integrity and security.
Dummy Data for Testing
You can use the dummy_files/ directory to add sample log files, images, or JSON data to test the application's upload functionality.

Optional Features and Advanced Functionalities
Auto-Update: The agent will check for updates on each run and download them automatically without user intervention.
Low Battery Detection: The agent will pause activity tracking when it detects a low battery state on laptops.
Enhanced Security: Multi-factor authentication (MFA) can be enabled for users to make changes to the agent’s configuration securely.
Error Handling
The agent has built-in error handling to manage:

Network disconnections: It will retry uploads once the connection is restored.
Application crashes: It ensures data integrity and avoids corruption on sudden application exits.
Firewall issues: Provides user-friendly error messages when network activity is blocked by a firewall.
Directory Structure

/workstatus-python-agent
    /dummy_files              # Folder for test files (images, logs)
    /uploads                  # Folder where uploaded screenshots/logs are stored
    agent.py                  # Main application script
    compression.py            # Handles file compression
    encryption.py             # Handles file encryption
    requirements.txt          # List of dependencies
    README.md                 # This file
    .env                      # Environment variables for AWS credentials (not included in repo)
Known Issues and Limitations
Windows OS Support: Some functionalities like low-battery detection might not work properly on non-laptop Windows systems.
Network Timeouts: Large files may take longer to upload depending on internet speed.
Contributing
We welcome contributions! Feel free to open a pull request or report issues.

License
This project is licensed under the MIT License. See the LICENSE file for details.
