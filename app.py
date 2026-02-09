
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Stock Image Store</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #111;
            color: white;
            padding: 15px;
            text-align: center;
        }
        .container {
            padding: 20px;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        .card {
            background: white;
            border-radius: 6px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            overflow: hidden;
            text-align: center;
        }
        .card img {
            width: 100%;
            height: 150px;
            object-fit: cover;
        }
        .card p {
            padding: 10px;
            font-weight: bold;
        }
        footer {
            background: #111;
            color: white;
            text-align: center;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<header>
    <h1>📸 Stock Image Store</h1>
    <p>High quality images for your projects</p>
</header>

<div class="container">
    <div class="gallery">
        <div class="card">
            <img src="https://picsum.photos/id/1015/400/300">
            <p>Nature Landscape</p>
        </div>
        <div class="card">
            <img src="https://picsum.photos/id/1025/400/300">
            <p>Wildlife</p>
        </div>
        <div class="card">
            <img src="https://picsum.photos/id/1035/400/300">
            <p>City Life</p>
        </div>
        <div class="card">
            <img src="https://picsum.photos/id/1045/400/300">
            <p>Mountains</p>
        </div>
    </div>
</div>

<footer>
    <p>© 2026 Stock Image Store | CI/CD Demo App</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
