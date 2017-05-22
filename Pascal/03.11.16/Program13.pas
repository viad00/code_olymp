const
  N = 30;

var
  a: array [1..N] of integer; 
  i, j, x: integer;

begin
  Randomize();
  for i := 1 to N do begin a[i] := Random(125);write(a[i], ' '); end;
  x:=Random(5);
  writeln('x:= ',x);
  j:=0;
  for i:=N downto 1 do begin if a[i]=x then j:=i; end;
  if j = 0 then writeln('none') else
  writeln(' ',j);
end.