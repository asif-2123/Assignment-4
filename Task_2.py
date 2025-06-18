x="outpur.txt"

b=input('Enter text to write to the file :')
file=open('x','w')
file.write(b)
file.close()
print('Data successfully written to output.txt.')
print('\n')

c=input('Enter additional text to append:')
file=open('x','a')
file.write('\n'+c)
file.close()
print('Data succesfully appended.')
print('\n')

file=open('x','r')
result=file.read()
file.close()
print('Final content of output.txt:')
print(result)