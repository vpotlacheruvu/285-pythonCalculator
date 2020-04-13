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

                Comm = BuyComm + SellComm
                Proceeds = Allotment * FinSharePrice
                CostBasis = Allotment * IniSharePrice
               
                TotCostBasis = CostBasis + Comm              
                Gains = Proceeds - TotalCostBasis
                GainsTax = Gains*(CapGainTaxRate/100)
                
                FinGains = Gains - GainsTax
                FinCostBasis = CostBasis + Comm + GainsTax
                
                ROI = ((FinalGains - CostBasis)/CostBasis)*100
                
                BreakEvenPrice = TotCostBasis / 100
                 
                # PROFIT REPORT:
           
            args = {"form": form, 
                    "Proceeds": "{:,.2f}".format(Proceeds), 
                    "Cost": "{:,.2f}".format(FinalCostBasis), 
                    "TotPurchasePrice": "{:,.2f}".format(CostBasis),
                    "BuyComm": "{:,.2f}".format(BuyComm), 
                    "SellComm": "{:,.2f}".format(SellComm),
                    "TaxOnCapGain": "{:,.2f}".format(GainsTax), 
                    "NetProfit": "{:,.2f}".format(FinGains), 
                    "ROI": "{:,.2f}".format(ROI),
                    "ToBreakEven": "{:,.2f}".format(BreakEvenPrice),
                    "Allotment": "{:,.0f}".format(Allotment), 
                    "IniSharePrice": "{:,.0f}".format(IniSharePrice), 
                    "FinSharePrice": "{:,.0f}".format(FinSharePrice), 
                    "capGain": "{:,.2f}".format(Gains)}

        return render(request, "result.html", args)
