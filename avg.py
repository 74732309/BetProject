a = float(input('Enter the first note: '))
b = float(input('Enter the second note: '))
c = float(input('Enter the third note: '))

def func(c):
     nf = (c + b) / 2
     print('The smallest note is {}'.format(a))
     print('The average is {}'.format(nf))
     x = nf - 5.75
     if x > 5.75:
             print('Approved Student.')
     else:
             print('Failed Student.')

nf = (c + b) / 2
if a < b:
      if a < c:
         nf = (c + b) / 2
         print('The smallest note is {}'.format(a))
         print('The average is {}'.format(nf))
         x = nf - 5.75
         if x > 5.75:
             print('Approved Student.')
         else:
             print('Failed Student.')

      else:
         nf = (a + b) / 2
         new_func(c)
         print('The average is {}'.format(nf))
         x = nf - 5.75
         if x > 5.75:
             print('Approved Student.')
         else:
             print('Failed Student.')

else:
     if b < c:
         nf = (a + c) / 2
         print('The smallest note is {}'.format(b))
         print('The average is {}'.format(nf))
         x = nf - 5.75
         if x > 5.75:
             print('Approved Student.')
         else:
             print('Failed Student.')

     else:
         x = nf - 5.75
         if x > 5.75:
             print('Approved Student.')
         else:
             print('Failed Student.')

         nf = (a + b) / 2
         print('The smallest note is {}'.format(c))
         print('The average is {}'.format(nf))



