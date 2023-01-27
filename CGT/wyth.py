#!env python
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

def mex(mex_set):
    ret = 0
    while ret in mex_set:
        ret += 1
    return ret

def wyth_p_positions(max_n = 10):
    mex_set = set()
    ret = []
    for n in range(max_n+1):
        a_n = mex(mex_set)
        b_n = a_n + n

        mex_set.add(a_n)
        mex_set.add(b_n)

        ret.append((a_n, b_n))
        ret.append((b_n, a_n))

    return ret

def plot():
    x,y = zip(*wyth_p_positions(30))

    phi = (1 + 5 ** 0.5) / 2

    x1 = [i for i in range(round(80/phi))]
    y1 = [phi*i for i in range(round(80/phi))]

    x2 = [i for i in range(80)]
    y2 = [i/phi for i in range(80)]

    fig, ax = plt.subplots(figsize=(10,10))
    # ax = fig.add_axes([0.1,0.1,9.9,9.9])
    # plt.title("Wythoff P Positons")
    ax.plot(x1, y1, label='$\phi \cdot x$')
    ax.plot(x2, y2, label='$1/\phi \cdot x$')
    ax.scatter(x, y, color='#222222')
    ax.legend()
    plt.show()
    fig.savefig('wyth_p_pos.jpg', bbox_inches='tight', dpi=300)

if __name__ == "__main__":
    plot()
