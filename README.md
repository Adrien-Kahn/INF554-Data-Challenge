# INF554-Data-Challenge

`abstracts.txt` is too large for git so we will assume that it is available at `../abstracts.txt`.

- Distinguer mots techniques et mots pas techniques
- "One-hot encoding" avec les mots qui apparaissent beaucoup
- Centralité
- Comptabiliser les différentes déclinaisons d'un mot comme un même mot ("MSE" et "Mean Square Error") 

- Cluster with spectral clustering (MINCUT not so cool it seems) and perform learning locally on each cluster
- An interesting feature could be the number of clusters an author connects to
- Look at sigma ?
- Directly use SpectralClustering ?
- If too expensive, clustering can be achieved by looking at subgraphs. Be careful that the first eigenvalues will be 0 corresponding to very small connected components which are thus not very relevant.

Interesting paper (cc Michalis):
https://arxiv.org/pdf/2104.05562.pdf