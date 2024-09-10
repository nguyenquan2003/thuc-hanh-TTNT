import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

class SVM:

    def __init__(self, k_toc_do_hoc=0.001, k_tham_so_lambda=0.01, k_so_vong_lap=1000):
        self.k_tdh = k_toc_do_hoc
        self.k_tham_so_lambda = k_tham_so_lambda
        self.k_so_vong_lap = k_so_vong_lap
        self.trong_so = None
        self.b = None

    def fit(self, X, y):
        so_mau, so_tinh_nang = X.shape
        y_ = np.where(y <= 0, -1, 1)

        # Khởi tạo trọng số
        self.trong_so = np.zeros(so_tinh_nang)
        self.b = 0

        for _ in range(self.k_so_vong_lap):
            for index, x_i in enumerate(X):
                dieu_kien = y_[index] * (np.dot(x_i, self.trong_so) - self.b) >= 1
                if dieu_kien:
                    self.trong_so -= self.k_tdh * (2 * self.k_tham_so_lambda * self.trong_so)
                else:
                    self.trong_so -= self.k_tdh * (2 * self.k_tham_so_lambda * self.trong_so - np.dot(x_i, y_[index]))
                    self.b -= self.k_tdh * y_[index]

    def predict(self, X):
        approx = np.dot(X, self.trong_so) - self.b
        return np.sign(approx)

# Kiểm thử
if __name__ == "__main__":
    X, y = datasets.make_blobs(
        n_samples=50, n_features=2, centers=2, cluster_std=1.05, random_state=40
    )
    y = np.where(y == 0, -1, 1)

    X_dao_tao, X_thu, y_dao_tao, y_thu = train_test_split(
        X, y, test_size=0.2, random_state=123
    )

    mo_hinh = SVM()
    mo_hinh.fit(X_dao_tao, y_dao_tao)
    du_doan = mo_hinh.predict(X_thu)

    def do_chinh_xac(y_true, y_pred):
        chinh_xac = np.sum(y_true == y_pred) / len(y_true)
        return chinh_xac

    print("Độ chính xác phân loại SVM:", do_chinh_xac(y_thu, du_doan))

    def hien_thi_svm():
        def lay_gia_tri_hyperplane(x, w, b, offset):
            return (-w[0] * x + b + offset) / w[1]

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.scatter(X[:, 0], X[:, 1], marker="o", c=y)

        x0_1 = np.amin(X[:, 0])
        x0_2 = np.amax(X[:, 0])
        x1_1 = lay_gia_tri_hyperplane(x0_1, mo_hinh.trong_so, mo_hinh.b, 0)
        x1_2 = lay_gia_tri_hyperplane(x0_2, mo_hinh.trong_so, mo_hinh.b, 0)
        x1_1_m = lay_gia_tri_hyperplane(x0_1, mo_hinh.trong_so, mo_hinh.b, -1)
        x1_2_m = lay_gia_tri_hyperplane(x0_2, mo_hinh.trong_so, mo_hinh.b, -1)
        x1_1_p = lay_gia_tri_hyperplane(x0_1, mo_hinh.trong_so, mo_hinh.b, 1)
        x1_2_p = lay_gia_tri_hyperplane(x0_2, mo_hinh.trong_so, mo_hinh.b, 1)

        ax.plot([x0_1, x0_2], [x1_1, x1_2], "y--")
        ax.plot([x0_1, x0_2], [x1_1_m, x1_2_m], "k")
        ax.plot([x0_1, x0_2], [x1_1_p, x1_2_p], "k")
        x1_min = np.amin(X[:, 1])
        x1_max = np.amax(X[:, 1])
        ax.set_ylim([x1_min - 3, x1_max + 3])

        plt.show()
        

    hien_thi_svm()

import joblib
# Lưu mô hình
joblib.dump(mo_hinh, 'svm_model.joblib')

# Đọc mô hình từ file
loaded_model = joblib.load('svm_model.joblib')

# Sử dụng mô hình đã đọc
du_doan_loaded = loaded_model.predict(X_thu)