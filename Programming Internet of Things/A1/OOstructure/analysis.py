import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 
import seaborn as sns

def seabornPlot():
    conn = sqlite3.connect("sensehat.db")
    df = pd.read_sql_query("SELECT date(timestamp) as date, AVG(temperature) as avgTemp from sensehat_data group by timestamp", conn)
    sns.barplot(x='date', y='avgTemp', data=df)
    plt.tick_params(axis='x', which='major', labelsize=6)
    plt.savefig('sebornplot.png', dpi=400)
  

    plt.clf()
    conn.close()

def plotTempVsHumid():
    conn = sqlite3.connect("sensehat.db")
    matplot = pd.read_sql_query("SELECT date(timestamp) as date, MIN(temperature) as minTemp, MAX(temperature) as maxTemp from sensehat_data group by timestamp", conn)
    plt.plot(matplot.date, matplot.minTemp)
    plt.plot(matplot.date, matplot.maxTemp)
    plt.legend(['Temperature'], ['Humidity (as a %)'])
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.tick_params(axis='x', which='major', labelsize=6)
    plt.savefig('matplotlib.png', dpi=400)

    plt.clf()
    conn.close()

def main():
    plotTempVsHumid()
    seabornPlot()


if __name__ == "__main__":
    main()

