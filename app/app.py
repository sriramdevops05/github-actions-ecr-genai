from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "CI/CD Pipeline Demo", 
                    "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Step 6** → Scroll down → Click **"Commit changes"**

**Step 7** → Click **"Commit changes"** again to confirm

---

## Then Create `app/test_app.py`

**Step 1** → Click **"Add file"** → **"Create new file"**

**Step 2** → Type in filename box:
```
app/test_app.py
