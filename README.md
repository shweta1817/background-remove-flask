
# Background Remover Web App

This is a simple and responsive web application that allows users to upload an image and remove its background using Python and Flask. The result is displayed on the page and can be downloaded. The UI is styled using Tailwind CSS and the app includes a loading animation while the background is being removed.

---

## 🚀 Features

- ✅ Upload an image (JPG, PNG)
- ✅ Remove image background with one click
- ✅ View both original and background-removed images
- ✅ Download the output image
- ✅ Responsive design (Mobile-friendly)
- ✅ Stylish layout using Tailwind CSS with black & purple theme
- ✅ Spinner shown while processing

---

## 🧰 Tech Stack

| Layer       | Technology       | Why Used                                   |
|-------------|------------------|---------------------------------------------|
| Frontend    | HTML, TailwindCSS, JavaScript | For responsive and modern UI                |
| Backend     | Python, Flask     | Lightweight server to handle uploads/process |
| Image Logic| `rembg` Python lib | To remove background from the image          |
| Deployment  | GitHub + Render   | GitHub for version control, Render for live hosting |

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/shweta1817/background-remover.git
cd background-remover
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Flask server

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to use the app locally.

---

## 📂 Folder Structure

```
background-remover/
│
├── static/
│   └── uploads/               # Stores uploaded and processed images
│
├── templates/
│   └── index.html             # Main HTML template with Tailwind CSS
│
├── app.py                     # Flask server and background remover logic
├── requirements.txt           # Python dependencies
└── README.md                  # Project info and instructions
```

---

## 🌐 Deployment

### Step-by-step:

1. Push code to GitHub.
2. Create a **Web Service** on [Render](https://render.com/).
3. Set the **Start Command** to:
   ```bash
   gunicorn app:app
   ```
4. Set the **Build Command** to:
   ```bash
   pip install -r requirements.txt
   ```
5. Set **Python 3** as your environment.
6. Click deploy — your site is live!

---

## 📸 Screenshot

> Add your own screenshot here using:

```markdown
![Screenshot](link-to-image)
```

---

## 🙌 Author

Created with ❤️ by [Shweta Bandawane](https://github.com/shweta1817)  
Web Devloper | PHP | Python

---

## 📃 License

This project is licensed under the [MIT License](LICENSE)
