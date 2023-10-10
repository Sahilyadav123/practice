import tkinter as tk
import yfinance as yf

class StockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Stock Tracking")
        
        self.label = tk.Label(root, text="Enter Stock Symbol:")
        self.label.pack()
        
        self.symbol_entry = tk.Entry(root)
        self.symbol_entry.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        self.button = tk.Button(root, text="Track", command=self.track_stock)
        self.button.pack()
        
        self.stock_symbol = ""

    def track_stock(self):
        self.stock_symbol = self.symbol_entry.get()
        
        try:
            stock_data = yf.Ticker(self.stock_symbol)
            current_price = stock_data.history(period="1d")["Close"].iloc[0]
            self.result_label.config(text=f"Current Price: {current_price:.2f} USD")
        except Exception as e:
            self.result_label.config(text="Invalid Stock Symbol or Error Fetching Data")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockApp(root)
    root.mainloop()
