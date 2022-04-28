# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:07:05 2019

@author: screa
"""
import os
from matplotlib import pyplot as plt
import numpy as np,random
from numpy.random import rand
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
import pandas as pd 


"""
Separa entre facil y dificil, aleatoriza el orden de aparición de 3 tipos de trials (estimulos).
Utiliza preferences.csv
"""

def plot_products_rankings(indexes,rankings):
    plt.rcParams["figure.figsize"] = [12,6]
    plt.bar(indexes,rankings)
    plt.xlabel('product')
    plt.ylabel('rankings')  
    plt.title('Products-rankings relation')
    plt.savefig('data/Products-rankings relation.png')
    plt.show() 


def compute_differences(rankings):
    numero_de_productos=len(rankings)
    differences_vector=np.zeros((numero_de_productos,numero_de_productos))
    indexes_vector_x=np.zeros((numero_de_productos,numero_de_productos),np.uint8)
    indexes_vector_y=np.zeros((numero_de_productos,numero_de_productos),np.uint8)

    for i in range(numero_de_productos):
        for j in range(numero_de_productos):
            if i==j:
                differences_vector[i,j]=None
            else:
                differences_vector[i,j]=rankings[i]-rankings[j]
            indexes_vector_x[i,j]=i
            indexes_vector_y[i,j]=j
                
    return indexes_vector_x,indexes_vector_y,differences_vector
            
def plot_differences(indexes_vector_x,indexes_vector_y,differences_vector,th_easy_hard,th_easy_medium,th_medium_hard):    
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    dif_f = differences_vector.flatten()
    idx_x = indexes_vector_x.flatten()
    idx_y = indexes_vector_y.flatten()

    idx_x_easy_medium = idx_x[np.logical_and(dif_f<th_easy_medium,dif_f>0)]
    idx_y_easy_medium = idx_y[np.logical_and(dif_f<th_easy_medium,dif_f>0)]
    dif_easy_medium = dif_f[np.logical_and(dif_f<th_easy_medium,dif_f>0)]
    
    data_easy = [idx_x_easy_medium,idx_y_easy_medium,dif_easy_medium]
    
    t = ["r" for dif_easy_medium in dif_easy_medium]
    #ax.scatter(idx_x_easy_medium,idx_y_easy_medium,dif_easy_medium,c=t,marker='.',alpha=0.5)
    
    idx_x_t1=idx_x[np.logical_and(dif_f>-th_easy_medium,dif_f<0)]
    idx_y_t1=idx_y[np.logical_and(dif_f>-th_easy_medium,dif_f<0)]
    dif_f_t1=dif_f[np.logical_and(dif_f>-th_easy_medium,dif_f<0)]
    
    t = ["r" for dif_f_t1 in dif_f_t1]
    #ax.scatter(idx_x_t1,idx_y_t1,dif_f_t1,c=t,marker='.',alpha=0.5)
    

    idx_x_t1=idx_x[np.logical_and(dif_f>th_easy_medium, dif_f<th_medium_hard)]
    idx_y_t1=idx_y[np.logical_and(dif_f>th_easy_medium, dif_f<th_medium_hard)]
    dif_f_t1=dif_f[np.logical_and(dif_f>th_easy_medium, dif_f<th_medium_hard)]
    
    data_medium=[idx_x_t1,idx_y_t1,dif_f_t1]

    
    t = ["g" for dif_f_t1 in dif_f_t1]
    #ax.scatter(idx_x_t1,idx_y_t1,dif_f_t1,c=t,marker='^',alpha=0.5)
    
    idx_x_t1=idx_x[np.logical_and(dif_f<-th_easy_medium,dif_f>-th_medium_hard)]
    idx_y_t1=idx_y[np.logical_and(dif_f<-th_easy_medium,dif_f>-th_medium_hard)]
    dif_f_t1=dif_f[np.logical_and(dif_f<-th_easy_medium,dif_f>-th_medium_hard)]
    
    t = ["g" for dif_f_t1 in dif_f_t1]
    #ax.scatter(idx_x_t1,idx_y_t1,dif_f_t1,c=t,marker='^',alpha=0.5)
    

  
    idx_x_t1=idx_x[dif_f>th_medium_hard]
    idx_y_t1=idx_y[dif_f>th_medium_hard]
    dif_f_t1=dif_f[dif_f>th_medium_hard]
    
    data_hard=[idx_x_t1,idx_y_t1,dif_f_t1]

    
    t = ["b" for dif_f_t1 in dif_f_t1]
    #ax.scatter(idx_x_t1,idx_y_t1,dif_f_t1,c=t,marker='*',alpha=0.5)
    
    idx_x_t1=idx_x[dif_f<-th_medium_hard]
    idx_y_t1=idx_y[dif_f<-th_medium_hard]
    dif_f_t1=dif_f[dif_f<-th_medium_hard]
    
    t = ["b" for dif_f_t1 in dif_f_t1]
    #ax.scatter(idx_x_t1,idx_y_t1,dif_f_t1,c=t,marker='*',alpha=0.5)

   
    
    #plt.xlabel('product a')
    #plt.ylabel('product b')  
    #plt.title('Product-difference relation')
    #plt.savefig('data/Product-difference relation.png')
    #plt.show() 
    
    
    
    return data_easy,data_medium,data_hard
    
    

def estimate_clusters(differences_vector):    
    values=differences_vector.flatten()[differences_vector.flatten()>0]
    sorted_values = np.sort(values)
    
    km = KMeans(n_clusters=2, random_state=0).fit(sorted_values.reshape(-1,1))

    labels = km.labels_    
    tmp1 = km.labels_[0]
    v = 0
    for i in range(len(labels)):
        if km.labels_[i] == tmp1:
            labels[i] = v
        else:
            tmp1 = km.labels_[i]
            v += 1            
    
    for i in range(len(km.labels_)):
        if km.labels_[i] == 1:
            break
    
    th_easy_hard = sorted_values[i]
    th_easy_medium = th_easy_hard - th_easy_hard/3
    th_medium_hard = (20-th_easy_hard)/3 + th_easy_hard

    
    return th_easy_hard, th_easy_medium, th_medium_hard

def plot_thresholds(differences_vector, th_easy_hard, th_easy_medium, th_medium_hard):
    differences_transformed=1/(1+1*np.exp(-differences_vector.flatten()))
    plt.scatter(differences_vector.flatten(),differences_transformed)

    plt.xlim(-20.1, 20.1), plt.ylim(-0.1, 1.1)

    x1, y1 = [th_easy_hard, th_easy_hard], [-1,1.5]
    x2, y2 = [-th_easy_hard, -th_easy_hard], [-1,1.5]
    plt.plot(x1, y1, 'k--')
    plt.plot(x2, y2, 'k--')
    

        
    x1, y1 = [th_easy_medium, th_easy_medium], [-1,1.5]
    x2, y2 = [-th_easy_medium, -th_easy_medium], [-1,1.5]
    plt.plot(x1, y1, 'r--')
    plt.plot(x2, y2, 'r--')
    
    
    x1, y1 = [th_medium_hard, th_medium_hard], [-1,1.5]
    x2, y2 = [-th_medium_hard, -th_medium_hard], [-1,1.5]
    plt.plot(x1, y1, 'g--')
    plt.plot(x2, y2, 'g--')
    
    plt.axvspan(-th_easy_hard+th_easy_hard/3, th_easy_hard-th_easy_hard/3, facecolor='r', alpha=0.1)
    plt.axvspan(-th_easy_hard+th_easy_hard/3, (-20+th_easy_hard)/3-th_easy_hard, facecolor='g', alpha=0.1)
    plt.axvspan(th_easy_hard-th_easy_hard/3, (20-th_easy_hard)/3+th_easy_hard, facecolor='g', alpha=0.1)
    plt.axvspan(-20, (-20+th_easy_hard)/3-th_easy_hard, facecolor='b', alpha=0.1)
    plt.axvspan(20, (20-th_easy_hard)/3+th_easy_hard, facecolor='b', alpha=0.1)
        
    plt.xlabel('decision level')
    plt.ylabel('difference value between two products')  
    plt.title('Decision segmentation')
    plt.savefig('data/Decision segmentation.png')  

    plt.show() 

def generate_data_differences_for_trials(indexes, rankings):
    #plot_products_rankings(indexes,rankings)
    indexes_vector_x, indexes_vector_y, differences_vector = compute_differences(rankings)
    th_easy_hard, th_easy_medium, th_medium_hard = estimate_clusters(differences_vector)
    #plot_thresholds(differences_vector,th_easy_hard,th_easy_medium,th_medium_hard)
    data_easy, data_medium, data_hard = plot_differences(indexes_vector_x, indexes_vector_y, differences_vector, th_easy_hard, th_easy_medium, th_medium_hard)
    
    data_easy = np.asarray(data_easy).T
    data_medium = np.asarray(data_medium).T
    data_hard = np.asarray(data_hard).T
    return data_easy, data_medium, data_hard


def define_test_phase_two(number_each_class, data_easy, data_medium, data_hard):
    # el numero de elecciones sera distribuido uniformemente entre los tres niveles de dificultad:
    number_per_difficulty = np.round(number_each_class)
    random.seed(1)

    random_indexes_de = random.sample(range(len(data_easy)), number_per_difficulty)
    random_indexes_dm = random.sample(range(len(data_medium)), number_per_difficulty)
    random_indexes_dh = random.sample(range(len(data_hard)), number_per_difficulty)
   
    sample_de = data_easy[random_indexes_de]
    sample_dm = data_medium[random_indexes_dm]
    sample_dh = data_hard[random_indexes_dh]
    
    sample_full = np.concatenate((sample_de, sample_dm, sample_dh))

    sample_full_random = np.take(sample_full, np.random.permutation(sample_full.shape[0]), axis=0, out=sample_full)
    
    screen_order = np.concatenate([np.array([0,1,2])] * number_each_class, axis=0)    
    np.take(screen_order, np.random.permutation(screen_order.shape[0]), axis=0, out=screen_order)
        
    item_order = np.concatenate([np.array([0,1])] * number_each_class*3, axis=0)[0:len(screen_order)]# izquierda y derecha
    return sample_full_random, screen_order, item_order
    

def generate_data_trials(samples_per_difficulty, subject_name="subject_test"):
    #data_easy, data_medium, data_hard = cluster_data_trials(rankings, samples_per_difficulty, subject_name=subject_name, is_save=False)
    data_easy, data_medium, data_hard = load_cluster_data_trials(subject_name=subject_name)
    return define_test_phase_two(samples_per_difficulty, data_easy, data_medium, data_hard)   

def cluster_data_trials(rankings, samples_per_difficulty, subject_name="subject_test", is_save=True):
    indexes = np.linspace(1,len(rankings),len(rankings))
    data_easy, data_medium, data_hard = generate_data_differences_for_trials(indexes, rankings)
    if is_save:
        if not os.path.exists(f'./results/{subject_name}'):
            os.mkdir(f'./results/{subject_name}')
        np.savetxt(f'./results/{subject_name}/segmented_trials_easy.csv', data_easy, delimiter=',')
        np.savetxt(f'./results/{subject_name}/segmented_trials_medium.csv', data_medium, delimiter=',')
        np.savetxt(f'./results/{subject_name}/segmented_trials_hard.csv', data_hard, delimiter=',') 
    return data_easy, data_medium, data_hard

def load_cluster_data_trials(subject_name="subject_test"):
    data_easy = np.loadtxt(f'./results/{subject_name}/segmented_trials_easy.csv', delimiter=',')
    data_medium = np.loadtxt(f'./results/{subject_name}/segmented_trials_medium.csv', delimiter=',')
    data_hard = np.loadtxt(f'./results/{subject_name}/segmented_trials_hard.csv', delimiter=',')
    return data_easy, data_medium, data_hard

def create_trials(samples_per_difficulty, subject_name="subject_test"):
    np.warnings.filterwarnings('ignore')
    data = pd.read_csv(f"./results/{subject_name}/preferences.csv", header=None)
    rankings = np.asarray(data).T[0]
    sample_full_random, screen_order, item_order = generate_data_trials(samples_per_difficulty, subject_name=subject_name)
    
    print('\n\n------------------------------------------------------------------------------------')
    print('Generando los trials basados en los rankings generados de ', len(rankings),' productos...')
    print('------------------------------------------------------------------------------------')
    
    values = np.zeros((len(rankings),2))
    values[:, 0] = np.linspace(1,len(rankings),len(rankings))
    values[:, 1] = rankings
    print('\nLos rankings determinados por el usuario son:\n')

    print('productos rankings')
    print(values)
    
    print('\nSe han generado '+str(samples_per_difficulty)+' muestras aleatorias por dificultad...\n')
    print(sample_full_random)
    
    print('\nEl orden de condición experimental (pantalla en blanco con movimiento ocular libre (0), pantalla en blanco con restricción de movimiento ocular (1),  ambas opciones desplegadas en la pantalla (2)) es...\n')
    print(screen_order.T)
    
    print('\nEl orden de aparición  (izquierda (0) o derecha (1) es...\n')

    print(item_order.T)
    
    
    return rankings, sample_full_random, screen_order, item_order


if __name__=='__main__':
    samples_per_difficulty = 3
    rankings, sample_full_random, screen_order, item_order = create_trials(samples_per_difficulty)

    
    
    

