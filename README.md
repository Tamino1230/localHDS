# LocalHDS (Local Host-Domain-Switch) by [Tamino1230](https://discord.com/users/702893526303637604)

LocalHDS is a Python-based program designed to manage and automate local host-domain settings. It allows you to add, remove, and manage local domains and IPs, as well as generate Flask-based web servers with customizable URL paths.

## Features

- Domain Management:
  - Add or remove domains and IPs.
  - List all active local domains.
- Logging:
  - View event logs.
  - Save logs for later use.
- Website Generation:
  - Add and remove URL paths for dynamic web server creation.
  - Automatically generate Flask web servers and basic HTML files.
- User-Friendly Menu:
  - Easy-to-navigate menu for selecting various options.

## Installation

1. Requirements:
   - Python 3.x
   - Dependencies:
     - flask
     - requests

   Install dependencies with:
  ```
  pip install flask requests
  ```

3. Clone the Repository:
   ```
   git clone https://github.com/Tamino1230/localHDS.git
   cd localHDS
   ```

4. Host File Path:
   The default host file path is set for Windows (C:\Windows\System32\drivers\etc\hosts). Update the HOST_PATH variable in the code for your operating system if needed.

## Usage

1. Run the Program:
   ```python main.py```

2. Menu Options:
   - 1: Change the local domain URL.
   - 2: Add a new domain and IP entry.
   - 3: Remove an existing domain and IP entry.
   - 4: List all active local domains.
   - 5: View log history.
   - 6: Save log history to a file.
   - 7: Add a new page (URL path).
   - 8: Remove an existing page (URL path).
   - 9: Show all existing pages.
   - 10: Generate Flask server files.
   - 11: Start the last generated server file.

3. Website Generation:
   - Add URL paths (e.g., /page) to define routes for the Flask server.
   - The program will generate Flask server files and basic HTML templates in the templates directory.

## Directory Structure

```localHDS/
│
├── assets/
│   ├── inputer.py       # Input functions and menus
│   ├── handler.py       # Error handling functions
│   ├── domain.py        # Domain management functions
│   ├── logs.py          # Logging functions
│   ├── generate.py      # Flask server and HTML generator
│
├── templates/           # Generated HTML templates
│
├── main.py              # Main program entry point
```

## Notes

- Some functions require administrator privileges (e.g., modifying the host file). Ensure you run the program with elevated permissions.
- Update the HOST_PATH, IP, and DOMAIN variables to suit your configuration.

## License

This project is licensed under the MIT License.

## Acknowledgments

Developed by [Tamino1230](https://discord.com/users/702893526303637604).

## My Socials:
- [Discord](https://discord.com/users/702893526303637604)
- [Twitter](https://twitter.com/NukeTamino)
- [GitHub](https://github.com/tamino1230)
