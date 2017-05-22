var 
x,y:real;
begin
Read(x,y);
if (y <=2-x*x) and ((y>=x) or (y>=0)) then
 print('принадлежит')
else
 Print('нет')
end.