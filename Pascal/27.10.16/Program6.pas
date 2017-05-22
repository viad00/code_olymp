var
  a, b, n, diff: integer;

begin
  Readln(a);
  diff := a;
  while a > 0 do 
  begin
    a := a div 10;
    n := n + 1;
  end;
  a := diff;
  diff := 5 - n;
  if diff > 0 then begin
  
end.