Online Payments Fraud Detection using Machine Learning (Flask)

This project is a Machine Learning–based Fraud Detection Web Application that predicts whether an online payment transaction is Fraud or Not Fraud in real time using a trained model integrated with a Flask web interface.

The ML model is trained on a Kaggle online payments fraud dataset and deployed through Flask for live predictions.


📂 Project Folder Structure:

ONLINE PAYMENTS FRAUD DETECTION USING ML
│
├── data
│   └── Sample Data.csv
│
├── Flask
│   ├── static
│   │   └── photo.png
│   │
│   ├── templates
│   │   ├── home.html
│   │   ├── predict.html
│   │   └── result.html
│   │
│   ├── app.py
│   └── model.pkl
│
├── training
│   ├── Online_payment_Fraud_detection.ipynb
│   └── model.pkl


💡 Key Features

1.Real-time fraud prediction

2.Flask-based web interface

3.ML model trained on real transaction dataset

4.Instant result after user inputs transaction details

5.High accuracy with Random Forest / XGBoost

6.Clean separation: Data | Training | Flask App

🛠️ Technologies Used

Component	Technology
Frontend	HTML, CSS
Backend	Python, Flask
ML Libraries	Scikit-learn, XGBoost, Pandas, NumPy
Visualization	Matplotlib, Seaborn
Model Storage	Pickle (model.pkl)

Clone the repository: 
https://github.com/abhinavh-77/Online-Payments-Fraud-Detection-using-Machine-Learning

⚙️ How to Run the Project:

1️⃣ Open Terminal in Flask Folder
	-cd Flask

2️⃣ Install Required Libraries
	-pip install flask numpy pandas scikit-learn xgboost

3️⃣ Run the Flask App
	-python app.py

4️⃣ Open in Browser
	-http://127.0.0.1:5000

🧠 Input Features for Prediction

The model uses the following transaction details:

Step

Type (encoded internally)

Amount

OldbalanceOrg

NewbalanceOrig

OldbalanceDest

NewbalanceDest

isFlaggedFraud (handled in backend)

🧪 Model Training

Model training notebook:

training/Online_payment_Fraud_detection.ipynb

Algorithms Tested
Algorithm	Accuracy
Decision Tree	99.96%
Random Forest	99.97%
SVM	80%
XGBoost	99.97%

Selected Model: Random Forest (model.pkl)

🚧 Known Limitations

Basic UI

No database to store predictions

Feature order must match model input

Transaction type must be encoded correctly

🔮 Future Enhancements

Cloud deployment (AWS / Render / Heroku)

Database integration for logging predictions

Improved UI using Bootstrap

User authentication

Fraud analytics dashboard

🙏 Credits

Dataset: Kaggle Online Payment Fraud Dataset

Model Training: training/Online_payment_Fraud_detection.ipynb

👨‍💻 Developed By

Haridasula Abhinav
Machine Learning Project

📧 Email: habhinavnaidu2005@gmail.com

📜 License

This project is for academic and educational purposes only.
