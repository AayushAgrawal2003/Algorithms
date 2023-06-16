# DBscan

## Density-based clustering
Can be used in the case of nested clusters, and also works in higher dimensions 

- core points: they have a certain number of x points in the vicinity
- We pick one core point and add to one cluster, we then add all core points in the vicinity of the first point and then repeat the process till we dont have any core points left in the vicinity.
- Then we add non core points in the raduis 
- Then we pick another core point not in the current cluster, this is used to make the second cluster 

- Thresholding Values: 
    - Number of points for a point to be considered core or not. 
    - Radius of the the circle to be considered.


