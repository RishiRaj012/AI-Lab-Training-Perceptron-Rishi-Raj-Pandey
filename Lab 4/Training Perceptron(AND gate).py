def threshold(inp, th):
    return 1 if inp >= th else 0
ds = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]
lr = 0.1 
th = 0.5  
w = [0.6, 0.7] 
epoch = 0
while True:
    tf = False  
    epoch += 1
    print(f"EPOCH: {epoch}")
    print("W1\tW2\tX1\tX2\tTg\tY\tError\tdW1\tdW2\tNewW1\tNewW2")
    for x1, x2, target in ds:
        inp = x1 * w[0] + x2 * w[1]
        y = threshold(inp, th)
        err = target - y

        if err != 0:
            tf = True
        dw1 = lr * x1 * err
        dw2 = lr * x2 * err
        print(f"{w[0]:.2f}\t{w[1]:.2f}\t{x1}\t{x2}\t{target}\t{y}\t{err:.2f}\t{dw1:.2f}\t{dw2:.2f}", end="\t")
        w[0] += dw1
        w[1] += dw2
        print(f"{w[0]:.2f}\t{w[1]:.2f}")
    print("--------------------------------------------------------------------------------------------------" )
    if not tf:
        break
print(f"Training Complete after {epoch} epochs.")
