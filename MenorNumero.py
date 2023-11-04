#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Faça um programa que leia 3 números inteiros e mostre o menor deles.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

print(num1, num2, num3) 

menor_numero = num1

if num2 < menor_numero:
    menor_numero = num2
if num3 < menor_numero:
    menor_numero = num3

print(f"O menor número é: {menor_numero}")