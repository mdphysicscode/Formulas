import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 定義運動方程
def free_fall(y, t, m, b, g):
    y0, y1 = y
    y2 = -b/m * y1 - g
    return [y1, y2]

# 定義初始條件
y0 = [100, 0]   # 初始高度為 100 米，初速度為 0
t = np.linspace(0, 30, 1001)   # 時間軸

# 定義物理參數
m = 0.5     # 質量
b = 0.1     # 空氣阻力係數
g = 9.8     # 重力加速度

# 求解運動方程
sol = odeint(free_fall, y0, t, args=(m, b, g))

# 繪製圖形
plt.plot(t, sol[:, 0], 'b', label='y(t)')
plt.plot(t, sol[:, 1], 'g', label='v(t)')
plt.legend(loc='best')
plt.xlabel('Time (s)')
plt.grid()
plt.show()
