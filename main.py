# Импорт sdk с вашей папки где находится main.py

from crystalpay_sdk import *
from crystalpay_sdk import CrystalPAY, PayoffSubtractFrom, InvoiceType

crystalpayAPI = CrystalPAY("auth_login", "secret_key", "secret_key2")

invoice = crystalpayAPI.Invoice.create(100, InvoiceType.purchase, 15, redirect_url="zelenka.guru/suck666suck")


payment_link = invoice.get("url")
amount = invoice.get("amount")


print(f"Ссылка на оплату - {payment_link}\nПлатёж на сумму {amount}")
print("")

BalanceGetInfo = crystalpayAPI.Balance.getinfo(hide_empty=False)

amountlzt = BalanceGetInfo.get("LZTMARKET", {}).get("amount", 0)
currencylzt = BalanceGetInfo.get("LZTMARKET", {}).get("currency", "RUB")

print(f"Баланс Кассы:\n\nLZTMARKET: {amountlzt} {currencylzt} рублей")
