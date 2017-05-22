var 
x,y:real;
begin
Read(x,y);
if (y<=0.5) and (y>=0) and (y<=Sin(x)) and (x>=0) and (x<=Pi) then
 print('принадлежит')
else
 Print('нет')
end.