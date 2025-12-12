import math, time


#Simple version 1.0

class Triangle:
    def __init__(self, a=None, b=None, c=None):
       self.a = a
       self.b = b
       self.c = c
       self.alpha = None
       self.beta = None
       self.gamma_deg = 90.0
       self.gamma_rad = math.radians(self.gamma_deg)

    #Calculates the missing side of a triangle
    def Pythagorean(self):
        #a^2 + b^2 = c^2
        if self.a is not None:
            if self.b is not None:
                if self.c is None:

                    c = math.sqrt(self.a**2 + self.b**2)
                    print(f'The length of the hypotenuse is: {c:.2f}')
                    self.c = c

                    
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
                                    
                    return result

                else:
                    return None

        #a^2 = c^2 - b^2
        if self.a is None:
            if self.b is not None:
                if self.c is not None:

                    a = math.sqrt(self.c**2 - self.b**2)
                    print(f'The length of the opposite side is: {a:.2f}')
                    self.a = a

                    
                    alpha_rads = math.acos(self.b/self.c)
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

                    return result
                else:
                    return None

                                    

                 
            


        if self.a is not None:
            if self.b is None:
                if self.c is not None:

                    b = math.sqrt(self.c**2 - self.a**2)
                    print(f'The length of the adjacent side is: {b:.2f}')
                    self.b = b
                
            
                    alpha_rads = math.acos(self.b/self.c)
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
                                        
                                                

                    return result
                else: 
                    return None
            
                
    #Calculates the sides if only one side and an angle is known        
    def one_side(self, alpha=None, beta=None, radians=False):
        use_alpha = False
        use_beta = False
        
        if alpha is not None:
            angle = alpha if radians else math.radians(alpha)
            use_alpha = True
        elif beta is not None:
            angle = beta if radians else math.radians(beta)
            use_beta = True


        #Calculating the other side
        if self.a is not None:
            if self.b is None:
                if self.c is None:
                    if use_alpha: 
                        #Alpha angles calculations
                        c = self.a/math.sin(angle)
                        self.c = float(c)
                        print(f'C side is: {self.c:.3f}')
                        b = self.c * math.cos(angle)
                        self.b = float(b)
                        print(f'B side is: {self.b:.3f}')
                        beta = 90 - math.degrees(angle) 
                        print(beta, ' Degrees')
                        #Beta angles calculations
                    elif use_beta:
                        b = self.a * math.tan(angle)
                        self.b = b
                        print(f'B side is: {self.b:.3f}')
                        c = self.a / math.cos(angle)
                        self.c = float(c)
                        print(f'C side is: {self.c:.3f}')
                        alpha = 90 - math.degrees(angle) 
                        print(alpha, ' Degrees')

        if self.a is None:
            if self.b is not None:
                if self.c is None:
                    if use_alpha: 
                        #Alpha angles calculations
                        a = self.b * math.tan(angle)
                        self.a = float(a)
                        print(f'A side is: {self.a:.3f}')
                        c = self.b / math.cos(angle)
                        self.c = float(c)
                        print(f'B side is: {self.b:.3f}')
                        beta = 90 - math.degrees(angle) 
                        print(beta, ' Degrees')
                        #Beta angles calculations
                    elif use_beta:
                        a = self.b / math.tan(angle)
                        self.a = a
                        print(f'A side is: {self.a:.3f}')
                        c = self.b / math.sin(angle)
                        self.c = float(c)
                        print(f'C side is: {self.c:.3f}')
                        alpha = 90 - math.degrees(angle) 
                        print(alpha, ' Degrees')
                     
        if self.a is  None:
            if self.b is None:
                if self.c is not None:
                    if use_alpha: 
                        #Alpha angles calculations
                        a = self.c * math.sin(angle)
                        self.a = a
                        print(f'A side is: {self.a:.3f}')
                        b = self.c * math.cos(angle)
                        self.b = float(b)
                        print(f'B side is: {self.b:.3f}')
                        beta = 90 - math.degrees(angle) 
                        print(beta, ' Degrees')
                        #Beta angles calculations
                    elif use_beta:
                        a = self.c * math.cos(angle)
                        self.a = a
                        print(f'A side is: {self.a:.3f}')
                        b = self.c * math.sin(angle)
                        self.b = float(b)
                        print(f'B side is: {self.b:.3f}')
                        alpha = 90 - math.degrees(angle) 
                        print(alpha, ' Degrees')
                                  
                           

def pretty_dict(d_i_c_t):
    data = d_i_c_t
    for k, v in data.items():
        print(f'{k}:{v}')
        
    

       







#Main program
calc_pythagorean = False
calc_sides = False
calc = True

obj = Triangle()

while calc: 
    print("Welcome to the calculator")
    choice = str(input('Pythagorean theorem = 1\nRight triangle calc = 2\n')).strip()
    print('Press enter if you need to skip :)')
    time.sleep(1)
    print('please enter the sides as shown, thanks!')
    if choice == '1':
        print('What sides of the triangle you know?')
        known = input('ab or ac or bc?\n').strip().lower()
        #a and b sides
        if 'a' in known and 'b' in known:
            val = input('Enter the value of side a:\n')
            val2 = input('Enter the value of side b:\n')
            a = float(val)
            b = float(val2)
            save = Triangle(a = a, b = b)
            res = save.Pythagorean()
            pretty_dict(res)
          
        #b and c sides
        elif 'b' in known and 'c' in known:
            val = input('Enter the length of side b:\n')
            val2 = input('Enter the length of side c:\n')
            b = float(val)
            c = float(val2)
            save = Triangle(b=b, c=c)
            res = save.Pythagorean()
            pretty_dict(res)            
        #a and c sides
        elif 'a' in known and 'c' in known:
            val = input('Enter the length of side a:\n')
            val2 = input('Enter the length of side c:\n')
            a = float(val)
            c = float(val2)    
            save = Triangle(a=a, c=c)
            res = save.Pythagorean()
            pretty_dict(res)
        else:
            print('Wrong input:')   
    elif choice == '2':
        print('What side of the triangle you know?')
        known = input('a or b or c?\n').strip().lower()
        print('please enter the side as shown, thanks!')
        
        if 1 < len(known) < 1:
            print('Wrong input...')
        
        if 'a' in known:
            choice = input('Enter the length of a:\n')
            a = float(choice)
            save = Triangle(a=a)
            angle = str(input('Do you know the alpha[1] or beta[2] angle?\n')).strip()
            rads_or_degs = str(input('Do you want to enter the angle in radians[r]\nor\ndegrees[d]?')).strip().lower()
            if rads_or_degs == 'r':
                num = float(input('Enter the size of the angle:\n'))
                rads = True
                degs = False
            elif rads_or_degs == 'd':
                num = float(input('Enter the size of the angle:\n'))
                degs = True
                rads = False
            if angle == '1':
                if rads:
                    save.one_side(alpha=num, radians=True)
                else:
                    save.one_side(alpha=num, radians=False)
            if angle == '2':
                if rads:
                    save.one_side(beta=num, radians=True)
                else:
                    save.one_side(beta=num, radians=False)
        elif 'b' in known:
            choice = input('Enter the length of b:\n')
            b = float(choice)
            save = Triangle(b=b)
            angle = str(input('Do you know the alpha[1] or beta[2] angle?\n')).strip()
            rads_or_degs = str(input('Do you want to enter the angle in radians[r]\nor degrees[d]?')).strip().lower()
            if rads_or_degs == 'r':
                num = float(input('Enter the size of the angle:\n'))
                rads = True
                degs = False
            elif rads_or_degs == 'd':
                num = float(input('Enter the size of the angle:\n'))
                degs = True
                rads = False
            if angle == '1':
                if rads:
                    save.one_side(alpha=num, radians=rads)
                else:
                    save.one_side(alpha=num, radians=False)
            if angle == '2':
                if rads:
                    save.one_side(beta=num, radians=rads)
                else:
                    save.one_side(beta=num, radians=False)
        elif 'c' in known:
            choice = input('Enter the length of c:\n')
            c = float(choice)
            save = Triangle(c=c)
            angle = str(input('Do you know the alpha[1] or beta[2] angle?\n')).strip()
            rads_or_degs = str(input('Do you want to enter the angle in radians[r]\nor\ndegrees[d]?')).strip().lower()
            if rads_or_degs == 'r':
                num = float(input('Enter the size of the angle:\n'))
                rads = True
                degs = False
            elif rads_or_degs == 'd':
                num = float(input('Enter the size of the angle:\n'))
                degs = True
                rads = False
            if angle == '1':
                if rads:
                    save.one_side(alpha=num, radians=rads)
                else:
                    save.one_side(alpha=num, radians=False)
            if angle == '2':
                if rads:
                    save.one_side(beta=num, radians=True)
                else:
                    save.one_side(beta=num, radians=False)



