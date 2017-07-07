import numpy as np
import matplotlib.pyplot as plt

N = 101  # Number of elements
T0 = 0  # Ambient temperature

# defining the analysis sample (the whole copper bar)
lenght = 1  # [m]
width = 0.01  # [m]
height = 0.1  # [m]

elementsPos = np.linspace(0.5*lenght/N, lenght, N)

Cu_th_cond = 400  # [W/m2K]

inQ = 100  # [W] Input power

# Preparation calculations
Xsec = width * height  # [m*m]
Area = 2 * (width + height) * lenght / N  # [m2]

inGc = 12 * Area  # Convectional admitance to ambient
inG = Cu_th_cond * Xsec / (lenght / N)   # Thermal conduction admitance between elements

# Thermal conductance vectors (for easier reference in matrix generation)
G = np.ones(N) * inG
G[N-1] = 0  # Cleaning to 0 the end element - as it dosnt conduct off system

# Vector of convection for all elements
Gc = np.ones(N) * inGc

Q = np.ones(N) * inGc * T0   # Preparing free elelments vector
# Q[int(3*N/4)] += inQ  # Seting up the middle element as the one with power losses
Q[N // 2] += inQ


def getGmatrix(n):
    ''' This function is about to return the generated matrix for
    thermal equation'''

    MATRIX = np.zeros((n, n), dtype=float)

    for Row in range(n):
        for Col in range(n):

            nx = Row

            if Row == Col:
                MATRIX[Row][Col] = G[nx] + Gc[nx]
                if Col > 0:
                    MATRIX[Row][Col] += G[nx - 1]

            elif Col == Row - 1:
                MATRIX[Row][Col] = -G[nx - 1]

            elif Col == Row + 1:
                MATRIX[Row][Col] = -G[nx]
    return MATRIX


def SMDD(matrixList):
    size = 0
    for m in matrixList:
        size += m.shape[0]

    megaMacierz = np.zeros((size, size), dtype=float)

    actualRow = 0
    for m in matrixList:

        m_size = m.shape[0]
        megaMacierz[actualRow:actualRow+m_size, actualRow:actualRow+m_size] = m

        actualRow += m_size

    return megaMacierz, size

M = getGmatrix(N)

T = np.linalg.solve(M, Q)

NoweM, s = SMDD([M, M])
NoweQ = np.concatenate((Q, Q), axis=0)

noweT = np.linalg.solve(NoweM, NoweQ)
print(M)
print(NoweM)

plt.plot(T)
plt.plot(noweT)
plt.show()
