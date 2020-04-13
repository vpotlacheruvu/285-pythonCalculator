from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from .forms import Calculator


# Create your views here.

class CalculatorView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        form = Calculator()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = Calculator(request.POST)
            if form.is_valid():
                TickerSymbol = form.cleaned_data['TickerSymbol']
                Allotment = form.cleaned_data['Allotment']
                FinSharePrice = form.cleaned_data['FinSharePrice']
                SellComm = form.cleaned_data['SellComm']
                IniSharePrice = form.cleaned_data['IniSharePrice']
                BuyComm = form.cleaned_data['BuyComm']
                CapGainTaxRate = form.cleaned_data['CapGainTaxRate']

                # PROFIT REPORT:
                Proceeds = Allotment * FinSharePrice

            capGain = ((FinSharePrice * Allotment) - SellComm) - \
                      ((IniSharePrice * Allotment) + BuyComm)

            Cost = (Allotment * IniSharePrice + (SellComm +
                                                 BuyComm) + (CapGainTaxRate / 100) * capGain)

            TotPurchasePrice = Allotment * IniSharePrice

            TaxOnCapGain = (CapGainTaxRate / 100) * capGain

            NetProfit = Proceeds - Cost

            ROI = NetProfit / Cost * 100			

            ToBreakEven = ((Allotment * IniSharePrice) +
                           BuyComm + SellComm) / 100

            args = {"form": form, "Proceeds": Proceeds, "Cost": Cost, "TotPurchasePrice": TotPurchasePrice,
                    "BuyComm": BuyComm, "SellComm": SellComm,
                    "TaxOnCapGain": TaxOnCapGain, "NetProfit": NetProfit, "ROI": ROI, "ToBreakEven": ToBreakEven,
                    "Allotment": Allotment, "IniSharePrice": IniSharePrice, "FinSharePrice": FinSharePrice, "capGain": capGain,}

        return render(request, "result.html", args)
