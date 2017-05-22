var
  even, odd, num: integer;

begin
  Readln(num);
  while num > 0 do 
  begin
    if num mod 2 = 0 then even := even + 1
    else odd := odd + 1;
    num := num div 10;
  end;
  writeln('odd ' , odd , ' even ' , even); 
end.