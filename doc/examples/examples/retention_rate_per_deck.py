grouped = col.cards.groupby("cdeck")
data = grouped.mean()["civl"].sort_values().tail()
ax = data.plot.barh()
ax.set_ylabel("Deck name")
ax.set_xlabel("Average expected retention length/review interval [days]")
ax.set_title("Average retention length per deck")
