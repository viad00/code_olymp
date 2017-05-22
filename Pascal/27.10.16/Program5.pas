var
  n, m, a: integer;

begin
  Readln(n);
  while n > 0 do 
  begin
    a := n mod 10;
    n := n div 10;
    m := m * 10 + a;
  end;
  write(m);
  
end.