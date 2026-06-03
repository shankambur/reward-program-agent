from services.investigation_service import investigate_submission,investigate_customer,investigate_offer


print('******* investigate_submission("SUB0001")\n')
result = investigate_submission("SUB0001")
print(result)
print("*******")

print('******* investigate_submission("SUB9999")\n')
result = investigate_submission("SUB9999")
print(result)
print("*******")

print('******investigate_customer("C1001")')
result = investigate_customer("C1001")
print(result)
print("*******")

print('******investigate_customer("C9999")')
result = investigate_customer("C9999")
print(result)
print("*******")

print('******investigate_offer("OFF600")')
result = investigate_offer("OFF600")
print(result)
print("*******")

print('******investigate_offer("OFF999")')
result = investigate_offer("OFF999")
print(result)
print("*******")
