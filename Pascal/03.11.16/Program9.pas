const
  N = 31;

var
  A: array[1..N] of integer; 
  i, x, y: integer; 
  s: real;

begin
  Randomize();
  for i := 1 to N do begin A[i] := Random(-20, 20);write(A[i], ' '); end;
  x := 0;
  y := 0;
  for i := 1 to N do 
  begin
    if A[i] > 0 then begin
      x := x + 1;
      y := y + A[i];
    end;
  end;
  write('x= ', x, ' y= ', y, ' cp= ', y / x);
end.