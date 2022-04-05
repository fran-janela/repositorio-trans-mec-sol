# cálculo da parede isolada
if j == 0:
        TM[l+1,i,j] = (TM[l,i,j] + gama * (2*TM[l,i,j+1]+ TM[l,i-1,j] + TM[l,i+1,j] - 4*TM[l,i,j]))