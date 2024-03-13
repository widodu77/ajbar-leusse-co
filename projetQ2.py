import numpy as np
def vectorvectormultiplication(v1,v2):
    result=0
    for i in range(len(v1)):
        result += v1[i]*v2[i]
    return result 

def collonesVector(m1):
    résultat = []
    for i in range(len(m1[0])): 
        result = []
        for j in range(len(m1)): 
            result.append(m1[j][i])
        résultat.append(result)
    return résultat

def search(arr,t):
    result=[]
    i=0
    while i<len(arr):
        if arr[i]==t:
            result.append(i)
            i+=1
        else :
            i+=1
    return result

def vectorsous(v1, v2):
    r = []
    for i in range(len(v1)):
        r.append(v1[i] - v2[i])
    return r

def matdezeros(size):
    a=size
    nombre_de_ligne=a[0]
    nombre_de_colonne=a[-1]
    i=0
    result=[]
    for q in range(nombre_de_ligne):
        r=[]
        result.append(r)
        for m in range(nombre_de_colonne):
            r.append(0)
            i+=1
    return result


def vectorsous(v1, v2):
    r = []
    for i in range(len(v1)):
        r.append(v1[i] - v2[i])
    return r

def gauss_jordan_red(m1, b):
    augmented_matrix = []
    for i in range(len(m1)):
        augmented_matrix.append(m1[i] + [b[i]])

    for i in range(len(m1)-1):
        for j in range(i+1, len(m1)):
            a = augmented_matrix[j][i] / augmented_matrix[i][i]
            new_m1_i = []
            for el in augmented_matrix[i]:
                new_m1_i.append(a * el)
            augmented_matrix[j] = vectorsous(augmented_matrix[j], new_m1_i)
    
    for k in range(len(m1)-1, 0, -1):
        for l in range(k-1, -1, -1):
            c = augmented_matrix[l][k]/augmented_matrix[k][k]
            new_m1_i=[]
            for el in augmented_matrix[k]:
                new_m1_i.append(c*el)
            augmented_matrix[l]=vectorsous(augmented_matrix[l],new_m1_i)

    return augmented_matrix


class Matrix:
    def __init__(self,size,values ):
        self.size=size
        self.values=values


    def matrix(self):
        a=self.size
        values=self.values
        nombre_de_ligne=a[0]
        nombre_de_colonne=a[-1]
        i=0
        result=[]
        for q in range(nombre_de_ligne):
            r=[]
            result.append(r)
            for m in range(nombre_de_colonne):
                r.append(values[i])
                i+=1
        return result

    def display(self):
        a=self.matrix()
        print(a)


    
    
    def addition(self,m2):
        a=self.matrix()
        b=m2.matrix()
        if len(a[1])==len(b[1])and len(a)==len(b):
            result=[]
            for i in range(len(a)):
                r=[]
                result.append(r)
                for j in range(len(a[1])):
                    r.append(a[i][j]+b[i][j])
            return result
        
        else:
            return"please enter matrices who have teh same size"
    def soustraction(self,m2):
        a=self.matrix()
        b=m2.matrix()
        if len(a[1])==len(b[1])and len(a)==len(b):
            result=[]
            for i in range(len(a)):
                r=[]
                result.append(r)
                for j in range(len(a[1])):
                    r.append(a[i][j]-b[i][j])
            return result
        
        else:
            return"please enter matrices who have teh same size"

    def matrix_vector_mult(self,v1):
        matrix=self.matrix()
        vector=v1.matrix()
        result=[]
        for i in range(len(matrix)):
            r=0
            for j in range(len(vector)):
                r+=matrix[i][j]*vector[j][0]
            result.append(r)
    
        return result
    
    def matrixMatrixmulti(self, b):
        m2 = b.matrix()
        m1 = self.matrix()
        collonesM2 = collonesVector(m2)
        résultat = []
        for i in range(len(m1)):  
            result = []
            résultat.append(result)
            for j in range(len(m2[0])):  
                result.append(vectorvectormultiplication(m1[i], collonesM2[j]))
        return résultat
    

    


    
    def L1norm(self):
        m1=self.matrix()
        m2=collonesVector(m1)
        result=[]
    
        for i in range(len(m2)):
            r=0
            
            for j in range(len(m2[1])):
                r+=m2[i][j]
            result.append(r)
                 
        return max(result)
    
    def linfnorm(self):
        m1=self.matrix()
        result=[]
        for i in range(len(m1)):
            r=0
            
            for j in range(len(m1[1])):
                r+=m1[i][j]
            result.append(r)
                 
        return max(result)
    
    def forbeniusnorm(self):
        r1=0
        m1=self.matrix()
        for i in range(len(m1)):
            for j in range(len(m1[1])):
                r1+=(m1[i][j])**2
        return r1**(1/2)


    
class DenseMatrix(Matrix):
    def __init__(self,size,values,sparcity ):
        Matrix.__init__(self,size,values)
        self.sparcity=sparcity in ["No","N","no","n"]

class SparseMatrix(Matrix):
    def __init__(self,size,values,sparcity ):
        Matrix.__init__(self,size,values)
        self.sparcity=sparcity in ["No","N","no","n"]



    def matrix(self):
        a=self.size
        values=self.values
        nombre_de_ligne=a[0]
        nombre_de_colonne=a[-1]
        i=0
        result=[]
        for q in range(nombre_de_ligne):
            r=[]
            result.append(r)
            for m in range(nombre_de_colonne):
                r.append(values[i])
                i+=1
        return result
    
    def to_csr_with_row_info(self):
        arr = self.matrix()
        data = []  
        col_indices = []  
        row_info = [] 
        for row_index, row in enumerate(arr):
            for col_index, value in enumerate(row):
                if value != 0:
                    data.append(value)
                    col_indices.append(col_index)
                    row_info.append(row_index)  

        return data, col_indices, row_info
    
    def addition(self, m2):
        m1 = self.to_csr_with_row_info()
        m2 = m2.to_csr_with_row_info()
        couplesm1 = []
        couplesM2 = []
        i = 0
        indexM1 = []
        indexM2 = []
    
        Rez = []
        col_indices = []
        row_info = []
    
        while i < len(m1[0]):
            couplesm1.append([m1[1][i], m1[2][i]])
            indexM1.append(i)
            i += 1
        
        j = 0
        while j < len(m2[0]):
            couplesM2.append([m2[1][j], m2[2][j]])
            indexM2.append(j)
            j += 1
    
        for k in couplesm1:
            for l in couplesM2:
                if k[0] == l[0] and k[1] == l[1]:
                    m1[0][indexM1[couplesm1.index(k)]] += m2[0][indexM2[couplesM2.index(l)]]
                    break
    
        return m1
    
    def soustraction(self, m2):
        m1 = self.to_csr_with_row_info()
        m2 = m2.to_csr_with_row_info()
        couplesm1 = []
        couplesM2 = []
        i = 0
        indexM1 = []
        indexM2 = []
    
        Rez = []
        col_indices = []
        row_info = []
    
        while i < len(m1[0]):
            couplesm1.append([m1[1][i], m1[2][i]])
            indexM1.append(i)
            i += 1
        
        j = 0
        while j < len(m2[0]):
            couplesM2.append([m2[1][j], m2[2][j]])
            indexM2.append(j)
            j += 1
    
        for k in couplesm1:
            for l in couplesM2:
                if k[0] == l[0] and k[1] == l[1]:
                    m1[0][indexM1[couplesm1.index(k)]] -= m2[0][indexM2[couplesM2.index(l)]]
                    break
    
        return m1
    
    

    

            
        


        



    def forbeniusnorm(self):
        m1=self.to_csr_with_row_info()
        r=0
        for i in range(m1[1]):
            r+=i**2
        return r**(1/2)
    
    def L1norm(self):
        m1=self.to_csr_with_row_info()
        col_indices=m1[1]
        data=m1[0]
        r=[]
        for i in col_indices:
            a=search(col_indices,i)
            re=0
            for j in a:
                re+=data[j]
            r.append(re)
        return max(r)
    
    def linfnorm(self):
        m1=self.to_csr_with_row_info()
        row_indices=m1[2]
        data=m1[0]
        r=[]
        for i in row_indices:
            a=search(row_indices,i)
            re=0
            for j in a:
                re+=data[j]
            r.append(re)
        return max(r)

       