var
  a, b, x: real;

begin
  readln(a, b, x); 
  if a = 0 then 
    write('нет решений') 
  else 
  begin
    if b = 0 then 
      write('x = 0') 
    else write('x =', b / a, ' или x =', -b / a); 
  end
end.