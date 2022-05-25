# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

nums = [n1, n2, n3]
nums.sort()

print('O menor valor digitado foi {}.'.format(nums[0]))
print('O maior valor digitado foi {}.'.format(nums[2]))
