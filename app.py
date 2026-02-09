from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Stockify | Premium Stock Images</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: "Segoe UI", Arial, sans-serif;
            background-color: #f5f7fa;
            color: #333;
        }

        /* ---------- HEADER ---------- */
        header {
            background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
            color: white;
            padding: 70px 20px;
            text-align: center;
        }

        header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
        }

        header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .search-box {
            margin-top: 30px;
        }

        .search-box input {
            width: 60%;
            max-width: 500px;
            padding: 14px;
            border-radius: 30px;
            border: none;
            outline: none;
            font-size: 1rem;
        }

        /* ---------- CATEGORIES ---------- */
        .categories {
            display: flex;
            justify-content: center;
            gap: 15px;
            padding: 30px 10px;
            flex-wrap: wrap;
        }

        .category {
            background: white;
            padding: 10px 20px;
            border-radius: 20px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            cursor: pointer;
            transition: 0.3s;
            font-weight: 500;
        }

        .category:hover {
            background: #2c5364;
            color: white;
        }

        /* ---------- GALLERY ---------- */
        .container {
            padding: 20px 40px 60px;
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 25px;
        }

        .card {
            position: relative;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            transition: transform 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);
        }

        .card img {
            width: 100%;
            height: 230px;
            object-fit: cover;
        }

        .overlay {
            position: absolute;
            inset: 0;
            background: rgba(0,0,0,0.45);
            opacity: 0;
            transition: 0.3s;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 15px;
            color: white;
        }

        .card:hover .overlay {
            opacity: 1;
        }

        .overlay h3 {
            margin-bottom: 10px;
        }

        .overlay button {
            padding: 10px;
            border: none;
            border-radius: 6px;
            background: #00c6ff;
            color: black;
            font-weight: bold;
            cursor: pointer;
        }

        .overlay button:hover {
            background: #00a3cc;
        }

        /* ---------- FOOTER ---------- */
        footer {
            background: #0f2027;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

<header>
    <h1>📸 Stockify</h1>
    <p>Premium stock images for designers, developers & creators</p>

    <div class="search-box">
        <input type="text" placeholder="Search images, categories, keywords...">
    </div>
</header>

<div class="categories">
    <div class="category">Nature</div>
    <div class="category">Business</div>
    <div class="category">Technology</div>
    <div class="category">People</div>
    <div class="category">Travel</div>
</div>

<div class="container">
    <div class="gallery">

        <div class="card">
            <img src="https://picsum.photos/id/1018/600/400">
            <div class="overlay">
                <h3>Mountain View</h3>
                <button>Download</button>
            </div>
        </div>

        <div class="card">
            <img src="https://picsum.photos/id/1024/600/400">
            <div class="overlay">
                <h3>Wildlife</h3>
                <button>Download</button>
            </div>
        </div>

        <div class="card">
            <img src="https://picsum.photos/id/1031/600/400">
            <div class="overlay">
                <h3>City Life</h3>
                <button>Download</button>
            </div>
        </div>

        <div class="card">
            <img src="https://picsum.photos/id/1043/600/400">
            <div class="overlay">
                <h3>Nature Waterfall</h3>
                <button>Download</button>
            </div>
        </div>

        <div class="card">
            <img src="https://picsum.photos/id/1050/600/400">
            <div class="overlay">
                <h3>Beach Travel</h3>
                <button>Download</button>
            </div>
        </div>

        <div class="card">
            <img src="https://picsum.photos/id/1060/600/400">
            <div class="overlay">
                <h3>Technology Workspace</h3>
                <button>Download</button>
            </div>
        </div>

    </div>
</div>

<footer>
    © 2026 Stockify | Professional CI/CD Demo Application
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
