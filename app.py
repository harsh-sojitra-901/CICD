import os
from flask import Flask, render_template_string, request, redirect, url_for, send_from_directory

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Pixora | Premium Stock Images</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            font-family: "Segoe UI", Arial, sans-serif;
            background: #f4f6f9;
            margin: 0;
        }

        /* NAVBAR */
        nav {
            background: #0f2027;
            padding: 15px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: white;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.5rem;
            font-weight: bold;
        }

        .brand img {
            height: 40px;
        }

        .upload-btn {
            background: #00c6ff;
            border: none;
            padding: 10px 18px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
        }

        /* HERO */
        header {
            background: linear-gradient(120deg, #203a43, #2c5364);
            color: white;
            padding: 60px 20px;
            text-align: center;
        }

        header h1 {
            font-size: 2.8rem;
        }

        /* GALLERY */
        .container {
            padding: 40px;
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 25px;
        }

        .card {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        }

        .card img {
            width: 100%;
            height: 220px;
            object-fit: cover;
        }

        .card .info {
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .download {
            background: #2c5364;
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 0.9rem;
        }

        footer {
            background: #0f2027;
            color: white;
            text-align: center;
            padding: 15px;
        }
    </style>
</head>
<body>

<nav>
    <div class="brand">
        <img src="/static/logo.png">
        Pixora
    </div>

    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="image" required>
        <button class="upload-btn">Upload Image</button>
    </form>
</nav>

<header>
    <h1>Premium Stock Images</h1>
    <p>Upload, download & use images for your creative projects</p>
</header>

<div class="container">
    <div class="gallery">
        {% for image in images %}
        <div class="card">
            <img src="/uploads/{{ image }}">
            <div class="info">
                <span>{{ image }}</span>
                <a class="download" href="/download/{{ image }}">Download</a>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

<footer>
    © 2026 Pixora | CI/CD Demo Stock Image Platform
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    images = os.listdir(app.config["UPLOAD_FOLDER"])
    return render_template_string(HTML_PAGE, images=images)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"]
    if file:
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
    return redirect(url_for("home"))

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
