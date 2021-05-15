import tensorflow as tf
import numpy as np

#sequential dense model

EPOCHS = 200
BATCH_SIZE = 128
VERBOSE = 1
NB_CLASSES = 10 #출력 개수 = 숫자의 개수
N_HIDDEN = 128 #히든 레이어 매개변수 개수
VALIDATION_SPLIT = 0.2 #검증을 위해 학습에 제외되는 훈련 데이터 비율

#MNIST 데이터셋
# 훈련과 테스트를 60000, 10000 으로 나눈다.
# 레이블에 대한 원핫 인코딩은 자동으로 적용된다.
mnist = tf.keras.datasets.mnist
(X_train, Y_train) , (X_test, Y_test) = mnist.load_data()

#X train 은 60000개의 28x28 데이터를 60000 x 784 2차원 형태로 변환한다.
RESHAPED = 784
X_train = X_train.reshape(60000,RESHAPED)
X_test = X_test.reshape(10000,RESHAPED)

#32비트 float형 사용
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

#입력 normalization
X_train /= 255
X_test /= 255
print(X_train.shape[0],'train samples')
print(X_test.shape[0],'test samples')

#레이블을 원핫 인코딩
Y_train = tf.keras.utils.to_categorical(Y_train, NB_CLASSES)
Y_test = tf.keras.utils.to_categorical(Y_test,NB_CLASSES)



