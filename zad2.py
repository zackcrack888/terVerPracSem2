# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. Какова вероятность, 
# что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?

from math import factorial

p=0.0004
n=5000
m0=0

m2=2

def puasson(n,p,m):
    return((((p*n)**m)/factorial(m))*2.72**(-p*n))

pm0=puasson(n,p,m0)*100

pm2=puasson(n,p,m2)*100

print(f'Вероятность того, что ни одна из них не перегорит в первый день = {pm0 :.2f}%')

print(f'Вероятность того, что перегорят ровно две = {pm2 :.2f}%')