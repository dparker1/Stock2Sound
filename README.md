# Stock2Sound
Draws equity prices to convert into audio tracks.

## To Use
You need an API key from [Alpha Vantage](https://www.alphavantage.co/) (They are free) in a .txt file named "Key.txt" in the same directory of main.py
```
python main.py [StockTicker]
```
Will generate a .wav file with the name [StockTicker].wav in the same directory

## Warning
Watch your sound level, as the audio may be annoying to listen to, until I find a better way to construct the frequencies from the data.