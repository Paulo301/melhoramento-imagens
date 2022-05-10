import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from skimage import data, img_as_float
from skimage import exposure

matplotlib.rcParams['font.size'] = 8


def plot_img_and_hist(image, axes, bins=256):
    """Realiza o plot da imagem junto com o histograma e o histograma cumulativo"""
    image = img_as_float(image)
    ax_img, ax_hist = axes
    ax_cdf = ax_hist.twinx()

    # Mostra a imagem
    ax_img.imshow(image, cmap=plt.cm.gray)
    ax_img.set_axis_off()

    # Mostra o histograma
    ax_hist.hist(image.ravel(), bins=bins, histtype='step', color='black')
    ax_hist.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    ax_hist.set_xlabel('Pixel intensity')
    ax_hist.set_xlim(0, 1)
    ax_hist.set_yticks([])

    # Mostra a distribuicao cumulativa
    img_cdf, bins = exposure.cumulative_distribution(image, bins)
    ax_cdf.plot(bins, img_cdf, 'r')
    ax_cdf.set_yticks([])

    return ax_img, ax_hist, ax_cdf


# Carrega uma imagem de exemplo
# img = data.moon()
img = data.astronaut()

# Gamma, segundo parametro e o valor de gamma
gamma_corrected = exposure.adjust_gamma(img, 4)

# Apresentacao dos resultados
fig = plt.figure(figsize=(8, 5))
axes = np.zeros((2, 3), dtype=np.object)
axes[0, 0] = plt.subplot(2, 3, 1)
axes[0, 1] = plt.subplot(2, 3, 2, sharex=axes[0, 0], sharey=axes[0, 0])
axes[1, 0] = plt.subplot(2, 3, 4)
axes[1, 1] = plt.subplot(2, 3, 5)

ax_img, ax_hist, ax_cdf = plot_img_and_hist(img, axes[:, 0])
ax_img.set_title('Imagem original')

y_min, y_max = ax_hist.get_ylim()
ax_hist.set_ylabel('Numero de pixels')
ax_hist.set_yticks(np.linspace(0, y_max, 5))

ax_img, ax_hist, ax_cdf = plot_img_and_hist(gamma_corrected, axes[:, 1])
ax_img.set_title('Correcao Gamma')

ax_cdf.set_ylabel('Fracao da intensidade total')
ax_cdf.set_yticks(np.linspace(0, 1, 5))

# Previne que os labels do eixo y se sobreponham
fig.tight_layout()
plt.show()