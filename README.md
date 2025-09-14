# wine-quality-prediction-app
A Streamlit web application that predicts wine quality using machine learning. Includes data preprocessing, model training (Random Forest), and interactive visualizations using Matplotlib and Plotly. Users can input wine chemical properties and instantly get quality predictions, along with graphical insights about the dataset.

<h1>🍷 Wine Quality Prediction App</h1>

<h2>📌 Project Objective</h2>
<p>
The goal of this project is to build a <b>machine learning web app</b> that predicts the <b>quality of wine</b> based on its physicochemical properties.  
The app helps <b>winemakers, laboratories, and enthusiasts</b> quickly assess wine quality using data-driven predictions.
</p>

<p align="center">
  <img src="https://github.com/pratiksutar841/wine-quality-prediction-app/blob/main/assets/wine_dashboard.png" alt="Wine Quality App Dashboard" width="800">
</p>

<hr>

<h2>🧠 Problem Statement</h2>
<p>
Wine quality assessment is traditionally done through <b>sensory analysis by experts</b>, which can be time-consuming and subjective.
</p>
<p>This project aims to:</p>
<ul>
  <li>Use a <b>dataset of wine samples</b> with measured features (acidity, sugar, pH, alcohol, etc.)</li>
  <li>Train a <b>classification model</b> to predict wine quality scores (0–10 scale)</li>
  <li>Deploy the model using <b>Streamlit</b> to build an interactive prediction web app</li>
  <li>Visualize key data insights through <b>charts and plots</b></li>
</ul>

<hr>

<h2>📂 Project Structure</h2>
<pre>
📁 wine-quality-prediction-app
│── app.py                             # Main Streamlit web app
│── winequality.csv                    # Dataset file
│── model.pkl                          # Trained ML model
│── requirements.txt                   # Dependencies
│── /assets/                           # Images and charts
│── /notebooks/                        # EDA and model training notebooks
│── README.md                          # Project documentation
</pre>

<hr>

<h2>🛠️ Tools & Technologies</h2>
<ul>
  <li><b>Programming & Libraries:</b> Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Pickle</li>
  <li><b>Frontend:</b> Streamlit (for the web app UI)</li>
  <li><b>Environment:</b> Jupyter Notebook, VS Code</li>
  <li><b>Version Control:</b> Git & GitHub</li>
</ul>

<hr>

<h2>📊 Methodology</h2>
<ol>
  <li><b>Data Preprocessing</b>
    <ul>
      <li>Load and clean the wine quality dataset</li>
      <li>Handle missing values, duplicates, and outliers</li>
      <li>Encode target labels and scale features</li>
    </ul>
  </li>
  <li><b>Exploratory Data Analysis (EDA)</b>
    <ul>
      <li>Distribution of wine quality ratings</li>
      <li>Correlation between features and wine quality</li>
      <li>Feature importance analysis</li>
    </ul>
  </li>
  <li><b>Model Training</b>
    <ul>
      <li>Algorithm: Random Forest Classifier</li>
      <li>Train/test split: 80% training, 20% testing</li>
      <li>Metrics: Accuracy, Precision, Recall, F1-score, ROC-AUC</li>
    </ul>
  </li>
  <li><b>Model Deployment</b>
    <ul>
      <li>Build a Streamlit interface for user input</li>
      <li>Load the trained model and display prediction result</li>
      <li>Visualize summary statistics and charts in the app</li>
    </ul>
  </li>
</ol>

<hr>

<h2>📈 Key Results</h2>
<ul>
  <li><b>Model Accuracy:</b> 92%</li>
  <li><b>Precision:</b> 90%</li>
  <li><b>Recall:</b> 88%</li>
  <li><b>F1-Score:</b> 89%</li>
</ul>

<p>📌 The model shows high predictive performance and generalizes well on unseen data.</p>

<hr>

<h2>📌 Features of the App</h2>
<ul>
  <li>Interactive form to input wine parameters</li>
  <li>Instant prediction of wine quality (Good / Average / Poor)</li>
  <li>Data visualizations like histograms, boxplots, and correlation heatmaps</li>
  <li>Responsive, clean UI with real-time updates</li>
</ul>

<hr>

<h2>📷 App Screenshots</h2>
<p align="center">
  <img src="https://github.com/pratiksutar841/wine-quality-prediction-app/blob/main/assets/app_preview1.png" alt="Wine Quality App UI - Input" width="800"><br><br>
  <img src="https://github.com/pratiksutar841/wine-quality-prediction-app/blob/main/assets/app_preview2.png" alt="Wine Quality App UI - Output" width="800"><br><br>
  <img src="https://github.com/pratiksutar841/wine-quality-prediction-app/blob/main/assets/app_preview3.png" alt="Wine Quality App UI - Charts" width="800">
</p>

<hr>

<h2>🚀 How to Run Locally</h2>
<ol>
  <li>Clone this repository
    <pre>git clone https://github.com/pratiksutar841/wine-quality-prediction-app.git</pre>
  </li>
  <li>Navigate to the project folder
    <pre>cd wine-quality-prediction-app</pre>
  </li>
  <li>Install dependencies
    <pre>pip install -r requirements.txt</pre>
  </li>
  <li>Run the Streamlit app
    <pre>streamlit run app.py</pre>
  </li>
</ol>

<hr>

<h2>🙋‍♂️ Author</h2>
<p>
<b>Pratik Prashant Sutar</b><br>
B.Tech in Computer Science & Engineering (Data Science)<br>
GitHub: <a href="https://github.com/pratiksutar841">pratiksutar841</a><br>
LinkedIn: <a href="https://www.linkedin.com/in/pratik-sutar-/">Pratik Sutar</a>
</p>
