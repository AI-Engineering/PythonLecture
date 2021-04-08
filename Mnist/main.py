import tensorflow as tf         # current ver. 2.3.0
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load
import numpy as np


# 데이터 셋을 로딩한다.
# 자주 쓸 것이라서 오프라인에 다운로드 해두었다.
def load_dataset(online=False):
    if online:
        (tr_data, tr_label), (te_data, te_label) = tf.keras.datasets.mnist.load_data()

    else:
        path = "D:/Project/Mnist/dataset/mnist.npz"
        (tr_data, tr_label), (te_data, te_label) = tf.keras.datasets.mnist.load_data(path)

    return (tr_data, tr_label), (te_data, te_label)


# 이미지로 보고 싶을 때
def show_image(dataset, index):
    plt.imshow(255-dataset[index], cmap="gray")
    plt.show()


# 모든 이미지 순서대로 보기
def show_all_image(dataset):
    user_input = True
    data_num = 0

    while user_input:
        show_image(dataset, data_num)
        data_num += 1

        # 키보드 입력 True, 마우스 입력 False 인 리스트를 리턴
        # 다소 오류가 있다. 나중에 opencv watekey 같은 것으로 대체한다.
        user_input = plt.waitforbuttonpress()


# 데이터 분포도
def show_data_values(lable):
    # pandas의 value_counts 같은 함수
    count_value = np.bincount(lable)
    print(count_value)
    plt.bar(np.arange(0, 10), count_value)
    plt.xticks(np.arange(0, 10))
    plt.grid()
    plt.show()


# 학습
def train(x, y):
    clf = RandomForestClassifier()
    clf.fit(x, y)
    print(clf.score(x, y))
    dump(clf, "D:/Project/Mnist/model/rf_mnist.pkl")


# 테스트
# 테스트 세트 데이터와 정답을 입력 받아 모델의 예측 결과와 비교
# 하는 코드를 완성하시오!
def test(model, test_x, test_y):
    accuricy = 0

    return accuricy


if __name__ == "__main__":
    (train_set, train_label), (test_set, test_label) = load_dataset()

    #show_all_image(train_set)
    #show_data_values(train_label)
    #show_data_values(test_label)

    # 학습 시키기 전에 28, 28 -> 784로 platten
    train_set = train_set.reshape(len(train_set), 784)

    # 학습!!!
    #train(train_set, train_label)

    # 학습된 모델 불러오기
    model = load("./model/rf_mnist.pkl")

    # 모델이 잘 로드 되었는지 확인
    result = model.predict(train_set[:10])

    print(result)
    print(train_label[:10])
