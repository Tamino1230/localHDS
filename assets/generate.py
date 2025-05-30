
import time
import os

def generate(filename, liste: list):
    def clear_file(filename):
        with open(filename, "w") as file:
            file.write("")

    def start_flask_generate(filename):
        with open(filename, "a") as file:
            file.write("\nfrom flask import Flask, render_template\n\napp = Flask(__name__)\n")

    def web_urls_generate(filename, liste: list):
        with open(filename, "a") as file:
            for url_path in liste:
                url_path_function = url_path.strip("/")
                if url_path_function == "":
                    url_path_function = "index"
                file.write(f"\n@app.route('{url_path}')\ndef function{url_path_function.replace("/", "")}():\n    return render_template(\"{url_path_function.replace("/", "")}.html\")\n")
                print(f"Created URL path Function: {url_path_function}")

    def html_generate(folderpath, liste: list):
        for filename in liste:
            filename = filename.strip("/")
            if filename == "":
                filename = "index"
            filename = filename + ".html"
            filename = filename.replace("/", "")
            pfad = os.path.join(os.getcwd() + "\\" + folderpath, filename)
            with open(pfad, "a") as f:
                f.write(f"HTML File {filename}.\n")
                print(f"Created {filename}")

    def finish_generate(filename):
        with open(filename, "a") as file:
            file.write("\napp.run(debug=False, host='0.0.0.0', port=80)")

    clear_file(filename)
    start_flask_generate(filename)
    web_urls_generate(filename, liste)
    html_generate("templates", liste)
    finish_generate(filename)
