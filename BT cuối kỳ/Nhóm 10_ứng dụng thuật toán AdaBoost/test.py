import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from tabulate import tabulate
from tkinter import Scrollbar
# Load dữ liệu và huấn luyện mô hình
titanic_url = r'Titanic_Dataset.csv'
df = pd.read_csv(titanic_url)


features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
target = 'Survived'

X = df[features]
y = df[target]


sex_mapping = {'male': 0, 'female': 1}
X['Sex'] = X['Sex'].map(sex_mapping)


X['Age'].fillna(X['Age'].median(), inplace=True)
X['Fare'].fillna(X['Fare'].median(), inplace=True)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)


model = AdaBoostClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)


app = tk.Tk()
app.title("Dự đoán Sống sót trên tàu Titanic")





pclass_label = ttk.Label(app, text="Pclass (Lớp Hành Khách):")
pclass_label.grid(row=0, column=0, padx=10, pady=10)
pclass_entry = ttk.Entry(app)
pclass_entry.grid(row=0, column=1, padx=10, pady=10)

sex_label = ttk.Label(app, text="Sex (Giới tính):")
sex_label.grid(row=1, column=0, padx=10, pady=10)
sex_var = tk.StringVar()
sex_combobox = ttk.Combobox(app, textvariable=sex_var, values=["male", "female"])
sex_combobox.grid(row=1, column=1, padx=10, pady=10)

age_label = ttk.Label(app, text="Age (Tuổi):")
age_label.grid(row=2, column=0, padx=10, pady=10)
age_entry = ttk.Entry(app)
age_entry.grid(row=2, column=1, padx=10, pady=10)

sibsp_label = ttk.Label(app, text="SibSp (Số lượng anh chị em hoặc vợ chồng trên tàu):")
sibsp_label.grid(row=3, column=0, padx=10, pady=10)
sibsp_entry = ttk.Entry(app)
sibsp_entry.grid(row=3, column=1, padx=10, pady=10)

parch_label = ttk.Label(app, text="Parch (Số lượng bố mẹ hoặc con cái trên tàu):")
parch_label.grid(row=4, column=0, padx=10, pady=10)
parch_entry = ttk.Entry(app)
parch_entry.grid(row=4, column=1, padx=10, pady=10)

fare_label = ttk.Label(app, text="Fare (Giá vé):")
fare_label.grid(row=5, column=0, padx=10, pady=10)
fare_entry = ttk.Entry(app)
fare_entry.grid(row=5, column=1, padx=10, pady=10)


def predict_survival():
    
    pclass = float(pclass_entry.get())
    sex = sex_var.get()
    age = float(age_entry.get())
    sibsp = float(sibsp_entry.get())
    parch = float(parch_entry.get())
    fare = float(fare_entry.get())

    # Chuyển đổi giá trị chuỗi sang số
    sex = sex_mapping[sex]

    
    new_data = pd.DataFrame({'Pclass': [pclass], 'Sex': [sex], 'Age': [age], 'SibSp': [sibsp], 'Parch': [parch], 'Fare': [fare]})

    
    prediction = model.predict(new_data)

  
    survival_mapping = {0: 'Không Sống sót', 1: 'Sống sót'}
    predicted_label = survival_mapping[prediction[0]]

    
    result_label.config(text=f"Khả năng sống sót: {predicted_label}")

predict_button = ttk.Button(app, text="Dự đoán Sống sót", command=predict_survival)
predict_button.grid(row=6, column=0, columnspan=2, pady=20)


result_label = ttk.Label(app, text="")
result_label.grid(row=7, column=0, columnspan=2)


def calculate_accuracy():
    
    predictions = model.predict(X_test)

    
    accuracy = accuracy_score(y_test, predictions)

    
    accuracy_label.config(text=f"Tỷ lệ dự đoán chính xác: {accuracy * 100:.2f}%")


accuracy_button = ttk.Button(app, text="Tính toán độ chính xác", command=calculate_accuracy)
accuracy_button.grid(row=8, column=0, columnspan=2, pady=10)


accuracy_label = ttk.Label(app, text="")
accuracy_label.grid(row=9, column=0, columnspan=2)


file_label = ttk.Label(app, text="Chọn file dữ liệu:")
file_label.grid(row=10, column=0, padx=10, pady=10)


file_var = tk.StringVar()
file_entry = ttk.Entry(app, textvariable=file_var, state="readonly")
file_entry.grid(row=10, column=1, padx=10, pady=10)


def browse_file():
    file_path = tk.filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    file_var.set(file_path)


browse_button = ttk.Button(app, text="Chọn file", command=browse_file)
browse_button.grid(row=10, column=2, pady=10)


data_text = tk.Text(app, height=10, width= 60)
data_text.grid(row=12, column=0, columnspan=3, padx=10, pady=10)

def map_to_survived(predictions):
    survival_mapping = {0: 'Không Sống sót', 1: 'Sống sót'}
    return [survival_mapping[p] for p in predictions]

def predict_from_file():
    file_path = file_var.get()
    if not file_path:
        result_label.config(text="Hãy chọn một file trước.")
        return

    try:
        
        new_data = pd.read_csv(file_path)

        
        new_data['Sex'] = new_data['Sex'].map(sex_mapping)
        new_data['Age'].fillna(new_data['Age'].median(), inplace=True)
        new_data['Fare'].fillna(new_data['Fare'].median(), inplace=True)
        
        
        predictions = model.predict(new_data[features])

        
        survival_mapping = {0: 'Không Sống sót', 1: 'Sống sót'}
        predicted_labels = [survival_mapping[p] for p in predictions]

        
        new_data['Predicted_Survival'] = predicted_labels

        
        data_text.delete(1.0, tk.END)  # Xóa nội dung cũ
        data_text.insert(tk.END, "Dữ liệu đầy đủ từ file:\n")
        
       
        table = tabulate(new_data, headers='keys', tablefmt='psql', showindex=False)
        data_text.insert(tk.END, table)
        data_text.config(width=100)
        
    except Exception as e:
        result_label.config(text=f"Lỗi: {str(e)}")
data_text = tk.Text(app, height=10, width=60, wrap=tk.NONE)  
data_text.grid(row=12, column=0, padx=10, pady=10, sticky='ew')  


xscrollbar = tk.Scrollbar(app, orient=tk.HORIZONTAL, command=data_text.xview)
xscrollbar.grid(row=13, column=0, padx=10, pady=5, sticky='ew')  


data_text.config(xscrollcommand=xscrollbar.set)


predict_file_button = ttk.Button(app, text="Dự đoán từ file", command=predict_from_file)
predict_file_button.grid(row=11, column=0, pady=10)

from joblib import dump

# Lưu mô hình
dump(model, 'titanic_model.joblib')


app.mainloop()