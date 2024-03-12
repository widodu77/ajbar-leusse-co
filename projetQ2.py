def vectorvectormultiplication(v1,v2):
    result=0
    for i in range(len(v1)):
        result += v1[i]*v2[i]
    return result 

def collonesVector(m1):
    résultat = []
    for i in range(len(m1[0])):  # Corrected to iterate over columns
        result = []
        for j in range(len(m1)): 
            result.append(m1[j][i])
        résultat.append(result)
    return résultat

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


  


