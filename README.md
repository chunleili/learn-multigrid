#多重网格法加速高斯赛德尔的练习

基于numpy

改自
https://zhuanlan.zhihu.com/p/337970166

多重网格(Multigrid)是一种加速迭代法的方法。它可以和任何迭代法结合使用。其基本原理是通过在不同粗细程度的网格上来回迭代，以消除残差中的长波分量和短波分量。


GS.py中运行的是Gauss-Seidel迭代的结果

下图展示的是不同迭代次数的残差。x坐标为原PDE中的自变量x，y坐标为残差。可见长波残差并未被消除。

![](/img/resi-wave.png)

下图展示的是收敛曲线。x坐标为迭代次数，y坐标为残差。需要2579次迭代收敛至残差小于1e-3

![](/img/converge-curve-GS.png)


MG.py中运行的是Multigrid加速GS之后的结果。每次V-cycle需要10次GS。

因此只需要40次迭代即可收敛至1e-3。
![](/img/converge-curve-MG.png)
