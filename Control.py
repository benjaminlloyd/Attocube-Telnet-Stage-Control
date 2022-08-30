class Control():
    def __init__(self,tn):
        self.tn=tn
        return
    def write(arg,txt):
        tn=arg.tn
        text=txt+'\n'
        textfinal=str.encode(text)
        tn.write(textfinal)
        return

    def move(arg,axis,steps,*args): #args = voltage, frequency; order important!
        tn=arg.tn
        try:
            volt='setv '+str(axis)+" "+str(args[0])+'\n'
            tn.write(str.encode(volt))
        except IndexError:
            pass
        try:
            freq='setf '+str(axis)+" "+str(args[1])+'\n'
            tn.write(str.encode(freq))
        except IndexError:
            pass

        if steps>0 or steps==0:
            stepperu='stepu '+str(axis)+' '+str(steps)+'\n'
            tn.write(str.encode(stepperu))
        if steps<0:
            stepperd='stepd '+str(axis)+' '+str(abs(steps))+'\n'
            tn.write(str.encode(stepperd))
        return

    def turnoff(arg):
        tn=arg.tn
        for i in range(1,7):
            tn.write(str.encode('setm '+str(i)+" gnd\n"))
    def turnon(arg):
        tn=arg.tn
        for i in range(1,7):
            tn.write(str.encode('setm '+str(i)+" stp\n"))

    def abort(arg):
        tn=arg.tn
        turnoff()
        return
    def turnoff(arg):
        tn=arg.tn
        for i in range(1,7):
            tn.write(str.encode('setm '+str(i)+" gnd\n"))
    def turnon(arg):
        tn=arg.tn
        for i in range(1,7):
            tn.write(str.encode('setm '+str(i)+" stp\n"))

    def roomtemp(arg):
        tn=arg.tn
        for i in range(1,7):
            tn.write(str.encode('setv '+str(i)+" 45\n"))
            tn.write(str.encode('setf '+str(i)+" 1000\n"))
    def lowtemp(arg):
        tn=arg.tn
        for i in range(1,7):
            tn.write(str.encode('setv '+str(i)+" 30\n"))
            tn.write(str.encode('setf '+str(i)+" 150\n"))


    def lowtemp_subtle(arg):
        tn=arg.tn
        for i in range(1,7):
            tn.write(str.encode('setv '+str(i)+" 25\n"))
            tn.write(str.encode('setf '+str(i)+" 150\n"))
        
   
