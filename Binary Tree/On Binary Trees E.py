
""" 
Disclaimer :

The first two solutions are copied from online as I needed to grasp the concept of Binary Tree and those of Object-Oriented Programming
"""

######### Depth of a Binary Tree ########### ########### ########### ########### ########### ########### ########### ########### ###########

class Solution:
    def maxDepth(self, root) -> int:
        if root == None:
            return 0
        ld = self.maxDepth(root.left)           #the keyword self if fundamental otherwise Python is looking for a global funtion called maxDepth and not the maxDepth we are working on
        rd = self.maxDepth(root.right)
        return 1 + max(ld,rd)
    
######### Same Binary Tree ########### ########### ########### ########### ########### ########### ########### ########### ########### ########### ###########

class Solution:
    def isSameTree(self, p,q) -> bool:
        if not p and not q:
            return True

            # 2. Cas de base 2: L'un est None et l'autre ne l'est pas, OU les valeurs sont différentes -> Différents.
        if not p or not q or p.val != q.val:
            return False

        # 3. Récursion: Vérifier la symétrie pour les sous-arbres gauche et droit.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

######### Inverted Binary Tree ########### ########### ########### ########### ########### ########### ########### ########### ########### ########### ###########

class Solution:
    def invertTree(self, root):
        if root == None:                    #Typical Case
            return None

        root.left,root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root                     #the return root is necessary to correctly linked all of the nodes together
                                        #to invert a Tree, you would write afterwards "inverted = invertTree(root)" where 'inverted' is the root of the new inverted tree
    

""" (French)
Dans les algorithmes récursifs sur les arbres, le return root est nécessaire pour que chaque nœud traité SE LIE CORRECTEMENT 
en tant qu'enfant au niveau supérieur de l'arbre, garantissant ainsi que l'arbre entier, y compris la nouvelle racine, soit 
complètement chaîné à la fin de l'exécution.
"""
    
######### Symmetric Binary Tree ########### ########### ########### ########### ########### ########### ########### ########### ########### ###########

class Solution:
    def isSameTree(self, p,q) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def invertTree(self, root) :
        if root == None:                
            return None

        root.left,root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root 

    def isSymmetric(self, root) -> bool:
        if root == None:
            return True

        return self.isSameTree(self.invertTree(root.right),root.left)

#Another solution :
class Solution:
    def isSymmetric(self, root) -> bool:
        
        def is_mirror(n1, n2): # n1:left, n2:right
            if not n1 and not n2:
                return True
            
            if not n1 or not n2:
                return False
            
            return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)
        
        return is_mirror(root.left, root.right)


######### 112. Path Sum ########### ########### ########### ########### ########### ########### ########### ########### ########### ########### ########### ###########

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if root == None:
            return False
        
        if root.right == root.left == None:
            return targetSum == root.val            #C'est bien targetSum == root.val et pas targetSum == 0 (attention au décalage)
        
        return self.hasPathSum(root.left, targetSum - root.val) or  self.hasPathSum(root.right, targetSum - root.val)   #On regarde à droite et à gauche s'il y a un chemin
    


############### 637. Average of Levels in Binary Tree ########################################################################################################################
class Solution:
    def averageOfLevels(self, root):

        from numpy import mean
        if root == None:
            return [0]
        
        distance = {root : 0}
        queue = [root]
        while queue:                                            #Le niveau de chaque noeud sera déterminé par sa distance à la racine
            traiter = queue.pop()
            if traiter.right:
                distance[traiter.right] = distance[traiter] + 1
                queue.append(traiter.right)
            if traiter.left:
                distance[traiter.left] = distance[traiter] + 1
                queue.append(traiter.left)
                    

        L = [[] for i in range(max(distance.values())+1)]
        for i in distance:
            L[distance[i]].append(i.val)
 
        Lmean = [mean(L[i]) for i in range(len(L))]

        return Lmean

## Another quicker solution using the Collections library 
from collections import deque
def averageOfLevels(self, root):  
        res = []
        if root == None:
            return res
            
        dq = deque()
        dq.append(root)

        while (len(dq) > 0):
            l = len(dq)
            s = 0
            for i in range(0, l):
                n = dq.popleft()
                s += n.val
                if n.left != None:
                    dq.append(n.left)
                if n.right != None:
                    dq.append(n.right)
            res.append(s / l)
        
        return res

class Solution:
    def getMinimumDifference(self, root) -> int:
        if root == None:
            return 0
        
        if root.left and root.right:
            mymin = min(root.val - root.left.val, root.right.val - root.val)
            return min(mymin,self.getMinimumDifference(root.left), self.getMinimumDifference(root.right))
    
        if root.left and not root.right:
            mymin = root.val - root.left.val
            return min(mymin,self.getMinimumDifference(root.left))
            

        if root.right and not root.left:
            mymin = root.right.val - root.val
            return min(mymin,self.getMinimumDifference(root.right))

        if not root.right and not root.left:   # on arrive au bout de l'arbre donc on s'arrête 
            return float('inf')