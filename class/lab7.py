import matplotlib.pyplot as plt
import matplotlib.image as mimg
import numpy as np

# 1 Line Plot
def plot():
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 18, 30, 22]

    plt.plot(x, y)
    plt.show()


def plot1():
    x = np.linspace(1, 50, 100)
    y = x**2
    z = x**3

    plt.plot(x, y, marker='o', linestyle='--',
             color='g', label='x^2 Data Pointers')
    plt.plot(x, z, marker='o', linestyle='-',
             color='r', label='x^3 Data Pointers')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Line Plot Example")
    plt.legend()
    plt.show()


# 2 Bar plot
def bar_plot():
    categories = ['category A', 'category B', 'category C']
    values = [25, 40, 30]

    plt.bar(categories, values, width=0.6,
            color='g', edgecolor='black', alpha=0.7)
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.title("Bar Plot Example")
    plt.grid(axis='y', linestyle="--", alpha=0.8)

    plt.show()

# 3 Scatter plot
def scat_plot():
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 18, 30, 22]

    plt.scatter(x, y, marker='o', color='r', label="Data Points")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Scatter Plot Example")
    plt.legend()
    plt.grid(True)

    plt.show()

# 4 Subplot
def subplot():
    x = [1, 2, 3, 4, 5]
    y1 = [10, 25, 18, 30, 22]
    y2 = [5, 12, 15, 8, 10]

    # Creating a 2*2 subplot grid
    # 1st subplot
    plt.subplot(2, 2, 1)
    plt.plot(x, y1, marker='o', linestyle='--',
             color='b', label='Data Points')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Line Plot")
    plt.grid(linestyle='--', alpha=0.8)

    # 2nd subplot
    plt.subplot(2, 2, 2)
    plt.plot(x, y2, color='g', alpha=0.6)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Bar Plot")
    plt.grid(linestyle='--', alpha=0.8)

    # 3rd subplot
    plt.subplot(2, 2, 3)
    plt.plot(x, y2, color='r', alpha=0.3)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Bar Plot 2")
    plt.grid(linestyle='--', alpha=0.8)

    # 4th subplot
    plt.subplot(2, 2, 4)
    plt.plot(x, y2, color='k', alpha=0.5)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Scatter Plot")
    plt.grid(linestyle='--', alpha=0.8)

    # Adjust teh spacing between subplots
    plt.tight_layout()

    plt.show()


# 5 Images as plot
def img_plot():
    img = mimg.imread("class\img.png")

    # Diaplay the iamge on a plot
    plt.imshow(img)
    plt.axis('off')
    plt.show()


plot()
plot1()
bar_plot()
scat_plot()
subplot()
