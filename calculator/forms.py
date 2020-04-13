from django import forms

class Calculator(forms.Form):
    TickerSymbol = forms.CharField(label='Ticker Symbol')
    Allotment = forms.FloatField(label='Allotment')
    FinSharePrice = forms.FloatField(label='Final Share Price')
    SellComm = forms.FloatField(label='Sell Commission')
    IniSharePrice = forms.FloatField(label='Initial Share Price')
    BuyComm = forms.FloatField(label='Buy Commission')
    CapGainTaxRate = forms.FloatField(label='Capital Gain Tax Rate (%)')