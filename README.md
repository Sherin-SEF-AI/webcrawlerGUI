# webcrawlerGUI
python application for WebCrawler 
# Web Crawler Application

## Overview
This application is a web crawler built using Python and `customtkinter` for the graphical user interface (GUI). It allows users to crawl a website up to a specified depth, filter links by domain, and save the results as a text or CSV file. The application supports pausing, resuming, and stopping the crawling process.

## Features
- **Crawl Websites**: Enter a URL and depth to start crawling.
- **Domain Filtering**: Filter the crawled links by a specific domain.
- **Pause/Resume/Stop**: Control the crawling process with pause, resume, and stop functionalities.
- **Save Results**: Save the crawled URLs as a TXT or CSV file.
- **GUI Interface**: Easy-to-use interface built with `customtkinter`.

## Requirements
- Python 3.10 or higher
- `requests`
- `beautifulsoup4`
- `customtkinter`

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/web-crawler-app.git
   cd webcrawlerGUI

pip install requests beautifulsoup4 customtkinter

Usage
Run the application:

sh
Copy code
python webcrawlerGUI.py
Using the GUI:

Enter URL: Type the URL you want to crawl.
Depth: Specify the depth for crawling.
Filter by Domain: Enter a domain to filter the crawled URLs (optional).
Crawl: Click the "Crawl" button to start the crawling process.
Pause: Click the "Pause" button to pause the crawling.
Resume: Click the "Resume" button to resume crawling.
Stop: Click the "Stop" button to stop the crawling process.
Save as TXT: Click the "Save as TXT" button to save the results in a TXT file.
Save as CSV: Click the "Save as CSV" button to save the results in a CSV file.
Troubleshooting
Error: "User-Agent": Ensure the correct User-Agent string is being used in the requests.
AttributeError: 'config' is not implemented for CTk widgets. Use configure instead of config for changing properties of customtkinter widgets.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
This project uses requests for HTTP requests.
Beautiful Soup is used for parsing HTML content.
customtkinter is used for the GUI.
