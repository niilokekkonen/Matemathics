import math, time

#Simple version 1.0

class Math:
    def __init__(self):
       self.a = None
       self.b = None
       self.c = None
       self.gamma_deg = 90.0
       self.gamma_rad = math.radians(self.gamma_deg)

    #Calculates the missing side of a triangle
    def Pythagorean(self):
       
        print('Do you want to use the pythagorean theroem? ' \
        '\nSoon you can enter the lengths of the sides' )
        question = str(input('answer yes or no, please\n')).strip().lower()


        if question == 'yes':
            print('Type yes or no.')
            ans_a = str(input('a?\n'))
            ans_b = str(input('b?\n')) 
            ans_c = str(input('c?\n'))
            print(ans_a,ans_b,ans_c)

            # a^2 + b^2 = c^2
            if ans_a == 'yes':
               if ans_b == 'yes':               
                    a = float(input('Enter side a:'))
                    b = float(input('Enter side b:'))
                    print(f'side a: {a}\nside b: {b}')
                    self.a = a
                    self.b = b
                    self.c = None

                    try:
                        if self.a is not None:
                            if self.b is not None:
                                if self.c is None:

                                    c = math.sqrt(self.a**2 + self.b**2)
                                    print(f'The length of the hypotenus{c}')
                                    self.c = c

                                    quest2 = str(input('Do you want to know all the angles?\n'))
                                    if quest2 == 'yes':
                                        alpha_rads = math.atan(self.a/self.b)
                                        beta_rads = math.atan(self.b/self.a)
                                    
                                        alpha_deg = math.degrees(alpha_rads)    
                                        beta_deg = math.degrees(beta_rads)


                                        result = {
                                            'alpha':{'radians': alpha_rads, 
                                                     'degrees' : alpha_deg },

                                            'beta':{'radians': beta_rads, 
                                                     'degrees' : beta_deg },
                                            'gamma':{'radians': self.gamma_rad,
                                                     'degrees': self.gamma_deg}
                                        }
                                        
                                        print(f'Alpha results: {result['alpha']}')
                                        print(f'Beta results: {result['beta']}')
                                        print(f'Gamma results: {result['gamma']}')


                                    
                                    

                    except Exception as e:
                       print('Error', e)


        else:
            print('going back....')
            
                
            
 
               
       
       



#c = float(input('Enter side c'))




#Main program
calc_pythagorean = False

obj = Math()

print('Do you want to calculate the pythagorean theorem\nor know the angles of your right triangle?')
main_quest = str(input('sure?\n'))
if main_quest == 'sure':
    calc_pythagorean = True
    while calc_pythagorean:
        obj.Pythagorean()
        calc_pythagorean = False
