from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    fig, ax = plt.subplots(1,1, figsize=(10,6))
    ax.set_title('Time-voltage graph')
    ax.set_xlabel("Time")
    ax.set_ylabel("Voltage")
    ax.grid(True)
    plt.plot(time, voltage)
    plt.show()

def plot_hist(time):
    fig, ax = plt.subplots(1,1, figsize=(10,6))
    plt.hist(time)
    plt.xlim(0, 0.06)
    ax.set_title('Time Hist')
    ax.set_xlabel("Time periods")
    ax.set_ylabel("Amount of measurements")
    ax.grid(True)
    plt.show()