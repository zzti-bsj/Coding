"""
模型训练过程，循环：
1. 前向传播
2. 反向传播
3. 更新参数

"""

x, y_true = 3.0, 100.0
w1, w2 = 3.0, 5.0
lr = 0.0001

for step in range(200):
    # 1. 前向传播：算预测、算loss，留下中间值 a1
    a1 = w1 * x
    pred = w2 * a1
    loss = (pred - y_true) ** 2
    
    # 2. 反向传播：从loss往回追责，算出每个参数的梯度；
    dpred = 2 * (pred - y_true)
    dw2 = dpred * a1
    da1 = dpred * w2
    dw1 = da1 * x
    
    # 3. 参数更新：沿梯度反方向微调
    w1 -= lr * dw1
    w2 -= lr * dw2

    print(f"step={step:3d}  loss={loss:10.4f}  w1={w1:.3f}  w2={w2:.3f}  w1*w2={w1*w2:.3f}")
        
print("\n最终预测:", w1 * w2 * x, " 目标:", y_true)