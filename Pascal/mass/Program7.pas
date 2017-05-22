const
  N = 30;

var
  A: array[1..N] of integer; 
  i, x, y: integer; 
  s: real;

begin
  for i := 1 to N do A[i] := Random(100); 
  for i := 1 to N do if A[i] < 20 then A[i] := -1;
  x := 0;
  y := 0;
  for i := 1 to N do 
  begin
    if A[i] <> -1 then begin
      x := x + A[i];
      y := y + 1;
    end;
  end;
  s := x / y;
  write(s);
end.