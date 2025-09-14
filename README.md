# wine-quality-prediction-app
A Streamlit web application that predicts wine quality using machine learning. Includes data preprocessing, model training (Random Forest), and interactive visualizations using Matplotlib and Plotly. Users can input wine chemical properties and instantly get quality predictions, along with graphical insights about the dataset.
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Wine Quality Prediction App — README</title>
  <style>
    :root{
      --bg:#0f1724; --card:#0b1220; --muted:#9aa6b2; --accent:#ff6b6b; --accent2:#6bcBFF;
      --panel:#0b1220; --glass: rgba(255,255,255,0.03);
      --mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    }
    html,body{height:100%; margin:0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; background: linear-gradient(180deg,#071226 0%, #081725 100%); color:#e6eef6;}
    .wrap{max-width:980px;margin:36px auto;padding:28px;border-radius:12px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); box-shadow: 0 6px 28px rgba(2,6,23,0.6); border:1px solid rgba(255,255,255,0.03)}
    header{display:flex;gap:18px;align-items:center}
    .logo{
      width:72px;height:72px;border-radius:10px;
      background:linear-gradient(135deg,var(--accent),var(--accent2));
      display:flex;align-items:center;justify-content:center;font-weight:700;color:#061221;font-size:28px;
      box-shadow: 0 6px 18px rgba(107,203,255,0.08);
    }
    h1{margin:0;font-size:22px}
    p.lead{margin:6px 0 18px;color:var(--muted)}
    .row{display:flex;gap:18px;flex-wrap:wrap;margin-top:18px}
    .card{background:var(--panel); padding:16px;border-radius:10px;flex:1;min-width:260px;border:1px solid rgba(255,255,255,0.02)}
    pre.cmd{background:linear-gradient(90deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); padding:12px;border-radius:8px;color:#cfe9ff;font-family:var(--mono);font-size:13px;overflow:auto}
    code.inline{background:rgba(255,255,255,0.03);padding:4px 6px;border-radius:6px;color:#bfe6ff;font-family:var(--mono);font-size:13px}
    ul{line-height:1.6;color:var(--muted)}
    .meta{display:flex;gap:12px;flex-wrap:wrap;margin-top:8px}
    .badge{padding:6px 10px;border-radius:8px;background:rgba(255,255,255,0.02);font-weight:600;color:var(--muted);font-size:13px;border:1px solid rgba(255,255,255,0.02)}
    footer{margin-top:22px;color:var(--muted);font-size:13px}
    .feature-list{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:12px}
    .feature{background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.00));padding:12px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);color:var(--muted)}
    .author{display:flex;align-items:center;gap:12px}
    .avatar{width:52px;height:52px;border-radius:10px;background:linear-gradient(135deg,var(--accent2),var(--accent));display:flex;align-items:center;justify-content:center;color:#061221;font-weight:700}
    a { color: #a9ddff; text-decoration: none; }
    a:hover { text-decoration: underline; }
    @media (max-width:600px){ .row{flex-direction:column} }
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">WQ</div>
      <div>
        <h1>Wine Quality Prediction App</h1>
        <p class="lead">A Streamlit web app that predicts wine quality from chemical properties using a trained machine learning model. Includes interactive visualizations and an easy-to-use UI — great for portfolio and interviews.</p>
        <div class="meta">
          <div class="badge">Streamlit • Python</div>
          <div class="badge">scikit-learn • Plotly • Matplotlib</div>
          <div class="badge">Model: Random Forest</div>
        </div>
      </div>
    </header>

    <section style="margin-top:18px">
      <div class="row">
        <div class="card">
          <h3>Project Overview</h3>
          <p style="color:var(--muted)">This project trains a model to predict wine quality (<code class="inline">quality</code>) from 11 chemical features. After training, the model and scaler are saved and used inside a Streamlit app to provide instant predictions and interactive charts.</p>

          <h4 style="margin-top:12px">Input features</h4>
          <ul>
            <li>fixed acidity</li>
            <li>volatile acidity</li>
            <li>citric acid</li>
            <li>residual sugar</li>
            <li>chlorides</li>
            <li>free sulfur dioxide</li>
            <li>total sulfur dioxide</li>
            <li>density</li>
            <li>pH</li>
            <li>sulphates</li>
            <li>alcohol</li>
          </ul>
        </div>

        <div class="card">
          <h3>Tech Stack</h3>
          <div class="feature-list" style="margin-top:8px">
            <div class="feature"><strong>Language</strong><div style="margin-top:6px;color:var(--muted)">Python 3.8+</div></div>
            <div class="feature"><strong>Web</strong><div style="margin-top:6px;color:var(--muted)">Streamlit</div></div>
            <div class="feature"><strong>ML</strong><div style="margin-top:6px;color:var(--muted)">scikit-learn (RandomForest)</div></div>
            <div class="feature"><strong>Viz</strong><div style="margin-top:6px;color:var(--muted)">Plotly (radar/gauge) & Matplotlib</div></div>
            <div class="feature"><strong>Data</strong><div style="margin-top:6px;color:var(--muted)">Wine Quality (UCI / Kaggle)</div></div>
            <div class="feature"><strong>Persistence</strong><div style="margin-top:6px;color:var(--muted)">model.pkl, scaler.pkl</div></div>
          </div>
        </div>
      </div>
    </section>

    <section style="margin-top:18px">
      <div class="row">
        <div class="card" style="flex:2">
          <h3>Quick Start</h3>
          <p style="color:var(--muted)">Clone, install dependencies, and run the Streamlit app locally.</p>

          <div style="margin-top:12px">
            <div style="font-weight:600;margin-bottom:8px">1. Clone</div>
            <pre class="cmd">git clone https://github.com/<strong>YOUR_USERNAME</strong>/wine-quality-prediction-app.git
cd wine-quality-prediction-app</pre>

            <div style="font-weight:600;margin-top:8px;margin-bottom:8px">2. Install dependencies</div>
            <pre class="cmd">pip install -r requirements.txt</pre>

            <div style="font-weight:600;margin-top:8px;margin-bottom:8px">3. Run</div>
            <pre class="cmd">streamlit run app.py</pre>
          </div>

          <h4 style="margin-top:14px">Files (important)</h4>
          <pre class="cmd">app.py          # Streamlit app
model.pkl        # trained RandomForest model
scaler.pkl       # StandardScaler fitted on train data
winequality.csv  # dataset (for visualizations / retraining)</pre>
        </div>

        <div class="card" style="flex:1">
          <h3>Usage</h3>
          <ul>
            <li>Open the app in your browser (Streamlit will show the URL)</li>
            <li>Adjust sliders for each feature</li>
            <li>Click <code class="inline">Predict</code> to see score + radar & gauge charts</li>
            <li>Optional: explore dataset histogram in the sidebar</li>
          </ul>

          <h4 style="margin-top:12px">Model details</h4>
          <ul>
            <li>RandomForest (n_estimators=100)</li>
            <li>Input features scaled with StandardScaler</li>
            <li>Saved with <code class="inline">joblib</code> (or <code class="inline">pickle</code>)</li>
          </ul>
        </div>
      </div>
    </section>

    <section style="margin-top:18px">
      <div class="card">
        <h3>Example Code (training snippet)</h3>
        <pre class="cmd">from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

data = pd.read_csv("winequality.csv")
X = data.drop("quality", axis=1)
y = data["quality"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)

joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")</pre>
      </div>
    </section>

    <section style="margin-top:18px">
      <div class="row">
        <div class="card">
          <h3>Deployment</h3>
          <ul>
            <li><strong>Streamlit Community Cloud</strong> — easiest: connect your GitHub repo and deploy.</li>
            <li>Render / Railway — alternative hosting providers (need a requirements.txt).</li>
          </ul>
          <p style="color:var(--muted);margin-top:8px">Make sure <code class="inline">model.pkl</code>, <code class="inline">scaler.pkl</code> and <code class="inline">requirements.txt</code> are in the repo before deploying.</p>
        </div>

        <div class="card">
          <h3>Future enhancements</h3>
          <ul>
            <li>Compare multiple models (RandomForest, LightGBM, XGBoost)</li>
            <li>Bulk upload CSV for batch prediction</li>
            <li>Interactive feature importance & partial dependence plots</li>
            <li>CI/CD via GitHub Actions</li>
          </ul>
        </div>
      </div>
    </section>

    <section style="margin-top:18px">
      <div class="card author">
        <div class="avatar">PS</div>
        <div>
          <div style="font-weight:700">YOUR_NAME</div>
          <div style="color:var(--muted);margin-top:6px">Machine Learning & Data Science | Final-year CS</div>
          <div style="margin-top:8px;color:var(--muted)">
            ✉️ <a href="mailto:your.email@example.com">your.email@example.com</a> •
            <a href="https://github.com/YOUR_USERNAME" target="_blank">GitHub</a> •
            <a href="https://linkedin.com/in/YOUR_PROFILE" target="_blank">LinkedIn</a>
          </div>
        </div>
      </div>

      <footer>
        <div style="margin-top:14px;color:var(--muted)">License: <strong>MIT</strong> — feel free to reuse and adapt. <br/> If you found this project useful, kindly ⭐ the repo on GitHub!</div>
      </footer>
    </section>
  </div>
</body>
</html>
