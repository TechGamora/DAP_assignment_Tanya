import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv("amazon.csv")
book=pd.DataFrame(data)
bookheader=book.head(25)
bookheader.plot(x="Name",y="User Rating",kind="bar",title="Amazon Top 50 Books")
plt.show()
