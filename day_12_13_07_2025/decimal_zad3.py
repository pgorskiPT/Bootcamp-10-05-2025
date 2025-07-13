from decimal import localcontext, getcontext, Decimal, ROUND_DOWN

print(getcontext().rounding)  # np. ROUND_UP z poprzedniego przykładu

with localcontext() as ctx:
    ctx.rounding = ROUND_DOWN
    value = Decimal('2.3456').quantize(Decimal('0.01'))
    print("W lokalnym kontekście:", value)  # np. 2.34

# Po wyjściu z bloku, globalny kontekst pozostaje niezmieniony
print("W globalnym kontekście:", Decimal('2.3456').quantize(Decimal('0.01')))
# ROUND_HALF_EVEN
# W lokalnym kontekście: 2.34
# W globalnym kontekście: 2.35