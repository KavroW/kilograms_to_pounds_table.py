x = 0
kg = 1
lb = 2.2
lb2 = 20
kg2 = 9.09
kg_label = 'Kilograms'
lb_label = 'Pounds'
line = '|'
print(f'{kg_label:<10s} {lb_label:<8s} {line:^10} {lb_label:<10s} {kg_label:<10s}')
for x in range(1,101,1):
    print(f'{kg:<10d} {lb:<8.1f} {line:^10} {lb2:<10} {kg2:<10.2f}')
    kg += 2
    lb += 4.4
    lb2 += 5
    kg2 = lb2/2.2