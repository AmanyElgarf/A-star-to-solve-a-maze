import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



forward = [36557, 136875
,26579
,65414
,6095
,18102
,25974
,10020
,16828
,31
,5140
,578
,4852
,278
,780
,35918
,24687
,330
,38085
,8409
,178481
,10966
,29479
,5141
,14787
,965
,49248
,6928
,67890
,47605
,31545
,6066
,83483
,51049
,18782
,21582
,12039
,290
,2802
,509
,80876
,6771
,76422
,195485
,29276
,48442
,20934
,10507
,114261
,102511]


forwardSG = [54943
,142663
,26781
,78184
,7021
,18379
,29020
,10702
,19305
,105
,6095
,3883
,4887
,332
,876
,41418
,38513
,402
,41815
,27257
,181520
,15229
,35125
,26127
,21645
,1271
,60615
,8647
,86437
,73203
,38255
,7739
,90932
,63591
,19103
,33673
,7279
,346
,2888
,421
,73182
,7250
,52097
,188779
,16407
,54267
,25101
,10691
,88030
,62513]

backward = [54998
,200960
,55145
,92999
,9922
,19527
,25160
,13795
,21686
,83
,8031
,852
,10616
,456
,1082
,74265
,40740
,432
,51424
,37150
,220799
,17422
,90289
,11867
,18134
,773
,31367
,12657
,114624
,59010
,35929
,6405
,103819
,78750
,21290
,38096
,11510
,352
,4854
,925
,134051
,8603
,56789
,337103
,14438
,59727
,18034
,15533
,143396
,103983]

adaptive=[
25243
,135388
,21151
,32982
,5261
,6708
,24007
,6429
,15165
,25
,5020
,515
,3129
,261
,705
,34366
,22151
,281
,24662
,7388
,128572
,10751
,19127
,4845
,13162
,882
,22235
,5950
,62054
,39828
,3413
,5024
,79257
,45068
,7348
,24714
,9812
,232
,3003
,470
,100933
,7448
,91777
,224892
,30977
,53550
,21431
,8228
,120920
,48060
]

plt.hist(forward, density=False, edgecolor='black', color = 'c', bins=50)
plt.title("Repeated Forward A*")
plt.xlabel('number of expanded nodes')
plt.axvline(sum(forward)/len(forward), color='b', linestyle='dashed', linewidth=3)
plt.ylabel('number of mazes')
plt.show()


plt.hist(forwardSG, density=False, edgecolor='black', color = 'c', bins=50)
plt.title("Repeated Forward A* in favor of smaller g value")
plt.xlabel('number of expanded nodes')
plt.axvline(sum(forwardSG)/len(forwardSG), color='b', linestyle='dashed', linewidth=3)
plt.ylabel('number of mazes')
plt.show()

plt.hist(backward, density=False, edgecolor='black', color = 'c', bins=50)
plt.title("Repeated Backward A*")
plt.xlabel('number of expanded nodes')
plt.axvline(sum(backward)/len(backward), color='b', linestyle='dashed', linewidth=3)
plt.ylabel('number of mazes')
plt.show()

plt.hist(adaptive, density=False, edgecolor='black', color = 'c', bins=50)
plt.title("Repeated Adaptive A*")
plt.xlabel('number of expanded nodes')
plt.axvline(sum(adaptive)/len(adaptive), color='b', linestyle='dashed', linewidth=3)
plt.ylabel('number of mazes')
plt.show()