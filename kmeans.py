import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def distance(p1, p2):
    #return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    return np.sqrt( (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]))
    #return abs(p1[0]-p2[0]) if abs(p1[0]-p2[0]) > abs(p1[1]-p2[1]) else abs(p1[1]-p2[1])

def kmeans(data, size):
    colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']

    #ランダムにクラスタリング
    ##分類
    classification = np.random.randint(0, size, len(data))
    ##分割
    clusters = []
    for claster_num in range(size):
        cluster = []
        for i in range(len(data)):
            if classification[i] == claster_num:
                cluster.append(data[i])
        clusters.append(cluster)

    #描画フレーム追加
    for i in range(size):
        cluster = clusters[i]
        x, y = zip(*cluster)
        plt.plot(x, y, 'o', c=colors[i])
    plt.savefig('fig/fig_0.png')

    #クラスタリングの繰り返し
    for n in range(10):
        #重心計算
        center = []
        for cluster in clusters:
            x, y = zip(*cluster)
            center.append((sum(x)/len(cluster), sum(y)/len(cluster)))

        #再クラスタリング
        ##分類
        classification = []
        for datum in data:
            dmin_cluster_num = 0
            for cluster_num in range(1, size):
                if distance(center[dmin_cluster_num], datum) > distance(center[cluster_num], datum):
                    dmin_cluster_num = cluster_num
            classification.append(dmin_cluster_num)
        ##分割
        clusters = []
        for claster_num in range(size):
            cluster = []
            for i in range(len(data)):
                if classification[i] == claster_num:
                    cluster.append(data[i])
            clusters.append(cluster)

        #描画フレーム追加
        for i in range(size):
            cluster = clusters[i]
            x, y = zip(*cluster)
            im = plt.plot(x, y, 'o', c=colors[i])
        plt.savefig('fig/fig_' + str(n + 1) + '.png')

    #描画
    plt.show()

if __name__ == '__main__':
    data = []
    for n in range(50):
        x = np.random.rand() * 100
        y = np.random.rand() * 100
        data.append((x, y))
    for n in range(50):
        x = np.random.rand() * 100 + 100
        y = np.random.rand() * 100 + 100
        data.append((x, y))
    for n in range(50):
        x = np.random.rand() * 100 + 200
        y = np.random.rand() * 100 - 10
        data.append((x, y))

    kmeans(data, 3)
